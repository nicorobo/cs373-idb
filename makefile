IDB1.log:
	git log > IDB1.log

models.html: models.py
	pydoc3 -w models

# This will be implemented in phase II.
test:
	python3 app/tests.py
