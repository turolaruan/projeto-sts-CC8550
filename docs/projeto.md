# Simulação e Teste de Software (CC8550) – Descrição do Projeto

## Membros do Grupo

> Felipe Orlando Lanzara - 22.225.015-1

> Pedro Henrique Lega Kramer Costa - 22.125.091-3

> Ruan Pastrelo Turola - 22.225.013-6

---

## 1. Tema

**Finance Manager API**: plataforma modular para gerenciamento de finanças pessoais.  
Os usuários conseguem registrar contas, transações, budgets mensais, metas de economia e gerar relatórios/exports. Toda a interação acontece por meio de uma API REST construída em FastAPI (com CLI opcional para facilitar testes manuais).

---

## 2. Características Técnicas

### 2.1 Arquitetura e Estrutura

- **Clean/Hexagonal inspirado:** `controllers` (FastAPI) → `services` → `repositories` → MongoDB.  
- **Injeção de dependências via FastAPI** (`get_*_service`) e em testes, permitindo trocar repositories por fakes/mocks.  
- **Interfaces/abstrações:** `AbstractRepository` define operações CRUD e é reutilizada em todos os repositórios concretos.  
- **Automação e scripts:** CLI (`scripts/cli.py`), menu interativo (`scripts/menu.py`), seed (`scripts/generate_demo_data.py`) e bootstrap de venv (`scripts/bootstrap_env.py`).

---

### 2.2 Funcionalidades Mínimas

- CRUD completo para **Usuários, Contas, Budgets, Metas e Transações** (cinco entidades principais).  
- Regras de negócio implementadas:
  1. **Bloqueio de saldo** considerando fundos reservados para metas antes de autorizar despesas/transferências.
  2. **Controle de budgets mensais** por categoria (limite, alerta, status `healthy/warning/exceeded`).  
  3. **Contribuições para metas** com bloqueio/desbloqueio automático do saldo e conclusão da meta.  
- Consultas/buscas:
  - `/transactions/search` com `min_amount`, `max_amount`, `category`, intervalo de datas e ordenação.  
  - `/budgets/summary/{user_id}` com agregação dinâmica do status dos budgets.  
- Tratamento de exceções customizado (`BusinessRuleError`, `NotFoundError`, `ValidationError`, `ServiceError`) com handlers FastAPI.  
- Validações de entrada via Pydantic (type hints, `PositiveFloat`, campos obrigatórios, enums etc.).

---

### 2.3 Persistência de Dados

- Banco **MongoDB** (container no `docker-compose`).  
- Repositórios assíncronos (`motor`) seguindo o padrão Repository.  
- `Memory*Repository` simulando persistência em testes (sem dependência externa).

---

### 2.4 Interface (Escolher pelo menos uma)

- **API REST (FastAPI)**: endpoints organizados por recurso (`/api/v1/users`, `/accounts`, `/transactions`, etc.).
- **Interface CLI/Menu (opcional):** `scripts/menu.py` consomem a API para utilizar o sistema.

---

### 2.5 Requisitos Técnicos Específicos

- **Configuração externa:** `.env` consumido por `pydantic-settings`.  
- **Logging:** `loguru` com configuração centralizada (`src/utils/logger.py`).  
- **Documentação/Type hints:** Pydantic models e services tipados com docstrings.   
- **Docker compose** para subir API + Mongo localmente.

---

## 3. Testes Desenvolvidos

### 3.1 Testes Unitários 

- Framework: `pytest` (modo estrito do `pytest-asyncio`).  
- Mais de **60 casos** cobrindo services (`accounts`, `budgets`, `transactions`, `goals`, `users`), utilitários e modelos.  
- Uso de fixtures comuns (`tests/fixtures`) e repositórios em memória para simular o banco.  
- Cobertura de fluxos normais, erros (`BusinessRuleError`, `NotFoundError`) e casos limite (saldo negativo, orçamento excedido etc.).

---

### 3.2 Testes de Integração 

- `tests/integration/test_integracao.py` com 12 cenários completos: criação de usuário/conta, budgets, goal contributions, relatórios e validações de HTTP status.  
- Utiliza FastAPI real + dependências injetadas (repositories em memória ou Mongo), simulando flows ponta a ponta.

