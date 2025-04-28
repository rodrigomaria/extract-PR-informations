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
	@echo "  make clean    - Remove Docker containers and images"
	@echo "  make help     - Show this help message"

# Build the Docker image
build:
	$(DOCKER_COMPOSE) build

# Run the scraper
run:
	$(DOCKER_COMPOSE) run --rm scraper

# Clean up Docker resources
clean:
	$(DOCKER_COMPOSE) down
	docker rmi pr-scraper || true

# All-in-one command: build and run
all: build run
