from fastapi import APIRouter


router = APIRouter()


#route for students api service
from .endpoints.Students.students import stu as studentAPIRouter   
router.include_router(studentAPIRouter)

#route for satff api service
from .endpoints.staff.staff import staff as staffAPIRouter   
router.include_router(staffAPIRouter)

 
