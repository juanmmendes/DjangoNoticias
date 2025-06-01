# 📰 Portal de Notícias Django

> Um portal moderno de notícias do Brasil utilizando Django e NewsAPI

<p align="center">
  <img src="https://img.shields.io/badge/Django-4.2.7-green?style=for-the-badge&logo=django" alt="Django">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/SQLite-Database-orange?style=for-the-badge&logo=sqlite" alt="SQLite">
  <img src="https://img.shields.io/badge/NewsAPI-Integration-red?style=for-the-badge" alt="NewsAPI">
</p>

## 🚀 Funcionalidades

- ✅ **Notícias em Tempo Real** - Consome API de notícias do Brasil
- ✅ **Design Responsivo** - Interface moderna e adaptável
- ✅ **Sistema de Cache** - Armazenamento inteligente no banco de dados
- ✅ **Atualização Manual** - Controle total sobre quando buscar novas notícias
- ✅ **Links Diretos** - Acesso direto às fontes originais das notícias

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Descrição |
|------------|--------|-----------|
| **Django** | 4.2.7 | Framework web Python |
| **SQLite** | - | Banco de dados embutido |
| **NewsAPI** | - | API de notícias |
| **HTML/CSS** | - | Interface responsiva |

## ⚙️ Configuração e Instalação

### 1. 📋 Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Conta gratuita no [NewsAPI](https://newsapi.org)

### 2. 🔧 Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/django-noticias.git
cd django-noticias

# Instale as dependências
pip install -r requirements.txt
```

### 3. 🔑 Configuração da API

1. Obtenha sua chave gratuita em: **https://newsapi.org**
2. Crie um arquivo `settings_local.py` na pasta `myproject/`
3. Adicione sua chave da API:

```python
# myproject/settings_local.py
NEWS_API_KEY = 'sua_chave_real_da_newsapi_aqui'
```

> ⚠️ **Importante**: Nunca commite sua chave da API! O arquivo `settings_local.py` está no `.gitignore`

### 4. 🗄️ Configuração do Banco de Dados

```bash
# Criar migrações
python manage.py makemigrations news

# Aplicar migrações
python manage.py migrate
```

### 5. 🚀 Executar o Servidor

```bash
python manage.py runserver
```

Acesse: **http://localhost:8000**

## 📁 Estrutura do Projeto

```
django-noticias/
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── settings_local.py  # Suas configurações locais
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── news/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── requirements.txt
├── manage.py
├── .gitignore
└── README.md
```

## 🎯 Como Usar

1. **Acesse o portal** em `http://localhost:8000`
2. **Visualize as notícias** na página inicial
3. **Clique em "Atualizar Notícias"** para buscar conteúdo mais recente
4. **Clique nos títulos** para acessar as fontes originais

## 🔧 Personalização

### Alterar País das Notícias

No arquivo `news/views.py`, modifique o parâmetro `country`:

```python
# Para notícias dos EUA
url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'

# Para notícias do Reino Unido
url = f'https://newsapi.org/v2/top-headlines?country=gb&apiKey={api_key}'
```

### Adicionar Categorias

Você pode filtrar por categorias específicas:

```python
url = f'https://newsapi.org/v2/top-headlines?country=br&category=technology&apiKey={api_key}'
```

Categorias disponíveis: `business`, `entertainment`, `general`, `health`, `science`, `sports`, `technology`

## 🐛 Resolução de Problemas

### Erro de API Key
```
Erro: API key inválida
```
**Solução**: Verifique se sua chave da NewsAPI está correta no arquivo `settings_local.py`

### Erro de Migração
```
Erro: No such table
```
**Solução**: Execute as migrações novamente
```bash
python manage.py makemigrations news
python manage.py migrate
```

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request


---

<p align="center">
  Feito com ❤️ usando Django
</p>
