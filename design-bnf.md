# Design - Binge N Fiesta

## UI
- **User UI**
- **Admin UI**

### Roles
- User
- Admin
- Custom Roles

---

## Booking Flow
1. Choose Theatre and Slot  
2. Payment  
3. Booking Details  
4. Choose Add Ons  
5. Choose Decoration  

### Data Needed
- Theatres  
- Decorations  
- Add Ons  
- User Data  
- Theatre, Slot, Decoration, Add Ons, Coupon  
- Payment Details  
- Booking Details  
- Communication Template  
- Role Management  
- Packages  

---

## Theatre
| Field | Description |
|-------|-------------|
| ID | Unique identifier |
| Name | Theatre name |
| Description | Theatre details |
| Location | Address |
| Capacity | Seating capacity |
| Images | Theatre photos |
| Video | Theatre video |
| Base Price/hr | Hourly rate |
| Price/person | Per person rate |
| Features | Special features |
| Projector detail | Projector info |
| Sound System | Audio setup |
| Others | Additional features |

---

## Slots
| Field | Description |
|-------|-------------|
| ID | Unique identifier |
| Name | Slot name |
| Start | Date & Time |
| End | Date & Time |
| Price | Slot price |
| Theatre | Linked theatre |
| Applied coupon | Coupon applied |

---

## Decorations
| Field | Description |
|-------|-------------|
| ID | Unique identifier |
| Name | Decoration name |
| Price | Cost |
| Theatre | Linked theatre |
| Slot | Linked slot |
| Images | Decoration photos |
| Video | Decoration video |
| Description | Details |

---

## Add-Ons
| Field | Description |
|-------|-------------|
| ID | Unique identifier |
| Name | Add-on name |
| Description | Details |
| Location | Applicable location |
| Capacity | Capacity |
| Images | Photos |
| Video | Video |
| Category | Type of add-on |
| Price | Cost |
| Options | Optional features |

---

## Coupons
| Field | Description |
|-------|-------------|
| ID | Unique identifier |
| Name | Coupon name |
| Start | Start date |
| End | End date |
| Count | Usage count |
| Coupon Code | Code |
| Theatre | Applicable theatre |
| Type | Percentage / Flat |
| Value | Discount value |
| Description | Details |
| Conditions | Terms |
| Options | Optional rules |

---

## Booking Details
| Field | Description |
|-------|-------------|
| ID | Unique identifier |
| Name of person | Customer name |
| Contact | Contact info |
| Total price | Final cost |
| Theatre | Theatre booked |
| Slot | Slot booked |
| Number of persons | Attendees |
| AddOns | Selected add-ons |
| AddOns options | Options chosen |
| Decorations | Selected decorations |
| Notes | Extra notes |
| Advance payment | Paid amount |
| Coupon Applied | Coupon used |
| Booking status | Status |
| Booking date | Date |
| Email | Customer email |
| Discount price | Discounted amount |
| Billing details | Billing info |
| Communication status | Communication record |
| Txn IDs | Transaction IDs |

---

## Roles
| Field | Description |
|-------|-------------|
| ID | Unique identifier |
| Name | Role name |
| Description | Role details |
| Permissions | Role permissions |

---

## Packages
| Field | Description |
|-------|-------------|
| ID | Unique identifier |
| Name | Package name |
| Description | Package details |
| Photo | Package photo |
| Video | Package video |
| Price | Cost |
| Theatre | Linked theatre |
| Decorations | Included decorations |
| Add Ons | Included add-ons |
| Add Ons options | Options |
| Conditions | Terms |
| Options | Optional rules |

---

## Communication Template
| Field | Description |
|-------|-------------|
| ID | Unique identifier |
| Type of communication | Email / SMS / Notification |
| Template | Message template |
| Photos | Attached photos |
