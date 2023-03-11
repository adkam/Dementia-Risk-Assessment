# Dementia Risk Assessment (Server-Side)

## Setup

1. Install Python3 and Pip
   - Run command `python --version`
     - If python is not installed, follow instructions here: https://www.python.org/downloads/windows/
   - Run command `pip --version`
     - If pip is not installed, follow instructions here: https://pip.pypa.io/en/stable/installing/
2. Run `pip install Flask`
3. Run `pip install pipenv`
4. Run `pipenv shell`
5. Run `pipenv install flask`
6. Run `./bootstrap.sh`
7. You should see the server running in the tab now:
   ```(backend) ➜  backend git:(main) ✗ ./bootstrap.sh
   * Serving Flask app './src/main.py'
   * Debug mode: off
   WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
   * Running on all addresses (0.0.0.0)
   * Running on http://127.0.0.1:5000
   * Running on http://192.168.40.56:5000
   ```
8. Press Control+C to stop the server and type `exit` to deactivate the shell
