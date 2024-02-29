from sqlalchemy.sql.sqltypes import String
import graphene
from flask import jsonify
from graphene import ObjectType, Field,List, relay, String 
from graphql_relay.node.node import from_global_id 

from ..filters import MyFilterableConnectionField

from ...models.Paket import Paket as PaketModel 
from .type import PaketConnection, PaketNode

class Query(ObjectType):
    paket = graphene.relay.Node.Field(PaketNode)
    all_paket = MyFilterableConnectionField(PaketConnection)

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
 
 


 
       
         
 