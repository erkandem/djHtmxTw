
compile_base:
	uv pip compile ./requirements/base.in -o ./requirements/base.txt

compile_local:
	uv pip compile ./requirements/local.in -o ./requirements/local.txt

install_base:
	uv pip install -r ./requirements/base.txt

install_local:
	uv pip install -r ./requirements/local.txt


create_superuser:
	@export DJANGO_SUPERUSER_USERNAME=admin && \
	export DJANGO_SUPERUSER_EMAIL=admin@example.com && \
	export DJANGO_SUPERUSER_PASSWORD=adminpass && \
	python manage.py createsuperuser --noinput

run:
	python manage.py runserver

shell_plus:
	python manage.py shell_plus
