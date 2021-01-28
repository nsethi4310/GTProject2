import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, render_template, jsonify
import pandas as pd

####################
# assign a variable that contains a string of your credentials
####################
credentials = "sqlite:///Resources/beer_test.sqlite"

####################
# read in your SQL query results using pandas
####################

####################
# database setup
####################
# engine = create_engine("sqlite:///Resources/beer_test.sqlite")

# reflect an existing database into a new model
# Base = automap_base()

# reflect the tables
# Base.prepare(engine, reflect=True)

# check tables
# Base.metadata.tables

# get table names
# Base.classes.keys()

# save reference to the table (from hw, leaving it here as reference)
# does not work due to lack of primary keys in database 
# M = Base.classes.measurement
# S = Base.classes.station

# Create our session (link) from Python to the DB
# session = Session(engine)

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
    return render_template('aboutme_test.html')

@app.route("/map")
def map():
    return render_template('map.html')    

@app.route("/map_data")
def map_data():

    Breweries_df = pd.read_sql("SELECT * FROM Breweries", con = credentials)
    Breweries = Breweries_df.to_json(orient = "index")

    return Breweries

@app.route("/ba_beerstyles")
def ba_beerstyles():

    ba_beerstyles_df = pd.read_sql("SELECT * FROM ba_beerstyles", con = credentials)
    ba_beerstyles = ba_beerstyles_df.to_json(orient = "index")

    return ba_beerstyles

@app.route("/us_state_data")
def us_state_data():

    us_state_data_df = pd.read_sql("SELECT * FROM us_state_data", con = credentials)
    us_state_data = us_state_data_df.to_json(orient = "index")

    return us_state_data

@app.route("/usa_breweries")
def usa_breweries():

    usa_breweries_df = pd.read_sql("SELECT * FROM usa_breweries", con = credentials)
    usa_breweries = usa_breweries_df.to_json(orient = "index")

    return usa_breweries

@app.route("/bar")
def bar():
    return render_template('index_bargraph_nagender.html')

@app.route("/scatter")
def scatter():
    return render_template('scatterplot.html') 

@app.route("/sunburst")
def sunburst():
    return render_template('index_sunburst.html')
@app.route("/sunburst2")
def sunburst2():
    return render_template('index_sunburst2.html')
 
if __name__ == "__main__":
    app.run(debug=True)