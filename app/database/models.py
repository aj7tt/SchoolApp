
from tokenize import Number
from sqlalchemy import Column, Integer, String,VARCHAR,Enum
from sqlalchemy.orm import relationship

from app.database.dbConfig import Base
    
    
class Students(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(80), nullable=False)
    classs =Column(Integer)
    rollNo = Column(Integer)
    MobileNo = Column(VARCHAR)
    address = Column(String(200))
    
    def __repr__(self):
        return 'studentsDetails(name=%s, classs=%s,rollNo=%s, MobileNo=%s, address=%s)' % (self.name, self.classs,self.rollNo, self.MobileNo, self.address)
    
    
class Staff(Base):
    __tablename__ = "staffs"
    
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(80), nullable=False)
    gender= Column(Enum('male', 'female'))
    MobileNo = Column(VARCHAR(32))
    address = Column(String(200))
    
    def __repr__(self):
        return 'staffDetails(name=%s, gender=%s, MobileNo=%s, address=%s)' % (self.name,self.gender, self.MobileNo, self.address)