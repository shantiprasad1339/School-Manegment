from fastapi import FastAPI
from mongoengine import connect
from Schools.routes import schoolsroutes
from Classes.routes import classroute
from students.routes import studentroute
from teachers.routes import teachersroutes
app = FastAPI()




connect('schoolManegmentSystem', host="mongodb+srv://avbigbuddy:nZ4ATPTwJjzYnm20@cluster0.wplpkxz.mongodb.net/schoolManegmentSystem")


app.include_router(schoolsroutes.router, tags=["School routes"])
app.include_router(classroute.router, tags=["Class routes"])
app.include_router(studentroute.router, tags=["Student routes"])
app.include_router(teachersroutes.router, tags=["Teachers routes"])
# app.include_router(categoryroutes.router, tags = ["Category"])
# app.include_router(addresrouter.router, tags=["User Address"])
# app.include_router(uploadroutes.router, tags=["Upload Image"])
# app.include_router(create_rating.router, tags=["Rating"])
# app.include_router(addtocartroute.router, tags=["AddToCart"      ])