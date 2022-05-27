class student:
    school = "AkiraChix"
    def __init__(self, first_name,last_name,age, current_year ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.current_year = current_year
    
    def full_name(self):
        return f"Hello {self.first_name} {self.last_name} is your full name."

    def initials(self):
        return f"Your initials are {self.first_name[0]} {self.last_name[0]}"
    
    def year_of_birth(self):
        year_of_birth = self.current_year - self.age
        return f"You were born in {year_of_birth}"

