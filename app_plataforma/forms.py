from django import forms
from app_plataforma.models import Curso, Modulo 

ModuloFormSet = forms.inlineformset_factory(Curso, Modulo, fields=('nome_curso', 'conteudo'), extra=1)
class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome_curso', 'quantidade_modulos', 'nivel', 'descricao', 'total_horas', 'nome_proprietario', 'preco']
        
