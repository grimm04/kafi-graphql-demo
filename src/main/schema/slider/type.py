 

import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType  
from graphene import Int, NonNull, ObjectType
from graphene.relay import Connection, Node 

from ..filters import MyFilterableConnectionField

from ...models.Slider import Slider as SliderModel 

class SliderNode(SQLAlchemyObjectType):
    class Meta:
        model = SliderModel
        interfaces = (Node,) 
        connection_field_factory = MyFilterableConnectionField.factory 

class SliderConnection(Connection):
    class Meta:
        node = SliderNode
    
    total_count = NonNull(Int)

    def resolve_total_count(self, info, **kwargs):
        return self.length 

class Slider(SQLAlchemyObjectType):
    class Meta:
        model = SliderModel
        interfaces = (graphene.relay.Node,)

class SliderAttribute:
    id = graphene.Int() 
    title = graphene.String()
    description = graphene.String()  
    image = graphene.String()  
    url = graphene.String()  
    url_label = graphene.String()  
    sort = graphene.Int()  
    active = graphene.String()  

class SliderInput(graphene.InputObjectType, SliderAttribute):
    title = graphene.String(required=True, description="Nama of the Slider.")
    description = graphene.String(description="description of the Slider.")  
    image = graphene.String(required=True, description="Image of the Slider.")
    url = graphene.String(required=True, description="url of the Slider.")
    url_label = graphene.String(required=True, description="url_label of the Slider.")
    sort = graphene.Int(required=True,description="Sort of the Slider.")  
    active = graphene.String(description="Active of the Slider.")  
 
class UpdateSliderInput(graphene.InputObjectType, SliderAttribute):
    """Arguments to update a Slider."""
    id = graphene.ID(required=True, description="Global Id of the Paket.")