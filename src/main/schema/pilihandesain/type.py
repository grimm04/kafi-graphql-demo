 

import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType  
from graphene import Int, NonNull, ObjectType
from graphene.relay import Connection, Node 

from ..filters import MyFilterableConnectionField

from ...models.PilihanDesain import PilihanDesain as PilihanDesainModel 

class PilihanDesainNode(SQLAlchemyObjectType):
    class Meta:
        model = PilihanDesainModel
        interfaces = (Node,) 
        connection_field_factory = MyFilterableConnectionField.factory 

class PilihanDesainConnection(Connection):
    class Meta:
        node = PilihanDesainNode
    
    total_count = NonNull(Int)

    def resolve_total_count(self, info, **kwargs):
        return self.length 

class PilihanDesain(SQLAlchemyObjectType):
    class Meta:
        model = PilihanDesainModel
        interfaces = (graphene.relay.Node,)

class PilihanDesainAttribute:
    id = graphene.Int() 
    title = graphene.String() 
    image = graphene.String()   

class PilihanDesainInput(graphene.InputObjectType, PilihanDesainAttribute):
    title = graphene.String(required=True, description="Nama of the PilihanDesain.") 
    image = graphene.String(required=True, description="Image of the PilihanDesain.") 
 
class UpdatePilihanDesainInput(graphene.InputObjectType, PilihanDesainAttribute):
    """Arguments to update a PilihanDesain."""
    id = graphene.ID(required=True, description="Global Id of the Paket.")