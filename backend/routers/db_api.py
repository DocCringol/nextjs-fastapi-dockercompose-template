from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
	prefix="/db-api"
)

@router.get("/")
def read_root():
	return "I'm dataBASE api"