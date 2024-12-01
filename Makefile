
compile_base:
	uv pip compile ./requirements/base.in -o ./requirements/base.txt

compile_local:
	uv pip compile ./requirements/local.in -o ./requirements/local.txt

compile_reqs: compile_base compile_local

install_base:
	pip install uv
	uv pip install -r ./requirements/base.txt

install_local:
	pip install uv
	uv pip install -r ./requirements/local.txt


create_superuser:
	@export DJANGO_SUPERUSER_USERNAME=admin && \
	export DJANGO_SUPERUSER_EMAIL=admin@example.com && \
	export DJANGO_SUPERUSER_PASSWORD=admin && \
	python manage.py createsuperuser --noinput

run:
	python manage.py runserver

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

shell_plus:
	python manage.py shell_plus

download_fixtures:
	mkdir -p "party/fixtures"
	wget -P ./party/fixtures --no-clobber https://raw.githubusercontent.com/testdrivenio/django-party/refs/heads/main/party/fixtures/initial_gifts.json
	wget -P ./party/fixtures --no-clobber https://raw.githubusercontent.com/testdrivenio/django-party/refs/heads/main/party/fixtures/initial_guests.json
	wget -P ./party/fixtures --no-clobber https://raw.githubusercontent.com/testdrivenio/django-party/refs/heads/main/party/fixtures/initial_parties.json

load_fixtures:
	python manage.py loaddata initial_parties.json
	python manage.py loaddata initial_gifts.json
	python manage.py loaddata initial_guests.json

test:
	python -m pytest -v

black:
	black .

ruff:
	ruff check

isort:
	isort .

lint: black isort ruff

precommit: lint test