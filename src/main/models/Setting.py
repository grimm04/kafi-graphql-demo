import datetime 
from sqlalchemy import func,Column, Integer, String , DateTime, Text,Enum
from sqlalchemy.ext.declarative import declared_attr 
 

from ..database.base import Base 
class PrefixerBase(Base):

    __abstract__ = True

    _the_prefix = 'wskf_'

    @declared_attr
    def __tablename__(cls):
        return cls._the_prefix + cls.__incomplete_tablename__

class Setting(PrefixerBase):   

    __incomplete_tablename__ = 'settings'  
    id = Column(Integer, primary_key=True)
    option = Column(String(250))  
    value = Column(String(250))  
    group = Column(String(250))  
    created_at = Column(DateTime, server_default=func.sysdate())
    updated_at = Column(DateTime,default=func.now(),onupdate=datetime.datetime.now)
 