
## A simple application to order products running across multiple Docker containers

### Getting started

Run in this directory to build and run the app:


### Code
          
          docker-compose up -d --build

The Ejedzenie app will be running at http://localhost:8000
Run this command to migrate db
        
         docker-compose run --rm web python manage.py migrate


Run this command to create superuser


          docker-compose run --rm web python manage.py createsuperuser



***