---

### 3.3 Testes Funcionais (Caixa-Preta) 

- `tests/functional/test_funcionais.py` (8 cenários) trata o sistema como caixa-preta: cada caso envia requisições HTTP e valida apenas respostas/efeitos visíveis (ex: orçamento não pode ser excedido, relatório deve bater com lançamentos).

---

### 3.4 Testes Estruturais (Caixa-Branca) 

- Suites em `tests/structural/` exercitam `AbstractRepository`, providers de dependência, utils e versionamento.  
- Ferramentas: `pytest --cov=src --cov-report=term --cov-report=html`.  
- Cobertura atual: **91 %** de linhas/branches, com relatório HTML (`htmlcov/index.html`).

---

### 3.5 Testes de Mutação 

- Ferramenta `mutmut` aplicada em `accounts`, `budgets` e `transactions`.  
- 81 mutantes gerados / 58 mortos / score 71.6 %.  
- Relatório inclui categorias dos sobreviventes e plano de ação (casos de borda e mensagens de erro).

---

### 3.6 Testes Específicos por Tipo 

- **API/REST:** suites funcionais/integradas usam `httpx` para validar endpoints e códigos HTTP.  
- **Exceções:** unitários capturam `BusinessRuleError`, `NotFoundError`, etc., garantindo mensagens coerentes.  
- **Mocks e Stubs:** `tests/unit/test_services_with_mocks.py` usa `MagicMock`; repositórios em memória servem como stubs do banco.  
- **Performance:** `tests/performance/test_transaction_search_benchmark.py` mede a busca de transações (~0.53 ms).  
- **Orientação a Objetos:** `tests/unit/test_models_oop.py` e unitários de serviços cobrem herança/polimorfismo e colaboração entre camadas.

---

## 4. Estrutura do Projeto

O projeto deve ser estruturado de forma modular, seguindo boas práticas de arquitetura, separação de camadas, testes automatizados e documentação, atendendo todos os requisitos técnicos e de testes descritos acima.


    projeto-sts-cc8550/                      
        ├── src/                      # Código fonte da aplicação
        │   ├── __init__.py           
        │   ├── models/               # Modelos de dados
        │   ├── controllers/          # Lógica de negócio
        │   ├── repositories/         # Acesso a dados
        │   ├── services/             # Serviços auxiliares
        │   └── utils/                # Utilitários
        │ 
        ├── tests/                    # Todos os testes
        │   ├── __init__.py           
        │   ├── unit/                 # Testes unitários
        │   ├── integration/          # Testes de integração
        │   ├── functional/           # Testes funcionais
        │   ├── mutation/             # Configuração de testes de mutação
        │   └── fixtures/             # Dados de teste
        │
        ├── docs/                     # Documentação
        │   ├── projeto.md            # Descrição do projeto
        │   ├── plano_testes.md       # Plano de testes
        │   └── relatorio_testes.md   # Relatório de execução
        │
        ├── config/                   # Arquivos de configuração
        │   ├── __init__.py           # Permite importar helpers de config
        │   ├── docker-compose.yml    # Orquestra API + MongoDB para desenvolvimento
        │   └── settings.py
        │
        ├── scripts/                  # CLI, menu e utilitários
        │   ├── cli.py                # Interface por linha de comando para consumir a API
        │   ├── menu.py               # Menu interativo em modo texto
        │   └── generate_demo_data.py # Seed de dados (usuários, contas, budgets, metas)           
        │
        ├── requirements.txt          # Dependências Python
        ├── pytest.ini                # Configuração do pytest
        ├── .env.example              # Exemplo de variáveis de ambiente
        ├── .env                      # Configuração local (URI do Mongo, log level, etc.)
        ├── README.md                 # Instruções do projeto
        ├── Dockerfile                # Build da imagem da API
        ├── sitecustomize.py          # Ajustes globais para execução da suíte
        ├── setup.cfg                 # Configuração de tooling (lint/pytest/mutmut)
        ├── run_mutmut_pytest.py      # Runner auxiliar para mutmut/pytest
        └── logs/                     # Saídas de log geradas pela aplicação
