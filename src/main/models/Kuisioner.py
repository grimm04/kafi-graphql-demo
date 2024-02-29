import datetime
from sqlalchemy import  func,Column, Integer, String ,ForeignKey,Text,Enum,DateTime
from sqlalchemy.ext.declarative import declared_attr


from ..database.base import Base 

class PrefixerBase(Base):

    __abstract__ = True

    _the_prefix = 'wskf_'

    @declared_attr
    def __tablename__(cls):
        return cls._the_prefix + cls.__incomplete_tablename__

class Kuisioner(PrefixerBase):   

    __incomplete_tablename__ = 'kuisioner'  
    id = Column(Integer, primary_key=True)
    nama = Column(String(200)) 
    provinsi = Column(String(250))
    kab_kota = Column(String(250))
    no_wa = Column(String(50)) 
    email = Column(String(50))  
    jenis_kelamin = Column(String(200)) 
    anggota_keluarga = Column(String(200))  
    kendaraan = Column(String(200)) 
    luas_lahan = Column(String(200)) 
    sketsa_lahan  = Column(String(200)) 
    video_lahan   = Column(String(200)) 
    jumlah_lantai   = Column(String(200)) 
    minat_tema_bangunan   = Column(String(200)) 
    kebutuhan_ruanglain   = Column(String(200)) 
    catatan = Column(String(1500))
    pilihan_desain = Column(String(1500)) 
    gambar_fasad = Column(String(1500)) 
    budget = Column(Integer)
    luas_bangunan = Column(Integer)
    anggota_keluarga_jml_anak = Column(Integer)
    kendaraan_r2_jml = Column(Integer)
    kendaraan_r4_jml = Column(Integer) 
    anggota_keluarga_lainnya = Column(String(200)) 
    kendaraan_r2_merk = Column(String(200)) 
    kendaraan_r4_merk = Column(String(200)) 
    paket = Column(String(200)) 
    harga = Column(Integer) 
    paket_id = Column(Integer, ForeignKey('wskf_paket.id'),
        nullable=False)
    status = Column(Enum('new','progress','done', name='status'), default='new') 

    created_at = Column(DateTime, server_default=func.sysdate())
    updated_at = Column(DateTime,default=func.now(),onupdate=datetime.datetime.now)
 