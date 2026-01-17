Нажмите на редактирование, чтобы увидеть нормальный формат!
📈 Deribit Price Collector

Асинхронное backend-приложение для периодического получения цен крипто-инструментов с Deribit API, их сохранения в PostgreSQL и предоставления REST API для чтения исторических данных.

🚀 Features
FastAPI REST API
Асинхронная работа с PostgreSQL (SQLAlchemy + asyncpg)
Фоновая загрузка данных через Celery
Планировщик задач (Celery Beat)
Redis как брокер сообщений
Docker + docker-compose
Полное покрытие бизнес-логики тестами (pytest)

🏗️ Architecture Overview
┌────────────┐        HTTP         ┌──────────────┐
│   Client   │ ─────────────────▶  │   FastAPI    │
└────────────┘                     │   (API)      │
                                   └─────┬────────┘
                                         │
                                         │ async SQLAlchemy
                                         ▼
                                   ┌──────────────┐
                                   │ PostgreSQL   │
                                   └──────────────┘
            Celery task                ▲
        ┌────────────────┐             │
        │  Celery Worker │ ────────────┘
        └──────┬─────────┘
               │
               ▼
           ┌────────┐
           │ Redis  │
           └────────┘
               ▲
               │
        ┌──────┴─────────┐
        │  Celery Beat   │
        └────────────────┘

🐳 Running with Docker
1. Build and run containers
bash: docker compose up --build

2. Services
Service          	Description
api	                FastAPI application
worker	            Celery worker
beat	            Celery scheduler
postgres	        PostgreSQL database
redis	            Celery broker


🌐 API Endpoints
Fetch prices manually
POST /tasks/fetch-prices
Triggers background Celery task.

Get latest price
GET /prices/latest?ticker=btc_usd

Get prices history
GET /prices/history?ticker=eth_usd&limit=100

Get prices for period
GET /prices/period?ticker=btc_usd&from_dt=2026-01-16T16:01:00Z&to_dt=2026-01-16T16:03:00Z&limit=100

🧪 Tests
bash: pytest
API layer
Services (business logic)
Celery tasks
Полностью изолированные unit-тесты
Используются AsyncMock и monkeypatch

⚙️ Configuration
.env file example:

DATABASE_URL=postgresql+asyncpg://postgres:postgres@postgres:5432/deribit
REDIS_URL=redis://redis:6379/0
DERIBIT_BASE_URL=https://deribit.com/api/v2/public

🧠 Design Decisions
🔹 FastAPI + async stack

Выбран FastAPI в сочетании с асинхронным SQLAlchemy для высокой пропускной способности и минимальных накладных расходов при работе с I/O.
🔹 Celery для фоновых задач

Celery используется для:
- периодического получения цен
- отделения фоновой логики от API
- масштабируемости (worker можно масштабировать независимо)

🔹 Redis как брокер
- Redis выбран как простой и быстрый message broker, полностью достаточный для данной задачи.

🔹 PostgreSQL
PostgreSQL используется как основное хранилище:
- поддержка временных рядов
- надёжность
- совместимость с asyncpg

🔹 Docker Compose
Каждый сервис вынесен в отдельный контейнер:
- API
- Celery worker
- Celery beat
- PostgreSQL
- Redis
Это упрощает развертывание и приближает окружение к production.
Образ api на dockerhub:
bash: docker push sumburovsn/deribit-client-api:tagname

🔹 Отказ от init_db скриптов
Инициализация БД полностью делегирована Docker-образу PostgreSQL.
Миграции (при необходимости) должны выполняться отдельно (например, через Alembic).

🔹 Чистая архитектура
API слой не содержит бизнес-логики
- Сервисы изолированы
- Внешние клиенты (Deribit) легко мокируются
- Код легко тестируется

✅ Status
✔ Fully working
✔ Covered by tests
✔ Dockerized
✔ Production-ready MVP

Спасибо составителям за задачу, ChatGPT за поддержку!
