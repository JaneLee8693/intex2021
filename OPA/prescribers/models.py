from django.db import models

from django.db.models.deletion import CASCADE, DO_NOTHING, SET_NULL

# Create your models here.
class State(models.Model):
    stateName = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=2)
    population = models.IntegerField()
    death = models.IntegerField()

    class Meta:
        db_table = "state"

    def __str__(self) :
        return (self.stateName)

class Drug(models.Model):
    drugName = models.CharField(max_length=150)
    isOpioid = models.BooleanField()

    class Meta:
        db_table = "drug"

    def __str__(self):
        return (self.drugName)

class Specialty(models.Model):
    specialtyName = models.CharField(max_length=50)

    class Meta:
            db_table = "specialty"

    def __str__(self):
        return (self.specialtyName)

class Credential(models.Model):
    credentialName = models.CharField(max_length=10)

    class Meta:
            db_table = "credential"

    def __str__(self):
        return (self.credentialName)


class Prescriber(models.Model):
    GENDER = (
                ('M', 'Male'),
                ('F', 'Female'),
                ('O', 'Other')
            )

    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    npi = models.IntegerField()
    gender = models.CharField(max_length=4, choices=GENDER, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=DO_NOTHING)
    specialtyId = models.ForeignKey(Specialty, on_delete=DO_NOTHING)
    isOpiodPrescriber = models.BooleanField()
    totalPrescriptions = models.IntegerField()

    presciber_drugs_field = models.ManyToManyField('Drug', through="Prescriber_Drug")

    prescriber_credential_field = models.ManyToManyField('Credential', through="Prescriber_Credential")
    class Meta:
        db_table = 'prescriber'

    def __str__(self):
        return (f"{self.firstName} {self.lastName}")
    
class Prescriber_Drug(models.Model):
    prescriber = models.ForeignKey(Prescriber, on_delete=CASCADE)
    drug = models.ForeignKey(Drug, on_delete=CASCADE)
    drugQuantity = models.IntegerField()
    
    class Meta:
        db_table = 'prescriber_drug'

    def __str__(self):
        return(f"{self.prescriber}: {self.drug} {self.drugQuantity}")

class Prescriber_Credential(models.Model):
    prescriber = models.ForeignKey(Prescriber, on_delete=CASCADE)
    credential = models.ForeignKey(Credential, on_delete=CASCADE)

    class Meta:
        db_table = "prescriber_credential"

    def __str__(self):
        return(f"{self.prescriber} {self.credential}")







    

    
