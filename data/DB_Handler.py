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

base = declarative_base()

class Reading(base):
    __tablename__ = 'Readings'
    time_stamp = Column('TimeDate', DateTime, primary_key=True, index=True)
    sensor = Column('Sensor', String(20))
    temperature = Column('Temperature', Float)
    humidity = Column('Humidity', Float)

class ControlStatus(base):
    __tablename__ = 'ControlStats'
    time_stamp = Column('TimeDate', DateTime, primary_key=True, index=True)
    heater_state = Column('Heater', Boolean)
    humidifier_state = Column('Humidifier', Boolean)
    fan_state = Column('Fan', Boolean)
    light_state = Column('Light', Boolean)

class DB_Manager:
    def __init__(self, config=None):
        if config:
            database_temp = config.database_loc
            database_loc = "sqlite:///{}".format(database_temp)
        else:
            print("Config Unavailable")
            database_loc = None
        self.engine = create_engine(database_loc, echo=False) #db address
        print("Connected to       :", database_loc)
        base.metadata.create_all(self.engine)
        self.session = sessionmaker(bind=self.engine)
        self.the_session = self.session()
        self.meta = MetaData()

class DB_Sensor(DB_Manager):
    def __init__(self, config=None):
        super().__init__(config)

        self.meta.create_all(self.engine)


        #if not self.engine.dialect.has_table(self.engine, Reading.__tablename__): #if table doesn't exist
            #self.meta.create_all(self.engine)

    def insert_record(self, reading):
        print("Processing         : Writing Reading to Database...")
        self.the_session.add(reading)
        self.the_session.commit()
        print("Success            : Write Complete")
        
    def get_last_sensor_rec(self):
        query = self.the_session.query(Reading).order_by(Reading.time_stamp.desc())
        last_record = query.first()
        return last_record

    def get_last_sensor_rec_from(self, sensor_name):
        query = self.the_session.query(Reading).filter(Reading.sensor == sensor_name).order_by(Reading.time_stamp.desc()).all()
        last_record = query[0]
        return last_record

    def get_table(self):
        query = self.the_session.query(Reading).all()
        return query

    def view_query_dict(self, a_query):
        print("Printing Each Record Dictionary")
        for each_record in a_query:
            print(each_record.__dict__)

    def dump_table(self):
        print("Dumping Table") 
        table = self.get_table()
        for each in table:
            print("Sensor     : ", each.sensor)
            print("Time       : ", each.time_stamp)
            print("Temperature: ", each.temperature)
            print("Humidity   : ", each.humidity)

    def get_last_recs_time(self, mins, sensor_name):
        last_record = self.get_last_sensor_rec()
        last_time_stamp = last_record.time_stamp
        past_time_stamp = last_time_stamp - timedelta(minutes = mins)
        query = self.the_session.query(Reading).filter(Reading.time_stamp >= past_time_stamp, Reading.sensor == sensor_name).all()
        return query

class DB_Control(DB_Manager):
    def __init__(self, config=None):
        super().__init__(config)
        if not self.engine.dialect.has_table(self.engine, ControlStatus.__tablename__): #if table doesn't exist
            self.meta.create_all(self.engine)

    def insert_record(self, control):
        print("Processing         : Writing Control to Database...")
        self.the_session.add(control)
        self.the_session.commit()
        print("Success            : Write Complete")

    def get_last_record(self):
        query = self.the_session.query(ControlStatus).order_by(ControlStatus.time_stamp.desc())
        last_record = query.first()
        print("HUMstate is: {}".format(last_record.humidifier_state))
        return last_record

    def get_last_records(self, past_minutes_time):
        last_record = self.get_last_record()
        last_time_stamp = last_record.time_stamp
        past_time_stamp = last_time_stamp - timedelta(minutes = past_minutes_time)
        query = self.the_session.query(ControlStatus).filter(ControlStatus.time_stamp >= past_time_stamp).all()
        return query