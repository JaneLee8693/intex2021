from django.shortcuts import render
from django.http import HttpResponse
from .models import Credential, Drug, Prescriber, Prescriber_Credential, Prescriber_Drug, Specialty, State
import math

def prescribersPageView(request):
    return render(request, 'prescribers/prescribers.html')

def searchPrescribersPageView(request):

    if request.method == "POST":
        pFirstName = request.POST['pFirstName']
        pLastName = request.POST['pLastName']
        pSpecialty = request.POST['pSpecialty']
        pCredential = request.POST.get('pCredential', 'MD')
        pGender = request.POST['pGender']
        pState = request.POST['pState']
        if pGender == "Any":
            if (request.POST.get('pCredential', 'MD') != ''):
                prescribers = Prescriber.objects.filter(firstName__icontains=pFirstName
                    ).filter(lastName__icontains=pLastName
                    ).filter(specialtyId__specialtyName__icontains=pSpecialty
                    ).filter(prescriber_credential_field__credentialName__icontains=pCredential
                    ).filter(state__stateName__icontains=pState)
            else: 
                prescribers = Prescriber.objects.filter(firstName__icontains=pFirstName
                    ).filter(lastName__icontains=pLastName
                    ).filter(specialtyId__specialtyName__icontains=pSpecialty
                    ).filter(state__stateName__icontains=pState)
        else: 
            if (request.POST.get('pCredential', 'MD') != ''):
                prescribers = Prescriber.objects.filter(firstName__icontains=pFirstName
                    ).filter(lastName__icontains=pLastName
                    ).filter(specialtyId__specialtyName__icontains=pSpecialty
                    ).filter(prescriber_credential_field__credentialName__icontains=pCredential
                    ).filter(state__stateName__icontains=pState
                    ).filter(gender__exact=pGender)
            else: 
                prescribers = Prescriber.objects.filter(firstName__icontains=pFirstName
                    ).filter(lastName__icontains=pLastName
                    ).filter(specialtyId__specialtyName__icontains=pSpecialty
                    ).filter(state__stateName__icontains=pState
                    ).filter(gender__exact=pGender)


        context = {
            "prescribers": prescribers,
        }
    else:
        prescribers = Prescriber.objects.all()
        context = {
            "prescribers": prescribers,
        }
        
    return render(request, "prescribers/searchPrescribers.html", context)

def singlePrescriberPageView(request, id):
    
    prescriber = Prescriber.objects.get(id = id)
    credentials = prescriber.prescriber_credential_field.all()
    availCredentials = Credential.objects.exclude(id__in=credentials)
    drugs = []
    for x in prescriber.prescriber_drug_set.all():
        drugs.append({"drugName": x.drug.drugName, "drugId":x.drug.id, "doctorQuantity": x.drugQuantity, "drugCount": 0, "drugSum": 0, "average": 0})
    
    for a in drugs:
        drug = Prescriber_Drug.objects.filter(drug__exact=a['drugId'])
        a["drugCount"] = len(drug)
        for b in drug:
            a["drugSum"] += b.drugQuantity
        a['average'] = math.trunc(a['drugSum'] / a['drugCount'])

    context = {
        "prescriber": prescriber,
        "drugs": drugs,
        "credentials": availCredentials
    }

    return render(request, 'prescribers/singlePrescriber.html', context)

def addPrescriberPageView(request):

    if request.method == "POST":
        prescriber = Prescriber()
        prescriber.firstName = request.POST['pFirstName']
        prescriber.lastName = request.POST['pLastName']
        prescriber.npi = request.POST['pNpi']
        prescriber.gender = request.POST['pGender']
        prescriber.state = State.objects.get(id=request.POST['pState']) 
        prescriber.specialtyId = Specialty.objects.get(id=request.POST['pSpecialty'])

        if request.POST['pOpioid'] == 'Yes':
            prescriber.isOpiodPrescriber = True
        else:
            prescriber.isOpiodPrescriber = False
        prescriber.totalPrescriptions = request.POST['pTotalPrescriptions']

        prescriber.save()


        return searchPrescribersPageView(request)


    credentials = Credential.objects.all()
    states = State.objects.all()
    specialties = Specialty.objects.all()
  

    context = {
        "credentials": credentials,
        "states": states,
        "specialties": specialties,
    }
    
    return render(request, 'prescribers/addPrescriber.html', context)

