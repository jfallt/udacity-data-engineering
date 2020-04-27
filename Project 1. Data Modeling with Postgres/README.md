# Sparkify Database & ETL Project
## Table of Contents
- [Database Purpose](#Database-Purpose)
- [Schema for Song Play Analysis](#Schema-for-Song-Play-Analysis)
    - [Fact Table: songplays](#Fact-Table:-songplays)
    - [Dimension Tables](#Dimension-Tables)
- [ETL Process](#ETL-Process)

***
## Database Purpose
- Sparkify wants to analyze songs and user activity data on their new music streaming app.
- The analytics team is particularly interested in understanding what songs users are listening to.
- Create an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

## Schema for Song Play Analysis
Star schema optimized for queries on song play analysis.

This includes the following tables.
### Fact Table: songplays
Records in log data associated with song plays (i.e. records with page NextSong)

- Columns:
    - songplay_id
    - start_time
    - user_id
    - level
    - song_id
    - artist_id
    - session_id
    - location
    - user_agent
    
***

### Dimension Tables
- Table: `users`
    - users in the app
- Columns:
    - user_id
    - first_name
    - last_name
    - gender
    - level
- Table: `songs`
    - songs in music database
- Columns:
    - song_id
    - title
    - artist_id
    - year
    - duration
- Table: `artists`
    - artists in music database
- Columns:
    - artist_id
    - name
    - location
    - latitude
    - longitude
- Table: `time`
    - timestamps of records in songplays broken down into specific units
- Columns:
    - start_time
    - hour
    - day
    - week
    - month
    - year
    - weekday
    
## ETL Process 
1. Process `song_data`
    - ETL on `song_data`, to create the `songs` and `artists` dimensional tables.
1. Process `log_data`
    - ETL on `log_data`, to create the `time` and `users` dimensional tables, as well as the `songplays` fact table.