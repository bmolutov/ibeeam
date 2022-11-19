CURRENT_DIRECTORY := $(shell pwd)

help:
	@echo "********************"
	@echo "Makefile Help"
	@echo "********************"
	@echo "MOST COMMONLY USED:"
	@echo "make status -> see running containers state"
	@echo "make start -> start services"
	@echo "make stop -> stop services"
	@echo "make restart -> restart services"
	@echo "********************"
	@echo "EXTRAS:"
	@echo "make web-cli -> run cli for django application container"
	@echo "make db-cli -> run cli for postgres database container"
	@echo "make logs -> run for seeing logs"
	@echo "********************"

start:
	@docker-compose up -d

stop:
	@docker-compose down

status:
	@docker-compose ps

restart: stop start

web-cli:
	@docker exec -it django bash

db-cli:
	@docker exec -it postgres bash

logs:
	@docker-compose logs -f

.PHONY: start stop status restart web-cli db-cli logs
