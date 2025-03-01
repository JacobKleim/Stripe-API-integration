# Stripe API integration

Django project with Stripe api integration with the ability to pay for purchases. You can get tokens for Stripe api on the website [Stripe](https://docs.stripe.com/)


## Admin:
  http://82.148.29.108/admin
  user:
   ```
   admin
   ```
  
  password:
   ```
   admin
   ```

  The application runs on a server in docker containers. Static is distributed using Nginx.

  Testing of the purchase of item:
  ``` 
  http://82.148.29.108/item/1/
  ```
  Testing the purchase of items in an order:
  ```
  http://82.148.29.108/order_items/1/
  ```


## Download
 Clone this repository:
   ```
   git clone git@github.com:JacobKleim/Stripe-API-integration.git
   
   ```

## Env
   ### Create .env file in the base directory:
   ```
   STRIPE_TEST_PUBLIC_KEY=your stripe public key
   STRIPE_TEST_SECRET_KEY=your stripe secret key
   SECRET_KEY=your_django_secret_key
   ALLOWED_HOSTS=hosts addreses
   DEBUG=True or False
   POSTGRES_USER=postgres_user
   POSTGRES_PASSWORD=postgres_password
   POSTGRES_DB=postgres_db
   POSTGRES_HOST=db
   ```
## Run
   ```
   docker compose build
   ```
   ```
   docker compose up
   ```
   ```
   docker compose run --rm django ./manage.py makemigrations
   ```
   ```
   docker compose run --rm django ./manage.py migrate
   ```
   ```
   docker compose run --rm django ./manage.py createsuperuser
   ```
