 

import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType 
from graphene import Int, NonNull, ObjectType
from graphene.relay import Connection, Node
from graphene_sqlalchemy import SQLAlchemyObjectType 

from ...models.Contact import Contact as ContactModel

from ..filters import MyFilterableConnectionField

class CountedConnection(Connection):
    class Meta: 
        abstract = True

    total_count = NonNull(Int)

    def resolve_total_count(self, info, **kwargs):
        return self.length


class ContactNode(SQLAlchemyObjectType):
    class Meta:
        model = ContactModel
        interfaces = (Node,) 
        connection_field_factory = MyFilterableConnectionField.factory 

class ContactConnection(Connection):
    class Meta:
        node = ContactNode
    
    total_count = NonNull(Int)

    def resolve_total_count(self, info, **kwargs):
        return self.length


class Contact(SQLAlchemyObjectType):
    class Meta:
        model = ContactModel
        interfaces = (graphene.relay.Node,)

class ContactAttribute:
    contact_id = graphene.Int()  
    nama = graphene.String()
    email = graphene.String()
    company = graphene.String() 
    phone    = graphene.String() 
    message	 = graphene.Int()  

class ContactInput(graphene.InputObjectType, ContactAttribute):
    nama = graphene.String(required=True, description="Nama of the Contact.")
    kuisioner_id = graphene.ID(description="Id Kuisioner of the Contact." ,default=None)
    email = graphene.String(description="E-mail of the Contact.")
    company = graphene.String(description="Company of the Contact.")  
    phone = graphene.String(description="Phone of the Contact.")  
    message = graphene.String(description="Message of the Contact.")   
 
class UpdateContactInput(graphene.InputObjectType, ContactAttribute):
    """Arguments to update a Portofolio."""
    contact_id = graphene.ID(required=True, description="Global Id of the Portofolio.")