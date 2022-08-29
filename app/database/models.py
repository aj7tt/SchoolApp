
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from app.database.dbConfig import Base
    
    
class Students(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(80), nullable=False)
    classs =Column(Integer)
    rollNo = Column(Integer)
    MobileNo = Column(Integer)
    address = Column(String(200))
    
    def __repr__(self):
        return 'studentsDetails(name=%s, classs=%s,rollNo=%s, MobileNo=%s, address=%s)' % (self.name, self.classs,self.rollNo, self.MobileNo, self.address)