def editOrRemovePrescribersPageView(request):

    if request.method == "POST":
        pFirstName = request.POST['pFirstName']
        pLastName = request.POST['pLastName']
        pSpecialty = request.POST['pSpecialty']
        pCredential = request.POST.get('pCredential', 'MD')
        pGender = request.POST['pGender']
        pState = request.POST['pState']
        if pGender == "Any":
            if (request.POST.get('pCredential', 'MD') != ''):
                prescribers = Prescriber.objects.filter(firstName__icontains=pFirstName
                    ).filter(lastName__icontains=pLastName
                    ).filter(specialtyId__specialtyName__icontains=pSpecialty
                    ).filter(prescriber_credential_field__credentialName__icontains=pCredential
                    ).filter(state__stateName__icontains=pState)
            else: 
                prescribers = Prescriber.objects.filter(firstName__icontains=pFirstName
                    ).filter(lastName__icontains=pLastName
                    ).filter(specialtyId__specialtyName__icontains=pSpecialty
                    ).filter(state__stateName__icontains=pState)
        else: 
            if (request.POST.get('pCredential', 'MD') != ''):
                prescribers = Prescriber.objects.filter(firstName__icontains=pFirstName
                    ).filter(lastName__icontains=pLastName
                    ).filter(specialtyId__specialtyName__icontains=pSpecialty
                    ).filter(prescriber_credential_field__credentialName__icontains=pCredential
                    ).filter(state__stateName__icontains=pState
                    ).filter(gender__exact=pGender)
            else: 
                prescribers = Prescriber.objects.filter(firstName__icontains=pFirstName
                    ).filter(lastName__icontains=pLastName
                    ).filter(specialtyId__specialtyName__icontains=pSpecialty
                    ).filter(state__stateName__icontains=pState
                    ).filter(gender__exact=pGender)


        context = {
            "prescribers": prescribers,
        }

        return render(request, "prescribers/editOrRemovePrescribers.html", context)
    else:
        prescribers = Prescriber.objects.all()
        context = {
            "prescribers": prescribers,
        }
        
        return render(request, "prescribers/editOrRemovePrescribers.html", context)

def deletePrescriberPageView(request, id):
    data = Prescriber.objects.get(id = id )

    data.delete()

    return editOrRemovePrescribersPageView(request)

def editPrescriberPageView(request, id):
    if request.method == "POST":
        prescriber = Prescriber.objects.get(id=id)

        prescriber.firstName = request.POST['pFirstName']
        prescriber.lastName = request.POST['pLastName']
        prescriber.npi = request.POST['pNpi']
        prescriber.gender = request.POST['pGender']
        prescriber.state = State.objects.get(id=request.POST['pState']) 
        prescriber.specialtyId = Specialty.objects.get(id=request.POST['pSpecialty'])

        if request.POST['pOpioid'] == 'Yes':
            prescriber.isOpiodPrescriber = True
        else:
            prescriber.isOpiodPrescriber = False
        prescriber.totalPrescriptions = request.POST['pTotalPrescriptions']

        prescriber.save()

        return editOrRemovePrescribersPageView(request)

    else:
        credentials = Credential.objects.all()
        states = State.objects.all()
        specialties = Specialty.objects.all()
        prescriber = Prescriber.objects.get(id=id)
    

        context = {
            "credentials": credentials,
            "states": states,
            "specialties": specialties,
            "prescriber": prescriber
        }
        return render(request, "prescribers/editPrescriber.html", context)


def editDrugQuantitiesPageView(request, prescriberId, drugId):
    if request.method == "POST":
        prescriber = Prescriber.objects.get(id = prescriberId)
        drug = Drug.objects.get(id=drugId)
        prescriber.presciber_drugs_field.remove(drug)

        newPrescriberDrug = Prescriber_Drug(prescriber=prescriber, drug=drug, drugQuantity=request.POST['pDrugQuantity'])
        newPrescriberDrug.id = 100000 + prescriber.id
        newPrescriberDrug.save()

        context = {
            "prescriber": prescriber,
            "drug": drug
        }

        return singlePrescriberPageView(request, prescriber.id)


    else:
        prescriber = Prescriber.objects.get(id = prescriberId)
        drug = Drug.objects.get(id= drugId)
        prescribedDrug = prescriber.prescriber_drug_set.get(drug=drug.id)
    
        context = {
            "prescriber": prescriber,
            "drug": drug,
            "prescribedDrug": prescribedDrug
        }

        return render(request, 'prescribers/editDrugQuantities.html', context)

def addCredentialsPageView(request, pId):
    if request.method == 'POST':
        prescriber = Prescriber.objects.get(id=pId)
        credential = Credential.objects.get(id=request.POST.get('pCredential'))
        newPrescriberCredential = Prescriber_Credential(prescriber=prescriber, credential=credential)
        newPrescriberCredential.save()
        
        return singlePrescriberPageView(request, prescriber.id)