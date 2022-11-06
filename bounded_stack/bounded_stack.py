class BoundedStack:
    PUSH_NIL: int = 0
    PUSH_OK: int = 1
    PUSH_ERR: int = 2

    POP_NIL: int = 0
    POP_OK: int = 1
    POP_ERR: int = 2

    PEEK_NIL: int = 0
    PEEK_OK: int = 1
    PEEK_ERR: int = 2

    DEFAULT_MAX_SIZE: int = 32

    # CONSTRUCTOR
    # POST-CONDITION: The new stack has been created.
    def __init__(self, max_size=DEFAULT_MAX_SIZE):
        self.peek_status = None
        self.pop_status = None
        self.stack = None
        self.push_status = None
        self.max_size = max_size
        self.clear()

    # __COMMAND__
    # PRE-CONDITION: Stack current size if less than max size limit.
    # POST-CONDITION: New item has been added at top of the stack.
    def push(self, value):
        if self.size() >= self.max_size:
            self.push_status = self.PUSH_ERR
        else:
            self.stack.append(value)
            self.push_status = self.PUSH_OK

    # __COMMAND__
    # PRE-CONDITION: The stack is not empty.
    # POST-CONDITION: The top item has been removed from the stack.
    def pop(self):
        if self.size() > 0:
            self.stack.pop(self.size()-1)
            self.pop_status = self.POP_OK
        else:
            self.pop_status = self.POP_ERR

    # __COMMAND__
    # POST-CONDITION: All items has beed deleted from the stack.
    def clear(self):
        self.stack = []
        self.push_status = self.PUSH_NIL
        self.pop_status = self.POP_NIL
        self.peek_status = self.PEEK_NIL

    # __QUERY__
    # PRE-CONDITOIN: The stack is not empty.
    def peek(self):
        if self.size() > 0:
            result = self.stack[-1]
            self.peek_status = self.PEEK_OK
        else:
            result = 0
            self.peek_status = self.PEEK_ERR

        return result

    def size(self):
        return len(self.stack)

    def get_peek_status(self):
        return self.peek_status

    def get_pop_status(self):
        return self.pop_status

    def get_push_status(self):
        return self.push_status