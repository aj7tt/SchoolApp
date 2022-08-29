
from typing import List, Optional

from pydantic import BaseModel



class studentBase(BaseModel):
    name: str
    classs: int
    rollNo: int
    MobileNo: int
    address: Optional[str] = None



class CreateStudent(studentBase):
    pass


class Students(studentBase):
    id: int

    class Config:
        orm_mode = True




