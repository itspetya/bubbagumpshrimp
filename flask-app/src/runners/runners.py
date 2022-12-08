from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


runners = Blueprint('runners', __name__)# -*- coding: utf-8 -*-

# adds a new journal entry to the journalentries table

@runners.route('/newjournalentry', methods=['POST'])
def enter_race_team():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()
    entry_title = request.form['entry_title']
    entry = request.form['entry']
    query = f'INSERT INTO journalentries(entry_title, entry) VALUES(\"{entry_title}\", \"{entry}\")'
    cursor.execute(query)
    db.get_db().commit()
    return "New entry added to journal."

# get the practices with a particular id of a coach

@runners.route('/team1practices')
def get_team1_pracs():
    cursor = db.get_db().cursor()
    query = '''
        SELECT prac_date, prac_time, prac_desc, attend_req
        FROM practiceplans
        WHERE planner_id = '643-7cn';
    '''
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)