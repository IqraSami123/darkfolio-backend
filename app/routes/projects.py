from fastapi import APIRouter, HTTPException
from typing import List
from app.database import prisma
from app.schemas import ProjectCreate, ProjectUpdate, ProjectOut

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


# Read all / optionally filter featured
@router.get("/", response_model=List[ProjectOut])
async def get_projects(featured: bool = None):
    filters = {}
    if featured is not None:
        filters["featured"] = featured
    return await prisma.project.find_many(
        where=filters,
        order={"id": "asc"}
    )


# Read single
@router.get("/{project_id}", response_model=ProjectOut)
async def get_project(project_id: int):
    project = await prisma.project.find_unique(where={"id": project_id})
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


# Create
@router.post("/", response_model=ProjectOut)
async def create_project(project: ProjectCreate):
    return await prisma.project.create(data=project.dict())


# Update
@router.put("/{project_id}", response_model=ProjectOut)
async def update_project(project_id: int, project: ProjectUpdate):
    existing = await prisma.project.find_unique(where={"id": project_id})
    if not existing:
        raise HTTPException(status_code=404, detail="Project not found")
    return await prisma.project.update(
        where={"id": project_id},
        data=project.dict(exclude_unset=True)
    )


# Delete
@router.delete("/{project_id}", response_model=dict)
async def delete_project(project_id: int):
    existing = await prisma.project.find_unique(where={"id": project_id})
    if not existing:
        raise HTTPException(status_code=404, detail="Project not found")
    await prisma.project.delete(where={"id": project_id})
    return {"detail": "Project deleted successfully"}



