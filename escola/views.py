from rest_framework import viewsets
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculasSerializer


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo Todos Os Alunos"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo Todos Os Cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    """Listando Todas As Matriculas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculasSerializer
