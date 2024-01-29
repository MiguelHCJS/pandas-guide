# Flake8: noqa
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from sqlalchemy.future.engine import Engine
from typing import Any


Base = declarative_base()


class DataBase:
    def __init__(self):
        self.__engine = self.create_engine()
        self.__session = self.create_session()

    def create_engine(
        self,
        postgresql: bool = False,
        sqlserver: bool = False,
        user: Any = None,
        password: Any = None,
        host: Any = None,
        port: int | None = None,
        database: str | None = None
    ) -> Engine | None:
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
            db = 'db_rpg.sqlite3'
            conn_str = f'sqlite:///{db}'
            self.__engine = sa.create_engine(
                url=conn_str,
                echo=True,
                connect_args={"check_same_thread": False}
            )

        if postgresql:
            conn_str = f'postgresql://{user}:{password}@{host}:{port}/{database}'
            self.__engine = sa.create_engine(url=conn_str)

        if sqlserver:
            conn_str = f'mssql://{user}:{password}@{host}:{port}/{database}'
            self.__engine = sa.create_engine(url=conn_str)

        return self.__engine

    def create_session(self):
        """Criando a Sessão vinculada a Engine

        Returns:
            Session: Estabelece a conexão
        """
        if not self.__engine:
            self.create_engine()

        self.__session = sessionmaker(self.__engine, expire_on_commit=False, class_=Session)

        return self.__session

    def create_tables(self) -> None:
        """Realiza a criação das tabelas no Banco de Dados"""
        if not self.__engine:
            self.create_engine()

        Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)
