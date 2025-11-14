# Plano de Testes: Gerenciador Financeiro

Este documento descreve o plano de testes adotado para validação do projeto, detalhando os tipos de testes existentes para cada tipo.

---

## 1. Testes Unitários

**Objetivo:** Validar os componentes de mais baixo nível (serviços, modelos, utilitários) de forma isolada, usando *mocks* (simuladores) e repositórios em memória.

**Pasta Principal:** `tests/unit/`

### Testes de Lógica de Serviço (Focados)
**Ficheiros:** `test_account_service.py`, `test_budget_service.py`, `test_goal_service.py`, `test_transaction_service.py`, `test_user_service.py`

Validam "ramos" (branches) de validação e regras de negócio específicas em cada serviço, como:
* `test_create_account_requires_existing_user`: Garante que uma conta só pode ser criada para um utilizador que existe.
* `test_apply_expense_beyond_limit_raises`: Garante que o serviço de orçamento levanta um `BusinessRuleError` se a despesa ultrapassar o limite.
* `test_create_transaction_insufficient_balance_raises`: Garante que o serviço de transação impede a criação de despesas que deixariam o saldo negativo.

### Testes de Lógica de Serviço (com Mocks)
**Ficheiro:** `test_services_with_mocks.py`

Valida a orquestração de ações e o tratamento de erros quando as dependências (repositórios, outros serviços) são simuladas com `AsyncMock`.
* `test_transaction_service_handles_repository_errors_with_mock`: Garante que o `TransactionService` lida corretamente com erros vindos do repositório.
* `test_report_service_uses_file_manager`: Verifica se o `ReportService` chama corretamente o `FileManager` para criar um ficheiro.

### Testes de Princípios de Design (OOP)
**Ficheiro:** `test_models_oop.py`

Valida que o design da aplicação segue os princípios de Orientação a Objetos (OOP) pretendidos.
* **Abstração (Contrato):** Garante que a classe base `Repository` define um "contrato" abstrato.
* **Polimorfismo:** Prova que um serviço (ex: `UserService`) pode funcionar com qualquer implementação concreta de um repositório.

### Testes de Utilitários e Configuração
**Ficheiros:** `test_file_manager.py`, `test_settings.py`, `test_report_service.py`

Valida a lógica de componentes auxiliares:
* `test_export_transactions_creates_csv`: Garante que o `FileManager` exporta corretamente um ficheiro CSV.
* `test_settings_loads_from_env_file`: Verifica se o `Settings` carrega as variáveis de ambiente.
* `test_report_service_exports_transactions`: Valida se o `ReportService` gera os dados corretos para o relatório.

---

## 2. Testes Estruturais

**Objetivo:** Validar a infraestrutura da aplicação e a "canalização" (wiring) dos componentes, garantindo que as dependências (como Injeção de Dependência e Repositórios) estão corretamente configuradas.

**Pasta Principal:** `tests/structural/`

* **Ficheiro:** `test_dependencies.py`
    * Garante que as funções de Injeção de Dependência (DI) do FastAPI (ex: `get_user_service`, `get_account_repository`) constroem e injetam os serviços e repositórios corretamente.

* **Ficheiro:** `test_repositories.py`
    * Testa o `MongoRepository` base abstrato para garantir que as operações CRUD (Create, Read, Update, Delete) funcionam como esperado contra uma base de dados em memória (`mongomock`).

* **Ficheiro:** `test_utils.py`
    * Valida utilitários de baixo nível, como o `MongoJSONEncoder`, para garantir a serialização correta de tipos como `ObjectId` e `datetime`.

* **Ficheiro:** `test_version_module.py`
    * Garante que o módulo de versão da aplicação está acessível e que a versão está definida.

---

## 3. Testes de Integração (Nível de Serviço)

**Objetivo:** Validar a *interação* entre os **Serviços reais** (ex: `TransactionService` e `AccountService`). Estes testes substituem a camada de banco de dados por **Repositórios em Memória** (ex: `InMemoryTransactionRepository`), permitindo testar a lógica de negócio completa de forma rápida e isolada.

**Arquivo Principal:** `tests/integration/test_integracao.py`

