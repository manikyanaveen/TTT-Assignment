# TTT-Assignment
Assignment for TTT Lovely Professional University

The assignment is to take a input n from user through front end and then pass the value to backend
In the back end we have to fetch a file and then count the frequencies of the words and then we have to display the top n  frequent words in front end in tabular form

In this project I used HTML for the Front End and Python Flask for Backend

Created 2 html files one for taking input from user i.e new.html and the other is for displaying the table i.e disp.html

An python file which is an flask app i.e app.py for getting input from html file and sending table to html file

Description of the Html file i.e; new.html - In this i have used the concepts of basic html and css. Css for styling of the page 
the form and action syntaxes are used for taking the input from user and passing the value to the python using the post request function

Description of Python file i.e: app.py - In this module the main concepts are flask and pandas. Flask is an web applicaton framework used to pass the variables and other data from html to python and vice versa. Pandas datframes are used to convert the data after reading the content fo the file into a tabular form.We have used the render_template function to read the html templates that are the front end pages.

Description of Html file i.e; disp.html - In this module we have used the table tags to display the file.


Steps to run: 
1. We have to create the virtual environment  and then install flask.
2. After creation of flask app we have to run the app.py file then we will get the url
3. Now browssing the url it will turn the html page then after data is taken and perfoms the function named  perform() the data then displays thrigh the disp.html page.

Modules Included:
1.Python Flask
2.Html CSS
3.Pandas for Python
4.RE(Regular Expression) module from Python
