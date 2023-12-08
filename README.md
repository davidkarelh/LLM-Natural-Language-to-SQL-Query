# LLM Natural Language to SQL Query

This is a Natural Language to SQL Query system using the PaLM LLM. You will need the google API key to be able to access PaLM LLM. This project uses few shot learning, where it uses ChromaDB for saving and retrieving the few shot examples. The few shot examples are saved in the <b>few_shots.py</b> file. You need to have access to MySQL database for this project. The query for initializing and seeding the database is in the <b>database</b> folder at the <b>db_retail.sql</b> file. Modify the .env file (format is in .env.example file) to be able to access the database.

## How To Run
1. You can create virtual environment, if you create it, use the virtual environment
2. Run <code>pip install -r requirements.txt</code> to install the necessary packages
3. Run <code>streamlit run main.py</code> and wait until the streamlit UI is opened on your browser, you can see the streamlit local URL in the terminal

## Pictures

Result of query:
<b>"If we have to sell all the Levi’s T-shirts today. How much revenue our store will generate without discount?"</b>
![Selling Levi's T-shirts without discounts](https://github.com/davidkarelh/LLM-Natural-Language-to-SQL-Query/blob/master/pictures/Levi's%20T-Shirts%20Without%20Discounts.png)

Result of query:
<b>"If we have to sell all the Nike’s T-shirts today with discounts applied. How much revenue our store will generate (post discounts)?"</b>
![Selling Nike's T-shirts without discounts](https://github.com/davidkarelh/LLM-Natural-Language-to-SQL-Query/blob/master/pictures/Nike's%20T-Shirts%20With%20Discounts.png)

Result of query:
<b>"What T-shirts brands are available in the inventory?"</b>
![All T-shirts brands](https://github.com/davidkarelh/LLM-Natural-Language-to-SQL-Query/blob/master/pictures/T-shirts%20brand.png)