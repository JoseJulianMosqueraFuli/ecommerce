# Ecommerce

This is a brief description of online shop website using django.

## Getting Started

Steps to run in local:

1. Download the repository
2. Create a new virtual environment

   ```bash
   python -m venv venv/ecommerce
   ```

3. Activate the virtual environment:

   ```bash
   source venv/ecommerce/bin/activate
   ```

4. Run the project:
   ```bash
   python manage.py runserver
   ```
5. Run for rabbitmq container:

   ```bash
   docker pull rabbitmq:3-management
   docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
   ```

## License

This project is licensed under the [MIT License](LICENSE).

## Author

Build it by [Jose Julian Mosquera Fuli](https://github.com/JoseJulianMosqueraFuli).
