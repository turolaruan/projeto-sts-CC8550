# Plano de Testes: Gerenciador Financeiro

Este documento descreve o plano de testes adotada para validação do projeto, detalhando os tipos de testes existentes para cada tipo.

---


## 1. Testes Unitários

**Objetivo:** Validar os componentes de **nível mais baixo** da aplicação (Modelos Pydantic, Utilitários, Exceções) de forma totalmente isolada.

**Arquivo Principal:** `test_unidade.py`


###  Validação de Modelos (Pydantic)

Testa se os modelos de criação e atualização estão aplicando as regras de validação e normalização de dados corretamente.

* **Normalização de Texto:** Garante que nomes e descrições são "limpos" (sem espaços extras no início ou fim).
    * *Funções:* `test_account_create_trims_name`, `test_category_create_trims_name`, `test_user_create_trims_name`, `test_transaction_create_trims_description`.

* **Rejeição de Campos Vazios:** Garante que campos obrigatórios (como `name`) são rejeitados se estiverem em branco.
    * *Funções:* `test_account_create_rejects_blank_name`, `test_category_create_rejects_blank_name`, `test_user_update_rejects_blank_name`.

* **Consistência Financeira:** Arredonda (quantiza) valores `Decimal` para 2 casas decimais, evitando problemas de precisão.
    * *Funções:* `test_account_create_normalizes_minimum_balance`, `test_budget_create_amount_is_quantized`, `test_transaction_create_amount_quantized`.

* **Normalização de Dados:** Converte dados para um formato padrão, como emails para minúsculas.
    * *Função:* `test_user_create_lowercases_email`.

###  Teste dos "Builders" (Construtores)

Valida as funções de construção (build) que transformam um *payload* de criação em um modelo maior. (Ex: um pequeno payload virar uma extrutura de dados maior  contendo dados adicionais de horário, dia , atualização, etc...)

* **Geração de IDs e Timestamps:** Usando `patch` (um tipo de *mock*), simula as funções `generate_object_id` e `now_utc`.
* **Garante a Correta Construção:** Verifica se o objeto finalizado contém o ID e os timestamps `created_at` e `updated_at` corretos.
    * *Funções:* `test_build_account_generates_ids_and_timestamps`, `test_build_budget_generates_ids_and_timestamps`, `test_build_category_respects_parent_id`, `test_build_transaction_normalizes_amount_and_sets_timestamps`, `test_build_user_generates_ids_and_timestamps`.

###  Teste de Utilitários

Valida as funções auxiliares encontradas em `src.models.common`.

* **Manipulação de IDs:** Testa a geração de `ObjectId` e a validação de strings de ID.
    * *Funções:* `test_generate_object_id_returns_valid_hex`, `test_ensure_object_id_valid_returns_objectid`, `test_ensure_object_id_invalid_raises_value_error`.
* **Manipulação de Datas:** Confirma que a função `now_utc` sempre retorna um *datetime* com fuso horário (timezone-aware).
    * *Função:* `test_now_utc_returns_timezone_aware_datetime`.
* **Manipulação de Strings:** Valida o utilitário de limpeza de strings.
    * *Funções:* `test_strip_and_validate_non_empty_returns_trimmed_value`, `test_strip_and_validate_non_empty_raises_for_empty_string`.

### Teste de Definições e Exceções

Garante que o mapeamento correto para os enums e as exceções estão sendo realizadas corretamente

* **Hierarquia de Exceções:** Verifica se as exceções customizadas (ex: `EntityNotFoundError`) herdam corretamente de `AppException`.
    * *Funções:* `test_app_exception_stores_context_dict`, `test_entity_not_found_error_is_subclass_of_app_exception`.
* **Valores de Enums:** Verifica se os valores de texto dos `Enums` (ex: `AccountType.CHECKING == "checking"`) estão corretos.

### Testes de Lógica de Serviço (com Mocks)

