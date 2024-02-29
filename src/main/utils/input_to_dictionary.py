# /books/utils/input_to_dictionary.py

from os import X_OK
from graphql_relay.node.node import from_global_id
from .extensions import bcrypt

def input_to_dictionary(input):
    """Method to convert Graphene inputs into dictionary"""
    dictionary = {}
    for key in input:
        # Convert GraphQL global id to database id
        if key[-2:] == 'id':
            input[key] = from_global_id(input[key])[1]
            pass
        if key[-8:] == 'password':
            input[key] = bcrypt.generate_password_hash(input[key])
        dictionary[key] = input[key]
    return dictionary