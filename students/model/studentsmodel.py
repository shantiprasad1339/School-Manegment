from mongoengine import Document,StringField,ListField,BooleanField,IntField
from pydantic import BaseModel

class Studenttable (Document):
    studentname = StringField(required = True)
    email = StringField(required = True)
    phone = IntField(required = False)
    seconphone = IntField(required = True)
    fathersname = StringField(required = True)
    mothersname = StringField(required = True)
    address1 = StringField(required = True)
    address2 = StringField(required = True)
    previousclass = StringField(required = True)
    dob = StringField(required = True)
    picture = StringField(required = True)
    marksheet = ListField(required=True)
    schoolid = StringField(required = True)
    classid = StringField(required = True)
    
class Studenttablecreate(BaseModel):
    studentname : str
    email : str
    phone : int
    seconphone : int
    fathersname : str
    mothersname : str
    address1 : str
    address2 : str
    previousclass : str
    dob : str
    picture : str
    marksheet: list[str]
    schoolid : str
    classid : str