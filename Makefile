.PHONY: setup 
setup:
	python3 -m venv .venv
	.venv/bin/pip install --upgrade pip setuptools wheel pip-tools
	.venv/bin/pip-compile --generate-hashes --output-file=requirements.txt requirements.in 
	.venv/bin/pip install -r requirements.txt

.PHONY: run 
run:
	pytest ./tests/api/test.py

.PHONY: format 
format:
	python3 -m black ./tests/api/

.PHONY: clean 
clean:
	rm -f .venv
	rm -f .pytest_cache