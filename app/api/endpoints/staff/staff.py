
from fastapi import Depends, APIRouter, HTTPException

from sqlalchemy.orm import Session
from app.database.dbConfig import get_db
from app.database.crud import StaffsRepo

import app.pydanticModel.schemas as schemas

staff = APIRouter()

@staff.post('/newstaff', tags=["staffs"], response_model=schemas.staffs, status_code=201)
async def Create_student(staff_request: schemas.CreateStaff, db: Session = Depends(get_db)):
    """
    Create an staff details 
    """

    # staff_details = StaffsRepo.fetch_by_name(db, name=staff_request.name)
    # if staff_details:
    #     raise HTTPException(status_code=400, detail="staff already exists!")

    return  StaffsRepo.create(db=db, Staff=staff_request)
