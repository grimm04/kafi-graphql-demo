
 
import graphene  
from flask_jwt_extended import jwt_required
from graphql_relay.node.node import from_global_id

from ...database.db_session import db_session 
from ...utils.input_to_dictionary import input_to_dictionary


from ...models.Whyus import Whyus as WhyusModel
from .type import Whyus, WhyusInput, UpdateWhyusInput 

class CreateWhyus(graphene.Mutation):
    whyus = graphene.Field(lambda: Whyus)
    ok = graphene.Boolean()
    msg = graphene.String()

    class Arguments: 
        input = WhyusInput(required=True)

    @jwt_required()
    def mutate(self, info, input):
        data = input_to_dictionary(input)  
        whyus = WhyusModel(**data)
        db_session.add(whyus) 
        db_session.commit()
        ok = True 
        msg = "whyus saved"
        return CreateWhyus(whyus=whyus, ok=ok,msg=msg)

# update existing Whyus
class updateWhyus(graphene.Mutation):
     
    ok = graphene.Boolean()
    msg = graphene.String()
    whyus = graphene.Field(lambda: Whyus, description="Whyus updated by this mutation.") 

    class Arguments:
        input = UpdateWhyusInput(required=True) 
  
    @jwt_required()
    def mutate(self, info, input):
         
        data = input_to_dictionary(input)  
        whyus = db_session.query(WhyusModel).filter_by(id=data['id'])
         
        if whyus:  
            whyus.update(data)   
            db_session.commit()  
            ok = True 
            msg = "whyus updated!" 
            whyus = db_session.query(WhyusModel).filter_by(id=data['id']).first()
            return updateWhyus(ok=ok, whyus=whyus,msg=msg) 

        ok = False  
        msg = "whyus not found!" 
        return updateWhyus(ok=ok,msg=msg,whyus=whyus)   

        


# delete whyus
class deleteWhyus(graphene.Mutation):
    
    class Arguments:
        id = graphene.String(required=True)  

    ok = graphene.Boolean()
    msg = graphene.String()
    whyus = graphene.Field(lambda: Whyus, description="whyus Delete by this mutation.")
 
    @jwt_required()
    def mutate(root, info, id):
        sliderId = from_global_id(id)[1]
        whyus = db_session.query(WhyusModel).filter_by(id=sliderId).first()
        if whyus:
            db_session.delete(whyus) 
            db_session.commit()
            ok = True  
            msg = "user deleted!" 
            return deleteWhyus(ok=ok,msg=msg)

        ok = False
        msg = "User Not Found" 
        return deleteWhyus(ok=ok,msg=msg)

class Mutation(graphene.ObjectType):
    createWhyus = CreateWhyus.Field() 
    updateWhyus = updateWhyus.Field() 
    deleteWhyus = deleteWhyus.Field() 