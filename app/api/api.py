from fastapi import APIRouter


router = APIRouter()


#route for students api service
from .endpoints.Students.students import stu as studentAPIRouter   
router.include_router(studentAPIRouter)

 
