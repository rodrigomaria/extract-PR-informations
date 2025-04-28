# GitHub PR Information Extractor

## English

### Overview
This tool extracts information from GitHub Pull Request HTML pages, specifically the titles of timeline items and their associated authors. It's designed to help teams easily compile release notes or changelog entries from PR activity.

### Features
- Extracts PR timeline items with their titles and authors
- Automatically adds @ symbol before author names
- Outputs results to a formatted text file
- Runs in an isolated Docker container to avoid dependency issues
- Includes a Makefile for easy execution

### Requirements
- Docker
- Docker Compose

### Installation
1. Clone this repository
2. Place your GitHub PR HTML file in the `page_for_scrape` directory
3. Build the Docker image with `make build`

### Usage
Run the scraper with:
```bash
make run
```

Or build and run in one step:
```bash
make all
```

The results will be saved to `issues_to_publish.txt` in the project root.

### Project Structure
- `extract_titles.py`: Main Python script that extracts information from HTML
- `Dockerfile`: Defines the Docker container for the scraper
- `docker-compose.yml`: Docker Compose configuration
- `requirements.txt`: Python dependencies
- `Makefile`: Simplifies common commands
- `.gitignore`: Excludes unnecessary files from version control
- `page_for_scrape/`: Directory where HTML files should be placed (contents are git-ignored)

---

## Português

### Visão Geral
Esta ferramenta extrai informações de páginas HTML de Pull Requests do GitHub, especificamente os títulos dos itens da timeline e seus respectivos autores. Foi projetada para ajudar equipes a compilar facilmente notas de lançamento ou entradas de changelog a partir da atividade de PRs.

### Funcionalidades
- Extrai itens da timeline de PR com seus títulos e autores
- Adiciona automaticamente o símbolo @ antes dos nomes dos autores
- Exporta resultados para um arquivo de texto formatado
- Executa em um container Docker isolado para evitar problemas de dependência
- Inclui um Makefile para execução simplificada

### Requisitos
- Docker
- Docker Compose

### Instalação
1. Clone este repositório
2. Coloque seu arquivo HTML de PR do GitHub no diretório `page_for_scrape`
3. Construa a imagem Docker com `make build`

### Uso
Execute o scraper com:
```bash
make run
```

Ou construa e execute em uma única etapa:
```bash
make all
```

Os resultados serão salvos em `issues_to_publish.txt` na raiz do projeto.

### Estrutura do Projeto
- `extract_titles.py`: Script Python principal que extrai informações do HTML
- `Dockerfile`: Define o container Docker para o scraper
- `docker-compose.yml`: Configuração do Docker Compose
- `requirements.txt`: Dependências Python
- `Makefile`: Simplifica comandos comuns
- `.gitignore`: Exclui arquivos desnecessários do controle de versão
- `page_for_scrape/`: Diretório onde os arquivos HTML devem ser colocados (conteúdo ignorado pelo git)