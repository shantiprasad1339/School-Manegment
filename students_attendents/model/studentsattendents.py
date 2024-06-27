from mongoengine import Document,StringField,ListField,BooleanField,IntField
class Studentssattendents (Document):
    studentsid = StringField(required = True)
    schoolid = StringField(required = True)
    date = StringField(required = False)
    attendentsstatus = StringField(required = True)
