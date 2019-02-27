# REST db access - Web frontend to mariadb backend
# Bill Erhard wherhard@student.rtc.edu
# CNA335

"""Hosts a web server on port 5000 (5 Points) Has 2 pages: /search and /update (20 Points)
/search queries an SQL DB and prints out the row data /update updates an SQL DB row"""

'''Launches web server on port 5000 (1 Point) Queries the DB and returns information (1 Point)
Updates the DB (1 Point) Uses XML or JSON -packed messages to transport data (2 Points)'''

'''Search allows the user to search the DB by zip code: 
Serves a web page that at minimum has the following elements (3 Points)
Text Label and Input Box: Zip Code Submit button Use GET to search the DB (3 Points) i.e. /search?zip=98144
Return the rows associated with that query (4 Points) 
Note: Population is the most important row. If you have trouble returning all rows at least return that'''

'''Update allows the user to update the population of a zip code: 
Serves a web page that at minimum has the following elements (3 Points)
Text Label and Input Box: Zip Code
Text Label and Input Box: Population
Submit button
Uses POST to update the DB using a JSON or XML-formatted message (5 Points)
Prints “Success” or “Failed” to the page depending on the result (2 Points)'''

'''This does NOT have to run on, nor be developed on a Pi 
(but it should run on one)
This is probably developed best on the WAMP/XAMPP/MAMP SQL + Phpmyadmin
setup on your host so you get your database up quickly
A VM is also good Should be developed on GitHub'''

from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


@app.route('/search/<zip>', methods=['POST', 'GET'])
def search(zip):
    return 'welcome %s' % zip


@app.route('/update', methods=['POST'])
def update(zip):
    return 'updated! %s' % zip


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('search', zip=user))



@app.route('/')
def root():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
