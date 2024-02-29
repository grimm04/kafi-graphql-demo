# Project
import graphene 
from sqlalchemy import and_, cast, inspection, not_, or_, types
from graphene_sqlalchemy_filter import FilterableConnectionField, FilterSet
from sqlalchemy import func ,Column, Integer, String ,DateTime
from datetime import date

from ..models.User import User as UserModel
from ..models.Portofolio import Portofolio as PortofolioModel
from ..models.Contact import Contact as ContactModel
from ..models.Paket import Paket as PaketModel
from ..models.Kuisioner import Kuisioner as KuisionerModel
from ..models.Slider import Slider as SliderModel
from ..models.Setting import Setting as SettingModel
from ..models.Whyus import Whyus as WhyusModel

def likeall_filter(field, value: str):
    return func.lower(func.cast(field, String)).like('%' + str(value).lower() + '%')

def today_filter(field, value: bool):
    today = func.date(field) == date.today()
    return today if value else not_(today)

class BaseFilter(FilterSet):
    ALL = '__all__' 
    
    LIKEALL = 'likeall'

    EXTRA_EXPRESSIONS = {
        'likeall': {
            'graphql_name': 'likeall',
            'for_types': [types.Date, types.DateTime, types.String, types.Integer, types.NUMERIC],
            'filter': likeall_filter,
            'input_type': (
                lambda type_, nullable, doc: graphene.String(nullable=False)
            ),
            'description': 'Filter like for all types',
        }
    } 
    class Meta:
        abstract = True

class UserFilter(BaseFilter):
    class Meta:
        model = UserModel
        fields = { 
                    'username': ['likeall'],
                    'fullname': ['eq', 'ne', 'in', 'likeall'],
                    'created_at':['range']
                  } 

class PortofolioFilter(BaseFilter):
    class Meta:
        model = PortofolioModel
        fields = { 
                    'nama': ['likeall'], 
                    'created_at':['range']
                  } 


class ContactFilter(BaseFilter):
    class Meta:
        model = ContactModel
        fields = { 
                    'nama': ['likeall'], 
                    'email': ['likeall'], 
                    'company': ['likeall'], 
                    'phone': ['likeall'], 
                    'created_at':['range']
                  } 
class PaketFilter(BaseFilter):
    class Meta:
        model = PaketModel
        fields = { 
                    'nama': ['likeall'], 
                    'kab_kota': ['likeall'], 
                    'provinsi': ['likeall'], 
                    'created_at':['range']
                  } 
class KuisionerFilter(BaseFilter):
    class Meta:
        model = KuisionerModel
        fields = { 
                    'nama': ['likeall'], 
                    'created_at':['range']
                  } 
class SliderFilter(BaseFilter):
    class Meta:
        model = SliderModel
        fields = { 
                    'title': ['likeall'], 
                    'active': ['eq'], 
                    'created_at':['range']
                  } 
class SettingFilter(BaseFilter):
    class Meta:
        model = SettingModel
        fields = { 
                    'option': ['likeall'], 
                    'group': ['likeall'], 
                    'created_at':['range']
                  } 
class WhyusFilter(BaseFilter):
    class Meta:
        model = WhyusModel
        fields = { 
                    'title': ['likeall'], 
                    'created_at':['range']
                  } 
 
class MyFilterableConnectionField(FilterableConnectionField):
    filters = {
                UserModel: UserFilter(),
                PortofolioModel:PortofolioFilter(),
                ContactModel:ContactFilter(),
                PaketModel:PaketFilter(),
                KuisionerModel:KuisionerFilter(),
                SliderModel:SliderFilter(),
                SettingModel:SettingFilter(),
                WhyusModel:WhyusFilter(),
            }