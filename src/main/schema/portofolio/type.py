 

import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType 
from graphene import Int, NonNull, ObjectType
from graphene.relay import Connection, Node
from graphene_sqlalchemy import SQLAlchemyObjectType 

from ...models.Portofolio import Portofolio as PortofolioModel

from ..filters import MyFilterableConnectionField

class CountedConnection(Connection):
    class Meta: 
        abstract = True

    total_count = NonNull(Int)

    def resolve_total_count(self, info, **kwargs):
        return self.length


class PortofolioNode(SQLAlchemyObjectType):
    class Meta:
        model = PortofolioModel
        interfaces = (Node,) 
        connection_field_factory = MyFilterableConnectionField.factory 

class PortofolioConnection(Connection):
    class Meta:
        node = PortofolioNode
    
    total_count = NonNull(Int)

    def resolve_total_count(self, info, **kwargs):
        return self.length


class Portofolio(SQLAlchemyObjectType):
    class Meta:
        model = PortofolioModel
        interfaces = (graphene.relay.Node,)

class PortofolioAttribute:
    id = graphene.Int() 
    kuisioner_id = graphene.Int() 
    nama = graphene.String()
    gambar = graphene.String()
    deskripsi = graphene.String() 
    owner    = graphene.String() 
    luas_lahan	 = graphene.Int() 
    luas_bangunan    = graphene.Int() 
    lokasi = graphene.String() 

class PortofolioInput(graphene.InputObjectType, PortofolioAttribute):
    nama = graphene.String(required=True, description="Nama of the Portofolio.")
    kuisioner_id = graphene.ID(description="Id Kuisioner of the Portofolio." ,default=None)
    gambar = graphene.String(description="Gambar of the Portofolio.")
    deskripsi = graphene.String(description="Deskripsi of the Portofolio.")  
    owner = graphene.String(description="owner of the Portofolio.")  
    luas_lahan = graphene.String(description="luas_lahan of the Portofolio.")  
    luas_bangunan = graphene.String(description="luas_bangunan of the Portofolio.")  
    lokasi = graphene.String(description="lokasi of the Portofolio.")  
 
class UpdatePortofolioInput(graphene.InputObjectType, PortofolioAttribute):
    """Arguments to update a Portofolio."""
    id = graphene.ID(required=True, description="Global Id of the Portofolio.")