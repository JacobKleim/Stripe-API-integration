# Stripe API integration

Django project with Stripe api integration with the ability to pay for purchases. You can get tokens for Stripe api on the website [Stripe](https://docs.stripe.com/)


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
