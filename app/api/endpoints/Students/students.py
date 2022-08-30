
from fastapi import Depends, APIRouter, HTTPException
from typing import List, Optional
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.database.dbConfig import get_db
from app.database.crud import StudentsRepo

import app.pydanticModel.schemas as schemas

stu = APIRouter()

@stu.post('/newstudent', tags=["Students"], response_model=schemas.Students, status_code=201)
async def Create_student(students_request: schemas.CreateStudent, db: Session = Depends(get_db)):
    """
    Create an students details 
    """

    studentsDetails = StudentsRepo.fetch_by_name(db, name=students_request.name)
    if studentsDetails:
        raise HTTPException(status_code=400, detail="student already exists!")

    return await StudentsRepo.create(db=db, Students=students_request)


@stu.get('/students', tags=["Students"], response_model=List[schemas.Students])
def get_all_students(name: Optional[str] = None, db: Session = Depends(get_db)):
    """
    Get all the students details stored in database
    """
    if name:
        students = []
        studentsDetails = StudentsRepo.fetch_by_name(db, name)
        students.append(studentsDetails)
        return students
    else:
        return StudentsRepo.fetch_all(db)


@stu.get('/students/{student_id}', tags=["Students"], response_model=schemas.Students)
def get_item(stu_id: int, db: Session = Depends(get_db)):
    """
    Get the student with the given ID provided by User stored in database
    """
    studentsDetails = StudentsRepo.fetch_by_id(db, stu_id)
    if studentsDetails is None:
        raise HTTPException(status_code=404, detail="students not found with the given ID")
    return studentsDetails


@stu.delete('/students/{student_id}', tags=["Students"])
async def delete_Stu(stu_id: int, db: Session = Depends(get_db)):
    """
    Delete the students with the given ID provided by User stored in database
    """
    studentsDetails = StudentsRepo.fetch_by_id(db, stu_id)
    if studentsDetails is None:
        raise HTTPException(status_code=404, detail="student not found with the given ID")
    await StudentsRepo.delete(db, stu_id)
    return "student deleted successfully!"

