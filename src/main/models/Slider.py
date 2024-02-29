import datetime 
from sqlalchemy import func,Column, Integer, String , DateTime, Enum
from sqlalchemy.ext.declarative import declared_attr


from ..database.base import Base 

 

class PrefixerBase(Base):

    __abstract__ = True

    _the_prefix = 'wskf_'

    @declared_attr
    def __tablename__(cls):
        return cls._the_prefix + cls.__incomplete_tablename__

class Slider(PrefixerBase):   

    __incomplete_tablename__ = 'sliders'  
    id = Column(Integer, primary_key=True)
    title = Column(String(200)) 
    description = Column(String(1500)) 
    image = Column(String(1500)) 
    url = Column(String(200)) 
    url_label = Column(String(200)) 
    sort = Column(Integer) 
    active = Column(Enum('Yes','No',name='active_types'), default='Yes') 
    created_at = Column(DateTime, server_default=func.sysdate())
    updated_at = Column(DateTime,default=func.now(),onupdate=datetime.datetime.now)
 