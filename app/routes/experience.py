from fastapi import APIRouter, HTTPException
from typing import List
from app.database import prisma
from app.schemas import ExperienceCreate, ExperienceUpdate, ExperienceOut
from fastapi import FastAPI

router = APIRouter(
    prefix="/experience",
    tags=["Experience"]
)


@router.post("/", response_model=ExperienceOut)
async def create_experience(experience: ExperienceCreate):
    return await prisma.experience.create(data=experience.dict())


@router.get("/", response_model=List[ExperienceOut])
async def get_experiences():
    return await prisma.experience.find_many(order={"id": "desc"})


@router.get("/{experience_id}", response_model=ExperienceOut)
async def get_experience(experience_id: int):
    exp = await prisma.experience.find_unique(where={"id": experience_id})
    if not exp:
        raise HTTPException(status_code=404, detail="Experience not found")
    return exp


@router.put("/{experience_id}", response_model=ExperienceOut)
async def update_experience(experience_id: int, experience: ExperienceUpdate):
    exp = await prisma.experience.update(
        where={"id": experience_id},
        data=experience.dict(exclude_unset=True)
    )
    return exp


@router.delete("/{experience_id}")
async def delete_experience(experience_id: int):
    await prisma.experience.delete(where={"id": experience_id})
    return {"message": "Experience deleted successfully"}