**Objetivo:** Validar a **lógica interna** de um *único serviço* em `test_service_with_mocks.py` (ex: `UserService`) em total isolamento, simulando suas dependências (como o repositório) com *Mocks*.

* **Verificação de Chamadas (Caminho Feliz):** Garante que o serviço chama corretamente os métodos do repositório (ex: `list` e `create`) ao executar uma ação.
    * *Função:* `test_user_service_create_with_mocked_repository`
* **Simulação de Erros (Exceções):** Simula o repositório retornando um erro (ex: um usuário duplicado) e verifica se o serviço trata esse erro corretamente, lançando a exceção de negócio (`EntityAlreadyExistsError`).
    * *Função:* `test_user_service_prevents_duplicate_email_and_simulates_error`
* **Simulação de "Não Encontrado":** Simula o repositório retornando `None` e verifica se o serviço trata esse caso corretamente, lançando `EntityNotFoundError`.
    * *Função:* `test_user_service_get_user_handles_not_found_with_mock`

---

## 2. Testes Estruturais

**Objetivo:** Validar a  infraestrutura da aplicação FastAPI. Estes testes garantem que os componentes (como Injeção de Dependência, Controladores e Configuração) estão corretamente conectados e que o ciclo de vida da aplicação desde a inicialização até o desligamento funcionem.

### Testes da Camada de Controladores (API)



Garante que os endpoints da API (controladores em `test_controllers.py`) lidam corretamente com os roteamentos de tarefas/páginas juntamente com o tratamendo de as exceções em respostas HTTP coerentes.

* **Verificação dos Caminhos de Sucesso:** Testa se as chamadas de serviço bem-sucedidas retornam os dados corretos e os códigos de status HTTP (200 OK, 204 No Content).
    * *Funções:* `test_users_controller_success_flows`, `test_accounts_controller_success_paths`, `test_budgets_controller_success_paths`, `test_categories_controller_success_paths`, `test_transactions_controller_success_paths`, `test_reports_controller_success_and_error`, `test_health_controller_uses_settings`.
* **Tradução de Erros para HTTP:** Verifica se as exceções de negócio (ex: `EntityNotFoundError`, `ValidationAppError`, `EntityAlreadyExistsError`) lançadas pelos serviços são capturadas e convertidas nos códigos HTTP corretos (404, 400, 409).
    * *Funções:* `test_users_controller_error_branches`, `test_accounts_controller_error_paths`, `test_budgets_controller_error_paths`, `test_categories_controller_error_paths`, `test_transactions_controller_error_paths`.

### Testes da Injeção de Dependência (DI)


Validar as intruções do  FastAPI em `test_service_dependencies.py`, garantindo que elas constroem e injetam corretamente os serviços e repositórios com suas próprias dependências.

* **Construção de Repositórios:** Confirma que as funções `deps.get_` e `_repository` retornam a instância correta do repositório (ex: `UserRepository`, `AccountRepository`).
    * *Função:* `test_repository_dependencies_return_instances`.
* **Construção de Serviços:** Garante que as funções `deps.get_` e `_service` recebem e conectam corretamente suas dependências (outros serviços ou repositórios).
    * *Funções:* `test_service_dependencies_wire_nested_components`, `test_user_service_dependency_returns_valid_instance`.

### Testes do Ciclo de Vida e Banco de Dados

**Arquivos Principais:** `test_app_and_config.py`, `test_database_utils.py`

Valida os eventos de startup e shutdown da aplicação, o gerenciamento da conexão com o banco de dados e a inicialização (em `test_app_and_config.py`e `test_database_utils.py`).

* **Fábrica da Aplicação (`create_app`):** Testa a função principal de criação da aplicação, verificando se ela registra as rotas e os eventos de ciclo de vida (conectar e fechar o `mongo_manager`).
    * *Função:* `test_create_app_registers_routes_and_settings` (`test_app_and_config.py`).
