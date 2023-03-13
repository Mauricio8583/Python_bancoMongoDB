import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DECIMAL
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import Select

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    cpf = Column(String)
    endereco = Column(String)

    conta = relationship(
        "Conta", back_populates="cliente", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"Cliente(id={self.id}, name={self.name}, cpf={self.cpf}, endereco={self.endereco})"        

class Conta(Base):
    __tablename__ = 'conta'

    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    agencia = Column(String)
    num = Column(Integer)
    id_cliente = Column(Integer, ForeignKey("cliente.id"))
    saldo = Column(DECIMAL)

    cliente = relationship(
        "Cliente", back_populates="conta"
    )

    def __repr__(self):
        return f"Conta(id={self.id}, tipo={self.tipo}, agencia={self.agencia}, num={self.num}, saldo={self.saldo})"

engine = create_engine("sqlite://")

Base.metadata.create_all(engine)

inspector = inspect(engine)

print(inspector.get_table_names())

with Session(engine) as session:
    mauricio = Cliente(
        name = "Mauricio Oliveira",
        cpf = "111222333444",
        endereco = "Rua 23 de Setembro, 666",
        conta = [Conta(tipo = "Conta Corrente", agencia = "0008", num = 333444, saldo = 600.00), Conta(tipo = "Conta Poupaca", agencia = "0008", num = 236784, saldo = 2000.00)]
    )

    fulano = Cliente(
        name = "Fulando da Silva",
        cpf = "333444777",
        endereco = "Rua 8 de Julho, 222",
        conta = [Conta(tipo = "Conta Corrente", agencia = "0009", num = 3333333, saldo = 4000.00)]
    )

    session.add_all([mauricio, fulano])

    session.commit()


stmt = Select(Cliente).where(Cliente.name.in_(['Mauricio Oliveira', 'Fulano da Silva']))

for cliente in session.scalars(stmt):
    print(cliente)

stmt_conta = Select(Conta).where(Conta.tipo.in_(['Conta Corrente']))

for contas in session.scalars(stmt_conta):
    print(contas)