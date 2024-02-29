from sqlalchemy.sql.sqltypes import String
import graphene
from flask import jsonify
from graphene import ObjectType, Field,List, relay, String 
from graphql_relay.node.node import from_global_id
from ...models.Portofolio import Portofolio as PortofolioModel 
from .type import Portofolio

from ..filters import MyFilterableConnectionField
from .type import PortofolioConnection,Portofolio,PortofolioNode

class Query(ObjectType):
    # Portofolio = List(Portofolio)
    # node = relay.Node.Field()  
    # Portofolio_by_id = Field(Portofolio, PortofolioId=graphene.ID())    


    Portofolio = graphene.relay.Node.Field(PortofolioNode)
    all_Portofolio = MyFilterableConnectionField(PortofolioConnection)
 


 
       
         
 