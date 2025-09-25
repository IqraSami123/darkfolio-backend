from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import SkillCategoryCreate, SkillCategoryUpdate, SkillCategoryOut
from app.database import prisma

router = APIRouter(
    prefix="/skills",
    tags=["Skills"]
)


@router.post("/", response_model=List[SkillCategoryOut])
async def create_skills(skills: List[SkillCategoryCreate]):
    created_skills = []
    for skill in skills:
        created = await prisma.skillcategory.create(data=skill.dict())
        created_skills.append(created)
    return created_skills


@router.get("/", response_model=List[SkillCategoryOut])
async def get_skill_categories():
    return await prisma.skillcategory.find_many(order={"id": "asc"})


@router.get("/{category_id}", response_model=SkillCategoryOut)
async def get_skill_category(category_id: int):
    category = await prisma.skillcategory.find_unique(where={"id": category_id})
    if not category:
        raise HTTPException(status_code=404, detail="Skill category not found")
    return category


@router.put("/{category_id}", response_model=SkillCategoryOut)
async def update_skill_category(category_id: int, category: SkillCategoryUpdate):
    updated = await prisma.skillcategory.update(
        where={"id": category_id},
        data=category.dict(exclude_unset=True)
    )
    return updated


@router.delete("/{category_id}")
async def delete_skill_category(category_id: int):
    await prisma.skillcategory.delete(where={"id": category_id})
    return {"message": "Skill category deleted successfully"}
