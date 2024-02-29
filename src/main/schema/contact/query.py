from sqlalchemy.sql.sqltypes import String
import graphene
from flask import jsonify
from graphene import ObjectType, Field,List, relay, String 
from graphql_relay.node.node import from_global_id
from ...models.Contact import Contact as ContactModel 
from .type import Contact

from ..filters import MyFilterableConnectionField
from .type import ContactConnection,Contact,ContactNode

class Query(ObjectType):
    # Contact = List(Contact)
    # node = relay.Node.Field()  
    # Contact_by_id = Field(Contact, ContactId=graphene.ID())    


    Contact = graphene.relay.Node.Field(ContactNode)
    all_Contact = MyFilterableConnectionField(ContactConnection)
 


 
       
         
 