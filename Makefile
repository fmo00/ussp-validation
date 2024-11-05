.PHONY: setup 
setup:
	python3 -m venv .venv
	. .venv/bin/activate
	python3 -m pip install --upgrade pip setuptools wheel
	pip install -r requirements.in

.PHONY: run 
run:
	pytest ./tests/api/test.py

.PHONY: format 
format:
	python3 -m black ./tests/api/

.PHONY: clean 
clean:
	deactivate
	rm -f .venv