## 0x0E. SQL - More queries
### Overview

This repository contains SQL scripts that demonstrate various queries and operations on a MySQL database. The tasks cover topics such as user privileges, database and table creation, constraints, subqueries, joins, and more.
Project Structure

    0-privileges.sql: Lists all privileges of the MySQL users user_0d_1 and user_0d_2 on the local server.
    1-create_user.sql: Creates the MySQL server user user_0d_1 with all privileges.
    2-create_read_user.sql: Creates the database hbtn_0d_2 and the user user_0d_2 with only SELECT privilege.
    3-force_name.sql: Creates the table force_name with id and name columns, where name cannot be null.
    4-never_empty.sql: Creates the table id_not_null with id and name columns, where id has a default value and name cannot be null.
    5-unique_id.sql: Creates the table unique_id with id and name columns, where id has a default value and must be unique.
    6-states.sql: Creates the database hbtn_0d_usa and the table states with id and name columns.
    7-cities.sql: Creates the table cities with id, state_id, and name columns, where state_id is a foreign key referencing the states table.
    8-cities_of_california_subquery.sql: Lists all cities of California without using the JOIN keyword.
    9-cities_by_state_join.sql: Lists all cities with their corresponding states using JOIN.
    10-genre_id_by_show.sql: Lists shows from hbtn_0d_tvshows with at least one genre linked.
    11-genre_id_all_shows.sql: Lists all shows from hbtn_0d_tvshows with their genre IDs, displaying NULL for shows without a genre.
    12-no_genre.sql: Lists shows from hbtn_0d_tvshows without a genre linked.
    13-count_shows_by_genre.sql: Displays the number of shows linked to each genre in descending order.
    14-my_genres.sql: Lists all genres of the show Dexter.
    15-comedy_only.sql: Lists all Comedy shows from hbtn_0d_tvshows.
    16-shows_by_genre.sql: Lists all shows and their linked genres, displaying NULL for shows without a genre.

#### Usage

To execute the SQL scripts, use the following command format:

cat script_name.sql | mysql -hlocalhost -uroot -p [database_name]

Replace script_name.sql with the desired script, and [database_name] with the name of the database you want to connect to.

Note: Make sure to have MySQL installed and running on your system. The scripts assume MySQL version 8.0.25 on Ubuntu 20.04 LTS.
