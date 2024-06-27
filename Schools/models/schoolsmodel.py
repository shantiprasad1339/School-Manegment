from mongoengine import Document,StringField,ListField,BooleanField,IntField
from pydantic import BaseModel

class Schooltable (Document):
    schoolname = StringField(required = True)
    schooltype = StringField(required = True)
    schoolphonenumber = IntField(required = True)
    schoolemail = StringField(required = True)
    schoollogo = StringField(required = True)
    schooladdress = StringField(required = True)
    contactperson = StringField(required = True)
    status = BooleanField(required=True)

class Schooltablecreate(BaseModel):
    schoolname : str
    schooltype : str
    schoolphonenumber : int
    schoolemail : str
    schoollogo : str
    schooladdress : str
    contactperson : str
