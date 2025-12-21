class InputValidationFailedError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
    
    def __str__(self, field_name:str = ""):
        return f"Input Validation : {field_name}"


class DeletedItemFailedError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

    def __str__(self, message):
        return f"Item Deletion Failed : {message}"