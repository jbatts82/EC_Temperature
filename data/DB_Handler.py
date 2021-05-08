###############################################################################
# File Name  : DB_Handler.py
# Date       : 03/18/2021
# Description: Interface to Database
###############################################################################

import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, DateTime, Float, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData
from datetime import datetime
from datetime import timedelta
from support import log
from support import div

base = declarative_base()

class Instant_Temperature(base):
    __tablename__ = 'Instant_Temperature'
    time_stamp = Column('TimeDate', DateTime, primary_key=True, index=True)
    channel = Column('Sensor', String(20))
    temperature = Column('Temperature', Float)

class Instant_Humidity(base):
    __tablename__ = 'Instant_Humidity'
    time_stamp = Column('TimeDate', DateTime, primary_key=True, index=True)
    channel = Column('Sensor', String(20))
    temperature = Column('Humidity', Float)

class ControlStatus(base):
    __tablename__ = 'ControlStats'
    time_stamp = Column('TimeDate', DateTime, primary_key=True, index=True)
    heater_state = Column('Heater', Boolean)
    humidifier_state = Column('Humidifier', Boolean)
    fan_state = Column('Fan', Boolean)
    light_state = Column('Light', Boolean)

def Init_Database_Engine(config=None):
    global the_session
    if config:
        database_temp = config.database_loc
        database_loc = "sqlite:///{}".format(database_temp)
    else:
        print("Config Unavailable")
        database_loc = None

    engine = create_engine(database_loc, echo=False) #db address
    log("Connected to", database_loc)
    base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    the_session = session()
    meta = MetaData()
    meta.create_all(engine)

def insert_instant_temp(reading):
    global the_session
    log("Processing", "Writing Temp to Database...")
    the_session.add(reading)
    the_session.commit()
    log("Success", "Write Complete")

def insert_instant_hum(reading):
    global the_session
    log("Processing", "Writing Hum to Database...")
    the_session.add(reading)
    the_session.commit()
    log("Success", "Write Complete")

def insert_control_record(control_data):
    global the_session
    log("Processing", "Writing Control to Database...")
    the_session.add(control_data)
    the_session.commit()
    log("Success", "Write Complete")
    
# def get_last_sensor_rec(self):
#     query = self.the_session.query(Reading).order_by(Reading.time_stamp.desc())
#     last_record = query.first()
#     return last_record

# def get_last_sensor_rec_from(sensor_name):
#     query = self.the_session.query(Reading).filter(Reading.sensor == sensor_name).order_by(Reading.time_stamp.desc()).all()
#     last_record = query[0]
#     return last_record

def get_table():
    global the_session
    query = the_session.query(Instant_Temperature).all()
    return query

# def view_query_dict(self, a_query):
#     print("Printing Each Record Dictionary")
#     for each_record in a_query:
#         print(each_record.__dict__)

def dump_table():
    print("Dumping Table") 
    table = get_table()
    for each in table:
        print("Sensor     : ", each.channel)
        print("Time       : ", each.time_stamp)
        print("Temperature: ", each.temperature)

# def get_last_recs_time(self, mins, sensor_name):
#     last_record = self.get_last_sensor_rec()
#     last_time_stamp = last_record.time_stamp
#     past_time_stamp = last_time_stamp - timedelta(minutes = mins)
#     query = self.the_session.query(Reading).filter(Reading.time_stamp >= past_time_stamp, Reading.sensor == sensor_name).all()
#     return query



# def get_last_record(self):
#     query = self.the_session.query(ControlStatus).order_by(ControlStatus.time_stamp.desc())
#     last_record = query.first()
#     print("HUMstate is: {}".format(last_record.humidifier_state))
#     return last_record

# def get_last_records(self, past_minutes_time):
#     last_record = self.get_last_record()
#     last_time_stamp = last_record.time_stamp
#     past_time_stamp = last_time_stamp - timedelta(minutes = past_minutes_time)
#     query = self.the_session.query(ControlStatus).filter(ControlStatus.time_stamp >= past_time_stamp).all()
#     return query