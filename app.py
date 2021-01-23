import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///beer_test.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
ba_beerstyles = Base.classes.ba_beerstyles

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/BeerStyles"
    )


@app.route("/api/v1.0/BeerStyles")
def ba_beerstyles():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of Beer Style data including the style, category, ABV, IBU, SRM, glassware, and description of each beer"""
    # Query all passengers
    results = session.query(ba_beerstyles.style, ba_beerstyles.category, ba_beerstyles.ABV_avg, ba_beerstyles.IBU_avg, ba_beerstyles.SRM_avg, ba_beerstyles.Glassware, ba_beerstyles.Description).all()

    session.close()


    print(results)
    # Create a dictionary from the row data and append to a list of all_passengers
    all_BeerStyles = []
    for style, category, ABV_avg, IBU_avg, SRM_avg, Glassware, Description in results:
        beerstyles_dict = {}
        beerstyles_dict["style"] = style
        beerstyles_dict["category"] = category
        beerstyles_dict["ABV_avg"] = ABV_avg
        beerstyles_dict["IBU_avg"] = IBU_avg
        beerstyles_dict["SRM_avg"] = SRM_avg
        beerstyles_dict["Glassware"] = Glassware
        beerstyles_dict["Description"] = Description
        all_BeerStyles.append(beerstyles_dict)

    return jsonify(all_BeerStyles)


if __name__ == '__main__':
    app.run(debug=True)