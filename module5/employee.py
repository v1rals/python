class Employee:
    def __init__(self, n, s, i):
        self.first_name = n.capitalize()
        self.last_name = s.capitalize()
        self.email = n.lower() + "_" + s.lower() + "@example.com"
        self.salary = i

    @property
    def full_name(self):
        return self.first_name + "," + " " + self.last_name

    @full_name.setter
    def full_name(self, full_name):
        self.first_name, self.last_name = full_name.split(", ")
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()

    @classmethod
    def from_str(cls, str_in):
        lst = str_in.split(',')
        cls.first_name = lst[0].capitalize()
        cls.last_name = lst[1].capitalize()
        #   cls.full_name = lst[0].capitalize(), lst[1].capitalize()
        cls.email = lst[0] + "_" + lst[1] + "@example.com"
        cls.salary = int(lst[2])
        return cls


class DevOps(Employee):
    def __init__(self, n, s, i, sk=None):
        Employee.__init__(self, n, s, i)
        self.skills = sk

    def add_skill(self, attr):
        if self.skills is None:
            self.skills = []
            pass
        self.skills.append(attr.capitalize())
        return self.skills

    def remove_skill(self, attr):
        if self.skills is None:
            self.skills = []
            pass
        try:
            self.skills.remove(attr.capitalize())
        except Exception:
            pass
        return self.skills

class Manager(Employee):
    def __init__(self, n, s, i, l=None):
        Employee.__init__(self, n, s, i)
        self.subordinates = l

    def add_subordinate(self, attr):
        if self.subordinates is None:
            self.subordinates = []
            pass
        self.subordinates.append(attr)
        return self.subordinates

    def remove_subordinate(self, attr):
        if self.subordinates is None:
            self.subordinates = []
            pass
        if attr == str(attr):
            print("email")
            print(attr)
            del self.subordinates[0]
        try:
            self.subordinates.remove(attr)
        except ValueError:
            pass
        return self.subordinates