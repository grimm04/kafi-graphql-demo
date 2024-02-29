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

class Portofolio(PrefixerBase):   

    __incomplete_tablename__ = 'portofolio'  
    id = Column(Integer, primary_key=True)
    kuisioner_id = Column(Integer)
    nama = Column(String(100)) 
    gambar = Column(String(1500)) 
    deskripsi = Column(String(1500)) 
    owner = Column(String(200)) 
    luas_lahan   = Column(Integer) 
    luas_bangunan = Column(Integer) 
    lokasi = Column(String(250)) 
    created_at = Column(DateTime, server_default=func.sysdate())
    updated_at = Column(DateTime,default=func.now(),onupdate=datetime.datetime.now)
 