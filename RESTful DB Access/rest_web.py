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

from flask import Flask, redirect, url_for, request, render_template, jsonify
import mysql.connector
import json

app = Flask(__name__)


@app.route('/search', methods=['GET'])
def search():
    zipcode = request.args.get('zip')
    return search_zipcode(zipcode)


@app.route('/update/result', methods=['POST'])
def update():
    zipcode = request.form['zip']
    population = request.form['pop']
    jsonpage = json.dumps({'zip': zipcode, 'pop': population})

    return update_pop(jsonpage)


@app.route('/input')
def xfers():
    return render_template('search.html')


@app.route('/update')
def xferu():
    return render_template('update.html')


@app.route('/')
def root():
    return render_template('index.html')


@app.errorhandler(404)
def four_oh_four(error):
    return 'Four-Oh-Four Page not found!'


def connect_to_sql():
    conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='cna335')
    return conn


# Searches the database for a particular zipcode and returns the row in json format
# json stuff: https://stackoverflow.com/questions/13081532/return-json-response-from-flask-view
def search_zipcode(zipcode):
    conn = connect_to_sql()
    cursor = conn.cursor()
    query = '''SELECT %s FROM %s WHERE %s="%s";''' % ("*", "zipcodes", "Zipcode", zipcode)
    cursor.execute(query)
    response = cursor.fetchall()
    return jsonify(response)


def update_pop(jsonpage):
    conn = connect_to_sql()
    cursor = conn.cursor()
    jsonpage = json.loads(jsonpage)
    query = '''SELECT %s FROM %s WHERE %s="%s";''' % ("*", "zipcodes", "Zipcode", jsonpage['zip'])
    cursor.execute(query)
    if not cursor.fetchall():
        return 'BROKED! No updates for you.'
    query = '''UPDATE %s SET %s = "%s" WHERE %s = "%s";''' % (
    "zipcodes", "EstimatedPopulation", jsonpage['pop'], "Zipcode", jsonpage['zip'])
    cursor.execute(query)
    return 'updated! zipcode - %s population - %s' % (jsonpage['zip'], jsonpage['pop'])


if __name__ == '__main__':
    app.run(debug=True)
