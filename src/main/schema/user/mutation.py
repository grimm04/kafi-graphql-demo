 
 
import graphene 
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from graphql_relay.node.node import from_global_id

from ...database.db_session import db_session 
from ...utils.input_to_dictionary import input_to_dictionary


from ...models.User import User as UserModel 
from .type import User, UserInput, UpdateUserInput,UserUpdatePasswordInput
from ...utils.extensions import bcrypt

# class ProtectedUser(graphene.Union):
#     class Meta:
#         types = (User,AuthInfoField)

class CreateUser(graphene.Mutation):
    user = graphene.Field(lambda: User)
    ok = graphene.Boolean()
    msg = graphene.String()

    class Arguments: 
        input = UserInput(required=True)

    @jwt_required()
    def mutate(self, info, input):
        data = input_to_dictionary(input) 

        user_query = User.get_query(info)  
        user = user_query.filter(UserModel.username.contains(data['username'])).first()
        if user:
            ok = False
            msg = "User alrady exist"
            return CreateUser(user=user,ok=ok,msg=msg) 

        user = UserModel(**data)
        db_session.add(user) 
        db_session.commit()
        ok = True 
        msg = "User saved"
        return CreateUser(user=user, ok=ok,msg=msg)


# update existing User
class updateUser(graphene.Mutation):
     
    ok = graphene.Boolean()
    msg = graphene.String()
    user = graphene.Field(lambda: User, description="User updated by this mutation.") 

    class Arguments:
        input = UpdateUserInput(required=True) 
  
    @jwt_required()
    def mutate(self, info, input):
         
        data = input_to_dictionary(input)  
        
        user = db_session.query(UserModel).filter_by(id=data['id'])
         
        if user:  
            user.update(data)   
            db_session.commit()  
            ok = True 
            msg = "user updated!" 
            user = db_session.query(UserModel).filter_by(id=data['id']).first()
            return updateUser(ok=ok, user=user,msg=msg) 

        ok = False  
        msg = "user not found!" 
        return updateUser(ok=ok,msg=msg,user=user)   

        


# delete User
class deleteUser(graphene.Mutation):
    
    class Arguments:
        id = graphene.String(required=True)  

    ok = graphene.Boolean()
    msg = graphene.String()
    user = graphene.Field(lambda: User, description="User Delete by this mutation.")
 
    @jwt_required()
    def mutate(root, info, id):
        userId = from_global_id(id)[1]
        user = db_session.query(UserModel).filter_by(id=userId).first()
        if user:
            db_session.delete(user) 
            db_session.commit()
            ok = True  
            msg = "user deleted!" 
            return deleteUser(ok=ok,msg=msg)

        ok = False
        msg = "User Not Found" 
        return deleteUser(ok=ok,msg=msg)


# update existing UserPassword
class updateUserPassword(graphene.Mutation):
     
    ok = graphene.Boolean()
    msg = graphene.String()
    user = graphene.Field(lambda: User, description="User updated by this mutation.") 

    class Arguments:
        input = UserUpdatePasswordInput(required=True) 
  
    @jwt_required()
    def mutate(self, info, input):
         
        data = input_to_dictionary(input)  
        
        user = UserModel.query.filter_by(id=data['id']).first() 
        if user:  
            if user is not None and user.check_password(data['password_lama']):  
                if data['password_baru1'] != data['password_baru2']:
                    ok = False 
                    msg = "Password tidak sama!" 
                    return updateUserPassword(ok=ok,msg=msg) 
                 
                user.password =  bcrypt.generate_password_hash(data['password_baru1']) 
                db_session.add(user)  
                db_session.commit()
                ok = True 
                msg = "Password berhasil diubah!"  
                return updateUserPassword(ok=ok, user=user,msg=msg)  
            ok = False 
            msg = "Password Salah!" 
            return updateUserPassword(ok=ok,msg=msg) 

        ok = False  
        msg = "User Tidak Ada!" 
        return updateUserPassword(ok=ok,msg=msg,user=user)   


class Mutation(graphene.ObjectType):
    createUser = CreateUser.Field()
    updateUser = updateUser.Field()
    deleteUser = deleteUser.Field()
    updateUserPassword = updateUserPassword.Field()