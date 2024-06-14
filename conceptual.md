### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
  is a database system in which can use, modify and distribute. Is open source object-relational. It supports advance data types and object-oriented features like table inheritance and function overloading.


- What is the difference between SQL and PostgreSQL?
  SQL is a lenguage used to interact with database wich is a standard followed by many database systems and PostgreSQl is a specific database system thathuses SQL as its primary language and additional features, functionalities and enhancements beyon the standard SQL


- In `psql`, how do you connect to a database?
  To connect to a database in psql, you can use the following command:

psql -U <username> -d <database_name>
Replace <username> with your username and <database_name> with the name of the database you want to connect to.


- What is the difference between `HAVING` and `WHERE`?
  WHERE is used in 'SELECT', 'UPDATE', 'DELETE' starementrs to specify conditions that needs to be met for the rows to be affected.


- What is the difference between an `INNER` and `OUTER` join?
  INNER JOIN returns only the rows that have  matching values in both tables, while the OUTER JOINT can be divided in three types: LEFT, RIGHT and FULL. The LEFT will return all rows from the left table and matched rows from the right table and rows from the left table with no match will have NULL. The RIGHT will return all rows from the right table and the matched rows from the left table and rows from the right table with no match will have NULL and The FULL will return all rows where there is a match in either left or right. The rows with no match in one of the tables will have NULL values.


- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
The LEFT will return all rows from the left table and matched rows from the right table and rows from the left table with no match will have NULL. The RIGHT will return all rows from the right table and the matched rows from the left table and rows from the right table with no match will have NULL.


- What is an ORM? What do they do?
ORM stands for Object-Relational Mapping. It is a technique used to map objects in an object-oriented programming language to tables in a relational database. ORM frameworks provide a way to interact with the database using objects and their relationships, rather than writing SQL queries directly. This helps in simplifying database operations and makes it easier to work with databases in an object-oriented manner.


- What are some differences between making HTTP requests using AJAX
  and from the server side using a library like `requests`?
  HTTP reqauest usinf AJAX from the client side and using library like request from the server will runs in the web browser, typically uses JavaScript and libraries/frameworks like jQuery, Axios or the Fetch API. Primarily used to update the user interface without reloading the entire page and it enables dynamic content loading and interactive user experiences.


- What is CSRF? What is the purpose of the CSRF token?
  CSRF stands for Cross-Site Request Forgery. It is a type of security vulnerability that allows an attacker to trick a user into performing actions on a website without their knowledge or consent.the purpuse is to prevent CSRF attacks, web applications can use techniques like CSRF tokens or double-submit cookies.


- What is the purpose of `form.hidden_tag()`?
  is to generate a hidden input field in an HTML form. This hidden input field is used to store data that is not visible to the user, but can be accessed and processed by the server-side code.