 

import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType  
from graphene import Int, NonNull, ObjectType
from graphene.relay import Connection, Node 

from ..filters import MyFilterableConnectionField

from ...models.Setting import Setting as SettingModel 

class SettingNode(SQLAlchemyObjectType):
    class Meta:
        model = SettingModel
        interfaces = (Node,) 
        connection_field_factory = MyFilterableConnectionField.factory 

class SettingConnection(Connection):
    class Meta:
        node = SettingNode
    
    total_count = NonNull(Int)

    def resolve_total_count(self, info, **kwargs):
        return self.length 

class Setting(SQLAlchemyObjectType):
    class Meta:
        model = SettingModel
        interfaces = (graphene.relay.Node,)

class SettingAttribute:
    id = graphene.Int() 
    option = graphene.String()
    value = graphene.String()
    group = graphene.String()  

class SettingInput(graphene.InputObjectType, SettingAttribute):
    option = graphene.String(required=True, description="Option of the Setting.")
    value = graphene.String(description="Value of the Setting.")  
    group = graphene.String(description="Group of the Setting.")   
 
class UpdateSettingInput(graphene.InputObjectType, SettingAttribute):
    """Arguments to update a Setting."""
    id = graphene.ID(required=True, description="Global Id of the Setting.")