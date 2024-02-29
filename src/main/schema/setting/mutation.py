
 
import graphene  
from flask_jwt_extended import jwt_required
from graphql_relay.node.node import from_global_id

from ...database.db_session import db_session 
from ...utils.input_to_dictionary import input_to_dictionary


from ...models.Setting import Setting as SettingModel
from .type import Setting, SettingInput, UpdateSettingInput 

class CreateSetting(graphene.Mutation):
    setting = graphene.Field(lambda: Setting)
    ok = graphene.Boolean()
    msg = graphene.String()

    class Arguments: 
        input =SettingInput(required=True)

    @jwt_required()
    def mutate(self, info, input):
        data = input_to_dictionary(input)  

        setting = SettingModel(**data)
        db_session.add(setting) 
        db_session.commit()
        ok = True 
        msg = "setting saved"
        return CreateSetting(setting=setting, ok=ok,msg=msg)

# update existing Setting
class updateSetting(graphene.Mutation):
     
    ok = graphene.Boolean()
    msg = graphene.String()
    setting = graphene.Field(lambda: Setting, description="setting updated by this mutation.") 

    class Arguments:
        input = UpdateSettingInput(required=True) 
  
    @jwt_required()
    def mutate(self, info, input):
         
        data = input_to_dictionary(input)  
        setting = db_session.query(SettingModel).filter_by(id=data['id'])
         
        if setting:  
            setting.update(data)   
            db_session.commit()  
            ok = True 
            msg = "setting updated!" 
            setting = db_session.query(SettingModel).filter_by(id=data['id']).first()
            return updateSetting(ok=ok, setting=setting,msg=msg) 

        ok = False  
        msg = "setting not found!" 
        return updateSetting(ok=ok,msg=msg,setting=setting)    
        


# delete Setting
class deleteSetting(graphene.Mutation):
    
    class Arguments:
        id = graphene.String(required=True)  

    ok = graphene.Boolean()
    msg = graphene.String()
    setting = graphene.Field(lambda: Setting, description="setting Delete by this mutation.")
 
    @jwt_required()
    def mutate(root, info, id):
        settingId = from_global_id(id)[1]
        setting = db_session.query(SettingModel).filter_by(id=settingId).first()
        if setting:
            db_session.delete(setting) 
            db_session.commit()
            ok = True  
            msg = "user deleted!" 
            return deleteSetting(ok=ok,msg=msg)

        ok = False
        msg = "User Not Found" 
        return deleteSetting(ok=ok,msg=msg)

class Mutation(graphene.ObjectType):
    createSetting = CreateSetting.Field() 
    updateSetting = updateSetting.Field()
    deleteSetting = deleteSetting.Field()