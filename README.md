# Ecommerce

This is a brief description of online shop website using django.

## Getting Started

Steps to run in local, do you requiere python 3.x and docker installed:

1. Clone the repository:

   ```bash
   git@github.com:JoseJulianMosqueraFuli/ecommerce.git
   ```

2. Navigate into the repository:

   ```bash
   cd ecommerce
   ```

3. Create a new virtual environment

   ```bash
   python -m venv venv/ecommerce
   ```

4. Activate the virtual environment:

   ```bash
   source venv/ecommerce/bin/activate
   ```

5. Run the project:

   ```bash
   pip3 install -r requirements.txt
   ```

6. Run the project:

   ```bash
   python manage.py runserver
   ```

7. Run for rabbitmq container:

   ```bash
   docker pull rabbitmq:3-management
   docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
   ```

8. Run for stripe container:

   ```bash
   docker pull stripe/stripe-cli:v1.17.2
   docker run --rm -it stripe/stripe-cli listen --forward-to localhost:80000/payment/webhook/    --api-keys sk_test..
   ```

   **Note**: More information about stripe docker [here](https://stripe.com/docs/cli/docker)

## License

This project is licensed under the [MIT License](LICENSE).

## Author

Build it by [Jose Julian Mosquera Fuli](https://github.com/JoseJulianMosqueraFuli).
