# Django Oscar payments

## Description
Project to test django oscar integration with payment gateway.

## Running the project.

Clone this repository and execute the common django commands.  
Create a new python enviroment and install the requirements.    
For testing the db.sqlite3 database and other files are included.
```
source credentials.sh
python manage.py runserver
```

If you want to create new database run:
```
source credentials.sh
python manage.py migreate
python manage.py oscar_populate_countries
python manage.py runserver
```

* There is a default superuser with credentials: admin@gmail.com, pass Django2021, or create a new one.
* go to **/dashboard** and access with superuser credentials.
* Check if exists or create a category, product_type, product and a partner to be able to make a checkout process.
* Add a product the basket and proceed to checkout.
* Follow the process of Stripe payment button and continue.

## Notes
* It is possible to make a payment using a stripe fake card 4242424242... with any future date and any number data for the 4 number code.
* Change the keys on credentials.sh if necessary for other account tests.
* The main files related to **Oscar checkout** process and stripe are located in **'apps/checkout'**
