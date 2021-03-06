"""Containers module."""

from dependency_injector import containers, providers
from api.repositories import AuthorRepository, BlogRepository
from api.services import AuthorService, BlogService, ManageUserService
from .database import Database


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=[".routes.authentication_routes", ".routes.author_routes", ".routes.blog_routes"])

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

    blog_repository = providers.Factory(
        BlogRepository,
        session_factory=db.provided.session,
    )

    blog_service = providers.Factory(
        BlogService,
        blog_repository=blog_repository,
    )

    manageuser_service = providers.Factory(
        ManageUserService,
        author_repository=author_repository,
        blog_repository=blog_repository
    )
