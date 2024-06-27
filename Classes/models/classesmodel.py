from mongoengine import Document,StringField,ListField,BooleanField,IntField
from pydantic import BaseModel

class Classtable (Document):
    classname = StringField(required = True)
    section = StringField(required = True)
    studentspace = IntField(required = False)
    schoolId = StringField(required = True)
    status = BooleanField(required = True)

class Classtablecreate(BaseModel):
    classname : str
    section : str
    studentspace : int
    schoolId : str
    status : bool


