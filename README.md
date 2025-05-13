# Okapi interface dummy app
The purpose of this applicaiton is to satisfy interface requirements for apps that you do not need. It responds 200 OK to all GET, POST, PUT, and DELETE requests.

## Usage
Build: `docker build -t mod-dummy:latest .`
Run the app as a docker container: `docker run mod-dummy:latest -p 8000:8000`

In a FOLIO environment, create a module descriptor for the application that provides all the interfaces you want to fake.
