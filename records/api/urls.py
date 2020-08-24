from django.urls import include, path
from rest_framework.routers import DefaultRouter

from records.api import views as rv

router = DefaultRouter()
router.register(r"tasks", rv.TaskViewSet, basename="tasks")
router.register(r"choices", rv.ChoiceViewSet, basename="choices")
router.register(r"incomes", rv.IncomeViewSet, basename="incomes")
router.register(r"expenditures", rv.ExpenditureViewSet, basename="expenditures")
router.register(r"categories", rv.CategoryViewSet, basename="categories")

urlpatterns = [
    path("", include(router.urls)), 

]