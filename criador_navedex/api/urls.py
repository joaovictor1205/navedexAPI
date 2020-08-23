from django.urls import path
from criador_navedex.views import RegisterView
from rest_framework.routers import SimpleRouter

from criador_navedex.views import NaverListCreate, ProjetoListCreate, NaverUpdateDelete, ProjetoUpdateDelete

# router = SimpleRouter()
# router.register('navers', NaverViewSets, basename='navers')
# router.register('projetos', ProjetoViewSets)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),

    path('navers/', NaverListCreate.as_view(), name='navers-list'),
    path('navers/<int:pk>', NaverUpdateDelete.as_view(), name='navers-detail'),

    path('projetos/', ProjetoListCreate.as_view(), name='projetos-list'),
    path('projetos/<int:pk>', ProjetoUpdateDelete.as_view(), name='projetos-detail'),

]
