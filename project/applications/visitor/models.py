from django.db import models
from dataclasses import dataclass


@dataclass
class VisitorContext:
    mobile_number: str
    email: str
    first_name: str
    last_name: str
    date_of_birth: str
    gender: str


class VisitorManager(models.Manager):
    def merge_separated_date_of_birth(self, year, month, day):
        return f"{year}-{month}-{day}"

    def create_new_visitor(self, VisitorContext: VisitorContext):
        visitor = Visitor(
            mobile_number= VisitorContext.mobile_number,
            email= VisitorContext.email,
            first_name= VisitorContext.first_name,
            last_name= VisitorContext.last_name,
            date_of_birth= VisitorContext.date_of_birth,
            gender= VisitorContext.gender,
        )
        visitor.save()
        return visitor


class Visitor(models.Model):
    GENDER_CHOICE = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    id = models.AutoField(primary_key=True)
    mobile_number = models.CharField(max_length=25, verbose_name="Mobile Number")
    email = models.EmailField(max_length=254, verbose_name='Email')
    first_name = models.CharField(max_length=50, verbose_name='First Name')
    last_name = models.CharField(max_length=50, verbose_name='Last Name')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name="Date Of Birth")
    gender = models.CharField(max_length=6, choices=GENDER_CHOICE, blank=True, null=True, verbose_name='Gender')

    objects = VisitorManager()

    class Meta:
        unique_together = ('mobile_number', 'email')
