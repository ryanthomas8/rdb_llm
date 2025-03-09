import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain.chains.sql_database.query import create_sql_query_chain
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.utilities import SQLDatabase
from langchain_community.tools import QuerySQLDatabaseTool
import json

# Initialize FastAPI app
app = FastAPI()


# Pydantic model to handle the user input
class QueryRequest(BaseModel):
    question: str


# Initialize database connection
db = SQLDatabase.from_uri(os.getenv("DATABASE_URL_DEV", None))

# Fetch schema information
schema_info = db.get_table_info()

# Initialize LLM
llm = ChatOpenAI(
    model="gemma2",
    temperature=0,
    max_tokens=512,
    timeout=30,
    max_retries=2,
    base_url=os.getenv("OLLAMA_URL", None),
    api_key=os.getenv("OLLAMA_API_KEY", None),
)

# Improved SQL query generation prompt
query_prompt = PromptTemplate.from_template(
    """You are a PostgreSQL expert. Given an input question, first create a syntactically correct PostgreSQL query to run.
Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per PostgreSQL. You can order the results to return the most informative data in the database.
Never write a query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in double quotes (") to denote them as delimited identifiers.
Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
Pay attention to use CURRENT_DATE function to get the current date, if the question involves "today".
Only respond with the exact query. Nothing more, nothing less.

Only use the following tables:
{table_info}

User input: 
{input}
"""
)

# SQL query generation chain
write_query = create_sql_query_chain(llm, db, prompt=query_prompt)

# SQL execution tool with result limiting
execute_query = QuerySQLDatabaseTool(db=db, top_k=10)

# Improved Answer Prompt
answer_prompt = PromptTemplate.from_template(
    """You are an AI assistant helping answer questions using SQL query results. 
Follow these rules:
- The SQL result **may be a subset of the full data**, but always generate an answer based **only on what is provided**.
- Do NOT suggest modifying the SQL query or needing more data. Assume this is all that is available.
- If multiple rows are returned, summarize them concisely.

User Question: {question}
SQL Query: {query}
SQL Result: {result}

Based ONLY on the User Question and SQL result above, provide a clear and direct answer:
"""
)


# FastAPI endpoint to handle user query
@app.post("/ask")
async def ask_user(query_request: QueryRequest):
    # Get user question from request
    user_question = query_request.question

    # Step 1: Generate SQL Query
    inputs = {"question": user_question}
    query = write_query.invoke(inputs)

    # Step 2: Execute the SQL Query
    try:
        result = execute_query.invoke(query)
        formatted_result = json.dumps(result, indent=2)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error executing query: {str(e)}")

    # Step 3: Generate Answer using LLM
    formatted_input = {
        "question": user_question,
        "query": query,
        "result": formatted_result,
    }
    try:
        final_answer = (answer_prompt | llm | StrOutputParser()).invoke(formatted_input)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error generating answer: {str(e)}"
        )

    # Return SQL Query and Final Answer
    return {
        "question": user_question,
        "sql_query": query,
        "query_result": formatted_result,
        "final_answer": final_answer,
    }
