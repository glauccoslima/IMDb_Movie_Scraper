# IMDb Movie Scraper 🎬

Este projeto é um sistema de scraping de filmes populares do IMDb, onde os dados são extraídos e armazenados em um arquivo CSV. O objetivo é obter informações detalhadas dos filmes, como título, data de lançamento, classificação e sinopse.

## Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Como Executar o Projeto](#como-executar-o-projeto)
- [Estrutura do Projeto](#estrutura-do-projeto)

## Sobre o Projeto

O objetivo deste projeto é coletar informações dos filmes mais populares disponíveis na plataforma IMDb, processá-las e armazená-las em um arquivo CSV para futuras análises ou pesquisas. O sistema faz uso de multithreading para melhorar a eficiência do processo de scraping.

## Funcionalidades

- **Extração de Filmes Populares**: O sistema busca e extrai informações dos filmes mais populares na página do IMDb.
- **Detalhes dos Filmes**: Para cada filme, são extraídos o título, data de lançamento, classificação e sinopse.
- **Armazenamento em CSV**: As informações extraídas são salvas em um arquivo CSV para fácil acesso e manipulação.
- **Multithreading**: Utiliza multithreading para otimizar o processo de scraping, fazendo várias requisições simultâneas.

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **BeautifulSoup**: Biblioteca utilizada para o parsing de HTML.
- **Requests**: Biblioteca para fazer as requisições HTTP.
- **CSV**: Para manipulação e armazenamento dos dados extraídos.
- **ThreadPoolExecutor**: Para a execução de tarefas em paralelo.

## Como Executar o Projeto

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/glauccoslima/IMDb_Movie_Scraper.git
   ```

2. **Navegue até o diretório do projeto:**

   ```bash
   cd IMDb_Movie_Scraper
   ```

3. **Crie um ambiente virtual (opcional, mas recomendado):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

4. **Instale as dependências necessárias:**

   ```bash
   pip install requests beautifulsoup4
   ```

5. **Execute o script:**

   ```bash
   python multithreading.py
   ```

6. **Confira o arquivo CSV gerado:**

   O arquivo `movies.csv` será criado no diretório atual, contendo os dados extraídos.

## Estrutura do Projeto

- `multithreading.py`: Script principal que executa o scraping e coordena as operações.
- `movies.csv`: Arquivo gerado contendo os detalhes dos filmes.
