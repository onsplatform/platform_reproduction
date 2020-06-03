"""
 Web Server Gateway Interface (WSGI) entry point.
 From root, run with:
 gunicorn wsgi:reproduction
"""
import reproduction

reproduction_api = reproduction.create_app()

if __name__ == "__main__":
    reproduction_api.run()
