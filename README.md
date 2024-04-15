# sqlalchemy-challenge
To help with trip planning, we perfomed a climate analysis about the area. 

Part 1: Analyze and Explore the Climate Data
In this section, we use Python and SQLAlchemy to do a basic climate analysis and data exploration climate database using SQLAlchemy ORM queries, Pandas, and Matplotlib. 

1. Used the provided files (climate_starter.ipynb and hawaii.sqlite) to complete climate analysis and data exploration.
2. Used the SQLAlchemy create_engine() function to connect to SQLite database.
3. Used the SQLAlchemy automap_base() function to reflect tables into classes, and then save references to the classes named station and measurement.
4. Linked Python to the database by creating a SQLAlchemy session.

Performed a precipitation analysis and then a station analysis by completing the steps in the following two subsections.

Precipitation Analysis
1. Found the most recent date in the dataset. Using that date, provided the previous 12 months of precipitation data by querying the previous 12 months of data.
2. Selected only the "date" and "prcp" values.
3. Loaded the query results into a Pandas DataFrame. Explicitly set the column names.
4. Sorted the DataFrame values by "date".
5. Plotted the results by using the DataFrame plot method
6. Used Pandas to print the summary statistics for the precipitation data.

Station Analysis
1. Designed a query to calculate the total number of stations in the dataset.
2. Designed a query to find the most-active stations (that is, the stations that have the most rows). 
   Listed the stations and observation counts in descending order.
   Answered the following question: which station id has the greatest number of observations
3. Designed a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.
4. Designed a query to get the previous 12 months of temperature observation (TOBS) data. To do so, completed the following steps:
  Filtered by the station that has the greatest number of observations.
  Queried the previous 12 months of TOBS data for that station.
  Plotted the results as a histogram with bins=12


Part 2: Design Climate App
1. Designed a Flask API based on the queries we developed. 
2. Listed all the available routes /api/v1.0/precipitation
3. Convered the query results from precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value
4. Returned the JSON representation of dictionary./api/v1.0/stations
5. Returned a JSON list of stations from the dataset./api/v1.0/tobs
6. Queried the dates and temperature observations of the most-active station for the previous year of data.
7. Returned a JSON list of temperature observations for the previous year./api/v1.0/<start> and /api/v1.0/<start>/<end>
8. Returned a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
9. For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
10. For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.


