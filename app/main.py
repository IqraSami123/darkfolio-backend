from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import prisma
from app.routes import experience, projects, skills, contact, llm

app = FastAPI(title="Darkfolio Backend")

# CORS configuration for frontend
origins = [
    "http://localhost:8080",
    "https://your-nextjs-deployment.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Startup and shutdown events to connect/disconnect Prisma
@app.on_event("startup")
async def startup():
    await prisma.connect()

@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()

# ✅ Include all routers (prefixes defined in router files)
app.include_router(experience.router)
app.include_router(projects.router)
app.include_router(skills.router)
app.include_router(contact.router)
# app.include_router(llm.router)

@app.get("/")
async def root():
    return {"message": "Darkfolio Backend Running"}
