.PHONY: build up down restart extract clean sh help

# Default target
.DEFAULT_GOAL := help

# Variables
DOCKER_COMPOSE = docker-compose

# Help message
help:
	@echo "PR Information Scraper"
	@echo "---------------------"
	@echo "Available commands:"
	@echo "  make help     - Show this help message"
	@echo "  make build    - Build the Docker image for the scraper"
	@echo "  make up       - Start the scraper container in background"
	@echo "  make down     - Stop and remove the scraper container"
	@echo "  make restart  - Restart the scraper container"
	@echo "  make extract  - Run the scraper to extract PR information"
	@echo "  make clean    - Remove content from page_for_scrape folder and clear issues_to_publish.txt"
	@echo "  make sh       - Open a shell inside the running container"

# Build the Docker image
build:
	$(DOCKER_COMPOSE) build

# Start container in background
up:
	$(DOCKER_COMPOSE) up -d

# Stop and remove container
down:
	$(DOCKER_COMPOSE) down

# Restart the container
restart:
	@make down
	@make up

# Run the scraper
extract:
	$(DOCKER_COMPOSE) exec scraper python extract_titles.py

# Clean the project
clean:
	@echo "Cleaning page_for_scrape folder and issues_to_publish.txt..."
	@rm -rf page_for_scrape/* 
	@echo "" > issues_to_publish.txt
	@echo "Clean completed successfully!"

# Shell inside container
sh:
	$(DOCKER_COMPOSE) exec scraper sh

# All-in-one command
all: build up extract down
