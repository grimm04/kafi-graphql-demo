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

class Paket(PrefixerBase):   

    __incomplete_tablename__ = 'paket'  
    id = Column(Integer, primary_key=True)
    nama = Column(String(100)) 
    deskripsi = Column(String(1500)) 
    details = Column(String(1500)) 
    harga = Column(Integer) 
    created_at = Column(DateTime, server_default=func.sysdate())
    updated_at = Column(DateTime,default=func.now(),onupdate=datetime.datetime.now)
     
 