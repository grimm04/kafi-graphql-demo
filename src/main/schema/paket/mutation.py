
 
import graphene  
from flask_jwt_extended import jwt_required
from graphql_relay.node.node import from_global_id

from ...database.db_session import db_session 
from ...utils.input_to_dictionary import input_to_dictionary


from ...models.Paket import Paket as PaketModel
from .type import Paket, PaketInput, UpdatePaketInput 

class CreatePaket(graphene.Mutation):
    paket = graphene.Field(lambda: Paket)
    ok = graphene.Boolean()
    msg = graphene.String()

    class Arguments: 
        input =PaketInput(required=True)

    @jwt_required()
    def mutate(self, info, input):
        data = input_to_dictionary(input) 

        paket_query = Paket.get_query(info)  
        paket = paket_query.filter(PaketModel.nama.contains(data['nama'])).first()
        if paket:
            ok = False
            msg = "paket alrady exist"
            return CreatePaket(paket=paket,ok=ok,msg=msg) 

        paket = PaketModel(**data)
        db_session.add(paket) 
        db_session.commit()
        ok = True 
        msg = "paket saved"
        return CreatePaket(paket=paket, ok=ok,msg=msg)

# update existing Paket
class updatePaket(graphene.Mutation):
     
    ok = graphene.Boolean()
    msg = graphene.String()
    paket = graphene.Field(lambda: Paket, description="paket updated by this mutation.") 

    class Arguments:
        input = UpdatePaketInput(required=True) 
  
    @jwt_required()
    def mutate(self, info, input):
         
        data = input_to_dictionary(input)  
        paket = db_session.query(PaketModel).filter_by(id=data['id'])
         
        if paket:  
            paket.update(data)   
            db_session.commit()  
            ok = True 
            msg = "paket updated!" 
            paket = db_session.query(PaketModel).filter_by(id=data['id']).first()
            return updatePaket(ok=ok, paket=paket,msg=msg) 

        ok = False  
        msg = "paket not found!" 
        return updatePaket(ok=ok,msg=msg,paket=paket)   

        


# delete Paket
class deletePaket(graphene.Mutation):
    
    class Arguments:
        id = graphene.String(required=True)  

    ok = graphene.Boolean()
    msg = graphene.String()
    paket = graphene.Field(lambda: Paket, description="paket Delete by this mutation.")
 
    @jwt_required()
    def mutate(root, info, id):
        paketId = from_global_id(id)[1]
        paket = db_session.query(PaketModel).filter_by(id=paketId).first()
        if paket:
            db_session.delete(paket) 
            db_session.commit()
            ok = True  
            msg = "user deleted!" 
            return deletePaket(ok=ok,msg=msg)

        ok = False
        msg = "User Not Found" 
        return deletePaket(ok=ok,msg=msg)

class Mutation(graphene.ObjectType):
    createPaket = CreatePaket.Field() 
    updatePaket = updatePaket.Field()
    deletePaket = deletePaket.Field()