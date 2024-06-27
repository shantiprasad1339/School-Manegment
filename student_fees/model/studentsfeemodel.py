from mongoengine import Document,StringField,ListField,BooleanField,IntField
class Studentsfee (Document):
    studentid = StringField(required = True)
    schoolid = StringField(required = True)
    feesamount = IntField(required = False)
    classid = StringField(required = False)
    paymenttype = StringField(required = False)
    crediteddate = StringField(required = False)
    creditor = StringField(required = False)
