def get_sample_appointments():
    return [
        {"date": "2025-04-20", "time": "10:00 AM", "doctor": "Dr. John Doe", "status": "Confirmed"},
        {"date": "2025-04-22", "time": "2:00 PM", "doctor": "Dr. Jane Smith", "status": "Pending"},
    ]

def get_sample_prescriptions():
    return [
        {"date": "2025-04-15", "medication": "Ibuprofen", "dosage": "200mg", "frequency": "Twice daily"},
        {"date": "2025-04-10", "medication": "Amoxicillin", "dosage": "500mg", "frequency": "Three times a day"},
    ]

def get_sample_patients():
    return [
        {"name": "Alice Brown", "condition": "Diabetes", "last_visit": "2025-04-12"},
        {"name": "Bob Green", "condition": "Hypertension", "last_visit": "2025-04-10"},
    ]

def get_sample_emergency_logs():
    return [
        {"date": "2025-04-14", "incident": "Cardiac arrest", "handled_by": "Team A"},
        {"date": "2025-04-13", "incident": "Accident Trauma", "handled_by": "Team B"},
    ]
