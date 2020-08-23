from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from criador_navedex.models import Naver, Projeto
from criador_navedex.api.permissions import IsResponsibleForNaverOrReadOnly

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer do Model de User, herdado do próprio Django
    """
    password = serializers.CharField(max_length=10, min_length=5, write_only=True)
    email = serializers.EmailField(max_length=100)

    class Meta:
        extra_kwargs={
            'password': {'write_only': True}
        }
        model = User
        fields='__all__'

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'Este e-mail já foi cadastrado!'})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class ProjetoSerializer(serializers.ModelSerializer):
    """
    Serializer do model de Projeto
    """

    class Meta:
        model = Projeto
        fields = '__all__'


class NaverSerializer(serializers.ModelSerializer):
    """
    Serializer do model de Naver
    """

    projetos = ProjetoSerializer(many=True, read_only=True)

    class Meta:
        model = Naver
        exclude=('user',) # Retornando todos os campos do model menos o campo 'user', porque a API retorna somente os Navers vinculados
                          # ao user que fez a requisição, ou seja, esta informação seria redundante
