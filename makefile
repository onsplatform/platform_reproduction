debug: export FLASK_ENV=development
debug:
	@flask run --port 8092

run:
	@gunicorn wsgi:reproduction_api --bind 0.0.0.0:8092 --log-level debug --log-file - --timeout 30000