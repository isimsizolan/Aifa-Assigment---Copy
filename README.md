uvicorn app.main:app --reload

http://localhost:8000/

http://localhost:8000/docs  

*await async structure (except langchain db agent)

*decorator pattern for logging and exception

*langchain based dispatcher

*repository pattern if user want to create distinc async db operations

![resim](https://github.com/user-attachments/assets/16c72529-f2d5-4774-8941-b89390f24f97)


Example Chat:
```
You:
price of samsung
16:16
Bot:
849.50
16:16
You:
tell me about istanbul
16:16
Bot:
Istanbul is the largest city in Turkey, located on two continents, Europe and Asia, straddling the Bosphorus strait. It's a major economic, cultural, and historical center with a population of over 15 million.
16:16
You:
weather in Tokyo
16:17
Bot:
The weather in Tokyo is 21.5°C, with wind at 7.6 km/h and a humidity of 2%.
16:17
You:
what are passive radars
16:17
Bot:
Passive radars are a type of radar that do not transmit their own radio waves. Instead, they detect and analyze radio waves that are already present in the environment, such as those emitted by aircraft, ships, or other objects.
16:17
You:
What are the products
16:17
Bot:
The products are iPhone 13 Pro and Samsung Galaxy S21.
16:17
You:
price of iphone
16:18
Bot:
The price of an iPhone is 999.99.
16:18
```

Example Log:
```
> Entering new AgentExecutor chain...
Thought: I need to query the products database for the price of an iphone. 
Action: ask_sql
Action Input: what is the price of iphone[2025-05-21 16:27:16] [INFO] [TOOL CALL] ask_sql | args: ('what is the price of iphone',), kwargs: {}


> Entering new SQL Agent Executor chain...
Thought: I should look at the tables in the database to see what I can query.  Then I should query the schema of the most relevant tables.
Action: sql_db_list_tables
Action Input: productsAction: sql_db_schema
Action Input: products
CREATE TABLE products (
        id BIGSERIAL NOT NULL,
        name TEXT NOT NULL,
        description TEXT,
        price NUMERIC(10, 2),
        CONSTRAINT products_pkey PRIMARY KEY (id),
        CONSTRAINT products_name_key UNIQUE NULLS DISTINCT (name)
)

/*
3 rows from products table:
id      name    description     price
1       iPhone 13 Pro   Apple smartphone with A15 chip  999.99
2       Samsung Galaxy S21      Samsung flagship phone with AMOLED display      849.50
*/Thought: I can query the products table for the price of an iPhone.
Action: sql_db_query_checker
Action Input: SELECT price FROM products WHERE name = 'iPhone 13 Pro'```sql
SELECT price FROM products WHERE name = 'iPhone 13 Pro'
Action: sql_db_query
Action Input: SELECT price FROM products WHERE name = 'iPhone 13 Pro'[(Decimal('999.99'),)]Final Answer: 999.99 


> Finished chain.
```
