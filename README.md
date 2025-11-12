# Simulação e Teste de Software — Sistema de Finanças Pessoais

## Visão Geral

Projeto desenvolvido para a disciplina **Simulação e Teste de Software (CC8550)**. O objetivo é construir uma API REST para gerenciamento de finanças pessoais com foco em arquitetura em camadas, regras de negócio complexas e ampla cobertura de testes.

Principais entidades já implementadas:
- Usuários
- Contas financeiras
- Categorias (receitas e despesas)
- Transações (receitas, despesas e transferências)
- Budgets mensais por categoria
- Relatórios mensais consolidados

## Requisitos Técnicos Atendidos

- Modularização por camadas (`controllers`, `services`, `repositories`, `models`)
- Injeção de dependências via FastAPI
- Type hints e docstrings nas principais classes
- Configuração externa via `.env`
- Logging configurável (`config/logging.yaml`)
- Persistência em MongoDB (Motor) com índices criados programaticamente

## Guia de Execução

### 1. Pré-requisitos
- Python 3.10+
- Docker e Docker Compose
- `pip`/`venv`

### 2. Clonar e instalar dependências
```bash
git clone <url-do-repositorio>
cd projeto-sts-CC8550
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python3 -m pip install -r requirements.txt
```

### 3. Configurar variáveis de ambiente
```bash
cp .env.example .env
# Edite .env se quiser customizar a URI/credenciais do Mongo
```

### 4. Subir o MongoDB local
```bash
docker compose up -d
```

### 5. Criar coleções e índices
```bash
python3 -m src.database.setup
```

### 6. (Opcional) Popular dados de exemplo
```bash
python3 - <<'PY'
from datetime import datetime, timezone
from bson import ObjectId
from pymongo import MongoClient

client = MongoClient('mongodb://root:root@localhost:27017/?authSource=admin')
db = client['personal_finance_db']

for name in ['users', 'accounts', 'categories', 'transactions', 'budgets']:
    db[name].delete_many({})

now = datetime.now(timezone.utc)
user_id = ObjectId()
account_id = ObjectId()
income_cat = ObjectId()
expense_cat = ObjectId()

db.users.insert_one({
    '_id': user_id,
    'name': 'Maria Souza',
    'email': 'maria.souza@example.com',
    'default_currency': 'BRL',
    'created_at': now,
    'updated_at': now,
})

db.accounts.insert_one({
    '_id': account_id,
    'user_id': user_id,
    'name': 'Conta Corrente Itaú',
    'account_type': 'checking',
    'currency': 'BRL',
    'description': 'Conta principal',
    'minimum_balance': 0,
    'balance': 2500.00,
    'created_at': now,
    'updated_at': now,
})

db.categories.insert_many([
    {
        '_id': income_cat,
        'user_id': user_id,
        'name': 'Salário',
        'category_type': 'income',
        'description': 'Recebimentos de salário',
        'parent_id': None,
        'created_at': now,
        'updated_at': now,
    },
    {
        '_id': expense_cat,
        'user_id': user_id,
        'name': 'Supermercado',
        'category_type': 'expense',
        'description': 'Compras de alimentação',
        'parent_id': None,
        'created_at': now,
        'updated_at': now,
    },
])

db.budgets.insert_one({
    '_id': ObjectId(),
    'user_id': user_id,
    'category_id': expense_cat,
    'year': now.year,
    'month': now.month,
    'amount': 1200.0,
    'alert_percentage': 80,
    'created_at': now,
    'updated_at': now,
})

db.transactions.insert_many([
    {
        '_id': ObjectId(),
        'user_id': user_id,
        'account_id': account_id,
        'category_id': income_cat,
        'amount': 5000.00,
        'transaction_type': 'income',
        'occurred_at': now,
        'description': 'Pagamento mensal',
        'notes': None,
        'counterparty': 'Empresa XYZ',
        'transfer_account_id': None,
        'created_at': now,
        'updated_at': now,
    },
    {
        '_id': ObjectId(),
        'user_id': user_id,
        'account_id': account_id,
        'category_id': expense_cat,
        'amount': 350.00,
        'transaction_type': 'expense',
        'occurred_at': now,
        'description': 'Compras semanais',
        'notes': None,
        'counterparty': 'Mercado Bom Preço',
        'transfer_account_id': None,
        'created_at': now,
        'updated_at': now,
    },
])

print('Dados de exemplo inseridos.')
PY
```

### 7. Executar a API
```bash
uvicorn src.main:app --reload
```
- Servidor: `http://127.0.0.1:8000`
- Documentação interativa: `http://127.0.0.1:8000/docs`

### 7.1 Interface em Linha de Comando (opcional)
```bash
python3 -m src.interface.cli
```
O menu permite listar/criar usuários, contas, categorias, budgets, registrar transações e visualizar o relatório mensal diretamente pelo terminal.

### 8. Rotas principais para testar
- `GET /api/users`
- `GET /api/accounts?user_id=<id>`
- `POST /api/transactions`
- `GET /api/budgets?user_id=<id>&year=YYYY&month=MM`
- `GET /api/reports/monthly-summary?user_id=<id>&year=YYYY&month=MM`

### 9. Encerrar serviços
```bash
docker compose down  # encerra o MongoDB opcionalmente
```

## Testes e cobertura

Execute toda a suíte (unitários, mutação, funcionais, integração e estruturais) com:

```bash
pytest
```

Para medir a cobertura com `coverage.py` (configuração em `.coveragerc`, com branch coverage e `fail_under=80`):

```bash
coverage run -m pytest
coverage report -m
coverage html  # gera htmlcov/index.html
```

> Evite rodar `pytest --cov` ao mesmo tempo que `coverage run`, pois ambos instrumentam o código. Os comandos acima já consolidam o relatório e permitem inspeção em HTML.

## Próximos Passos Sugeridos
- Implementar suítes automatizadas (unit, integration, mutation etc.)
- Adicionar mais regras de negócio (ex.: metas por conta, notificações)
- Expandir relatórios (dashboards ou exportação de CSV/JSON)

---

**Professor responsável:** Luciano Rossi — Centro Universitário FEI
