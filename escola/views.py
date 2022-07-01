from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculasSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosSerializer


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


class ListaMatriculasAluno(generics.ListAPIView):
    """Listando As Matriculas Do Aluno"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer


class ListaAlunosMatriculados(generics.ListAPIView):
    """Listando Alunos Dos Curso"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer
