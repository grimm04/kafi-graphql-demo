import graphene  
from flask_jwt_extended import jwt_required
from graphql_relay.node.node import from_global_id

from ...database.db_session import db_session 
from ...utils.input_to_dictionary import input_to_dictionary


from ...models.Portofolio import Portofolio as PortofolioModel
from .type import Portofolio, PortofolioInput, UpdatePortofolioInput 

class CreatePortofolio(graphene.Mutation):
    portofolio = graphene.Field(lambda: Portofolio)
    ok = graphene.Boolean()
    msg = graphene.String()

    class Arguments: 
        input =PortofolioInput(required=True)

    @jwt_required()
    def mutate(self, info, input): 
        data = input_to_dictionary(input)

        portofolio = PortofolioModel(**data) 
        db_session.add(portofolio) 
        db_session.commit()
        ok = True 
        msg = "portofolio saved"
        return CreatePortofolio(portofolio=portofolio, ok=ok,msg=msg)

# update existing Portofolio
class updatePortofolio(graphene.Mutation):
     
    ok = graphene.Boolean()
    msg = graphene.String()
    portofolio = graphene.Field(lambda: Portofolio, description="portofolio updated by this mutation.") 

    class Arguments:
        input = UpdatePortofolioInput(required=True) 
  
    @jwt_required()
    def mutate(self, info, input): 
        data = input_to_dictionary(input) 
        portofolio = db_session.query(PortofolioModel).filter_by(id=data['id']) 
        if portofolio:    
            portofolio.update(data)
            db_session.commit()  
            ok = True 
            msg = "portofolio updated!" 
            portofolio = db_session.query(PortofolioModel).filter_by(id=data['id']).first()
            return updatePortofolio(ok=ok, portofolio=portofolio,msg=msg) 

        ok = False  
        msg = "portofolio not found!" 
        return updatePortofolio(ok=ok,msg=msg,portofolio=portofolio)   

        


# delete Portofolio
class deletePortofolio(graphene.Mutation):
    
    class Arguments:
        id = graphene.String(required=True)  

    ok = graphene.Boolean()
    msg = graphene.String()
    portofolio = graphene.Field(lambda: Portofolio, description="portofolio Delete by this mutation.")
 
    @jwt_required()
    def mutate(root, info, id):
        portofolioId = from_global_id(id)[1]
        portofolio = db_session.query(PortofolioModel).filter_by(id=portofolioId).first()
        if portofolio:
            db_session.delete(portofolio) 
            db_session.commit()
            ok = True  
            msg = "user deleted!" 
            return deletePortofolio(ok=ok,msg=msg)

        ok = False
        msg = "User Not Found" 
        return deletePortofolio(ok=ok,msg=msg)

class Mutation(graphene.ObjectType):
    createPortofolio = CreatePortofolio.Field() 
    updatePortofolio = updatePortofolio.Field()
    deletePortofolio = deletePortofolio.Field()