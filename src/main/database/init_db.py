
from .db_session import db_session, engine
from .base import Base

from ..utils.extensions import bcrypt 

def init_db(): 
    from ..models.User import User 
    from ..models.Paket import Paket 
    from ..models.Produk import Produk 
    from ..models.Kuisioner import Kuisioner 

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    bronze = Paket(nama='Bronze')
    db_session.add(bronze) 

    
    produk1 = Produk(nama='Test')
    db_session.add(produk1) 

    # bandungbarat = AdmKabkota(kabkota='Bandung Barat', provinsi=jawabarat)
    # db_session.add(bandungbarat) 

    # kecamatan = AdmKecamatan(kecamatan='Padalarang', kabkota=bandungbarat)
    # db_session.add(kecamatan) 

    pw_hash = bcrypt.generate_password_hash('secret')

    user = User(fullname='SyahrilRamdani',username="grimm",password=pw_hash,email="grimm@gmail.com")
    db_session.add(user) 

    db_session.commit()