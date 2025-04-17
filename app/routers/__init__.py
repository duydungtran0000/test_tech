from fastapi import APIRouter
from .stack import router as stack_router
from .operation import router as operation_router

router = APIRouter(prefix="/rpn", tags=["RPN"])

router.include_router(stack_router)
router.include_router(operation_router)