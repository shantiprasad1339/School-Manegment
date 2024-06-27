from fastapi import APIRouter,Body
from fastapi.responses import JSONResponse
import json
from bson import ObjectId
from pydantic import BaseModel
from teachers.models.teachersmodels import Teachermodel,Teachermodelcreate

router = APIRouter()

@router.post("/api/v1/teacher/create")
async def teachercreate(body: Teachermodelcreate):
    teacher = Teachermodel(
        name=body.name,
        schoolId=body.schoolId,
        phone=body.phone,
        email=body.email,
        education=body.education,
        shifttiming = body.shifttiming,
        role = body.role,
        cv_resume = body.cv_resume,
        joiningdate = body.joiningdate,
        salary = body.salary,
        address1 = body.address1,
        address2 = body.address2,
        status = body.status,
   

    )
    teacher.save()
    tojson = teacher.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"Teacher Added Successfully",
        "status":True,
        "data":fromjson
    }


@router.get("/api/v1/teacher/all")
async def teachergetall():
    data = Teachermodel.objects.all()
    tojson = data.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"teacher get successfully",
        "data":fromjson,
        "status":True
    }



@router.get("/api/v1/teacher/{id}")
async def teachergetbyid(id : str):
    data = Teachermodel.objects.get(id = ObjectId(id))
    tojson = data.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"Teacher get successfully",
        "data":fromjson,
        "status":True
    }


@router.delete("/api/v1/teacher/delete/{teacherid}")
async def teachergetbyid(teacherid : str):
    data = Teachermodel.objects.get(id = ObjectId(teacherid))
    data.delete()
    tojson = data.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"Teacher deleted successfully",
        "data":fromjson,
        "status":True
    }


@router.put("/api/v1/teacher/update/{teacherid}")
async def teacherupdate(teacherid:str , body: Teachermodelcreate):
    teacher = Teachermodel.objects.get(id = ObjectId(teacherid))
    teacher.name = body.name
    teacher.schoolId = body.schoolId
    teacher.phone = body.phone
    teacher.email = body.email
    teacher.education = body.education
    teacher.shifttiming = body.shifttiming
    teacher.role = body.role
    teacher.cv_resume = body.cv_resume
    teacher.joiningdate = body.joiningdate
    teacher.salary = body.salary
    teacher.address2 = body.address2
    teacher.status = body.status
    teacher.save()
    tojson = teacher.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"Teacher updated Successfully",
        "status":True,
        "data":fromjson
    }
