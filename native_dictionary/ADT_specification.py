"""
BaseNativeDictionary is abstract data type (base class) definition for
implementing a native dictionary data types.
CONSTANTS
    PUT_NIL         # put() was not called
    PUT_OK          # last put() call completed
    PUT_UPDATE      # last put() call was not completed

    REMOVE_NIL      # remove() was not called
    REMOVE_OK       # last remove() call completed
    REMOVE_ERR      # last remove() call was not completed

    GET_NIL         # __getitem__() not called yet
    GET_OK          # last __getitem__() returned correct value
    GET_ERR         # in not key of the dictionary

    INITIAL_SIZE    # Initial size of internal key-value storage

CONSTRUCTOR
    __new__(cls) -> new instance.
        Post-condition:
            - new instance created.
    __init__(self, capacity: int):
        Initializing the instance after its creation.
        Post-condition:
            - items count in the internal storage eq to 0.
            - command statuses set to initial constants.
COMMANDS
    put(self, key: str, value: object):
        Put/update __value__ object under __key__ in the NativeDictionary.
        Post-condition:
            - __value__ was placed in NativeDictionary under specified __key__.
    remove(self, key: str):
        Remove an object from the NativedDictionary by specified __key__.
        Pre-condition:
            - __key__ exists in the NativeDictionary.
        Post-condition:
            - Object stored under __key__ is removed from NativeDictionary.
REQUESTS
    __len__(self) -> count of items in the NativeDictionary.
    get(self, key: str) -> item value.
        Pre-condition:
            - __key__ exists in the NativeDictionary.
STATUS REQUESTS
    get_put_status(self) -> status of last put() call.
    get_remove_status(self) -> status of last remove() call.
    get_get_status(self) -> status of last get() call.
"""


# Overall lazy implementation

class BaseNativeDictionary():
    PUT_NIL = 0
    PUT_OK = 1
    PUT_ERR = 2

    GET_NIL = 0
    GET_OK = 1
    GET_ERR = 2

    REMOVE_NIL = 0
    REMOVE_OK = 1
    REMOVE_ERR = 2

    def __init__(self):
        self.internal_storage = {}

        self.status_put = self.PUT_NIL
        self.status_get = self.GET_NIL
        self.status_remove = self.REMOVE_NIL

    # COMMANDS
    def put(self, key, value):
        self.status_put = self.PUT_OK
        self.internal_storage[key] = value

    def remove(self, key):
        if key in self.internal_storage:
            self.internal_storage.pop(key)
            self.status_remove = self.REMOVE_OK
        else:
            self.status_remove = self.REMOVE_ERR

    # REQUESTS
    def get(self, key):
        if key in self.internal_storage:
            self.status_get = self.GET_OK
            return self.internal_storage[key]
        else:
            self.status_get = self.GET_ERR
            return None

    def is_key(self, key):
        return key in self.internal_storage

    # ADDITIONAL REQUESTS
    def get_get_status(self):
        return self.status_get

    def get_remove_status(self):
        return self.status_remove