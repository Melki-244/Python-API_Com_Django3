from rest_framework import viewsets
from escola.models import Aluno, Curso
from escola.serializer import AlunoSerializer, CursoSerializer


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo Todos Os Alunos"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo Todos Os Cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
