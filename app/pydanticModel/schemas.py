
from typing import List, Optional
from enum import Enum
from pydantic import BaseModel, ValidationError, validator,conint


#student model
class studentBase(BaseModel):
    name: str
    classs: int
    rollNo: int
    MobileNo: int
    address: Optional[str] = None
    
    @validator('name')
    def name_must_contain_space(cls, fullname):
        if ' ' not in fullname:
            raise ValueError('must contain a space')
        return fullname.title()


class CreateStudent(studentBase):
    pass


class Students(studentBase):
    id: int

    class Config:
        orm_mode = True


#staff model
class staffBase(BaseModel):
    name: str
    gender: Enum('Male', 'Female')
    MobileNo: Optional[conint( strict=False)]
    address: Optional[str] = None



class CreateStaff(staffBase):
    pass


class staffs(staffBase):
    id: int

    class Config:
        orm_mode = True



