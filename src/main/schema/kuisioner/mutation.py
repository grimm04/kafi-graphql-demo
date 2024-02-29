import graphene  
from flask_jwt_extended import jwt_required
from graphql_relay.node.node import from_global_id

from ...database.db_session import db_session 
from ...utils.input_to_dictionary import input_to_dictionary


from ...models.Kuisioner import Kuisioner as KuisionerModel
from .type import Kuisioner, KuisionerInput, UpdateKuisionerInput 

class CreateKuisioner(graphene.Mutation):
    kuisioner = graphene.Field(lambda: Kuisioner)
    ok = graphene.Boolean()
    msg = graphene.String()

    class Arguments: 
        input =KuisionerInput(required=True)
 
    def mutate(self, info, input): 
        data = input_to_dictionary(input)  
 
        kuisioner = KuisionerModel(**data)
        db_session.add(kuisioner) 
        db_session.commit()
        ok = True 
        msg = "kuisioner saved"
        return CreateKuisioner(kuisioner=kuisioner, ok=ok,msg=msg)

# update existing Kuisioner
class UpdateKuisioner(graphene.Mutation):
     
    ok = graphene.Boolean()
    msg = graphene.String()
    kuisioner = graphene.Field(lambda: Kuisioner, description="Kuisioner updated by this mutation.") 

    class Arguments: 
        input = UpdateKuisionerInput(required=True) 
  
    @jwt_required()
    def mutate(self, info, input): 
        data = input_to_dictionary(input)  
        kuisioner = db_session.query(KuisionerModel).filter_by(id=data['id']) 
        if kuisioner:   
            kuisioner.update(data)
            db_session.commit()  
            ok = True 
            msg = "Kuisioner updated!" 
            kuisioner = db_session.query(KuisionerModel).filter_by(id=data['id']).first()
            return UpdateKuisioner(ok=ok, kuisioner=kuisioner,msg=msg) 

        ok = False  
        msg = "Kuisioner not found!" 
        return UpdateKuisioner(ok=ok,msg=msg,kisioner=kuisioner) 

# delete Kuisioner
class deleteKuisioner(graphene.Mutation):
    
    class Arguments:
        id = graphene.String(required=True)  

    ok = graphene.Boolean()
    msg = graphene.String()
    kuisioner = graphene.Field(lambda: Kuisioner, description="kuisioner Delete by this mutation.")
 
    @jwt_required()
    def mutate(root, info, id):
        kuisionerId = from_global_id(id)[1]
        kuisioner = db_session.query(KuisionerModel).filter_by(id=kuisionerId).first()
        if kuisioner:
            db_session.delete(kuisioner) 
            db_session.commit()
            ok = True  
            msg = "user deleted!" 
            return deleteKuisioner(ok=ok,msg=msg)

        ok = False
        msg = "User Not Found" 
        return deleteKuisioner(ok=ok,msg=msg)  
        
class Mutation(graphene.ObjectType):
    CreateKuisioner = CreateKuisioner.Field()   
    UpdateKuisioner = UpdateKuisioner.Field()   
    deleteKuisioner = deleteKuisioner.Field()   