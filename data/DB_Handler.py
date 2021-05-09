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
    time_stamp = Column('Time_Date', DateTime, primary_key=True, index=True)
    channel = Column('Channel', String(20))
    temperature = Column('Temperature', Float)

class Instant_Humidity(base):
    __tablename__ = 'Instant_Humidity'
    time_stamp = Column('Time_Date', DateTime, primary_key=True, index=True)
    channel = Column('Channel', String(20))
    temperature = Column('Humidity', Float)

class Control_Status(base):
    __tablename__ = 'ControlStats'
    time_stamp = Column('Time_Date', DateTime, primary_key=True, index=True)
    heater_state = Column('Heater', Boolean)
    humidifier_state = Column('Humidifier', Boolean)
    fan_state = Column('Fan', Boolean)
    light_state = Column('Light', Boolean)

def init_database_engine(config=None):
    global the_session
    if config:
        database_temp = config.database_loc
        database_loc = "sqlite:///{}".format(database_temp)
    else:
        print("Config Unavailable")
        database_loc = None
    engine = create_engine(database_loc, connect_args={'check_same_thread': False}, echo=False)
    log("Connected to", database_loc)
    base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    the_session = session()
    meta = MetaData()
    meta.create_all(engine)

def insert_instant_temp(reading):
    global the_session
    the_session.add(reading)
    the_session.commit()

def insert_instant_hum(reading):
    global the_session
    the_session.add(reading)
    the_session.commit()

def insert_control_record(control_data):
    global the_session
    the_session.add(control_data)
    the_session.commit()

def get_last_temp_rec(channel):
    global the_session
    query = the_session.query(Instant_Temperature).filter(Instant_Temperature.channel == channel).order_by(Instant_Temperature.time_stamp.desc()).all()
    last_record = query[0]
    return last_record

def get_last_temp_list(channel, time):
    global the_session
    last_record = get_last_temp_rec(channel)
    last_time_stamp = last_record.time_stamp
    past_time_stamp = last_time_stamp - timedelta(minutes = time)
    query = the_session.query(Instant_Temperature).filter(Instant_Temperature.time_stamp >= past_time_stamp, Instant_Temperature.channel == channel).all()
    return query

def get_last_humid_rec(channel):
    global the_session
    query = the_session.query(Instant_Humidity).filter(Instant_Humidity.channel == channel).order_by(Instant_Humidity.time_stamp.desc()).all()
    last_record = query[0]
    return last_record

def get_last_humid_list(channel, time):
    global the_session
    last_record = get_last_humid_rec(channel)
    last_time_stamp = last_record.time_stamp
    past_time_stamp = last_time_stamp - timedelta(minutes = time)
    query = the_session.query(Instant_Humidity).filter(Instant_Humidity.time_stamp >= past_time_stamp, Instant_Humidity.channel == channel).all()
    return query