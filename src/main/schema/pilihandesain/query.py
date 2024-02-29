from sqlalchemy.sql.sqltypes import String
import graphene
from flask import jsonify
from graphene import ObjectType, Field,List, relay, String 
from graphql_relay.node.node import from_global_id 

from ..filters import MyFilterableConnectionField

from ...models.PilihanDesain import PilihanDesain as PilihanDesainModel 
from .type import PilihanDesainConnection, PilihanDesainNode

class Query(ObjectType):
    PilihanDesain = graphene.relay.Node.Field(PilihanDesainNode)
    all_PilihanDesain = MyFilterableConnectionField(PilihanDesainConnection) 
 


 
       
         
 