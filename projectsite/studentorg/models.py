from django.db import models

# Create your models here.
#class Boat(models.Model):
#    boat_name = models.CharField(max_length=150)
#    length = models.DecimalField(max_digits=10, decimal_places=2)
#    width = models.DecimalField(max_digits=10, decimal_places=2)
#    height = models.DecimalField(max_digits=10, decimal_places=2)

class BaseModel (models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class College(BaseModel):
    college_name = models.CharField(max_length=150, verbose_name="College")

    def __str__(self) :
        return self.college_name
    
class Program(BaseModel):
    prog_name = models.CharField(max_length=150, verbose_name="Program Name")
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self) :
        return self.prog_name

class Organization(BaseModel):
    name = models.CharField(max_length=250)
    college = models.ForeignKey(College, null=True, blank=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Student(BaseModel):
    student_id = models.CharField(max_length=15)
    lastname = models.CharField(max_length=25, verbose_name="Last Name")
    firstname = models.CharField(max_length=25, verbose_name="First Name")
    middlename = models.CharField(max_length=25, blank=True, null=True , verbose_name="Middle Name")
    program = models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.lastname}, {self.firstname}"

class OrgMember(BaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    date_joined = models.DateField()
    
    def __str__(self) -> str:
        return f"{self.student}"



