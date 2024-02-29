
from graphene import Int, NonNull, ObjectType
from graphene.relay import Connection, Node 

class CountedConnection(Connection):
    class Meta: 
        abstract = True

    total_count = NonNull(Int)

    def resolve_total_count(self, info, **kwargs):
        return self.length