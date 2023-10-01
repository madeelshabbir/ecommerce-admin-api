from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from app.utils.database import Base
from app.constants.envs import DATABASE_URL

config = context.config

if config.config_file_name is not None:
  fileConfig(config.config_file_name)

target_metadata = Base.metadata

def run_migrations_offline() -> None:
  context.configure(
    url=DATABASE_URL,
    target_metadata=target_metadata,
    literal_binds=True,
    dialect_opts={'paramstyle': 'named'},
  )

  with context.begin_transaction():
    context.run_migrations()


def run_migrations_online() -> None:
  db_config = config.get_section(config.config_ini_section, {})
  db_config['sqlalchemy.url'] = DATABASE_URL

  connectable = engine_from_config(
    db_config,
    prefix='sqlalchemy.',
    poolclass=pool.NullPool,
  )

  with connectable.connect() as connection:
    context.configure(
      connection=connection, target_metadata=target_metadata
    )

    with context.begin_transaction():
      context.run_migrations()


if context.is_offline_mode():
  run_migrations_offline()
else:
  run_migrations_online()
