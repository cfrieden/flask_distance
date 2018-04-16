.EXPORT_ALL_VARIABLES:

FLASK_APP = distance_app.py

.PHONY: run
run:
	flask run
