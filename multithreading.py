import requests
import time
import csv
import random
import concurrent.futures
from bs4 import BeautifulSoup

# Cabeçalhos globais a serem usados para as requisições
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}

# Número máximo de threads a serem usadas
MAX_THREADS = 12

def extract_movie_details(movie_link):
    """
    Extrai detalhes de um filme a partir de um link fornecido.
    """
    # Pausa aleatória para evitar sobrecarregar o servidor
    time.sleep(random.uniform(0, 0.2))

    # Faz a requisição HTTP para o link do filme
    response = requests.get(movie_link, headers=headers)
    movie_soup = BeautifulSoup(response.content, 'html.parser')

    if movie_soup is not None:
        title = None
        date = None

        # Encontrando a seção específica da página do filme
        page_section = movie_soup.find('section', attrs={'class': 'ipc-page-section'})

        if page_section is not None:
            # Encontrando todas as divs dentro da seção
            divs = page_section.find_all('div', recursive=False)

            if len(divs) > 1:
                target_div = divs[1]

                # Encontrando o título do filme
                title_tag = target_div.find('h1')
                if title_tag:
                    title = title_tag.find('span').get_text()

                # Encontrando a data de lançamento
                date_tag = target_div.find('a', href=lambda href: href and 'releaseinfo' in href)
                if date_tag:
                    date = date_tag.get_text().strip()

                # Encontrando a classificação do filme
                rating_tag = movie_soup.find('div', attrs={'data-testid': 'hero-rating-bar__aggregate-rating__score'})
                rating = rating_tag.get_text() if rating_tag else None

                # Encontrando a sinopse do filme
                plot_tag = movie_soup.find('span', attrs={'data-testid': 'plot-xs_to_m'})
                plot_text = plot_tag.get_text().strip() if plot_tag else None

                # Escrevendo os detalhes do filme no arquivo CSV
                with open('movies.csv', mode='a', newline='', encoding='utf-8') as file:
                    movie_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    if all([title, date, rating, plot_text]):
                        print(title, date, rating, plot_text)
                        movie_writer.writerow([title, date, rating, plot_text])

def extract_movies(soup):
    """
    Extrai links de filmes a partir da página principal e inicia a extração de detalhes usando multithreading.
    """
    # Encontrando a tabela de filmes na página principal
    movies_table = soup.find('div', attrs={'data-testid': 'chart-layout-main-column'}).find('ul')
    movies_table_rows = movies_table.find_all('li')

    # Construindo a lista de links dos filmes
    movie_links = ['https://imdb.com' + movie.find('a')['href'] for movie in movies_table_rows]

    # Determinando o número de threads a serem usadas
    threads = min(MAX_THREADS, len(movie_links))

    # Usando ThreadPoolExecutor para processar os links dos filmes em paralelo
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(extract_movie_details, movie_links)

def main():
    """
    Função principal que inicia o processo de extração de filmes populares do IMDB.
    """
    start_time = time.time()

    # URL dos filmes mais populares do IMDB
    popular_movies_url = 'https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm'

    # Fazendo a requisição HTTP para a página principal
    response = requests.get(popular_movies_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Função principal para extrair os 100 filmes mais populares do IMDB
    extract_movies(soup)

    end_time = time.time()
    print('Total time taken: ', end_time - start_time)

if __name__ == '__main__':
    main()
