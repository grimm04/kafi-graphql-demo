
 
import graphene  
from flask_jwt_extended import jwt_required
from graphql_relay.node.node import from_global_id

from ...database.db_session import db_session 
from ...utils.input_to_dictionary import input_to_dictionary


from ...models.Slider import Slider as SliderModel
from .type import Slider, SliderInput, UpdateSliderInput 

class CreateSlider(graphene.Mutation):
    slider = graphene.Field(lambda: Slider)
    ok = graphene.Boolean()
    msg = graphene.String()

    class Arguments: 
        input = SliderInput(required=True)

    @jwt_required()
    def mutate(self, info, input):
        data = input_to_dictionary(input)  
        slider = SliderModel(**data)
        db_session.add(slider) 
        db_session.commit()
        ok = True 
        msg = "slider saved"
        return CreateSlider(slider=slider, ok=ok,msg=msg)

# update existing slider
class updateSlider(graphene.Mutation):
     
    ok = graphene.Boolean()
    msg = graphene.String()
    slider = graphene.Field(lambda: Slider, description="slider updated by this mutation.") 

    class Arguments:
        input = UpdateSliderInput(required=True) 
  
    @jwt_required()
    def mutate(self, info, input):
         
        data = input_to_dictionary(input)  
        slider = db_session.query(SliderModel).filter_by(id=data['id'])
         
        if slider:  
            slider.update(data)   
            db_session.commit()  
            ok = True 
            msg = "slider updated!" 
            slider = db_session.query(SliderModel).filter_by(id=data['id']).first()
            return updateSlider(ok=ok, slider=slider,msg=msg) 

        ok = False  
        msg = "slider not found!" 
        return updateSlider(ok=ok,msg=msg,slider=slider)   

        


# delete slider
class deleteSlider(graphene.Mutation):
    
    class Arguments:
        id = graphene.String(required=True)  

    ok = graphene.Boolean()
    msg = graphene.String()
    slider = graphene.Field(lambda: Slider, description="slider Delete by this mutation.")
 
    @jwt_required()
    def mutate(root, info, id):
        sliderId = from_global_id(id)[1]
        slider = db_session.query(SliderModel).filter_by(id=sliderId).first()
        if slider:
            db_session.delete(slider) 
            db_session.commit()
            ok = True  
            msg = "user deleted!" 
            return deleteSlider(ok=ok,msg=msg)

        ok = False
        msg = "User Not Found" 
        return deleteSlider(ok=ok,msg=msg)

class Mutation(graphene.ObjectType):
    createSlider = CreateSlider.Field() 
    updateSlider = updateSlider.Field()
    deleteSlider = deleteSlider.Field()