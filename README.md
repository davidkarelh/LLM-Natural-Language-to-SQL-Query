# LLM Natural Language to SQL Query

This is a Natural Language to SQL Query system using the PaLM LLM. You will need the google API key to be able to access PaLM LLM. This project uses few shot learning, where it uses ChromaDB for saving and retrieving the few shot examples. The few shot examples are saved in the <b>few_shots.py</b> file. You need to have access to MySQL database for this project. The query for initializing and seeding the database is in the <b>database</b> folder at the <b>db_retail.sql</b> file. Modify the .env file (format is in .env.example file) to be able to access the database.

## How To Run
1. You can create virtual environment, if you create it, use the virtual environment
2. Run <code>pip install -r requirements.txt</code> to install the necessary packages
3. Run <code>streamlit run main.py</code> and wait until the streamlit UI is opened on your browser, you can see the streamlit local URL in the terminal