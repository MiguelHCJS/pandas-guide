import sqlalchemy as sa
from datetime import datetime
from ..db_conf import Base


class Jogador(Base):
    __tablename__: str = 'jogadores'

    id: int = sa.Column(sa.Integer,
                        primary_key=True,
                        autoincrement=True)
    data_criacao: datetime = sa.Column(sa.DateTime,
                                       default=datetime.now,
                                       index=True)
    nome: str = sa.Column(sa.String(30),
                          nullable=False)
    sobrenome: str = sa.Column(sa.Strin(30),
                               nullable=False)
    # classe: int = sa.Column(sa.models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE))
    # raca: int = sa.models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
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
