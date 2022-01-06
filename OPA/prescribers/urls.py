from django.urls import path
from .views import addCredentialsPageView, addPrescriberPageView, deletePrescriberPageView, editPrescriberPageView, prescribersPageView, searchPrescribersPageView, singlePrescriberPageView, editOrRemovePrescribersPageView, editDrugQuantitiesPageView

urlpatterns = [
    path("prescribers/", prescribersPageView, name="prescribers"),
    path("searchPrescribers/", searchPrescribersPageView, name="searchPrescribers"),
    path("singlePrescriber/<id>/", singlePrescriberPageView, name="singlePrescriber"),
    path("addPrescriber", addPrescriberPageView, name="addPrescriber"),
    path("editOrRemovePrescribers/", editOrRemovePrescribersPageView, name="editOrRemovePrescribers"),
    path("deletePrescriber/<id>/", deletePrescriberPageView, name="deletePrescriber"),
    path("editPrescriber/<id>/", editPrescriberPageView, name="editPrescriber"),
    path("editDrugQuantities/<prescriberId>/<drugId>", editDrugQuantitiesPageView, name="editDrugQuantities"),
    path("addCredentials/<pId>/", addCredentialsPageView, name="addCredentials")
]