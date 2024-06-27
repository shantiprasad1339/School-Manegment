from mongoengine import Document,StringField,ListField,BooleanField,IntField
class Subjecttablemarks (Document):
    studentsid = StringField(required = True)
    subjectname = StringField(required = True)
    marks = StringField(required = False)
    status = StringField(required = True)
