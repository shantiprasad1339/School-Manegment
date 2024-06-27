from mongoengine import Document,StringField,ListField,BooleanField,IntField
class Teachersattendents (Document):
    teacherid = StringField(required = True)
    schoolid = StringField(required = True)
    date = StringField(required = False)
    attendentsstatus = StringField(required = True)
