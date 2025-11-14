# Finance Manager API

Sistema modular para gerenciamento de finanças pessoais desenvolvido para o projeto da disciplina **Simulação e Teste de Software (CC8550)**. A aplicação expõe uma API REST sobre FastAPI com camadas bem definidas (controllers → services → repositories → MongoDB) e já está preparada para receber a suíte completa de testes especificada no `docs/projeto.md`.

## Principais entidades

- `User`: registra dados pessoais e a renda mensal.
- `Account`: contas financeiras com saldo e valores bloqueados para metas.
- `Transaction`: lançamentos de receitas, despesas e transferências com filtros avançados.
- `Budget`: orçamentos por categoria e período com controle de limites.
- `Goal`: metas de economia com bloqueio automático de saldo.

## Regras de negócio implementadas

1. **Validação de saldo com bloqueios**: despesas/transferências não são permitidas quando o saldo disponível (`balance - goal_locked_amount`) ficaria negativo.
2. **Orçamento por categoria**: antes de efetivar uma despesa, o serviço verifica e atualiza o orçamento mensal correspondente, bloqueando transações que excedam o limite definido.
3. **Metas com fundos bloqueados**: contribuições para metas travam o saldo na conta, liberando automaticamente quando a meta é concluída ou removida.

## Configuração e Execução

1. Copie o `.env.example` para `.env` ajustando as variáveis conforme necessário.
2. Instale dependências: `pip install -r requirements.txt`.
3. Inicie o MongoDB+API via Docker Compose:

```bash
docker compose -f config/docker-compose.yml up --build
```

O serviço ficará disponível em `http://localhost:8000`. A documentação interativa pode ser acessada em `/docs` ou `/redoc`. Se preferir rodar sem Docker, assegure que há um Mongo em execução e suba o FastAPI com:

```bash
uvicorn src.main:app --reload
```

### Popular dados de demonstração

```bash
python scripts/generate_demo_data.py --users 5 --drop-existing --mongodb-uri mongodb://localhost:27018
```

Isso cria usuários/contas/orçamentos/metas/transações no Mongo apontado no `.env`.

### Interface CLI

Também é possível interagir com a API via CLI:

```bash
python scripts/cli.py users-list
python scripts/cli.py users-create --name "CLI User" --email cli@example.com
```

### Menu interativo (modo guiado)

Para quem prefere um fluxo com prompts, utilize o menu textual:

```bash
python scripts/menu.py
# ou informe explicitamente o host/porta do backend
python scripts/menu.py --base-url http://localhost:8001/api/v1
```

O menu permite listar e criar usuários, consultar/criar contas, registrar transações e exportar relatórios sem precisar memorizar endpoints ou parâmetros.


## Estrutura

- `src/models`: modelos de domínio e schemas Pydantic.
- `src/repositories`: camda de acesso a dados com interfaces intercambiáveis.
- `src/services`: regras de negócio, validações e integração entre entidades.
- `src/controllers`: routers FastAPI organizados por recurso.
- `src/utils`: helpers de configuração, logging, acesso ao MongoDB e exportação de relatórios.
- `config/docker-compose.yml`: orquestração do app + MongoDB em containers.

## Próximos passos

1. Implementar a suíte de testes (unitários, integração, funcionais etc.) seguindo o plano definido.
2. Configurar fixtures de dados em `tests/fixtures` para cenários replicáveis.
3. Documentar plano e relatório de testes nos arquivos `docs/plano_testes.md` e `docs/relatorio_testes.md`.

Com o backend completo, o próximo foco será construir e automatizar os testes exigidos pelo projeto.

## Execução dos testes

```bash
pytest                              # executa toda a suíte
coverage run -m pytest -v --cov=src --cov-branch --cov-report=term-missing --cov-report=html
coverage report -m
# Tests de mutação
rm -rf .mutmut-cache mutants && PYTEST_ADDOPTS= PROJECT_ROOT=$(pwd) mutmut run
```

- As fixtures/mocks estão em `tests/fixtures`.
- Os testes de integração/funcionais usam `httpx.AsyncClient` com dependências sobrescritas (sem Mongo real).
- Testes de performance usam `pytest-benchmark` (`tests/performance/test_transaction_search_benchmark.py`).
