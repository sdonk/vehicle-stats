webserver:
	docker-compose up

build:
	docker-compose build

shell:
	docker-compose run django python manage.py shell

migrate:
	docker-compose run django python manage.py migrate

makemigrations:
	docker-compose run django python manage.py makemigrations

manage:
	docker-compose run django python manage.py $(cmd)

test:
	docker-compose run django pytest --cov=. --capture=no --cov-config=.coveragerc -s -vv $(pytest_args)


.PHONY: webserver, build, shell, migrate, makemigrations, manage, test
