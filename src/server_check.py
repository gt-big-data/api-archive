from flask import Flask, request, jsonify
import json
import os
import subprocess
import pymysql
import requests

app = Flask(__name__);

@app.route("/db")            
def db():
    try:
        connection = pymysql.connect(host=-insert host-,user='testing')
    except Exception as e:
        return str(e)
    cursor = connection.cursor()
    a = cursor.execute("SELECT * FROM `gtfs_data`.`agency` LIMIT 200")
    if a == 1:
        return "Database is on"
    else: 
        return "Something is wrong"
    
@app.route("/api")
def api()
    try: 
        r = requests.get("http://-url-/ping")
    except:
        return "API server is down"
    if r.content == b'pong':
        return "API server is on"
    
@app.route("/website")
    try: 
        r = requests.get("http://gtbigdata.club/")
    except:
        return "Website is down"
    if r.status_code == 200:
        return "Website is good"
    #return jsonified obj as deployable product 


if __name__ == "__main__":
    app.run()
