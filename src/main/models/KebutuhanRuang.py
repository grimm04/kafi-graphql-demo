import datetime
from sqlalchemy import func, Column, Integer, String ,DateTime
from sqlalchemy.ext.declarative import declared_attr


from ..database.base import Base 

class PrefixerBase(Base):

    __abstract__ = True

    _the_prefix = 'wskf_'

    @declared_attr
    def __tablename__(cls):
        return cls._the_prefix + cls.__incomplete_tablename__

class KebutuhanRuang(PrefixerBase):   

    __incomplete_tablename__ = 'kebutuhan_ruang'  
    id = Column(Integer, primary_key=True)
    label = Column(String(150)) 
    description = Column(String(1500)) 
    order = Column(Integer) 
    created_at = Column(DateTime, server_default=func.sysdate())
    updated_at = Column(DateTime,default=func.now(),onupdate=datetime.datetime.now)
     
 