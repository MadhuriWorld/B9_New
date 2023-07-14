#===================================================== ONE TO ONE RELATIONSHIP============================================


from django.db import models

# Create your models here.


class Person(models.Model):                                             # pid act as a primary key
    name = models.CharField(max_length= 100)
    age = models.IntegerField()
    email = models.EmailField()
    mobile = models.BigIntegerField(null= True, unique= True)
    is_active = models.BooleanField(default= True)


    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "person"



class Aadhar(models.Model):
    a_number = models.BigIntegerField(unique= True)
    address = models.CharField(max_length= 200)
    created_date = models.DateTimeField(auto_now= True)
    created_by = models.CharField(max_length= 100)
    updated_by = models.CharField(max_length= 100)
    dob = models.DateField()
    person = models.OneToOneField("Person", on_delete= models.CASCADE, null= True)          # can use related_name = "aadhar_num"
                                                                                            # establishing one to one relation bewtween person and aadhar. pid act as foreign key 
                                                                                            # class Person should be use and variable name must be small lette.
                                                                                            # on_delete = models.CASCADE, means if PERSON table deleted then AADHAR table also get deletd 
    is_active = models.BooleanField(default= True)

    def __str__(self):
        return str(self.a_number)

    
    class Meta:
        db_table = "aadhar"


#============================================== ONE TO MANY RELATIONSHIP=================================================


class Car(models.Model):
    name = models.CharField(max_length= 255)


    def __str__(self):
        return self.name
    

    class Meta:
        db_table = "car"


class CarModel(models.Model):
    name = models.CharField(max_length= 255)
    car = models.ForeignKey(Car, on_delete= models.SET_NULL, null= True)            # on_delete = models.SET_NULL, means if we delete CAR model then the value of CARMODEL set to NULL


    def __str__(self):
        return self.name


    class Meta:
        db_table = "car_model"



