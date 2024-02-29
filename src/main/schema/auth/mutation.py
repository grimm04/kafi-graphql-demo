# /books/schema/mutation.py
 
import graphene
from flask_jwt_extended import ( 
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required
)
 
from ...database.db_session import db_session 
from ...utils.input_to_dictionary import input_to_dictionary


from ...models.User import User as UserModel
from ..user.type import User, UserInput, UpdateUserInput
from ...utils.extensions import bcrypt  

class AuthMutation(graphene.Mutation):
    access_token = graphene.String()
    refresh_token = graphene.String()

    class Arguments:
        username = graphene.String()
        password = graphene.String()
    
    def mutate(self, info , username, password) :
         
        user = UserModel.query.filter_by(username=username).one_or_none() 
        if not user:
            raise Exception('Authenication Failure : User is not registered')
        if user.check_password(password):
            username =user.username
            return AuthMutation(
                access_token = create_access_token(identity=username),
                refresh_token = create_refresh_token(identity=username)
            )
        raise Exception('Authenication Failure : Incorrect password')

# refress
class RefreshMutation(graphene.Mutation):

    class Arguments(object):
        pass

    new_token = graphene.String()

    @jwt_required(refresh=True)
    def mutate(self,info):
        username = get_jwt_identity() 
        new_token = create_access_token(identity=username)
        return RefreshMutation(new_token=new_token)
        
class Mutation(graphene.ObjectType):
    auth = AuthMutation.Field() 
    refresh = RefreshMutation.Field() ## this is added