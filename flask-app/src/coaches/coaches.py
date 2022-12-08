from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


coaches = Blueprint('coaches', __name__)# -*- coding: utf-8 -*-

# get the runners with team_id = 1

@coaches.route('/team1members')
def get_team1_members():
    cursor = db.get_db().cursor()
    query = '''
        SELECT first_name, last_name, email
        FROM runners
        WHERE team_id = 1;
    '''
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# Get all races from the DB for a coach

@coaches.route('/races', methods=['GET'])
def get_racesforcoach():
    cursor = db.get_db().cursor()
    cursor.execute('select race_id, race_name, race_city, race_state, race_date, race_desc from races')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response# -*- coding: utf-8 -*-

# enters a team entry for a race into teamentries table

@coaches.route('/enterarace', methods=['POST'])
def enter_race_team():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()
    team_id = request.form['team_id']
    race_id = request.form['race_id']
    query = f'INSERT INTO teamentries(team_id, race_id) VALUES(\"{team_id}\", \"{race_id}\")'
    cursor.execute(query)
    db.get_db().commit()
    return "Your team has been signed up!"