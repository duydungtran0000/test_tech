from fastapi import APIRouter, Path, HTTPException, status
from app.models.stack import PushRequest
from app.core.stack_manager import stack_manager

router = APIRouter(prefix="/stack")

@router.post("")
def create_stack():
    stack_id = stack_manager.create_stack()
    return {"stack_id": stack_id}

@router.get("")
def list_stacks():
    return stack_manager.list_stacks()

@router.get("/{stack_id}")
def get_stack(stack_id: int = Path(..., ge=1)):
    try:
        return {"stack": stack_manager.get_stack(stack_id)}
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Stack {stack_id} not found")

@router.post("/{stack_id}")
def push_value(stack_id: int = Path(..., ge=1), data: PushRequest = ...):
    try:
        return {"stack": stack_manager.push(stack_id, data.value)}
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Stack {stack_id} not found")

@router.delete("/{stack_id}")
def delete_stack(stack_id: int = Path(..., ge=1)):
    try:
        stack_manager.delete_stack(stack_id)
        return {"message": f"Stack {stack_id} deleted"}
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Stack {stack_id} not found")
