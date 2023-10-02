# Ecommerce Admin API

- Ecommerce Admin API can power a web admin dashboard for e-commerce managers. This API should provide detailed insights into sales, revenue, and inventory status, as well as allow new product registration.

## Technology

- python-3.11.5
- pip-23.2.1
- fastapi-0.103.2
- mysql-8.1
- docker-24.0.6

## Development

### 1. Prerequisites

**For Linux**

- Install [Docker Engine](https://docs.docker.com/engine/install) and [Docker Compose](https://docs.docker.com/compose/install/standalone).

**For Mac**

- Install [Docker Desktop](https://docs.docker.com/desktop/install/mac-install/).

### 2. Initial Setup

Clone the project repository

      $ git clone https://<TOKEN>@github.com/madeelshabbir/ecommerce-admin-api.git

Get into the project directory

      $ cd ecommerce-admin-api

Copy `.env.example` to `.env`

      cp .env.example .env

- Update all missing values.

#### For Linux Only

- Update `DB_HOST` with the IP value of `inet ip` of `<BROADCAST,MULTICAST,UP,LOWER_UP>` received from following command

      ip a

### 3. Run the server

- Run following command and verify the server [status](http:localhost:8000/api/status)

      docker-compose up --build
