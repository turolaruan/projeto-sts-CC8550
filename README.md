# Finance Manager API

Sistema modular para gerenciamento de finanças pessoais desenvolvido para a disciplina **Simulação e Teste de Software (CC8550)**. A aplicação expõe uma API REST sobre FastAPI com camadas bem definidas (controllers → services → repositories → MongoDB) e já está integrada a uma suíte completa de testes.

## Principais entidades

- `User`: registra dados pessoais e renda mensal.
- `Account`: contas financeiras com saldo e valores bloqueados para metas.
- `Transaction`: lançamentos de receitas/despesas/transferências com filtros.
- `Budget`: orçamentos por categoria/período com status dinâmico.
- `Goal`: metas de economia com bloqueio automático de saldo.

## Regras de negócio (destaques)

1. **Validação de saldo considerando metas bloqueadas** (`balance - goal_locked_amount` não pode ficar negativo).
2. **Controle de budgets mensais** com limites e alertas (`healthy`, `warning`, `exceeded`).
3. **Contribuições para metas** travam/destravaram o saldo automaticamente ao atingir o objetivo.

## Pré-requisitos

- Python **3.10+**
- Git, `pip` e (opcional) Docker/Docker Compose
- Terminal bash (Linux/macOS) ou PowerShell (Windows)

## Configuração do ambiente

1. **Copie as variáveis**
   ```bash
   cp .env.example .env        # Linux/macOS
   copy .env.example .env      # Windows PowerShell
   ```
   Ajuste `MONGODB_URI`, `LOG_LEVEL`, etc.

2. **Crie e ative a virtualenv**
   ```bash
   python -m venv .venv
   source .venv/bin/activate         # Linux/macOS
   .venv\Scripts\Activate.ps1        # Windows PowerShell
   ```

3. **Instale dependências**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **(Opcional) Script de bootstrap**
   ```bash
   python scripts/bootstrap_env.py
   ```

## Execução da API

### Via Docker Compose

```bash
docker compose -f config/docker-compose.yml up --build
```

### Via Python + Mongo local

1. Garanta um Mongo rodando (ex.: `docker run -p 27017:27017 mongo:7`).
2. Ajuste o `.env` para a instância.
3. Rode:
   ```bash
   uvicorn src.main:app --reload
   ```

API disponível em `http://localhost:8000` (Swagger em `/docs` e Redoc em `/redoc`).

## Ferramentas auxiliares

- **Popular dados**  
  ```bash
  python scripts/generate_demo_data.py --users 5 --drop-existing --mongodb-uri mongodb://localhost:27018
  ```

- **CLI**  
  ```bash
  python scripts/cli.py users-list
  python scripts/cli.py users-create --name "CLI User" --email cli@example.com
  ```

- **Menu interativo**  
  ```bash
  python scripts/menu.py
  python scripts/menu.py --base-url http://localhost:8001/api/v1  # custom host
  ```

## Testes automatizados

### Todos os testes + cobertura

```bash
pytest --cov=src --cov-report=term-missing --cov-report=html tests
```

Relatório HTML disponível em `htmlcov/index.html`.

### Por tipo

| Tipo                            | Comando                                                                 |
|--------------------------------|-------------------------------------------------------------------------|
| Unitários                      | `pytest tests/unit`                                                     |
| Integração                     | `pytest tests/integration`                                              |
| Funcionais (caixa-preta)       | `pytest tests/functional`                                               |
| Estruturais (caixa-branca)     | `pytest tests/structural`                                               |
| Performance/benchmark          | `pytest tests/performance -k benchmark`                                 |
| Mutação                        | `mutmut run --runner "python3 -m pytest tests/mutation"`               |

### Métricas atuais

- Cobertura: **91 %** (linhas + branches).  
- Mutation score: **71,6 %** (58/81 mutantes).  
- Benchmark (busca de transações): ~**0.53 ms** por requisição (OPS ≈ 1.88 Kops/s).

## Estrutura do repositório (resumo)

- `src/models`: entidades Pydantic e modelos de domínio.
- `src/repositories`: camada de acesso a dados (\AbstractRepository + implementações Mongo).
- `src/services`: regras de negócio (accounts, budgets, goals, transactions, users).
- `src/controllers`: routers FastAPI organizados por recurso.
- `src/utils`: logger, FileManager, conexões Mongo etc.
- `scripts/`: CLI, menu, seed e bootstrap do ambiente.
- `tests/`: unit, integration, functional, structural, mutation, performance + fixtures.
- `config/`: `docker-compose.yml`, settings e helpers.
- Documentação: `docs/projeto.md`, `docs/plano_testes.md`, `docs/relatorio_testes.md`.

