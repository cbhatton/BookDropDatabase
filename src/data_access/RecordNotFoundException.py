class RecordNotFoundException(Exception):
    def __init__(self, key):
        self.key = key
        self.message = f"The requested record with key [{key}] does not exist."
        super().__init__(self.message)
