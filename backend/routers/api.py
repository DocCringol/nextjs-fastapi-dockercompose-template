from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
	prefix="/api"
)

@router.get("/")
def read_root():
	return "I'm main api"