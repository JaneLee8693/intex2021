from django.urls import path
from .views import indexPageView, drugsPageView, learnMorePageView, mlModelsPageView, opioidHistoryPageView, predictorPageView, recommenderPageView, searchDrugsPageView, singleDrugPageView, tableauPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("drugs/", drugsPageView, name="drugs"),
    path("recommender/", recommenderPageView, name="recommender"),
    path("learnMore/", learnMorePageView, name="learnMore"),
    path("searchDrugs/", searchDrugsPageView, name="searchDrugs"),
    path("singleDrug/<drugName>", singleDrugPageView, name="singleDrug" ),
    path("mlModels/", mlModelsPageView, name="mlModels"),
    path("predictor/", predictorPageView, name="predictor"),
    path("opioidHistory/", opioidHistoryPageView, name="opioidHistory"),
    path("tableau/", tableauPageView, name="tableau")
]