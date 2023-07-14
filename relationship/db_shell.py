#=========================================== ONE TO ONE RELATIONSHIP======================================


# exec(open(r"E:\Python_class\DjangoProjects\B9_Library\relationship\db_shell.py").read()) 


from relationship.models import *


#creating person details, data enter in db 

# p1 = Person.objects.create(name = "STU", age= 28, mobile = 9630258741, email = 'stu@gmail.com')



# fetching all person data from database 

# all = Person.objects.all()
# print(all)



# fetching single person detail from db using id

# p1 = Person.objects.get(id = 1)
# print(p1)

# CREATING AADAHAR USER


from django.utils import timezone
from datetime import date 

# THERE ARE TWO WAYS TO ADD PERSON IN AADHAR

# 1ST WAY (giving person instance and fetching id from database)

# a1 = Aadhar.objects.create(a_number = 456987123698, address = "Pune", created_by = "GOI", updated_by = "A", dob = date(1991, 6, 2), person = p1)


# 2ND WAY (directly giving id)

# a1 = Aadhar.objects.create(a_number = 147025836987, address = "RJ", created_by = "GOI", updated_by = "E", dob = date(1998, 2, 28), person_id = 5)


# 3rd WAY (CREATING PERSON AND AADHAR OBJECT SEPRATELY, PUT NULL= TRUE IN PERSON IN AADHAR AND NOY GIVING PERSON ID DURING AADHAR OBJECT CREATION)

# p1 = Person.objects.create(name = "AWS", age= 20, mobile = 7456892310, email = 'aws@gmail.com')

# a1 = Aadhar.objects.create(a_number = 201345678933, address = "MP", created_by = "GOI", updated_by = "F", dob = date(1997, 3, 15))


# FETCHING PERSON FROM AADHAR DETAILS  (Aadhar.object.person)           person in small letter


# a3 = Aadhar.objects.get(id = 5)
# print(a3)                                             # AADHAR DETAILS OF ID = 5

# p1 = Aadhar.objects.get(a_number =3698521473355)
# print(p1.person)                                      # PERSON NAME WHERE AADHAR NUMBER IS GIVEN
# print(p1.person.email)
# print(p1.person.mobile)
# print(p1.person.age)
# print(p1.person.id)


# FETCHING AADHAR DETAILS FROM PERSON   (Person.object.aadhar)       aadhar in small letter

# p1 = Person.objects.get(id = 1)
# print(p1.aadhar)                                            # aadhar number
# print(p1.aadhar.address)                                    # address of id=1
# print(p1.__dict__)                                          # perons dict
# print(p1.aadhar.__dict__)                                   # aadhar dict where id =1

# print(p1.aadhar.created_date)
# print(p1.aadhar.person_id)
# print(p1.aadhar.dob)

#--------------------------------------CODE OPTIMIZATION-------------------------------

# TO REDUCE TIME
# HERE USING "SELECT_RELATED"


# a3 = Aadhar.objects.select_related("person").get(a_number =3698521473355)             # FOR SINGLE PERSON
# print(a3.person)


# a1 = Aadhar.objects.all().select_related("person")
# print(a1)                                                 # QUERY SET
# print(list(a1))                                           # list


# for i in Aadhar.objects.all().select_related("person"):                           FOR ALL
    # print(i)
    # print(i.person)
    # print(i.person.age)
    # print(i.person.mobile)



# for p in Person.objects.all().select_related("aadhar"):           # if related_name is define then-- Person.object.all().select_related("aafhar_num")
    # print(p)
    # print(p.aadhar.a_number)
    # print(p.aadhar.address)
    # print(p.aadhar.dob)


#================================================== ONE TO MANY RELATIONSHIP=====================================


# CREATING CAR OBJECTS

# c1 = Car.objects.create(name = "BMW")

# c1 = Car.objects.all()
# print(c1)


# CREATING CAR MODEL OBJECTS 

mercedes = Car.objects.get(name = "Mercedes")
c1 = CarModel.objects.create(name = "C200", car = mercedes)


# bmw = Car.objects.get(name = "BMW")
# c1 = CarModel.objects.create(name = "X7", car = bmw)


# FETCHING DATA FROM TABLE

c2= CarModel.objects.get(name = "C180")
print(c2.car.name)