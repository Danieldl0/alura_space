from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Nome de Login', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Daniel Oliveira'
            }
        )
    )

    senha = forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha',
            }

        )
    )


class CadastroForms(forms.Form):
    nome_login = forms.CharField(
        label='Nome de Login', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Daniel Oliveira'
            }
        )
    )

    email = forms.CharField(
        label='Email', 
        required=True, 
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: danieloliveira@gmail.com'
            }
        )
    )

    senha_1 = forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha',
            }

        )
    )

    senha_2 = forms.CharField(
        label='Confirme sua senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha novamente',
            }

        )
    )

    def clean_nome_login(self):
        nome = self.cleaned_data.get('nome_login')

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Espaços não são permitidos nesse campo')
            else:
                return nome
    
    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get('senha_1')
        senha_2 = self.cleaned_data.get('senha_2')

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError('As senhas devem ser iguais')
                return senha_2