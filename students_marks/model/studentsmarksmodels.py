from mongoengine import Document,StringField,ListField,BooleanField,IntField
class Studentsmarks (Document):
    studentid = StringField(required = True)
    classid = StringField(required = True)
    schoolid = StringField(required = False)
    subjects = ListField(required = True)
