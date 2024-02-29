from sqlalchemy.sql.sqltypes import String
import graphene
from flask import jsonify
from graphene import ObjectType, Field,List, relay, String 
from graphql_relay.node.node import from_global_id

from ..filters import MyFilterableConnectionField

from ...models.Kuisioner import Kuisioner as KuisionerModel 
from .type import KuisionerConnection, KuisionerNode

class Query(ObjectType):
    kuisioner = graphene.relay.Node.Field(KuisionerNode)
    all_kuisioner = MyFilterableConnectionField(KuisionerConnection)

    # kuisioner = List(Kuisioner)
    # node = relay.Node.Field()  
    # kuisioner_by_id = Field(Kuisioner, kuisionerId=graphene.ID())    

    # #getall 
    # def resolve_kuisioner(root, info):
    #     kuisioner_query = Kuisioner.get_query(info)  
    #     return kuisioner_query

    # #getbyID
    # def resolve_kuisioner_by_id(root, info, **args):
    #     kuisionerId = args.get('kuisionerId') 
    #     kuisioner_query = Kuisioner.get_query(info)    
    #     # return kuisioner_query 
    #     return kuisioner_query.filter(KuisionerModel.id.contains(from_global_id(kuisionerId)[1])).first()
 
 


 
       
         
 