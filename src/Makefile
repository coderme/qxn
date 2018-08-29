##
## make file for coderme.com

BIN = ../ENV/bin
PYTHON = $(BIN)/python

run:
	$(PYTHON) manage.py runserver 8000

run2:
	$(PYTHON) -OO server.py -i localhost:8000

watch:
	while true; do $(PYTHON) manage.py collectstatic --noinput; sleep 7; done

install: requirements.txt
	$(PYTHON) $(BIN)/pip install -r requirements.txt

clean:
	-rm -rf db.sqlite3 build
	-find ./ -type f -name '*.pyc' -delete
	-find ./ -type f -name '*.pyo' -delete
lint:
	-find -name '*.py' | xargs flake8 --show-source - | grep "E[0-9]* [a-zA-Z]*Error:"


