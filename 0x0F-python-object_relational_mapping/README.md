Python Object-Relational Mapping (ORM) Project

This project focuses on the integration of Python with databases using Object-Relational Mapping (ORM). The goal is to demonstrate the power of SQLAlchemy, a popular ORM library in Python, which allows developers to interact with databases using Python code rather than raw SQL queries.
Project Overview

The project is divided into several tasks, each highlighting a specific aspect of ORM and database interaction. The tasks cover the following key areas:

    Connecting to MySQL Database: Demonstrates how to connect to a MySQL database using the MySQLdb module and execute SQL queries.

    Introduction to SQLAlchemy: Introduces SQLAlchemy as an ORM solution, allowing developers to work with Python objects rather than direct SQL queries. The focus is on creating a virtual environment and installing the necessary dependencies.

    Creating a State Class: Defines a Python class, State, and establishes a mapping between the class and a MySQL table. This showcases the fundamental concept of ORM.

    Querying States: Demonstrates how to query and retrieve data from the states table using SQLAlchemy, emphasizing the shift from raw SQL queries to Python code.

    Filtering and SQL Injection Prevention: Explores filtering data based on specific conditions and addresses potential SQL injection vulnerabilities by ensuring safe user input handling.

    Relational Mapping - Cities by State: Illustrates the relationship between two tables, states, and cities, and how to retrieve data from the cities table, displaying the associated state information.

    Advanced Queries - Filtering Cities by State: Extends the previous task by allowing users to input a state name and retrieve all cities within that state.

    Defining a State Model and Fetching Data: Establishes a State class using SQLAlchemy's declarative_base() and fetches all state objects from the database.

    Fetching the First State: Retrieves the first state object from the database using SQLAlchemy.

    Filtering States by Letter: Retrieves all states containing the letter 'a' from the database.

    Fetching a Specific State: Retrieves the ID of a specific state from the database, handling cases where the state is not found.

    Inserting a New State: Adds a new state, "Louisiana," to the database and prints the assigned ID.

    Updating a State Name: Modifies the name of a state with a specific ID to "New Mexico."

    Deleting States with a Letter 'a': Deletes all states with names containing the letter 'a' from the database.

    City Class and Fetching Cities by State: Introduces a City class and retrieves all city objects from the database, displaying associated state information.

    Project Structure

        0-select_states.py: Script for listing all states from the database.
        1-filter_states.py: Script for listing states starting with the letter 'N.'
        2-my_filter_states.py: Script for filtering states based on user input, preventing SQL injection.
        3-my_safe_filter_states.py: Script for safe filtering of states based on user input.
        4-cities_by_state.py: Script for listing all cities with associated states.
        5-filter_cities.py: Script for filtering cities by state based on user input.
        6-model_state.py: Script for defining a State class and creating a database table.
        7-model_state_fetch_all.py: Script for fetching all state objects from the database.
        8-model_state_fetch_first.py: Script for fetching the first state object from the database.
        9-model_state_filter_a.py: Script for filtering states with names containing the letter 'a.'
        10-model_state_my_get.py: Script for fetching a state's ID based on user input.
        11-model_state_insert.py: Script for inserting a new state, "Louisiana," into the database.
        12-model_state_update_id_2.py
