from mongoengine import Document,StringField,ListField,BooleanField,IntField
from pydantic import BaseModel

class Teachermodel (Document):
    name = StringField(required = True)
    schoolId = StringField(required = True)
    phone = IntField(required = True)
    email = StringField(required = True)
    education = StringField(required = True)
    shifttiming = StringField(required = True)
    role = StringField(required = True)
    cv_resume = StringField(required = True)
    joiningdate = StringField(required = True)
    salary = IntField(required = True)
    address1 = StringField(required = True)
    address2 = StringField(required = True)
    status = BooleanField(required = True)


class Teachermodelcreate(BaseModel):
    name : str
    schoolId : str
    phone : int
    email : str
    education : str
    shifttiming : str
    role : str
    cv_resume : str
    joiningdate : str
    salary : int
    address1 : str
    address2 : str
    status : bool
