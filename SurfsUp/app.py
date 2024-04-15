# Import the dependencies.

import datetime as dt
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
from datetime import timedelta


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")


# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)


# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

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
        r"Available Routes:<br/>"
        r"/api/v1.0/precipitation<br/>"
        r"/api/v1.0/stations<br/>"
        r"/api/v1.0/tobs<br/>"
        r"/api/v1.0/<<start>><br/>"
        r"/api/v1.0/<start>/<end>>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    last_date = dt.datetime.strptime(last_date, '%Y-%m-%d')
    year_ago = last_date - dt.timedelta(days=365)
    query_results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > year_ago).order_by(Measurement.date).all()
    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_measurements = []
    for date, prcp in query_results:
        measurement_dict = {}
        measurement_dict["date"] = date
        measurement_dict["prcp"] = prcp
        all_measurements.append(measurement_dict)

    return jsonify(all_measurements)

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    query_results = session.query(Station.station).all()
    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_stations = []
    for station in query_results:
        station_dict = {}
        station_dict["station"] = station[0]
        all_stations.append(station_dict)

    return jsonify(all_stations)


@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    query_results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date > '2016-08-23').filter(Measurement.station == 'USC00519281').all()
    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_tobs = []
    for date, tob in query_results:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tob"] = tob
        all_tobs.append(tobs_dict)

    return jsonify(all_tobs)


@app.route("/api/v1.0/<start>")
def start(start):
    # Create our session (link) from Python to the DB
    session = Session(engine)
    min_temp = session.query(func.min(Measurement.tobs)).filter(Measurement.date >= start).all()[0][0]
    max_temp = session.query(func.max(Measurement.tobs)).filter(Measurement.date >= start).all()[0][0]
    avg_temp = session.query(func.avg(Measurement.tobs)).filter(Measurement.date >= start).all()[0][0]
    session.close()
    result = {}
    result["min_temp"] = min_temp
    result["max_temp"] = max_temp
    result["avg_temp"] = round(avg_temp, 2)

    return jsonify(result)


@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    # Create our session (link) from Python to the DB
    session = Session(engine)
    min_temp = session.query(func.min(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()[0][0]
    max_temp = session.query(func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()[0][0]
    avg_temp = session.query(func.avg(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()[0][0]
    session.close()
    result = {}
    result["min_temp"] = min_temp
    result["max_temp"] = max_temp
    result["avg_temp"] = round(avg_temp, 2)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

