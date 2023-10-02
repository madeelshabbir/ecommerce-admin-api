FROM python:3.11.5

WORKDIR '/var/www/ecommerce-admin-api'
RUN apt-get install -y libpq-dev
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./
RUN chmod 755 ./entrypoints/app.sh

ENTRYPOINT ["sh", "./entrypoints/app.sh"]
