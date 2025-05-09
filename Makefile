.PHONY: build run clean help

# Default target
.DEFAULT_GOAL := help

# Variables
DOCKER_COMPOSE = docker-compose

# Help message
help:
	@echo "PR Information Scraper"
	@echo "---------------------"
	@echo "Available commands:"
	@echo "  make build    - Build the Docker image for the scraper"
	@echo "  make run      - Run the scraper to extract PR information"
	@echo "  make clean    - Remove content from page_for_scrape folder and clear issues_to_publish.txt"
	@echo "  make help     - Show this help message"

# Build the Docker image
build:
	$(DOCKER_COMPOSE) build

# Run the scraper
run:
	$(DOCKER_COMPOSE) run --rm scraper

# Clean the project
clean:
	@echo "Cleaning page_for_scrape folder and issues_to_publish.txt..."
	@rm -rf page_for_scrape/* 
	@echo "" > issues_to_publish.txt
	@echo "Clean completed successfully!"

# All-in-one command: build and run
all: build run
