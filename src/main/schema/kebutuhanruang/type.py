 

import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType  
from graphene import Int, NonNull, ObjectType
from graphene.relay import Connection, Node 

from ..filters import MyFilterableConnectionField

from ...models.KebutuhanRuang import KebutuhanRuang as KebutuhanRuangModel 

class KebutuhanRuangNode(SQLAlchemyObjectType):
    class Meta:
        model = KebutuhanRuangModel
        interfaces = (Node,) 
        connection_field_factory = MyFilterableConnectionField.factory 

class KebutuhanRuangConnection(Connection):
    class Meta:
        node = KebutuhanRuangNode
    
    total_count = NonNull(Int)

    def resolve_total_count(self, info, **kwargs):
        return self.length 

class KebutuhanRuang(SQLAlchemyObjectType):
    class Meta:
        model = KebutuhanRuangModel
        interfaces = (graphene.relay.Node,)

class KebutuhanRuangAttribute:
    id = graphene.Int() 
    label = graphene.String()
    description = graphene.String() 
    order = graphene.Int() 

class KebutuhanRuangInput(graphene.InputObjectType, KebutuhanRuangAttribute):
    label = graphene.String(required=True, description="label of the KebutuhanRuang.")
    description = graphene.String(description="description of the KebutuhanRuang.")  
    order = graphene.Int(description="order of the KebutuhanRuang.")  
 
class UpdateKebutuhanRuangInput(graphene.InputObjectType, KebutuhanRuangAttribute):
    """Arguments to update a KebutuhanRuang."""
    id = graphene.ID(required=True, description="Global Id of the KebutuhanRuang.")