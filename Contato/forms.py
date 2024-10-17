from django import forms
from Contato.models import Categoria, Contato
from django.contrib.auth.models import User


# maneira dificil de fazer, mas faz pásso a passo, bom aprender
class ContatoForm(forms.Form):
    Nome = forms.CharField(max_length=250)
    Categoria = forms.ModelChoiceField(Categoria.objects.all())
    User = forms.ModelChoiceField(User.objects.all())
    Email = forms.EmailField()
    Telefone = forms.CharField(max_length=20)
    DataNascimento = forms.DateField()
    CEP = forms.CharField()
    Foto = forms.ImageField()

    def save(self):
        Contatos = Contato(Nome=self.cleaned_data['Nome'],
                           Categoria=self.cleaned_data['Categoria'],
                           Email=self.cleaned_data['Email'],
                           Telefone=self.cleaned_data['Telefone'],
                           DataNascimento=self.cleaned_data['DataNascimento'],
                           CEP=self.cleaned_data['CEP'],
                           Foto=self.cleaned_data['Foto'],
                           User=self.cleaned_data['User'],)
        Contatos.save()
        return Contato


class ContatoModelForm(forms.ModelForm):  # maneira facil de fazer
    class Meta:
        model = Contato
        fields = '__all__'

    def clean_CEP(self): # QUANDO RODAR IS VALID EM VIEWS, RODA AO MESMO TEMPO TODOS AS VALIDAÇÕES COM ESSE PREFIXO CLEAN 
        CEP = self.cleaned_data.get('CEP')

        if CEP is not None and len(CEP) < 5:
            self.add_error('CEP', 'O CEP precisa conter pelo menos 5 digitos')
        return CEP
