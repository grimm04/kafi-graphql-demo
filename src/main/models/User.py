import datetime 
from sqlalchemy import func, Column, Integer, String , DateTime
from sqlalchemy.ext.declarative import declared_attr
 

from ..database.base import Base
from ..utils.extensions import bcrypt


class PrefixerBase(Base):

    __abstract__ = True

    _the_prefix = 'wskf_'

    @declared_attr
    def __tablename__(cls):
        return cls._the_prefix + cls.__incomplete_tablename__

class User(PrefixerBase):

    __incomplete_tablename__ = 'user'  

    id = Column(Integer, primary_key=True)
    fullname = Column(String(100)) 
    username = Column(String(20),unique=True,nullable=False)
    email = Column(String(100))
    avatar = Column(String(100)) 
    password = Column(String(100),nullable=False)
    created_at = Column(DateTime, server_default=func.sysdate())
    updated_at = Column(DateTime,default=func.now(),onupdate=datetime.datetime.now)
     

    def set_password(self, password):
        """Create hashed password."""
        self.password = bcrypt.generate_password_hash(
            password 
        )

    def check_password(self, password):
        """Check hashed password."""
        return bcrypt.check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

