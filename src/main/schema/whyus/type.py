 

import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType  
from graphene import Int, NonNull, ObjectType
from graphene.relay import Connection, Node 

from ..filters import MyFilterableConnectionField

from ...models.Whyus import Whyus as WhyusModel 

class WhyusNode(SQLAlchemyObjectType):
    class Meta:
        model = WhyusModel
        interfaces = (Node,) 
        connection_field_factory = MyFilterableConnectionField.factory 

class WhyusConnection(Connection):
    class Meta:
        node = WhyusNode
    
    total_count = NonNull(Int)

    def resolve_total_count(self, info, **kwargs):
        return self.length 

class Whyus(SQLAlchemyObjectType):
    class Meta:
        model = WhyusModel
        interfaces = (graphene.relay.Node,)

class WhyusAttribute:
    id = graphene.Int() 
    title = graphene.String()
    description = graphene.String()  
    image = graphene.String()  
    sort = graphene.Int()  
    active = graphene.String()  

class WhyusInput(graphene.InputObjectType, WhyusAttribute):
    title = graphene.String(required=True, description="Nama of the Whyus.")
    description = graphene.String(description="description of the Whyus.")  
    image = graphene.String(required=True, description="Image of the Whyus.")
    sort = graphene.Int(required=True,description="Sort of the Whyus.")  
    active = graphene.String(description="Active of the Whyus.")  
 
class UpdateWhyusInput(graphene.InputObjectType, WhyusAttribute):
    """Arguments to update a Whyus."""
    id = graphene.ID(required=True, description="Global Id of the Paket.")