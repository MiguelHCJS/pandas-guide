# Flake8: noqa
# import sqlalchemy as sa
# from sqlalchemy.orm import sessionmaker, Session, declarative_base
# from sqlalchemy.future.engine import Engine
from typing import Any
from sqlmodel import SQLModel, create_engine


# Base = declarative_base()


class DataBase:
    def __init__(self):
        self.__engine = self.createEngine()

    def createEngine(
        self,
        postgresql: bool = False,
        sqlserver: bool = False,
        user: Any = None,
        password: Any = None,
        host: Any = None,
        port: int | None = None,
        database: str | None = None,
    ):
        """Criando Engine

        Args:
            postgresql (bool, optional): Se for utilizar, passar parâmetro True, por padrão é False.
            sqlserver (bool, optional): Se for utilizar, passar parâmetro True, por padrão é False.
            user (Any, optional): Só há necessidade de passar, se for utilizar Posgresql ou SqlServer.
            password (Any, optional): Só há necessidade de passar, se for utilizar Posgresql ou SqlServer.
            host (Any, optional): Só há necessidade de passar, se for utilizar Posgresql ou SqlServer.
            port (int | None, optional): Só há necessidade de passar, se for utilizar Posgresql ou SqlServer.
            database (str | None, optional): Só há necessidade de passar, se for utilizar Posgresql ou SqlServer.

        Returns:
            Engine | None: Ele retornarar a criação de DB SQLite por padrão, se não optar por Posgresql ou SqlServer.
        """
        if not postgresql and not sqlserver:
            db = 'db_rpg.db'
            conn_str = f'sqlite:///{db}'
            self.__engine = create_engine(
                url=conn_str,
                echo=True,
                connect_args={'check_same_thread': False},
            )

        if postgresql:
            conn_str = (
                f'postgresql://{user}:{password}@{host}:{port}/{database}'
            )
            self.__engine = sa.create_engine(url=conn_str)

        if sqlserver:
            conn_str = f'mssql://{user}:{password}@{host}:{port}/{database}'
            self.__engine = sa.create_engine(url=conn_str)

        return self.__engine

    def create_tables(self) -> None:
        """
        Realiza a criação das tabelas no Banco de Dados
        """
        if not self.__engine:
            self.createEngine()

        SQLModel.metadata.create_all(self.__engine)
