from django.shortcuts import render
from django.http import HttpResponse
from prescribers.models import Drug, Prescriber_Drug, Prescriber, Credential, State, Specialty
import operator

def indexPageView(request):
    return render(request, 'homepages/index.html')

def drugsPageView(request):
    return render(request, 'drugs/drugs.html')

def learnMorePageView(request):
    return render(request, 'homepages/learnMore.html')

def mlModelsPageView(request):
    return render(request, "homepages/mlModels.html")

def predictorPageView(request):
    credentials = Credential.objects.all()
    states = State.objects.all()
    specialties = Specialty.objects.all()
  

    context = {
        "credentials": credentials,
        "states": states,
        "specialties": specialties,
    }
    
    return render(request, 'homepages/predictor.html', context)

def recommenderPageView(request):
    credentials = Credential.objects.all()
    states = State.objects.all()
    specialties = Specialty.objects.all()
  

    context = {
        "credentials": credentials,
        "states": states,
        "specialties": specialties,
    }
    
    return render(request, 'homepages/recommender.html', context)

def searchDrugsPageView(request):
    if request.method == "POST":
        drugSearchValue = request.POST['drugSearchValue']
        opioid = request.POST['isOpioid']
        if opioid == 'isOpioid':
            data = Drug.objects.filter(drugName__icontains=drugSearchValue).filter(isOpioid=True)
        elif opioid == 'isNotOpioid':
            data = Drug.objects.filter(drugName__icontains=drugSearchValue).filter(isOpioid=False)
        else:
            data = Drug.objects.filter(drugName__icontains=drugSearchValue)
        context = {
            "drugs": data,
            "opioid": opioid
        }
        return render(request, "drugs/searchDrugs.html", context)
    
    else:
        data = Drug.objects.all()
        context = {
            "drugs": data
        }
        return render(request, "drugs/searchDrugs.html", context)

def singleDrugPageView(request, drugName):
    data = Drug.objects.get(drugName = drugName)
    prescribedDrugs = Prescriber_Drug.objects.filter(drug_id = data.id)
    prescribedDrugs = prescribedDrugs.order_by('-drugQuantity')[:10]
    prescribers = Drug.objects.get(drugName = drugName).prescriber_set.all()

    context = {
        "drug": data,
        "prescribedDrugs": prescribedDrugs,
        "prescribers": prescribers
    }

    return render(request, 'drugs/singleDrug.html', context)

def opioidHistoryPageView(request):
    return render(request, 'homepages/opioidHistory.html')

def tableauPageView(request):
    return render(request, 'homepages/tableau.html')

    