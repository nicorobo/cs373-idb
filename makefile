IDB1.log:
	git log > IDB1.log

models.html: models.py
	pydoc3 -w models
