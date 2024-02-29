import graphene  
from flask_jwt_extended import jwt_required
from graphql_relay.node.node import from_global_id

from ...database.db_session import db_session 
from ...utils.input_to_dictionary import input_to_dictionary


from ...models.Contact import Contact as ContactModel
from .type import Contact, ContactInput, UpdateContactInput 

class CreateContact(graphene.Mutation):
    contact = graphene.Field(lambda: Contact)
    ok = graphene.Boolean()
    msg = graphene.String()

    class Arguments: 
        input =ContactInput(required=True)

    # @jwt_required()
    def mutate(self, info, input): 
        data = input_to_dictionary(input)

        contact = ContactModel(**data) 
        db_session.add(contact) 
        db_session.commit()
        ok = True 
        msg = "contact saved"
        return CreateContact(contact=contact, ok=ok,msg=msg)

# update existing contact
class updateContact(graphene.Mutation):
     
    ok = graphene.Boolean()
    msg = graphene.String()
    contact = graphene.Field(lambda: Contact, description="contact updated by this mutation.") 

    class Arguments:
        input = UpdateContactInput(required=True) 
  
    @jwt_required()
    def mutate(self, info, input): 
        data = input_to_dictionary(input) 
        contact = db_session.query(ContactModel).filter_by(id=data['id']) 
        if contact:    
            contact.update(data)
            db_session.commit()  
            ok = True 
            msg = "contact updated!" 
            contact = db_session.query(ContactModel).filter_by(id=data['id']).first()
            return updateContact(ok=ok, contact=contact,msg=msg) 

        ok = False  
        msg = "contact not found!" 
        return updateContact(ok=ok,msg=msg,contact=contact)   

        


# delete contact
class deleteContact(graphene.Mutation):
    
    class Arguments:
        id = graphene.String(required=True)  

    ok = graphene.Boolean()
    msg = graphene.String()
    contact = graphene.Field(lambda: Contact, description="contact Delete by this mutation.")
 
    @jwt_required()
    def mutate(root, info, id):
        contactId = from_global_id(id)[1]
        contact = db_session.query(ContactModel).filter_by(id=contactId).first()
        if contact:
            db_session.delete(contact) 
            db_session.commit()
            ok = True  
            msg = "user deleted!" 
            return deleteContact(ok=ok,msg=msg)

        ok = False
        msg = "User Not Found" 
        return deleteContact(ok=ok,msg=msg)

class Mutation(graphene.ObjectType):
    createContact = CreateContact.Field() 
    updateContact = updateContact.Field()
    deleteContact = deleteContact.Field()