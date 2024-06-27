from mongoengine import Document,StringField,ListField,BooleanField,IntField
class Subjectnamebyclass (Document):
    classid = StringField(required = True)
    schoolid = StringField(required = True)
    subjectname = StringField(required = False)
