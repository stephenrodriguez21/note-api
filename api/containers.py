"""Containers module."""

from dependency_injector import containers, providers
from api.repositories import AuthorRepository
from api.services import AuthorService
from .database import Database


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=[".endpoints"])

    config = providers.Configuration(yaml_files=["config.yml"])

    db = providers.Singleton(Database, db_url=config.db.url)

    author_repository = providers.Factory(
        AuthorRepository,
        session_factory=db.provided.session,
    )

    author_service = providers.Factory(
        AuthorService,
        author_repository=author_repository,
    )
