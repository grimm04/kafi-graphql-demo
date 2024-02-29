 

import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType     
from graphene import Int, NonNull, ObjectType
from graphene.relay import Connection, Node 

from ..filters import MyFilterableConnectionField

from ...models.Kuisioner import Kuisioner as KuisionerModel 

class KuisionerNode(SQLAlchemyObjectType):
    class Meta:
        model = KuisionerModel
        interfaces = (Node,) 
        connection_field_factory = MyFilterableConnectionField.factory 

class KuisionerConnection(Connection):
    class Meta:
        node = KuisionerNode
    
    total_count = NonNull(Int)

    def resolve_total_count(self, info, **kwargs):
        return self.length 

class Kuisioner(SQLAlchemyObjectType):
    class Meta:
        model = KuisionerModel
        interfaces = (graphene.relay.Node,)

class KuisionerAttribute:
    id = graphene.Int() 
    nama = graphene.String()
    gambar = graphene.String()
    deskripsi = graphene.String()  
    kab_kota = graphene.String()
    provinsi = graphene.String()
    no_wa = graphene.String() 
    email = graphene.String()  
    jenis_kelamin = graphene.String()
    anggota_keluarga = graphene.String()  
    kendaraan = graphene.String() 
    luas_lahan = graphene.String() 
    sketsa_lahan  = graphene.String() 
    video_lahan   = graphene.String() 
    jumlah_lantai   = graphene.Int()
    minat_tema_bangunan   = graphene.String() 
    kebutuhan_ruanglain   = graphene.String() 
    catatan = graphene.String()
    pilihan_desain = graphene.String() 
    gambar_fasad = graphene.String() 
    budget = graphene.Int()
    luas_bangunan = graphene.Int()
    paket = graphene.String() 
    paket_id =graphene.Int()
    status = graphene.String()  
    anggota_keluarga_jml_anak = graphene.Int() 
    anggota_keluarga_lainnya = graphene.String() 
    kendaraan_r2_merk = graphene.String() 
    kendaraan_r2_jml = graphene.Int()
    kendaraan_r4_merk = graphene.String() 
    kendaraan_r4_jml = graphene.Int() 


class KuisionerInput(graphene.InputObjectType, KuisionerAttribute):
    nama = graphene.String(required=True, description="Nama of the Kuisioner.") 
    kab_kota =  graphene.String( description="Kabupaten Kota of the Kuisioner.") 
    provinsi =  graphene.String( description="Provinsi of the Kuisioner.") 
    no_wa = graphene.String( description="Nomor Whatsapp of the Kuisioner.") 
    email = graphene.String( description="Email of the Kuisioner.") 
    jenis_kelamin = graphene.String( description="Jenis Kelamin of the Kuisioner.") 
    anggota_keluarga = graphene.String( description="Anggota Keluarga of the Kuisioner.") 
    kendaraan = graphene.String( description="Kendaraan of the Kuisioner.") 
    luas_lahan = graphene.String( description="Luas Lahan of the Kuisioner.") 
    sketsa_lahan  = graphene.String( description="Sketsa Lahan of the Kuisioner.") 
    video_lahan   = graphene.String( description="Video Lahan of the Kuisioner.") 
    jumlah_lantai   = graphene.String( description="Jumlah Lantai of the Kuisioner.") 
    minat_tema_bangunan   = graphene.String( description="Minat Bangunan of the Kuisioner.")  
    kebutuhan_ruanglain   =  graphene.String( description="Kebutuhan Ruangan lain of the Kuisioner.") 
    catatan = graphene.String( description="Catatan of the Kuisioner.") 
    pilihan_desain = graphene.String( description="Pilihan Desain of the Kuisioner.") 
    gambar_fasad = graphene.String( description="Gambar Fasad of the Kuisioner.") 
    budget = graphene.Int( description="Budget of the Kuisioner.") 
    luas_bangunan = graphene.Int( description="Luas Bangunan of the Kuisioner.") 
    anggota_keluarga_jml_anak = graphene.Int(required=True, description="anggota_keluarga_jml_anak of the Kuisioner.") 
    anggota_keluarga_lainnya = graphene.String(required=True, description="anggota_keluarga_lainnya of the Kuisioner.") 
    kendaraan_r2_merk = graphene.String(required=True, description="Nama of the Kuisioner.") 
    kendaraan_r2_jml = graphene.Int(required=True, description="kendaraan_r2_jml of the Kuisioner.") 
    kendaraan_r4_merk = graphene.String(required=True, description="kendaraan_r4_merk of the Kuisioner.") 
    kendaraan_r4_jml = graphene.Int(required=True, description="kendaraan_r4_jml of the Kuisioner.") 
    harga = graphene.Int(required=True, description="Harga of the Kuisioner.") 
    paket = graphene.String(required=True, description="Nama Paket of the Kuisioner.") 
    paket_id = graphene.ID(required=True, description="Paket ID of the Kuisioner.") 
    status = graphene.String(description="Nama status of the Kuisioner.") 
 
class UpdateKuisionerInput(graphene.InputObjectType, KuisionerAttribute):
    """Arguments to update a Kuisioner."""
    id = graphene.ID(required=True, description="Global Id of the Kuisioner.")

 
    