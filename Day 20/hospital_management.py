class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print("Name   :", self.name)
        print("Age    :", self.age)
        print("Gender :", self.gender)


class Doctor(Person):
    def __init__(self, name, age, gender, specialization, experience_years):
        super().__init__(name, age, gender)
        self.specialization = specialization
        self.experience_years = experience_years

    def display(self):
        super().display()
        print("Specialization     :", self.specialization)
        print("Experience (years) :", self.experience_years)


class Nurse(Person):
    def __init__(self, name, age, gender, department):
        super().__init__(name, age, gender)
        self.department = department

    def display(self):
        super().display()
        print("Department :", self.department)


class Patient(Person):
    def __init__(self, name, age, gender, patient_id, disease):
        super().__init__(name, age, gender)
        self.patient_id = patient_id
        self.disease = disease

    def display(self):
        super().display()
        print("Patient ID :", self.patient_id)
        print("Disease    :", self.disease)

if __name__ == "__main__":
    doc = Doctor("Dr. Sharma", 45, "Male", "Cardiology", 18)
    nurse = Nurse("Anita", 30, "Female", "ICU")
    patient = Patient("Rohan", 55, "Male", "P1001", "Hypertension")

    print("=== Doctor ===")
    doc.display()

    print("\n=== Nurse ===")
    nurse.display()

    print("\n=== Patient ===")
    patient.display()