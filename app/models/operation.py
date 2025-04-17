from enum import Enum

class Operation(str, Enum):
    add = "add"
    sub = "sub"
    mul = "mul"
    div = "div"