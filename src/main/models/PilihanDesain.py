import datetime 
from sqlalchemy import func,Column, Integer, String , DateTime
from sqlalchemy.ext.declarative import declared_attr


from ..database.base import Base 

 

class PrefixerBase(Base):

    __abstract__ = True

    _the_prefix = 'wskf_'

    @declared_attr
    def __tablename__(cls):
        return cls._the_prefix + cls.__incomplete_tablename__

class PilihanDesain(PrefixerBase):   

    __incomplete_tablename__ = 'pilihandesain'  
    id = Column(Integer, primary_key=True)
    title = Column(String(100))  
    image = Column(String(1500))   
    created_at = Column(DateTime, server_default=func.sysdate())
    updated_at = Column(DateTime,default=func.now(),onupdate=datetime.datetime.now)
 