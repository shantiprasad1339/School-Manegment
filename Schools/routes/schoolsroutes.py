from fastapi import APIRouter,Body
from fastapi.responses import JSONResponse
import json
from bson import ObjectId
from Schools.models.schoolsmodel import Schooltablecreate,Schooltable
from pydantic import BaseModel

router = APIRouter()

class sofdeletebody(BaseModel):
    status:bool

@router.post("/api/v1/school/create")
async def schoolcreate(body: Schooltablecreate):
    ew_school = Schooltable(
        schoolname=body.schoolname,
        schooltype=body.schooltype,
        schoolphonenumber=body.schoolphonenumber,
        schoolemail=body.schoolemail,
        schoollogo=body.schoollogo,
        schooladdress=body.schooladdress,
        contactperson=body.contactperson,
        status = True
    )
    ew_school.save()
    tojson = ew_school.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"School Added Successfully",
        "status":True,
        "data":fromjson
    }

@router.get("/api/v1/allschools")
async def getschools():
    data = Schooltable.objects.all()
    tojson = data.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"All Schools",
        "data":fromjson,
        "status":True
    }
@router.delete("/api/v1/soft/schoolsdelte/{schoolid}")
async def softdeleteschool(body:sofdeletebody, schoolid:str):
    findschool = Schooltable.objects.get(id = ObjectId(schoolid))
    findschool.status = body.status
    findschool.save()
    tojson = findschool.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"School deleted",
        "data":fromjson,
        "status":True
    }


@router.put("/api/v1/schools/update/{schoolid}")
async def updateschools(schoolid:str,body:Schooltablecreate):
    findschool = Schooltable.objects.get(id = ObjectId(schoolid))
    findschool.schoolname = body.schoolname
    findschool.schooltype = body.schooltype
    findschool.schoolphonenumber = body.schoolphonenumber
    findschool.schoolemail = body.schoolemail
    findschool.schoollogo = body.schoollogo
    findschool.schooladdress = body.schooladdress
    findschool.contactperson = body.contactperson
    findschool.save()
    tojson = findschool.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"All Schools",
        "data":fromjson,
        "status":True
    }


@router.get("/api/v1/schoolgetbyid/{schoolid}")
async def schoolgetbyid(schoolid:str):
    findschool = Schooltable.objects.get(id = ObjectId(schoolid))
    findschool.save()
    tojson = findschool.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"School deleted",
        "data":fromjson,
       
    }