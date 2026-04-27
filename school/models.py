from django.db import models

# Create your models here

# Model User
class User(models.Model):
    email = models.CharField(max_length=100)
    password = models.TextField(max_length=500)
    status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


# Model Identification_Type
class IdentificationType(models.Model):
    name = models.CharField(max_length=50)
    abrev = models.CharField(max_length=10)
    description = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


# Model Country
class Country(models.Model):
    name = models.CharField(max_length=100)
    abrev = models.CharField(max_length=10)
    description = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


# Model Departments

class Department(models.Model):
    name = models.CharField(max_length=100)
    abrev = models.CharField(max_length=10)
    description = models.CharField(max_length=100)

    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)



# Model cities

class City(models.Model):
    name = models.CharField(max_length=100)
    abrev = models.CharField(max_length=10)
    description = models.CharField(max_length=100)

    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)



# Model Persons
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    identification_type = models.ForeignKey(IdentificationType, on_delete=models.CASCADE)
    ident_number = models.CharField(max_length=15)

    city = models.ForeignKey(City, on_delete=models.CASCADE)

    address = models.CharField(max_length=150)
    mobile = models.CharField(max_length=50)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


# Model  Students 
class Student(models.Model):
    code = models.CharField(max_length=50)

    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)