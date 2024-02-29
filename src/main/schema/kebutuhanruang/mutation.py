
 
import graphene  
from flask_jwt_extended import jwt_required
from graphql_relay.node.node import from_global_id

from ...database.db_session import db_session 
from ...utils.input_to_dictionary import input_to_dictionary


from ...models.KebutuhanRuang import KebutuhanRuang as KebutuhanRuangModel
from .type import KebutuhanRuang, KebutuhanRuangInput, UpdateKebutuhanRuangInput 

class createKebutuhanRuang(graphene.Mutation):
    kebutuhanruang = graphene.Field(lambda: KebutuhanRuang)
    ok = graphene.Boolean()
    msg = graphene.String()

    class Arguments: 
        input =KebutuhanRuangInput(required=True)

    @jwt_required()
    def mutate(self, info, input):
        data = input_to_dictionary(input)   
        kebutuhanruang = KebutuhanRuangModel(**data)
        db_session.add(kebutuhanruang) 
        db_session.commit()
        ok = True 
        msg = "kebutuhanruang saved"
        return createKebutuhanRuang(kebutuhanruang=kebutuhanruang, ok=ok,msg=msg)

# update existing kebutuhanruang
class updateKebutuhanRuang(graphene.Mutation):
     
    ok = graphene.Boolean()
    msg = graphene.String()
    kebutuhanruang = graphene.Field(lambda: KebutuhanRuang, description="kebutuhanruang updated by this mutation.") 

    class Arguments:
        input = UpdateKebutuhanRuangInput(required=True) 
  
    @jwt_required()
    def mutate(self, info, input):
         
        data = input_to_dictionary(input)  
        kebutuhanruang = db_session.query(KebutuhanRuangModel).filter_by(id=data['id'])
         
        if kebutuhanruang:  
            kebutuhanruang.update(data)   
            db_session.commit()  
            ok = True 
            msg = "kebutuhanruang updated!" 
            kebutuhanruang = db_session.query(KebutuhanRuangModel).filter_by(id=data['id']).first()
            return updateKebutuhanRuang(ok=ok, kebutuhanruang=kebutuhanruang,msg=msg) 

        ok = False  
        msg = "kebutuhanruang not found!" 
        return updateKebutuhanRuang(ok=ok,msg=msg,kebutuhanruang=kebutuhanruang)   

        


# delete KebutuhanRuang
class deleteKebutuhanRuang(graphene.Mutation):
    
    class Arguments:
        id = graphene.String(required=True)  

    ok = graphene.Boolean()
    msg = graphene.String()
    kebutuhanruang = graphene.Field(lambda: KebutuhanRuang, description="kebutuhanruang Delete by this mutation.")
 
    @jwt_required()
    def mutate(root, info, id):
        kebutuhanruangId = from_global_id(id)[1]
        kebutuhanruang = db_session.query(KebutuhanRuangModel).filter_by(id=kebutuhanruangId).first()
        if kebutuhanruang:
            db_session.delete(kebutuhanruang) 
            db_session.commit()
            ok = True  
            msg = "user deleted!" 
            return deleteKebutuhanRuang(ok=ok,msg=msg)

        ok = False
        msg = "User Not Found" 
        return deleteKebutuhanRuang(ok=ok,msg=msg)

class Mutation(graphene.ObjectType):
    createKebutuhanRuang = createKebutuhanRuang.Field() 
    updateKebutuhanRuang = updateKebutuhanRuang.Field()
    deleteKebutuhanRuang = deleteKebutuhanRuang.Field()