### Regra de Negócio: Fluxos de Transação e Impacto no Saldo
Valida se a criação e exclusão de transações (via `TransactionService`) causam o impacto correto nos saldos (geridos pelo `AccountService`).
* `test_income_transaction_updates_balance_and_listing`: Garante que uma `INCOME` (receita) aumenta o saldo da conta.
* `test_transfer_transaction_updates_both_accounts`: Garante que uma `TRANSFER` debita da origem e credita no destino.
* `test_delete_transaction_reverts_account_balance`: Garante que deletar uma despesa reverte o valor no saldo (estorno).

### Regra de Negócio: Validação de Restrições
Valida se os serviços aplicam corretamente as regras que cruzam domínios.
* `test_expense_transaction_respects_budget_limit`: Garante que o `TransactionService` consulta o `BudgetService` e **impede** uma despesa que ultrapasse o orçamento.
* `test_delete_account_blocked_when_transactions_exist`: Impede que o `AccountService` delete uma conta se ela possuir transações.
* `test_delete_category_blocked_by_budget`: Impede que o `CategoryService` delete uma categoria se ela estiver a ser usada por um `Budget`.

### Regra de Negócio: Relatórios
Valida a capacidade do `ReportService` de consultar e agregar dados de múltiplos domínios.
* `test_report_monthly_summary_combines_categories_and_budgets`: Verifica se o relatório mensal combina gastos, receitas e valores orçados.

---

## 4. Testes Funcionais (Nível de API)

**Objetivo:** Validar a aplicação como uma "caixa preta" (black-box) através da camada de **HTTP**. Estes testes validam o fluxo completo, desde a requisição HTTP até à resposta JSON, usando os **Serviços reais** e **Repositórios em Memória** (injetados via `app.dependency_overrides`).

**Arquivo Principal:** `tests/functional/test_funcionais.py`

#### Cenários de Teste (Exemplos):
* `test_user_cannot_exceed_budget`: Simula duas transações (`POST /transactions`) para garantir que a segunda é bloqueada (HTTP 409) se exceder o orçamento.
* `test_goal_completion_flow`: Simula múltiplas contribuições para uma meta e verifica (`GET /goals/{id}`) se o status da meta muda para "completed".
* `test_report_generation_returns_file`: Valida o endpoint de relatórios (`GET /reports/transactions/{user_id}`), verificando se o JSON de resposta contém o caminho para um `.csv`.
* `test_account_creation_with_invalid_user_returns_404`: Garante que a API retorna `404 Not Found` se um `user_id` inválido for usado no `POST /accounts`.
* `test_transaction_negative_amount_validation`: Garante que um `POST /transactions` com `amount: -10` é rejeitado com HTTP 422 (Erro de Validação).

---

## 5. Testes de Mutação

**Objetivo:** Medir a **eficácia** e a **qualidade** da suíte de testes existente (Unitários e Integração). O objetivo não é testar o código da aplicação, mas sim **testar os próprios testes** para encontrar "falhas" na cobertura.

**Ferramenta:** `mutmut`

**Arquivos de Teste Alvo:** `tests/mutation/test_mutacao.py`, `test_mutmut_guard.py`

**Processo:**
1.  O `mutmut` altera subtilmente o código-fonte (ex: `src/services/transactions.py`), criando "mutantes" (pequenos bugs, como trocar um `>` por `<=`).
2.  A suíte de testes (`test_mutacao.py`) é executada contra cada mutante.
3.  **Mutante Morto (Killed) :** Os testes *falham*. (Bom: o bug foi detetado).
4.  **Mutante Sobrevivente (Survived) :** Os testes *passam*. (Mau: uma lacuna foi encontrada nos testes).

A suíte `test_mutacao.py` executa testes focados nas regras de negócio mais críticas (limite de saldo, limite de orçamento, restrições de exclusão) para garantir que qualquer "mutante" (bug) nessas lógicas seja "morto" (detetado).

---

## 6. Testes Não-Funcionais (Performance)

**Objetivo:** Medir o desempenho de operações específicas para detectar regressões (perda de performance) ao longo do tempo.

**Arquivo Principal:** `tests/performance/test_transaction_search_benchmark.py`

* **Ferramenta:** `pytest-benchmark`
* **Estratégia:** O `pytest-benchmark` executa a função de pesquisa de transações (`TransactionService.search`) múltiplas vezes para medir o tempo médio de execução e garantir que a filtragem de dados permanece eficiente.