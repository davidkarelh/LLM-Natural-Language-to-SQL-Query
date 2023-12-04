import streamlit as st
from langchain_helper import get_few_shot_db_chain

st.title("Retail: Database Q&A 👕")

question = st.text_input("Question: ")

if question:
    chain = get_few_shot_db_chain()

    chain.return_sql = True
    sql = chain.run(question)

    chain.return_sql = False
    response = chain.run(sql)

    st.header("Answer")
    st.write(response)

    st.header("SQL")
    st.write(sql)





