# Portal de Notícias Django

## Configuração

1. Instalar dependências:
`ash
pip install -r requirements.txt
`

2. Configurar chave da API:
- Obtenha uma chave gratuita em: https://newsapi.org
- Edite myproject/settings.py e substitua your_newsapi_key_here pela sua chave

3. Executar migrações:
`ash
python manage.py makemigrations news
python manage.py migrate
`

4. Executar servidor:
`ash
python manage.py runserver
`

## Funcionalidades

- ✅ Consome API de notícias do Brasil
- ✅ Interface responsiva e moderna  
- ✅ Sistema de cache no banco de dados
- ✅ Atualização manual de notícias
- ✅ Links diretos para as fontes

## Tecnologias

- Django 4.2.7
- SQLite
- NewsAPI
- HTML/CSS responsivo