* **Gerenciador do Mongo:** Testa o `MongoManager` para garantir que ele gerencia corretamente o ciclo de vida do cliente (conecta, armazena em cache e fecha).
    * *Função:* `test_mongo_manager_connect_close_and_client_property` (`test_database_utils.py`).
* **Inicialização do Banco de Dados:** Verifica se o script de setup (`ensure_indexes`) é chamado e se ele tenta criar os índices esperados nas coleções corretas.
    * *Funções:* `test_get_client_context_manager_closes_client`, `test_ensure_indexes_creates_expected_entries`, `test_initialize_database_uses_context_manager` (`test_database_utils.py`).
* **Dependência do Banco de Dados:** Testa o *provider* `get_database` usado pelo FastAPI.
    * *Função:* `test_database_dependency_returns_manager_database` (`test_database_utils.py`).

### Testes de Configuração e Entrypoints


Valida o carregamento das configurações (`Settings`), a configuração de logs e os pontos de entrada (entrypoints) da aplicação (como `src.main`) em `test_app_and_config.py`, `test_logging_config.py`, `test_database_utils.py`.

* **Modelo de Configurações (`Settings`):** Verifica se o modelo `Settings` carrega as variáveis de ambiente e se suas propriedades (ex: `is_production`) funcionam.
    * *Função:* `test_settings_helpers_and_properties` (`test_app_and_config.py`).
* **Configuração de Logging:** Testa a função `configure_logging`, garantindo que ela lida com arquivos de configuração ausentes (fallback) e que cria os diretórios de log necessários.
    * *Funções:* `test_configure_logging_falls_back_to_basic_config`, `test_configure_logging_creates_directories_and_applies_yaml` (`test_logging_config.py`).
* **Pontos de Entrada (Entrypoints):** Testa os módulos `src.main` e `src.database.setup` para garantir que eles executam as funções corretas quando chamados como scripts.
    * *Funções:* `test_main_module_import_exposes_app`, `test_main_entrypoint_runs_uvicorn` (`test_app_and_config.py`).
    * *Função:* `test_setup_main_invokes_initializer` (`test_database_utils.py`).

---

## 3. Testes de Integração

**Objetivo:** Validar a lógica de negócio e as regras de dominiu

Estes testes utilizam os **Serviços reais** (ex: `TransactionService`) mas substituem a camada de banco de dados por **Repositórios em Memória** (ex: `InMemoryTransactionRepository`). Isso permite testar a lógica de negócio completa de forma rápida, simulada e isolada (sem um banco de dados real), verificando se os serviços interagem corretamente entre si em `test_integracao.py`.


###  Regra de Negócio: Fluxos de Transação e Impacto no Saldo

Valida se a criação e exclusão de transações (através do `TransactionService`) causam o impacto correto nos saldos das contas (gerenciadas pelo `AccountService`).

* **Receita:** Garante que uma transação de `INCOME` (receita) aumenta o saldo da conta.
    * *Função:* `test_income_transaction_updates_balance_and_listing`
* **Transferência:** Garante que uma transação de `TRANSFER` atualiza *duas* contas, debitando da origem e creditando no destino.
    * *Função:* `test_transfer_transaction_updates_both_accounts`
* **Estorno (Delete):** Garante que deletar uma transação (despesa) reverte o valor no saldo da conta, devolvendo-o a pessoa e ao seu estado original.
    * *Função:* `test_delete_transaction_reverts_account_balance`

###  Regra de Negócio: Validação de Restrições nas Regras de Negócio

Valida se os serviços aplicam corretamente as regras de negócio, bloqueando ações que violam a integridade dos dados.

* **Limite de Orçamento:** Garante que o `TransactionService` consulta o `BudgetService` e **impede** a criação de uma despesa que ultrapasse o limite do orçamento definido para o mês.
    * *Função:* `test_expense_transaction_respects_budget_limit`
