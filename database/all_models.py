from datetime import datetime
from db_conf import DataBase
# from typing import Optional
from sqlmodel import Field, SQLModel  # , Session, create_engine, select


db = DataBase()


class Classe(SQLModel, table=True):
    id_classe: int = Field(default=None, primary_key=True)
    nome: str
    data_criacao: datetime

    def __repr__(self) -> str:
        return f"""
            <Classe>
            Nome: {self.nome}
        """


class Raca(SQLModel, table=True):
    id_raca: int = Field(default=None, primary_key=True)
    nome: str = Field(nullable=False)
    data_criacao: datetime = Field(default=datetime.now, index=True)

    def __repr__(self) -> str:
        return f"""
            <Raca>
            Nome: {self.nome}
        """


# class Jogador(SQLModel, table=True):
#     id_jogador: int = Field(default=None, primary_key=True)
#     data_criacao: datetime = Field(default=datetime.now, index=True)    
#     nome: str = Field(nullable=False)
#     sobrenome: str = Field(nullable=False)

#     id_classe: int = sa.Column(sa.Integer, sa.ForeignKey('classes.id_classe'))
#     classe = orm.relationship(
#         'classes', lazy='joined'
#     )  # Configuração interna do SQLalchemy
#     id_raca: int = sa.Column(sa.Integer, sa.ForeignKey('racas.id_raca'))
#     raca = orm.relationship(
#         'racas', lazy='joined'
#     )  # Configuração interna do SQLalchemy
#     nivel: int = sa.Column(sa.Integer, nullable=False)
#     pontos_vida: int = sa.Column(sa.Integer, nullable=False)
#     pontos_mana: int = sa.Column(sa.Integer, nullable=False)
#     forca: int = sa.Column(sa.Integer, nullable=False)
#     destreza: int = sa.Column(sa.Integer, nullable=False)
#     constituicao: int = sa.Column(sa.Integer, nullable=False)
#     inteligencia: int = sa.Column(sa.Integer, nullable=False)
#     sabedoria: int = sa.Column(sa.Integer, nullable=False)
#     carisma: int = sa.Column(sa.Integer, nullable=False)

#     def __repr__(self) -> str:
#         return f"""
#             <Jogador>
#             Nome: {self.nome}
#             Nível: {self.nivel}
#         """


if __name__ == '__main__':
    db.create_tables()
