from fastapi import APIRouter,Body
from fastapi.responses import JSONResponse
import json
from bson import ObjectId
from pydantic import BaseModel
from Classes.models.classesmodel import Classtable,Classtablecreate

router = APIRouter()

@router.post("/api/v1/class/create")
async def classcreate(body: Classtablecreate):
    classes = Classtable(
        classname=body.classname,
        section=body.section,
        studentspace=body.studentspace,
        schoolId=body.schoolId,
        status=body.status
    )
    classes.save()
    tojson = classes.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"Class Added Successfully",
        "status":True,
        "data":fromjson
    }

@router.get("/api/v1/class/get")
async def classget():
    data = Classtable.objects.all()
    tojson = data.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"class get successfully",
        "data":fromjson,
        "status":True
    }


@router.put("/api/v1/class/update/{classid}")
async def updateclass(schoolid:str,body:Classtablecreate):
    findclass = Classtable.objects.get(id = ObjectId(schoolid))
    findclass.classname = body.classname
    findclass.section = body.section
    findclass.studentspace = body.studentspace
    findclass.schoolId = body.schoolId
    findclass.status = body.status
    findclass.save()
    tojson = findclass.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"Schools Updated",
        "data":fromjson,
        "status":True
    }


@router.delete("/api/v1/class/delete/{classid}")
async def classdelete(classid:str):
    findclass = Classtable.objects.get(id = ObjectId(classid))
    findclass.delete()
    tojson = findclass.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"class deleted",
        "data":fromjson,
        "status":True
    }


@router.get("/api/v1/class/getbyid/{classid}")
async def classgetbyid(classid:str):
    data = Classtable.objects.get(id = ObjectId(classid))
    tojson = data.to_json()
    fromjson = json.loads(tojson)
    return {
        "message":"class get successfully",
        "data":fromjson,
        "status":True
    }