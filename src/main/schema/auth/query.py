# /books/schema/query.py

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField
from flask_jwt_extended import (  
    jwt_required,
    current_user
) 

from ..user.type import User
class Query(graphene.ObjectType): 
     
    
    @jwt_required()
    def resolve_me(parent, info):  
        return current_user

 