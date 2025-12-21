from src.utils.constants import Collections
from src.models.theatre_model import TheatresList, Theatre
from src.exceptions.db_operation_errors import InputValidationFailedError, DeletedItemFailedError
from src.core.validators import validate_whole_number


def get_complete_theatre_list(start=0, page_size=10, page_num=1):
    skip_count = (page_num - 1) * page_size
    converted_data = Collections.theater.connection.get_records(skip_count=skip_count, page_size=page_size)
    object_model = TheatresList.model_validate_json(converted_data)
    return object_model.model_dump_json(indent=2)

def add_new_theatre(theatre: Theatre):
    # Verify Inputs
    if not validate_whole_number(theatre.capacity):
        raise InputValidationFailedError("Capacity Should not atleast be 1")
    if not theatre.location:
        raise InputValidationFailedError("Location cannot be empty")
    if not validate_whole_number(theatre.base_price_per_hr):
        raise InputValidationFailedError("Base price cannot be 0 or empty")
    if not validate_whole_number(theatre.price_per_person):
        raise InputValidationFailedError("Price per person cannot be 0 or empty")

    return Collections.theater.connection.insert_record(theatre.model_dump_json(indent=2))

def delete_theatre(id: str):
    #TODO: Add conditions which checks other links to this record (Set it as soft delete)
    
    record = Collections.theater.connection.get_record(id)
    if 'delete' in record:
        if record['delete']:
            raise DeletedItemFailedError("Item has been deleted previously")
    
    count = Collections.theater.connection.delete_record(id)
    if count == 1 :
        return True
    return False