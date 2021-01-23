import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, render_template, jsonify
import pandas as pd

# assign a variable that contains a string of your credentials
credentials = "sqlite:///Resources/beer_test2.sqlite"

# read in your SQL query results using pandas
dataframe = pd.read_sql("SELECT * FROM BREWERIES", con = credentials)
# return your first five rows
# dataframe.head()

Breweries = dataframe.to_json()

####################
# database setup
####################
engine = create_engine("sqlite:///Resources/beer_test.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# check tables
# Base.metadata.tables

# get table names
# Base.classes.keys()

# save reference to the table (from hw, leaving it here as reference)
# M = Base.classes.measurement
# S = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

####################
# flask setup
####################
app = Flask(__name__)

####################
# flask routes
####################
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/roman")
def roman():
    return render_template('index.html')    

@app.route("/data")
def data():
    return jsonify(Breweries)
 
if __name__ == "__main__":
    app.run(debug=True)