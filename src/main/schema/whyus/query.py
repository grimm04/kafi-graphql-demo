from sqlalchemy.sql.sqltypes import String
import graphene
from flask import jsonify
from graphene import ObjectType, Field,List, relay, String 
from graphql_relay.node.node import from_global_id 

from ..filters import MyFilterableConnectionField

from ...models.Whyus import Whyus as WhyusModel 
from .type import WhyusConnection, WhyusNode

class Query(ObjectType):
    whyus = graphene.relay.Node.Field(WhyusNode)
    all_whyus = MyFilterableConnectionField(WhyusConnection)

    # paket = List(Paket)
    # node = relay.Node.Field()  
    # paket_by_id = Field(Paket, paketId=graphene.ID())    

    #getall 
    # def resolve_paket(root, info):
    #     paket_query = Paket.get_query(info)  
    #     return paket_query

    #getbyID 
    # def resolve_paket_by_id(root, info, **args):
    #     paketId = args.get('paketId') 
    #     paket_query = Paket.get_query(info)    
    #     # return paket_query 
    #     return paket_query.filter(PaketModel.id.contains(from_global_id(paketId)[1])).first()
 
 


 
       
         
 