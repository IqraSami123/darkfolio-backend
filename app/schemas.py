from typing import List, Optional
from pydantic import BaseModel, EmailStr, HttpUrl
from datetime import datetime


class ExperienceBase(BaseModel):
    role: str
    company: str
    location: str
    duration: str
    type: str
    description: str
    achievements: List[str]
    technologies: List[str]


class ExperienceCreate(ExperienceBase):
    pass


class ExperienceUpdate(BaseModel):
    role: Optional[str] = None
    company: Optional[str] = None
    location: Optional[str] = None
    duration: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None
    achievements: Optional[List[str]] = None
    technologies: Optional[List[str]] = None


class ExperienceOut(ExperienceBase):
    id: int

    class Config:
        orm_mode = True


class SkillCategoryCreate(BaseModel):
    title: str
    description: str
    color: str
    skills: List[str]


class SkillCategoryUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    color: Optional[str]
    skills: Optional[List[str]]


class SkillCategoryOut(BaseModel):
    id: int
    title: str
    description: str
    color: str
    skills: List[str]

    class Config:
        orm_mode = True


class ContactMessageCreate(BaseModel):
    name: str
    email: EmailStr
    subject: str
    message: str


class ContactMessageOut(ContactMessageCreate):
    id: int
    createdAt: datetime

    class Config:
        orm_mode = True


class ProjectBase(BaseModel):
    title: str
    description: str
    technologies: List[str]
    imageUrl: HttpUrl
    githubUrl: Optional[HttpUrl] = None
    demoUrl: Optional[HttpUrl] = None
    featured: bool = False


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    technologies: Optional[List[str]]
    imageUrl: Optional[HttpUrl]
    githubUrl: Optional[HttpUrl]
    demoUrl: Optional[HttpUrl]
    featured: Optional[bool]


class ProjectOut(ProjectBase):
    id: int

    class Config:
        orm_mode = True