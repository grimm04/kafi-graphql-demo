# /books/types/admProvinsi.py

import graphene 
from ...models.User import User as UserModel
from graphene import Int, NonNull, ObjectType
from graphene.relay import Connection, Node
from graphene_sqlalchemy import SQLAlchemyObjectType 


from ..filters import MyFilterableConnectionField

  
 
class UserNode(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (Node,) 
        connection_field_factory = MyFilterableConnectionField.factory 

class UserConnection(Connection):
    class Meta:
        node = UserNode
    
    total_count = NonNull(Int)

    def resolve_total_count(self, info, **kwargs):
        return self.length


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        exclude_fields = ('created_at', 'updated_at')
        filter_fields = ('username', )
        interfaces = (graphene.relay.Node,)  
     
class UserAttribute:
    id = graphene.Int() 
    fullname = graphene.String()
    avatar = graphene.String()
    username = graphene.String()
    password =graphene.String()
    email =graphene.String() 

class UserInput(graphene.InputObjectType, UserAttribute):
    fullname = graphene.String(required=True, description="Fullname of the User.")
    avatar = graphene.String(description="Avatar of the User.")
    username = graphene.String(required=True, description="Username of the User.")
    password =graphene.String(required=True,description="Passoword of the User.")
    email =graphene.String(required=True, description="Email of the User.")  

class UserUpdatePasswordInput(graphene.InputObjectType):
    id = graphene.ID(required=True, description="Global Id of the User.")
    password_lama = graphene.String(required=True, description="Password Lama of the User.")
    password_baru1 = graphene.String(required=True, description="Password Baru of the User.") 
    password_baru2 = graphene.String(required=True, description="Password Baru of the User.") 

class UpdateUserInput(graphene.InputObjectType, UserAttribute):
    """Arguments to update a User."""
    id = graphene.ID(required=True, description="Global Id of the User.")