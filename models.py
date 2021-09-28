from sqlalchemy import Column, DateTime, String, Integer, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Alarms(Base):
    __tablename__ = 'alarms'
    id = Column(Integer, primary_key=True)
    alarm_name = Column(String, unique=True)
    cause = Column(String)
    who_to_notify = Column(String)
    notification_end_date = Column(DateTime, default=func.now())
    severity_level = Column(String)
    start_date = Column(DateTime, default=func.now())
    
    def __init__(self, alarm_name, cause, who_to_notify, notification_end_date, severity_level, start_date):
        self.alarm_name = alarm_name
        self.cause = cause
        self.who_to_notify = who_to_notify
        self.notification_end_date = notification_end_date
        self.severity_level = severity_level
        self.start_date = start_date

    def __repr__(self):
        return 'id: {}, root cause: {}'.format(self.id, self.root_cause)
