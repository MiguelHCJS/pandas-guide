from db_conf import DataBase, Base
import sqlalchemy as sa
from sqlalchemy import orm
from datetime import datetime


db = DataBase()


class Classe(Base):
    __tablename__ = 'classes'

    id_classe: int = sa.Column(sa.Integer,
                               primary_key=True,
                               autoincrement=True)
    nome: str = sa.Column(sa.String(30),
                          nullable=False)
    data_criacao: datetime = sa.Column(sa.DateTime,
                                       default=datetime.now,
                                       index=True)

    def __repr__(self) -> str:
        return f"""
            <Classe>
            Nome: {self.nome}
        """


class Raca(Base):
    __tablename__ = 'racas'

    id_raca: int = sa.Column(sa.Integer,
                             primary_key=True,
                             autoincrement=True)
    nome: str = sa.Column(sa.String,
                          nullable=False)
    data_criacao: datetime = sa.Column(sa.DateTime,
                                       default=datetime.now,
                                       index=True)

    def __repr__(self) -> str:
        return f"""
            <Raca>
            Nome: {self.nome}
        """


class Jogador(Base):
    __tablename__: str = 'jogadores'

    id_jogador: int = sa.Column(sa.Integer,
                                primary_key=True,
                                autoincrement=True)
    data_criacao: datetime = sa.Column(sa.DateTime,
                                       default=datetime.now,
                                       index=True)
    nome: str = sa.Column(sa.String(30),
                          nullable=False)
    sobrenome: str = sa.Column(sa.String(30),
                               nullable=False)
    id_classe: int = sa.Column(sa.Integer,
                               sa.ForeignKey('classes.id_classe'))
    classe = orm.relationship('classes',
                              lazy='joined')  # Configuração interna do SQLalchemy
    id_raca: int = sa.Column(sa.Integer,
                             sa.ForeignKey('racas.id_raca'))
    raca = orm.relationship('racas',
                            lazy='joined')  # Configuração interna do SQLalchemy
    nivel: int = sa.Column(sa.Integer,
                           nullable=False)
    pontos_vida: int = sa.Column(sa.Integer,
                                 nullable=False)
    pontos_mana: int = sa.Column(sa.Integer,
                                 nullable=False)
    forca: int = sa.Column(sa.Integer,
                           nullable=False)
    destreza: int = sa.Column(sa.Integer,
                              nullable=False)
    constituicao: int = sa.Column(sa.Integer,
                                  nullable=False)
    inteligencia: int = sa.Column(sa.Integer,
                                  nullable=False)
    sabedoria: int = sa.Column(sa.Integer,
                               nullable=False)
    carisma: int = sa.Column(sa.Integer,
                             nullable=False)

    def __repr__(self) -> str:
        return f"""
            <Jogador>
            Nome: {self.nome}
            Nível: {self.nivel}
        """


if __name__ == '__main__':
    db.create_tables()
