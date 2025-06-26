# functions/services/employee_service.py
from firebase_admin import firestore

db = firestore.client()

def get_all_active_employees():
    try:
        employees_ref = db.collection('employees')
        query = employees_ref.where('es_activo', '==', 1).order_by('apellido')
        employees = []
        for doc in query.stream():
            employee_data = doc.to_dict()
            employee_data['id'] = doc.id
            employees.append(employee_data)
        return employees
    except Exception as e:
        print(f"Error al obtener empleados: {e}")
        return []

def add_employee(employee_data):
    try:
        employee_data['es_activo'] = 1
        employee_data['fecha_creacion'] = firestore.SERVER_TIMESTAMP
        timestamp, doc_ref = db.collection('employees').add(employee_data)
        return doc_ref.id
    except Exception as e:
        print(f"Error al añadir empleado: {e}")
        return None