### *SQL Introduction*

This repository contains SQL scripts that cover fundamental concepts and tasks related to MySQL databases. The scripts are designed to be executed on an Ubuntu 20.04 LTS environment using MySQL 8.0.25. The tasks aim to reinforce understanding of essential SQL concepts, database creation, table manipulation, and data retrieval.
#### *Project Structure*

    0-list_databases.sql: Lists all databases on the MySQL server.
    1-create_database_if_missing.sql: Creates the database hbtn_0c_0 if it doesn't already exist.
    2-remove_database.sql: Deletes the database hbtn_0c_0 if it exists.
    3-list_tables.sql: Lists all tables in a specified database.
    4-first_table.sql: Creates a table named first_table with specified columns.
    5-full_table.sql: Prints the full description of the table first_table.
    6-list_values.sql: Lists all rows of the table first_table.
    7-insert_value.sql: Inserts a new row into the table first_table.
    8-count_89.sql: Displays the number of records with id = 89 in the table first_table.
    9-full_creation.sql: Creates a table second_table and adds multiple rows.
    10-top_score.sql: Lists all records of the table second_table ordered by score.
    11-best_score.sql: Lists records with a score >= 10 in the table second_table.
    12-no_cheating.sql: Updates the score of a specific record in second_table.
    13-change_class.sql: Removes records with a score <= 5 in second_table.
    14-average.sql: Computes the average score of all records in second_table.
    15-groups.sql: Lists the number of records with the same score in second_table.
    16-no_link.sql: Lists all records of second_table excluding rows without a name value.
    100-move_to_utf8.sql: Converts the hbtn_0c_0 database, first_table table, and name field to UTF8.
    101-avg_temperatures.sql: Displays the average temperature by city in Fahrenheit.
    102-top_city.sql: Displays the top 3 cities' temperatures during July and August.
    103-max_state.sql: Displays the max temperature of each state ordered by state name.
