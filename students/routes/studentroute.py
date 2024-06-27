from fastapi import APIRouter,Body
from fastapi.responses import JSONResponse
import json
from bson import ObjectId
from pydantic import BaseModel
from students.model.studentsmodel import Studenttablecreate,Studenttable

router = APIRouter()

@router.post("/api/v1/student/create")
async def studentscreate(body: Studenttablecreate):
    students = Studenttable(
        studentname=body.studentname,
        email=body.email,
        phone=body.phone,
        mothersname=body.mothersname,
        fathersname=body.fathersname,
        seconphone = body.seconphone,
        classid = body.classid,
        schoolid = body.schoolid,
        marksheet = body.marksheet,
        previousclass = body.previousclass,
        address1 = body.address1,
        address2 = body.address2,
        dob = body.dob,
        picture = body.picture

    )
    students.save()
    tojson = students.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"Student Added Successfully",
        "status":True,
        "data":fromjson
    }


@router.get("/api/v1/student/all")
async def studentget():
    data = Studenttable.objects.all()
    tojson = data.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"students get successfully",
        "data":fromjson,
        "status":True
    }

@router.get("/api/v1/student/{id}")
async def studentgetbyid(id : str):
    data = Studenttable.objects.get(id = ObjectId(id))
    tojson = data.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"students get successfully",
        "data":fromjson,
        "status":True
    }


@router.delete("/api/v1/student/delete/{studentid}")
async def studentgetbyid(studentid : str):
    data = Studenttable.objects.get(id = ObjectId(studentid))
    data.delete()
    tojson = data.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"students deleted successfully",
        "data":fromjson,
        "status":True
    }



@router.put("/api/v1/student/update/{studentid}")
async def studentgetbyid(studentid : str,body : Studenttablecreate):
    findstudent = Studenttable.objects.get(id = ObjectId(studentid))
    findstudent.studentname = body.studentname
    findstudent.email = body.email
    findstudent.phone = body.phone
    findstudent.seconphone = body.seconphone
    findstudent.fathersname = body.fathersname
    findstudent.mothersname = body.mothersname
    findstudent.address1 = body.address1
    findstudent.address2 = body.address2
    findstudent.previousclass = body.previousclass
    findstudent.dob = body.dob
    findstudent.picture = body.picture
    findstudent.marksheet = body.marksheet
    findstudent.schoolid = body.schoolid
    findstudent.classid = body.classid
    findstudent.save()
    tojson = findstudent.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"students updated successfully",
        "data":fromjson,
        "status":True
    }

