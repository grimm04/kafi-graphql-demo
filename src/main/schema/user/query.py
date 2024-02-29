# /books/schema/query.py

from sqlalchemy.orm.base import NOT_EXTENSION
from sqlalchemy.sql.functions import user
from sqlalchemy.sql.sqltypes import String
import graphene
from flask import jsonify
from graphene import ObjectType, Field,List, relay, String
from graphene_sqlalchemy import SQLAlchemyConnectionField
from graphql import GraphQLError 
from graphql_relay.node.node import from_global_id  
from flask_jwt_extended import (  
    jwt_required,
    current_user,
    get_jwt_identity
)
from ..filters import MyFilterableConnectionField

from ...models.User import User as UserModel 
from .type import UserConnection,User,UserNode


class Query(ObjectType): 
    # user_by_id = Field(User, userId=graphene.Int())  
    # 
    #  
    user = Field(User, userId=graphene.ID())     
    all_users = MyFilterableConnectionField(UserConnection) 

    @jwt_required()
    def resolve_user(root, info,**args): 
        userId = args.get('userId') 
        user_query = User.get_query(info)     
        return user_query.filter(UserModel.id.contains(from_global_id(userId)[1])).first()

    @jwt_required()
    def resolve_all_users(root, info,**args):  
        filters = args.get('filters')
        user_query = UserNode.get_query(info)   
        if filters is not None: 
            username = ''
            fullname = ''
            if 'fullname_likeall' in filters :
                fullname = filters['fullname_likeall']
            if 'username_likeall' in filters  :  
                username = filters['username_likeall']
            user_query = user_query.filter(UserModel.fullname.contains(fullname), UserModel.username.contains(username)).all()
        return user_query  

    user_login = Field(lambda : User) 
    
    @jwt_required()
    def resolve_user_login(root, info): 
        current_user = get_jwt_identity() 
        if current_user is None:
            raise GraphQLError('You must be logged!')

        user_query = User.get_query(info)  
        return user_query.filter(UserModel.username.contains(current_user)).first() 


 
  
         
 