from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets, generics

from django.contrib.auth.models import User

from criador_navedex.models import Naver, Projeto
from criador_navedex.api.serializers import NaverSerializer, ProjetoSerializer
from criador_navedex.api.permissions import IsResponsibleForNaverOrReadOnly, IsResponsibleForProjectOrReadOnly
from criador_navedex.api.serializers import UserSerializer


class RegisterView(GenericAPIView):
    """
    View responsável por cadastrar novos usuários
    """
    permission_classes=[AllowAny] # Desabilitando a autenticação JWT
    serializer_class=UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NaverListCreate(generics.ListCreateAPIView):
    """
    View para requisições GET e POST de Naver,
    ou seja, listagem e criação.
    """

    serializer_class=NaverSerializer
    permission_classes=[IsAuthenticated] # Autenticação configurada para aceitar apenas JWT incluido no Header do Request

    # Filtrar por nome, tempo de empresa e cargo
    def get_queryset(self):
        queryset=Naver.objects.filter(user=self.request.user) # Filtrando a queryset para exibir somente os navers 
                                                              # vinculados ao usuário que fez a requisição http

        name = self.request.query_params.get('name', None)
        admission_date = self.request.query_params.get('admission_date', None)
        job_role = self.request.query_params.get('job_role', None)

        if name is not None:
            queryset=queryset.filter(name=name)

        if admission_date is not None:
            queryset=queryset.filter(admission_date=admission_date)

        if job_role is not None:
            queryset=queryset.filter(job_role=job_role)

        return queryset


class NaverUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    """
    View para requisições GET, UPDATE e DELETE de Naver,
    ou seja, listagem de um único registro, atualização
    de um registro e remoção do banco de um registro.
    """

    serializer_class=NaverSerializer
    permission_classes=[IsAuthenticated, IsResponsibleForNaverOrReadOnly]

    def get_queryset(self):
        queryset=Naver.objects.filter(user=self.request.user)
        return queryset

class ProjetoListCreate(generics.ListCreateAPIView):
    """
    View para requisições GET e POST de Projeto,
    ou seja, listagem e criação.
    """

    serializer_class=ProjetoSerializer
    permission_classes=[IsAuthenticated] # Autenticação configurada para aceitar apenas JWT incluido no Header do Request

    # Filtrar por nome
    def get_queryset(self):
        queryset=Projeto.objects.filter(naver__user=self.request.user)
        
        name = self.request.query_params.get('name', None)

        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset

class ProjetoUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    """
    View para requisições GET, UPDATE e DELETE de Projeto,
    ou seja, listagem de um único registro, atualização
    de um registro e remoção do banco de um registro.
    """

    serializer_class=ProjetoSerializer
    permission_classes=[IsAuthenticated, IsResponsibleForProjectOrReadOnly]

    def get_queryset(self):
        queryset=Projeto.objects.filter(naver__user=self.request.user)
        return queryset

