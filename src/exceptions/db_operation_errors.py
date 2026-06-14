class InputValidationFailedError(Exception):
    def __init__(self, field_name: str = ""):
        self.field_name = field_name
        super().__init__(field_name)

    def __str__(self):
        return f"Input Validation : {self.field_name}"


class DeletedItemFailedError(Exception):
    def __init__(self, message: str = ""):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f"Item Deletion Failed : {self.message}"