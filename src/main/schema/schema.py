import graphene

#import query
from .auth.query import Query as Auth
from .user.query import Query as User
from .paket.query import Query as Paket
from .portofolio.query import Query as Portofolio
from .contact.query import Query as Contact
from .kuisioner.query import Query as Kuisioner
from .slider.query import Query as Slider
from .setting.query import Query as Setting
from .whyus.query import Query as Whyus
from .pilihandesain.query import Query as PilihanDesain
from .kebutuhanruang.query import Query as KebutuhanRuang


#import mutation
from .auth.mutation import Mutation as Auth
from .user.mutation import Mutation as UserMutation
from .paket.mutation import Mutation  as PaketMutation
from .portofolio.mutation import Mutation  as PortofolioMutation
from .contact.mutation import Mutation  as ContactMutation
from .kuisioner.mutation import Mutation  as KuisionerMutation
from .slider.mutation import Mutation  as SliderMutation
from .setting.mutation import Mutation  as SettingMutation 
from .whyus.mutation import Mutation  as WhyusMutation 
from .pilihandesain.mutation import Mutation  as PilihanDesainMutation 
from .kebutuhanruang.mutation import Mutation  as KebutuhanRuangMutation 


class Query(  
    User,
    Paket,
    Portofolio,
    Contact,
    Kuisioner,
    Slider,
    Setting,
    Whyus,
    PilihanDesain,
    KebutuhanRuang
):
    pass

  
class Mutation(  
    Auth,
    UserMutation,
    ContactMutation,
    PortofolioMutation,
    PaketMutation,
    KuisionerMutation,
    SliderMutation, 
    SettingMutation,
    WhyusMutation,
    PilihanDesainMutation,
    KebutuhanRuangMutation
):
    pass 

schema = graphene.Schema(query=Query, mutation=Mutation)