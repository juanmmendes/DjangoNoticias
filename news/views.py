import requests
from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from .models import NewsArticle
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

def fetch_news_from_api():
    '''Busca notícias da API NewsAPI'''
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': 'br',
        'apiKey': settings.NEWS_API_KEY,
        'pageSize': 20
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logger.error(f'Erro ao buscar notícias: {e}')
        return None

def save_articles(articles_data):
    '''Salva artigos no banco de dados'''
    saved_count = 0
    for article in articles_data.get('articles', []):
        if not article.get('title') or not article.get('url'):
            continue
            
        # Verifica se já existe
        if NewsArticle.objects.filter(url=article['url']).exists():
            continue
            
        try:
            published_at = datetime.fromisoformat(
                article['publishedAt'].replace('Z', '+00:00')
            )
            
            NewsArticle.objects.create(
                title=article['title'][:200],
                description=article.get('description', '')[:500],
                url=article['url'],
                published_at=published_at,
                source=article.get('source', {}).get('name', 'Desconhecido')
            )
            saved_count += 1
        except Exception as e:
            logger.error(f'Erro ao salvar artigo: {e}')
            
    return saved_count

def news_list(request):
    '''View principal que exibe as notícias'''
    # Busca notícias da API
    if request.GET.get('refresh') == '1':
        api_data = fetch_news_from_api()
        if api_data:
            saved = save_articles(api_data)
            if saved > 0:
                messages.success(request, f'{saved} novas notícias foram adicionadas!')
            else:
                messages.info(request, 'Nenhuma notícia nova encontrada.')
        else:
            messages.error(request, 'Erro ao buscar notícias da API.')
    
    # Busca notícias do banco
    articles = NewsArticle.objects.all()[:20]
    
    return render(request, 'news/news_list.html', {
        'articles': articles,
        'total_articles': NewsArticle.objects.count()
    })
