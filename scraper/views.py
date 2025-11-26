from django.shortcuts import render
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup
import re

def buscar_wikipedia(request):
    query = request.GET.get('q', '')
    resultados = []
    
    if query:
        try:
            # Limpiar query para URL de Wikipedia
            clean_query = query.strip().replace(' ', '_')
            #url = f"https://en.wikipedia.org/wiki/{clean_query}"
            url = f"https://es.wikipedia.org/wiki/{clean_query}"

            # Headers para parecer navegador real
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            
            # Hacer request
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()  # Lanza error si HTTP no es 200
            
            # Parsear HTML
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extraer título
            titulo = soup.find('h1', {'class': 'firstHeading'})
            titulo_texto = titulo.get_text().strip() if titulo else "Título no encontrado"
            
            # Extraer primer párrafo (contenido principal)
            contenido_div = soup.find('div', {'class': 'mw-parser-output'})
            primer_parrafo = ""
            
            if contenido_div:
                # Buscar el primer párrafo que tenga texto significativo
                for elemento in contenido_div.find_all(['p', 'div'], recursive=False):
                    texto = elemento.get_text().strip()
                    if len(texto) > 100:  # Solo párrafos con contenido real
                        primer_parrafo = texto
                        break
            
            # Limpiar texto (remover referencias [1], [2], etc.)
            primer_parrafo = re.sub(r'\[\d+\]', '', primer_parrafo)
            
            if primer_parrafo:
                resultados.append({
                    'titulo': titulo_texto,
                    'contenido': primer_parrafo[:500] + '...' if len(primer_parrafo) > 500 else primer_parrafo,
                    'url': url,
                    'fuente': 'Wikipedia'
                })
            else:
                resultados.append({
                    'titulo': 'No se encontró contenido',
                    'contenido': f'No se pudo encontrar información sobre "{query}" en Wikipedia.',
                    'url': '#',
                    'fuente': 'Sistema'
                })
                
        except requests.exceptions.RequestException as e:
            resultados.append({
                'titulo': 'Error de conexión',
                'contenido': f'No se pudo conectar a Wikipedia. Error: {str(e)}',
                'url': '#',
                'fuente': 'Error'
            })
        except Exception as e:
            resultados.append({
                'titulo': 'Error inesperado',
                'contenido': f'Ocurrió un error inesperado: {str(e)}',
                'url': '#', 
                'fuente': 'Error'
            })
    
    return render(request, 'scraper/buscar.html', {
        'resultados': resultados,
        'query': query,
        'total_resultados': len(resultados)
    })