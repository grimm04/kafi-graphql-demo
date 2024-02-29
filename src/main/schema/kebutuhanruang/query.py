from sqlalchemy.sql.sqltypes import String
import graphene
from flask import jsonify
from graphene import ObjectType, Field,List, relay, String 
from graphql_relay.node.node import from_global_id 

from ..filters import MyFilterableConnectionField

from ...models.KebutuhanRuang import KebutuhanRuang as KebutuhanRuangModel 
from .type import KebutuhanRuangConnection, KebutuhanRuangNode

class Query(ObjectType):
    kebutuhanRuang = graphene.relay.Node.Field(KebutuhanRuangNode)
    all_kebutuhanRuang = MyFilterableConnectionField(KebutuhanRuangConnection)

    