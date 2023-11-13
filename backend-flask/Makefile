BIN=env/bin/

.PHONY: clean system-packages python-packages install tests run all

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

system-packages:
	sudo apt install python3-pip -y

python-packages:
	$(BIN)pip install -r requirements.txt

install: system-packages python-packages

tests:
	$(BIN)python microblog.py test

run:
	$(BIN)python microblog.py run 

all: clean install tests run
