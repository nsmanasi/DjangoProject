class Emply():
    
 def __init__ (self, title, fname, lname):
    self.title = title
    self.fname = fname
    self.lname = lname

 def __eq__ (self, other):
     return self.title == other.title and self.fname == other.fname and \
            self.lname == other.lname

 def __hash__ (self):
     return hash(('title', self.title, 'fname', self.fname, 'lname', self.lname))
    
emp1 = Emply("Mr.", "Prakash", "Sharma")
emp2 = Emply("Ms.", "Mansi", "Sharma")
emp3 = Emply("Mr.", "Prakash", "Sharma")


emp_set = set()
emp_set.add(emp1)
emp_set.add(emp2)
emp_set.add(emp3)
print(len(emp_set))


