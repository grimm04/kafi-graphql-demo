 

import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType  
from graphene import Int, NonNull, ObjectType
from graphene.relay import Connection, Node 

from ..filters import MyFilterableConnectionField

from ...models.Paket import Paket as PaketModel 

class PaketNode(SQLAlchemyObjectType):
    class Meta:
        model = PaketModel
        interfaces = (Node,) 
        connection_field_factory = MyFilterableConnectionField.factory 

class PaketConnection(Connection):
    class Meta:
        node = PaketNode
    
    total_count = NonNull(Int)

    def resolve_total_count(self, info, **kwargs):
        return self.length 

class Paket(SQLAlchemyObjectType):
    class Meta:
        model = PaketModel
        interfaces = (graphene.relay.Node,)

class PaketAttribute:
    id = graphene.Int() 
    nama = graphene.String()
    deskripsi = graphene.String() 
    details = graphene.String() 
    harga = graphene.Int() 

class PaketInput(graphene.InputObjectType, PaketAttribute):
    nama = graphene.String(required=True, description="Nama of the Paket.")
    deskripsi = graphene.String(description="Deskripsi of the Paket.")  
    details = graphene.String(description="Details of the Paket.")  
    harga = graphene.Int(description="harga of the Paket.")  
 
class UpdatePaketInput(graphene.InputObjectType, PaketAttribute):
    """Arguments to update a Paket."""
    id = graphene.ID(required=True, description="Global Id of the Paket.")