from mongoengine import Document,StringField,ListField,BooleanField,IntField
class Marksheettable (Document):
    marksheettype = StringField(required = True)
    marksheet = StringField(required = True)
    createdat = StringField(required = False)
    updatedat = StringField(required = True)
