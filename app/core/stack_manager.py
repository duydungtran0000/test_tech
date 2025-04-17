class StackManager:
    def __init__(self):
        self.stacks = {}
        self.counter = 1

    def create_stack(self):
        stack_id = self.counter
        self.stacks[stack_id] = []
        self.counter += 1
        return stack_id

    def list_stacks(self):
        return self.stacks

    def get_stack(self, stack_id: int):
        if stack_id not in self.stacks:
            raise KeyError
        return self.stacks[stack_id]

    def push(self, stack_id: int, value: float):
        if stack_id not in self.stacks:
            raise KeyError
        self.stacks[stack_id].append(value)
        return self.stacks[stack_id]

    def delete_stack(self, stack_id: int):
        if stack_id not in self.stacks:
            raise KeyError
        del self.stacks[stack_id]

stack_manager = StackManager()