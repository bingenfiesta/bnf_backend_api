from src.utils.constants import Collections
from src.models.slot_model import Slot, SlotsList
from src.exceptions.db_operation_errors import InputValidationFailedError, DeletedItemFailedError


def get_slots_list(start=0, page_size=10, page_num=1):
    skip_count = (page_num - 1) * page_size
    converted_data = Collections.slots.value.connection.get_records(skip_count=skip_count, page_size=page_size)
    payload = {"slots": converted_data}
    object_model = SlotsList.model_validate(payload)
    return object_model.model_dump_json(indent=2)


def add_new_slot(slot: Slot):
    # basic validation
    if slot.start >= slot.end:
        raise InputValidationFailedError("Slot start must be before end")
    if slot.price < 0:
        raise InputValidationFailedError("Price cannot be negative")

    insertion = slot.model_dump()
    return Collections.slots.value.connection.insert_record(insertion)


def delete_slot(id: str):
    record = Collections.slots.value.connection.get_record(id)
    if not record:
        raise DeletedItemFailedError("Item not found")
    if record.get('delete'):
        raise DeletedItemFailedError("Item already deleted")

    count = Collections.slots.value.connection.delete_record(id)
    return True if count == 1 else False


def update_slot(id: str, updates: dict):
    if 'start' in updates and 'end' in updates:
        if updates['start'] >= updates['end']:
            raise InputValidationFailedError("Slot start must be before end")
    if 'price' in updates:
        if updates['price'] < 0:
            raise InputValidationFailedError("Price cannot be negative")

    modified_count = Collections.slots.value.connection.update_record(id, updates)
    return modified_count
