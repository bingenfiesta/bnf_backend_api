from src.utils.constants import Collections
from src.models.theatre_model import TheatresList, Theatre
from src.exceptions.db_operation_errors import InputValidationFailedError, DeletedItemFailedError
from src.core.validators import validate_whole_number


def get_complete_theatre_list(start=0, page_size=10, page_num=1):
    skip_count = (page_num - 1) * page_size
    converted_data = Collections.theater.value.connection.get_records(skip_count=skip_count, page_size=page_size)
    # Wrap into expected structure for model validation
    payload = {"theaters": converted_data}
    object_model = TheatresList.model_validate(payload)
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

    # Insert as dict
    insertion = theatre.model_dump()
    return Collections.theater.value.connection.insert_record(insertion)

def delete_theatre(id: str):
    #TODO: Add conditions which checks other links to this record (Set it as soft delete)
    
    record = Collections.theater.value.connection.get_record(id)
    if 'delete' in record:
        if record['delete']:
            raise DeletedItemFailedError("Item has been deleted previously")
    
    count = Collections.theater.value.connection.delete_record(id)
    if count == 1:
        return True
    return False


def update_theatre(id: str, updates: dict):
    # basic validation on provided fields
    if 'capacity' in updates:
        if not validate_whole_number(updates['capacity']):
            raise InputValidationFailedError("Capacity must be > 0")
    if 'base_price_per_hr' in updates:
        if not validate_whole_number(updates['base_price_per_hr']):
            raise InputValidationFailedError("Base price must be > 0")
    if 'price_per_person' in updates:
        if not validate_whole_number(updates['price_per_person']):
            raise InputValidationFailedError("Price per person must be > 0")

    modified_count = Collections.theater.value.connection.update_record(id, updates)
    return modified_count