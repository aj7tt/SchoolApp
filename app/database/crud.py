
from sqlalchemy.orm import Session

from ..pydanticModel import schemas
from . import models

class StudentsRepo:
    
    async def create(db: Session, Students: schemas.CreateStudent):
        student_details = models.Students(name=Students.name,classs=Students.classs,rollNo=Students.rollNo, MobileNo= Students.MobileNo,address=Students.address)
        db.add(student_details)
        db.commit()
        db.refresh(student_details)
        return student_details

    def fetch_by_id(db: Session,_id):
        return db.query(models.Students).filter(models.Students.id == _id).first()

    def fetch_by_name(db: Session,name):
        return db.query(models.Students).filter(models.Students.name == name).first()

    def fetch_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Students).offset(skip).limit(limit).all()

    async def delete(db: Session,student_id):
        db_item= db.query(models.Students).filter_by(id=student_id).first()
        db.delete(db_item)
        db.commit()
        
        
    async def update(db: Session,item_data):
        updated_item = db.merge(item_data)
        db.commit()
        return updated_item
    