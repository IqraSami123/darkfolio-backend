# routes/contact.py
from fastapi import APIRouter, HTTPException
from typing import List
from app.database import prisma
from app.schemas import ContactMessageCreate, ContactMessageOut

router = APIRouter(prefix="/contact", tags=["Contact"])


# Create a new contact message
@router.post("/", response_model=ContactMessageOut)
async def create_contact_message(contact: ContactMessageCreate):
    return await prisma.contactmessage.create(data=contact.dict())


# Get all messages
@router.get("/", response_model=List[ContactMessageOut])
async def get_all_messages():
    return await prisma.contactmessage.find_many(order={"createdAt": "desc"})


# Get a single message by ID
@router.get("/{message_id}", response_model=ContactMessageOut)
async def get_message(message_id: int):
    message = await prisma.contactmessage.find_unique(where={"id": message_id})
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    return message


# Delete a message by ID
@router.delete("/{message_id}", response_model=dict)
async def delete_message(message_id: int):
    message = await prisma.contactmessage.delete(where={"id": message_id})
    return {"detail": f"Message {message.id} deleted successfully"}
