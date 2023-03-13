import pymongo

client = pymongo.MongoClient('mongodb+srv://pymongo:pymongo@cluster0.492s2eg.mongodb.net/?retryWrites=true&w=majority')

db = client.bank

conta_um = {
    "tipo": "Conta Corrente",
    "agencia": "0008",
    "num": 3334445,
    "saldo": 300.00

}

conta_dois = {
    "tipo": "Conta Corrente",
    "agencia": "0008",
    "num": 22233322,
    "saldo": 700.00

}

conta_tres = {
    "tipo": "Conta Poupança",
    "agencia": "1002",
    "num": 1222333,
    "saldo": 2000.00
}

new_clientes = [{
    "nome": "Mauricio Oliveira",
    "cpf": "122233344",
    "endereco": "Rua 2 de Outubro, 333",
    "contas": [conta_um, conta_dois]
},
{
    "nome": "Fulano da Sila",
    "cpf": "223335555",
    "endereco": "Rua 7 de Setembro, 777",
    "contas": [conta_um]
},
{
    "nome": "Ciclano de Souza",
    "cpf": "55533344",
    "endereco": "Rua 5 de Maio, 555",
    "contas": [conta_dois, conta_tres]
}]

clientes = db.clientes

clientes_id = clientes.insert_many(new_clientes).inserted_ids

print(clientes_id)