* **Integridade da Conta:** Impede que o `AccountService` delete uma conta se ela possuir transações registradas.
    * *Função:* `test_delete_account_blocked_when_transactions_exist`
* **Integridade da Categoria:** Impede que o `CategoryService` delete uma categoria se ela estiver sendo usada por um `Budget`.
    * *Função:* `test_delete_category_blocked_by_budget`

### Regra de Negócio: Relatórios

Valida a capacidade do `ReportService` de consultar e agregar dados de múltiplos domínios (transações, orçamentos, categorias) em um único relatório.

* **Resumo Mensal:** Verifica se o relatório mensal combina corretamente os gastos, as receitas, as informações das categorias e os valores orçados (calculando o saldo restante do orçamento).
    * *Função:* `test_report_monthly_summary_combines_categories_and_budgets`

### Regra de Negócio: Fluxos de CRUD

Testes mais simples que validam o fluxo básico de criação e listagem de entidades através da camada de serviço.

* **Usuários:** Criação e listagem de usuários.
    * *Função:* `test_user_creation_and_listing_flow`
* **Contas:** Criação e verificação do saldo inicial.
    * *Função:* `test_account_creation_persists_starting_balance`
* **Orçamentos:** Criação e listagem de orçamentos para diferentes meses.
    * *Função:* `test_budget_creation_and_listing_flow`

---



## 4. Testes de Mutação


**Objetivo:** Introduzir mutações para os testes 1 e 2 ultilizando `mutmut` introduzindo "bugs" (mutações) no código-fonte para verificar comportamento da aplicação mediante a falhas

(ver o que colocar)

---

## 5. Testes Funcionais (Camada de API/HTTP)

**Objetivo:** Validar a camada de **HTTP** da aplicação FastAPI em `test_funcionais.py`. Estes testes verificam se a aplicação, como um todo, responde corretamente às requisições HTTP, se os *endpoints* (rotas) estão corretos e se os dados (JSON) são serializados e desserializados corretamente.


### Teste da Aplicação e Rotas

Valida a configuração básica da API, o cliente de teste e o *endpoint* de "saúde" (`health check`).

* **Fábrica de Aplicação (`app_factory`):**
    * É uma *fixture* do `pytest` que constrói a aplicação FastAPI (`create_app`) para os testes.
    * Ela usa `monkeypatch` para desativar conexões reais com o banco de dados (`mongo_manager`), garantindo que o teste seja focado apenas na camada web.
* **Verificação do Health Check:**
    * Garante que o *endpoint* `GET /api/health/` está funcionando e retorna o status `200 OK`, juntamente com os metadados corretos da aplicação (nome, ambiente).
    * *Função:* `test_health_endpoint_returns_environment_metadata`


### Teste de Fluxos HTTP (Sucesso e Erro)

Simula requisições HTTP reais (POST, GET, DELETE) e verifica se a API responde com os códigos de status e corpos JSON corretos, usando Serviços "Stub" (simulados).

* **Simulação de Sucesso (Happy Path):**
    * Substitui o `UserService` por um `SuccessfulUserService` (um dublê que sempre retorna sucesso).
    * Envia uma requisição `POST /api/users/` (para criar) e `DELETE /api/users/{id}` (para deletar).
    * Verifica se a API retorna os códigos de status corretos (`201 Created` e `204 No Content`) e se o JSON recebido está correto.
    * *Função:* `test_user_endpoints_support_post_and_delete`

* **Simulação de Erro (Não Encontrado):**
    * Substitui o `UserService` por um `NotFoundUserService` (um dublê que sempre lança `EntityNotFoundError`).
    * Envia uma requisição `GET /api/users/inexistente`.
    * Verifica se a API trata a exceção do serviço e a converte corretamente em uma resposta HTTP `404 Not Found`, contendo o JSON de erro esperado.
    * *Função:* `test_user_get_returns_404_and_error_message`

---

## 5. Testes Não-Funcionais

(ver o que colocar)