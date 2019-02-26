from flask import Flask
from flask_cors import CORS
from buses import bp as buses_blueprint
from ping import bp as ping_blueprint
from census import bp as census_blueprint

app = Flask(__name__)

app.register_blueprint(buses_blueprint)
app.register_blueprint(ping_blueprint)
app.register_blueprint(census_blueprint)

CORS(app)

@app.route('/')
def hello_world():
    return "Hello from the API!"

if __name__ == '__main__':
    app.run()
