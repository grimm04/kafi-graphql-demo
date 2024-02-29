
 
import graphene  
from flask_jwt_extended import jwt_required
from graphql_relay.node.node import from_global_id

from ...database.db_session import db_session 
from ...utils.input_to_dictionary import input_to_dictionary


from ...models.PilihanDesain import PilihanDesain as PilihanDesainModel
from .type import PilihanDesain, PilihanDesainInput ,UpdatePilihanDesainInput

class CreatePilihanDesain(graphene.Mutation):
    pilihandesain = graphene.Field(lambda: PilihanDesain)
    ok = graphene.Boolean()
    msg = graphene.String()

    class Arguments: 
        input = PilihanDesainInput(required=True)

    @jwt_required()
    def mutate(self, info, input):
        data = input_to_dictionary(input)  
        pilihandesain = PilihanDesainModel(**data)
        db_session.add(pilihandesain) 
        db_session.commit()
        ok = True 
        msg = "Pilihan Desain Tersimpan."
        return CreatePilihanDesain(pilihandesain=pilihandesain, ok=ok,msg=msg)

# update existing PilihanDesain
class updatePilihanDesain(graphene.Mutation):
     
    ok = graphene.Boolean()
    msg = graphene.String()
    pilihandesain = graphene.Field(lambda: PilihanDesain, description="Pilihan Desain updated by this mutation.") 

    class Arguments:
        input = UpdatePilihanDesainInput(required=True) 
  
    @jwt_required()
    def mutate(self, info, input):
         
        data = input_to_dictionary(input)  
        pilihandesain = db_session.query(PilihanDesainModel).filter_by(id=data['id'])
         
        if pilihandesain:  
            pilihandesain.update(data)   
            db_session.commit()  
            ok = True 
            msg = "Pilihan Desain Berhasil Di Ubah" 
            pilihandesain = db_session.query(PilihanDesainModel).filter_by(id=data['id']).first()
            return updatePilihanDesain(ok=ok, pilihandesain=pilihandesain,msg=msg) 

        ok = False  
        msg = "Pilihan Desain Tidak Ada!" 
        return updatePilihanDesain(ok=ok,msg=msg,pilihandesain=pilihandesain)   

        


# delete pilihandesain
class deletePilihanDesain(graphene.Mutation):
    
    class Arguments:
        id = graphene.String(required=True)  

    ok = graphene.Boolean()
    msg = graphene.String()
    pilihandesain = graphene.Field(lambda: PilihanDesain, description="Pilihan Desain Delete by this mutation.")
 
    @jwt_required()
    def mutate(root, info, id):
        pilihandesainId = from_global_id(id)[1]
        pilihandesain = db_session.query(PilihanDesainModel).filter_by(id=pilihandesainId).first()
        if pilihandesain:
            db_session.delete(pilihandesain) 
            db_session.commit()
            ok = True  
            msg = "Pilihan Desain Terhapus!" 
            return deletePilihanDesain(ok=ok,msg=msg)

        ok = False
        msg = "Pilihan Desain Tidak Ada" 
        return deletePilihanDesain(ok=ok,msg=msg)

class Mutation(graphene.ObjectType):
    createPilihanDesain = CreatePilihanDesain.Field() 
    updatePilihanDesain = updatePilihanDesain.Field()
    deletePilihanDesain = deletePilihanDesain.Field()