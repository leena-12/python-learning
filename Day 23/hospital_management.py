# Composition: Department owns its own record-keeping (name, ward)
# Aggregation: Hospital uses Doctors and Patients (they exist independently)

class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization


class Patient:
    def __init__(self, name, disease):
        self.name = name
        self.disease = disease
        self.assigned_doctor = None


class Department:
    def __init__(self, name):
        self.name = name


class Hospital:
    def __init__(self, name):
        self.name = name
        self.doctors = []     # aggregation
        self.patients = []    # aggregation
        self.departments = []  # composition - created and owned by hospital

    def add_department(self, dept_name):
        dept = Department(dept_name)
        self.departments.append(dept)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def admit_patient(self, patient):
        self.patients.append(patient)

    def assign_doctor(self, patient, doctor):
        patient.assigned_doctor = doctor
        print(f"Dr. {doctor.name} assigned to {patient.name}")


hospital = Hospital("City Care")
hospital.add_department("Cardiology")

doc = Doctor("Sharma", "Cardiologist")
patient = Patient("Rahul", "Chest pain")

hospital.add_doctor(doc)
hospital.admit_patient(patient)
hospital.assign_doctor(patient, doc)