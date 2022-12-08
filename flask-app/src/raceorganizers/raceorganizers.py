from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


raceorganizers = Blueprint('raceorganizers', __name__)# -*- coding: utf-8 -*-# -*- coding: utf-8 -*-

# get some of the races from the database that the organizer has "created"

@raceorganizers.route('/managingraces')
def get_most_pop_products():
    cursor = db.get_db().cursor()
    query = '''
        SELECT race_id, race_name, race_city, race_state, race_desc, organizer_id
        FROM races
        WHERE organizer_id = 11;
    '''
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# get the volunteers with race_id 3

@raceorganizers.route('/race3volunteers')
def get_race3_volunteers():
    cursor = db.get_db().cursor()
    query = '''
        SELECT first_name, last_name, job_desc
        FROM volunteers
        WHERE race_id = 3;
    '''
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# get the services with race_id 3

@raceorganizers.route('/race3services')
def get_race3_services():
    cursor = db.get_db().cursor()
    query = '''
        SELECT company_name, service_desc, cost, hours_hired
        FROM services
        WHERE race_id = 3;
    '''
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)










