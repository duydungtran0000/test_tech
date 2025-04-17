from fastapi import APIRouter, HTTPException, Path
from app.models.operation import Operation
from app.core.stack_manager import stack_manager

router = APIRouter(prefix="/op")

@router.get("")
def list_all_operands():
    return {
        "add": {"symbol": "+", "description": "Addition"},
        "sub": {"symbol": "-", "description": "Subtraction"},
        "mul": {"symbol": "*", "description": "Multiplication"},
        "div": {"symbol": "/", "description": "Division"}
    }


@router.post("/{op}/stack/{stack_id}")
def apply_operation(op: Operation, stack_id: int = Path(..., ge=1)):
    try:
        stack = stack_manager.get_stack(stack_id)
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Stack {stack_id} not found")

    if len(stack) < 2:
        raise HTTPException(status_code=400, detail="Not enough operands")

    b = stack.pop()
    a = stack.pop()

    if op == Operation.add:
        result = a + b
    elif op == Operation.sub:
        result = a - b
    elif op == Operation.mul:
        result = a * b
    elif op == Operation.div:
        if b == 0:
            raise HTTPException(status_code=400, detail="Division by zero")
        result = a / b

    stack.append(result)
    return {"result": result, "stack": stack}
