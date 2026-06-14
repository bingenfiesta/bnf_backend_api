from src.utils.constants import Collections
from src.models.booking_details_model import Booking, BookingList
from src.exceptions.db_operation_errors import InputValidationFailedError, DeletedItemFailedError
from src.core.validators import validate_contact_number, validate_email, validate_whole_number


def get_bookings_list(start=0, page_size=10, page_num=1):
    skip_count = (page_num - 1) * page_size
    converted_data = Collections.bookings.value.connection.get_records(skip_count=skip_count, page_size=page_size)
    payload = {"bookings": converted_data}
    object_model = BookingList.model_validate(payload)
    return object_model.model_dump_json(indent=2)


def add_new_booking(booking: Booking):
    # basic validations
    if not validate_contact_number(booking.contact):
        raise InputValidationFailedError("Invalid contact number")
    if not validate_email(booking.email):
        raise InputValidationFailedError("Invalid email")
    if not validate_whole_number(booking.number_of_people):
        raise InputValidationFailedError("Number of people must be > 0")

    insertion = booking.model_dump()
    return Collections.bookings.value.connection.insert_record(insertion)


def delete_booking(id: str):
    record = Collections.bookings.value.connection.get_record(id)
    if not record:
        raise DeletedItemFailedError("Item not found")
    if record.get('delete'):
        raise DeletedItemFailedError("Item already deleted")

    count = Collections.bookings.value.connection.delete_record(id)
    return True if count == 1 else False


def update_booking(id: str, updates: dict):
    if 'contact' in updates:
        if not validate_contact_number(updates['contact']):
            raise InputValidationFailedError("Invalid contact number")
    if 'email' in updates:
        if not validate_email(updates['email']):
            raise InputValidationFailedError("Invalid email")
    if 'number_of_people' in updates:
        if not validate_whole_number(updates['number_of_people']):
            raise InputValidationFailedError("Number of people must be > 0")

    modified_count = Collections.bookings.value.connection.update_record(id, updates)
    return modified_count
