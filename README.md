### VENV - Ambiente Virtual do Python

Ajuda a manter as dependências do projeto separadas das dependências globais do sistema.

###### Criar

``` bash
python -m venv venv
```

###### Ativar


``` bash
venv\Scripts\Activate
```

**(venv)** indica que está ativado:

```bash
(venv) PS C:\
```

### INSTALAÇÃO DE BIBLIOTECAS

###### DJANGO


``` bash
pip install django  
```

###### PILLOW
Usado para imagens no projeto.

``` bash
pip install pillow
```

### CRIANDO PROJETO

O gerenciador do Django cria o projeto. A pasta **core** é criada e o arquivo **manage.py**.

``` bash
django-admin startproject core .
```
**.** indica que será criado na mesma pasta

### CRIANDO apps

``` bash
python manage.py startapp evento
```
- cria app com nome **evento**.
-  **'evento'** é adicionado no bloco **INSTALLED APPS** do arquivo **settings** na pasta **core** para ser reconhecido coomo app.

### Configuração de URL

#### Arquivo core/urls.py

Criação da url  **evento**.

``` bash
from django.urls import path, include

urlpatterns = [
    path('evento/', include('evento.urls')),
]
```
- **urlpatterns** lista onde as urls são mencionadas.

- **evento.urls** faz referência ao arquivo **urls** na pasta **evento**, onde as suburls são listadas. Criar arquivo caso não exista.

*O processo se repete para cada url criada na pasta core.*

### Configuração Templates

Arquivo **settings** pasta **core**

```bash
'DIRS': [BASE_DIR / 'templates'],
```

Pasta **templates** com arquivos específicos na raíz do projeto 

```bash
'APP_DIRS': True,
```

Pasta **templates** nas pastas dos apps.

### Configuração Static

Arquivo **settings** pasta **core**

```bash
import os
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'templates/static'),)
STATIC_ROOT = os.path.join('static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

- Arquivos Estáticos adicionados por devs
- Arquivos de Mídia adicionados por usuários

### MIGRAÇÕES

``` bash
python manage.py makemigrations
```
- Informa ao Django como as migrações devem ser executadas conforme arquivo **models.py** 

- Arquivo **0001_initial.py** criado na pasta **migrations**.

##### Salvar no Banco de Dados

``` bash
python manage.py migrate
```

### RODANDO PROJETO

``` bash
python manage.py runserver
```

**Ctrl + C** interrompe o servidor.

