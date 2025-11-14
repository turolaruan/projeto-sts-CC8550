# Plano de Testes: Gerenciador Financeiro

Este documento descreve o plano de testes adotada para validação do projeto, detalhando os tipos de testes existentes para cada tipo.

---

## 1. Testes Unitários

**Objetivo:** Validar os componentes de **nível mais baixo** da aplicação (Modelos Pydantic, Utilitários, Exceções) de forma totalmente isolada.

**Arquivo Principal:** `test_unidade.py`

### Validação de Modelos (Pydantic)

Testa se os modelos de criação e atualização estão aplicando as regras de validação e normalização de dados corretamente.

* **Normalização de Texto:** Garante que nomes e descrições são "limpos" (sem espaços extras no início ou fim).
    * *Funções:* `test_account_create_trims_name`, `test_category_create_trims_name`, `test_user_create_trims_name`, `test_transaction_create_trims_description`.

* **Rejeição de Campos Vazios:** Garante que campos obrigatórios (como `name`) são rejeitados se estiverem em branco.
    * *Funções:* `test_account_create_rejects_blank_name`, `test_category_create_rejects_blank_name`, `test_user_update_rejects_blank_name`.

* **Consistência Financeira:** Arredonda (quantiza) valores `Decimal` para 2 casas decimais, evitando problemas de precisão.
    * *Funções:* `test_account_create_normalizes_minimum_balance`, `test_budget_create_amount_is_quantized`, `test_transaction_create_amount_quantized`.

* **Normalização de Dados:** Converte dados para um formato padrão, como emails para minúsculas.
    * *Função:* `test_user_create_lowercases_email`.

### Teste dos "Builders" (Construtores)

Valida as funções de construção (build) que transformam um *payload* de criação em um modelo maior. (Ex: um pequeno payload virar uma extrutura de dados maior contendo dados adicionais de horário, dia , atualização, etc...)

* **Geração de IDs e Timestamps:** Usando `patch` (um tipo de *mock*), simula as funções `generate_object_id` e `now_utc`.
* **Garante a Correta Construção:** Verifica se o objeto finalizado contém o ID e os timestamps `created_at` e `updated_at` corretos.
    * *Funções:* `test_build_account_generates_ids_and_timestamps`, `test_build_budget_generates_ids_and_timestamps`, `test_build_category_respects_parent_id`, `test_build_transaction_normalizes_amount_and_sets_timestamps`, `test_build_user_generates_ids_and_timestamps`.

### Teste de Utilitários

Valida as funções auxiliares encontradas em `src.models.common`.

* **Manipulação de IDs:** Testa a geração de `ObjectId` e a validação de strings de ID.
    * *Funções:* `test_generate_object_id_returns_valid_hex`, `test_ensure_object_id_valid_returns_objectid`, `test_ensure_object_id_invalid_raises_value_error`.
* **Manipulação de Datas:** Confirma que a função `now_utc` sempre retorna um *datetime* com fuso horário (timezone-aware).
    * *Função:* `test_now_utc_returns_timezone_aware_datetime`.
* **Manipulação de Strings:** Valida o utilitário de limpeza de strings.
    * *Funções:* `test_strip_and_validate_non_empty_returns_trimmed_value`, `test_strip_and_validate_non_empty_raises_for_empty_string`.

### Teste de Definições e Exceções

Garante que o mapeamento correto para os enums e as exceções estão sendo realizadas corretamente.

* **Hierarquia de Exceções:** Verifica se as exceções customizadas (ex: `EntityNotFoundError`) herdam corretamente de `AppException`.
    * *Funções:* `test_app_exception_stores_context_dict`, `test_entity_not_found_error_is_subclass_of_app_exception`.
* **Valores de Enums:** Verifica se os valores de texto dos `Enums` (ex: `AccountType.CHECKING == "checking"`) estão corretos.

---

### Validação Adicional de Modelos


**Objetivo:** Fortalecer a cobertura de validação dos modelos Pydantic em `test_models_validation.py`

* **Campos Proibidos (Extra Fields):** Garante que campos extras não permitidos causem um `ValidationError`.
    * *Função:* `test_account_create_normalizes_defaults_and_forbids_extra_fields`
* **Verificação de Construtores (Builders):** Confirma que os *builders* (ex: `build_account`) usam corretamente os campos gerados (ID, timestamps) e normalizam os dados (ex: `balance`).
    * *Funções:* `test_build_account_generates_consistent_fields`, `test_build_budget_uses_timestamp`, `test_build_transaction_preserves_optional_fields`, `test_build_user_uses_generated_fields`

---

### Testes de Lógica de Serviço (com Mocks)


**Objetivo:** Validar a **lógica interna** de *todos* os serviços em `test_services.py` (`AccountService`, `BudgetService`, `CategoryService`, `TransactionService`, `ReportService`, `UserService`) em total isolamento, simulando todas as dependências (repositórios e outros serviços) com `AsyncMock`.


* **Validação de Regras de Negócio:** Garante que as regras complexas da aplicação sejam aplicadas.
    * *Funções (Exemplos):*
        * `test_create_account_validates_starting_balance`: Impede que o saldo inicial seja menor que o mínimo.
        * `test_create_budget_requires_expense_category`: Impede a criação de orçamentos para categorias de `INCOME`.
        * `test_create_transaction_budget_limit`: Verifica se uma nova despesa ultrapassa o orçamento (`ValidationAppError`).
        * `test_create_transaction_validates_category_type`: Impede que uma transação de `EXPENSE` (despesa) seja salva em uma categoria de `INCOME` (receita).

* **Orquestração de Ações:** Verifica se os serviços chamam os *mocks* corretos na ordem correta.
    * *Funções (Exemplos):*
        * `test_create_transaction_expense_success`: Confirma que o serviço chama `transaction_repo.create` e `account_service.adjust_balance` com o valor negativo.
        * `test_delete_transaction_reverts_balance`: Confirma que `account_service.adjust_balance` é chamado com o valor *positivo* (estorno).
        * `test_monthly_summary_builds_response`: Garante que o `ReportService` chama os repositórios corretos e agrega os dados.

* **Tratamento de Erros e Exceções:** Garante que o serviço lança as exceções corretas (`EntityNotFoundError`, `ValidationAppError`) quando os *mocks* simulam uma falha.
    * *Funções (Exemplos):* `test_get_account_not_found`, `test_update_account_requires_payload`, `test_delete_account_blocks_transactions`.

---

### Testes de Serviço Focados (Validação)

**Objetivo:** Testes unitários de serviço mais focados, que validam "ramos" (branches) de validação específicos para aumentar a cobertura e a pontuação de mutação (`test_account_service.py`, `test_budget_service.py`, `test_category_service.py`, `test_transaction_service.py`, `test_user_service.py`, `test_service_with_mocks.py`).

* **Validação de Entidades (Exemplos):**
    * `test_create_account_requires_existing_user`
    * `test_create_budget_rejects_category_from_other_user`
    * `test_create_transaction_rejects_account_user_mismatch`
    * `test_create_user_rejects_duplicate_email`

* **Validação de Regras de Integridade (Exemplos):**
    * `test_delete_account_blocks_when_transactions_exist`
    * `test_delete_category_blocks_when_budget_exists`
    * `test_delete_budget_prevents_when_transactions_exist`

* **Validação de Payloads Vazios (Exemplos):**
    * `test_update_account_rejects_empty_payload`
    * `test_update_budget_rejects_empty_payload`
    * `test_update_user_rejects_empty_payload`



### Testes de Princípios de Design 


**Objetivo:** Validar que o design da aplicação segue os princípios de Orientação a Objetos (OOP) pretendidos em `test_oop_principles.py`.

* **Abstração (Contrato):** Garante que a classe base `Repository` define um "contrato" abstrato. Uma tentativa de criar uma classe (ex: `IncompleteRepository`) que não implementa todos os métodos abstratos (como `delete`) falha com um `TypeError`.
    * *Função:* `test_repository_inheritance_requires_all_abstract_methods`
* **Polimorfismo:** Prova que o `UserService` (que espera uma *abstração* `Repository`) pode funcionar com qualquer implementação *concreta* (como `InMemoryUserRepository`), demonstrando polimorfismo.
    * *Função:* `test_user_service_polymorphism_with_custom_repository`
* **Encapsulamento:** Verifica se a classe `Settings` "esconde" (encapsula) a lógica de resolução de caminhos (como `log_config_file`) do resto da aplicação.
    * *Função:* `test_settings_log_config_file_encapsulates_path_resolution`


---
## 2. Testes Estruturais

**Objetivo:** Validar a infraestrutura da aplicação FastAPI. Estes testes garantem que os componentes (como Injeção de Dependência, Controladores e Configuração) estão corretamente conectados e que o ciclo de vida da aplicação desde a inicialização até o desligamento funcionem.

### Testes da Camada de Controladores (API)


Garante que os endpoints da API (controladores em `test_controllers.py`) lidam corretamente com os roteamentos de tarefas/páginas juntamente com o tratamendo de as exceções em respostas HTTP coerentes.

* **Verificação dos Caminhos de Sucesso:** Testa se as chamadas de serviço bem-sucedidas retornam os dados corretos e os códigos de status HTTP (200 OK, 204 No Content).
    * *Funções:* `test_users_controller_success_flows`, `test_accounts_controller_success_paths`, `test_budgets_controller_success_paths`, `test_categories_controller_success_paths`, `test_transactions_controller_success_paths`, `test_reports_controller_success_and_error`, `test_health_controller_uses_settings`.
* **Tradução de Erros para HTTP:** Verifica se as exceções de negócio (ex: `EntityNotFoundError`, `ValidationAppError`, `EntityAlreadyExistsError`) lançadas pelos serviços são capturadas e convertidas nos códigos HTTP corretos (404, 400, 409).
    * *Funções:* `test_users_controller_error_branches`, `test_accounts_controller_error_paths`, `test_budgets_controller_error_paths`, `test_categories_controller_error_paths`, `test_transactions_controller_error_paths`.

### Testes da Injeção de Dependência (DI)

Validar as intruções do FastAPI em `test_service_dependencies.py`, garantindo que elas constroem e injetam corretamente os serviços e repositórios com suas próprias dependências.

* **Construção de Repositórios:** Confirma que as funções `deps.get_` e `_repository` retornam a instância correta do repositório (ex: `UserRepository`, `AccountRepository`).
    * *Função:* `test_repository_dependencies_return_instances`.
* **Construção de Serviços:** Garante que as funções `deps.get_` e `_service` recebem e conectam corretamente suas dependências (outros serviços ou repositórios).
    * *Funções:* `test_service_dependencies_wire_nested_components`, `test_user_service_dependency_returns_valid_instance`.

### Testes do Ciclo de Vida e Banco de Dados

**Arquivos Principais:** `test_app_and_config.py`, `test_database_utils.py`

Valida os eventos de startup e shutdown da aplicação, o gerenciamento da conexão com o banco de dados e a inicialização (em `test_app_and_config.py`e `test_database_utils.py`).

* **Fábrica da Aplicação (`create_app`):** Testa a função principal de criação da aplicação, verificando se ela registra as rotas e os eventos de ciclo de vida (conectar e fechar o `mongo_manager`).
    * *Função:* `test_create_app_registers_routes_and_settings`.
* **Gerenciador do Mongo:** Testa o `MongoManager` para garantir que ele gerencia corretamente o ciclo de vida do cliente (conecta, armazena em cache e fecha).
    * *Função:* `test_mongo_manager_connect_close_and_client_property`.
* **Inicialização do Banco de Dados:** Verifica se o script de setup (`ensure_indexes`) é chamado e se ele tenta criar os índices esperados nas coleções corretas.
    * *Funções:* `test_get_client_context_manager_closes_client`, `test_ensure_indexes_creates_expected_entries`, `test_initialize_database_uses_context_manager`.
* **Dependência do Banco de Dados:** Testa o *provider* `get_database` usado pelo FastAPI.
    * *Função:* `test_database_dependency_returns_manager_database`.

### Testes de Configuração e Entrypoints


Valida o carregamento das configurações (`Settings`), a configuração de logs e os pontos de entrada (entrypoints) da aplicação (como `src.main`) em `test_app_and_config.py`, `test_logging_config.py`, `test_database_utils.py`.

* **Modelo de Configurações (`Settings`):** Verifica se o modelo `Settings` carrega as variáveis de ambiente e se suas propriedades (ex: `is_production`) funcionam.
    * *Função:* `test_settings_helpers_and_properties`.
* **Configuração de Logging:** Testa a função `configure_logging`, garantindo que ela lida com arquivos de configuração ausentes (fallback) e que cria os diretórios de log necessários.
    * *Funções:* `test_configure_logging_falls_back_to_basic_config`, `test_configure_logging_creates_directories_and_applies_yaml`.
* **Pontos de Entrada (Entrypoints):** Testa os módulos `src.main` e `src.database.setup` para garantir que eles executam as funções corretas quando chamados como scripts.
    * *Funções:* `test_main_module_import_exposes_app`, `test_main_entrypoint_runs_uvicorn`.
    * *Função:* `test_setup_main_invokes_initializer`.

### Testes da Interface de Linha de Comando (CLI)

**Objetivo:** Validar a lógica estrutural, os fluxos e os *helpers* da interface de linha de comando através de `test_cli.py` (encontrada em `src.interface.cli`).


* **Simulação de Input:** Utiliza uma classe `InputFeeder` para simular a entrada de dados do usuário (teclado), permitindo testar o fluxo interativo de forma automatizada.
    * *Função:* `test_input_feeder_raises_when_empty`
* **Ciclo de Vida (Entrypoint):** Testa o ponto de entrada principal (`run`) e garante que ele orquestra corretamente o ciclo de vida dos serviços (setup e shutdown).
    * *Funções:* `test_async_main_manages_lifecycle`, `test_run_invokes_asyncio_run`, `test_setup_and_shutdown_services_use_configured_client`
* **Lógica do Menu Principal:** Verifica se o menu principal (`main_menu`) consegue despachar (rotear) para a ação correta e lidar com opções inválidas.
    * *Função:* `test_main_menu_dispatches_action_and_handles_invalid_option`
* **Validação de Fluxo (Guards):** Garante que os menus de sub-rotina (ex: registrar transação) possuem "guardas" que impedem o fluxo se as dependências (como um usuário ou conta) não existirem.
    * *Funções:* `test_register_transaction_requires_user_and_account`, `test_register_transaction_requires_account`, `test_register_transaction_requires_category`, `test_show_report_requires_user`
* **Lógica de Sub-menu:** Testa os fluxos específicos de cada tela de gerenciamento (usuários, contas, categorias, orçamentos, relatórios).
    * *Funções:* `test_manage_users_lists_and_creates_users`, `test_manage_accounts_handles_listing_and_creation`, `test_manage_categories_handles_parent_selection`, `test_manage_budgets_creates_budget`, `test_register_transaction_transfer_flow`, `test_show_report_displays_summary`

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

**Objetivo:** Medir a **eficácia** e a **qualidade** da suíte de testes existente (Testes Unitários e de Integração). O objetivo não é testar o código da aplicação, mas sim **testar os próprios testes** para encontrar "falhas" na cobertura.

**Ferramenta:** `mutmut`

**Processo:**
1.  A ferramenta `mutmut` altera sutilmente o código-fonte (ex: `src/services/transaction_service.py`), criando "mutantes" (pequenos bugs, como trocar um `>` por `<=`).
2.  Uma suíte de testes específica (`test_gerenciador.py`) é executada contra cada mutante.
3.  **Mutante Morto (Killed) :** Os testes *falham*. Isso é **bom**, pois significa que seus testes detectaram o bug.
4.  **Mutante Sobrevivente (Survived) :** Os testes *passam*. Isso é **ruim**, pois indica uma lacuna na sua suíte de testes (um bug passou despercebido).

### Suíte de Testes Alvo

**Arquivo Principal:** `test_gerenciador.py`

* **Objetivo:** validar as **regras de negócio mais críticas** (ex: limites de saldo, restrições de orçamento, validação de tipos de transação) que devem ser rigorosamente protegidas por testes em `test_gerenciador.py`.
* **Funções de Teste (Exemplos):**
    * `test_adjust_balance_respects_minimum_balance`: Garante que os testes peguem mutações na lógica de saldo mínimo.
    * `test_budget_limit_is_enforced_for_expenses`: Garante que os testes peguem mutações na lógica de limite de orçamento.
    * `test_delete_account_fails_when_transactions_exist`: Garante que os testes peguem mutações na lógica de restrição de exclusão.
    * `test_category_type_must_match_transaction_type`: Garante que os testes peguem mutações na validação de tipos de transação vs. categoria.
    * `test_transfer_requires_destination_account`: Garante que a validação de transferências seja testada.

---

## 5. Testes Funcionais (Camada de API/HTTP)

**Objetivo:** Validar a camada de **HTTP** da aplicação FastAPI. Estes testes verificam se a aplicação, como um todo, responde corretamente às requisições HTTP, se os *endpoints* (rotas) estão corretos e se os dados (JSON) são serializados e desserializados corretamente, conforme visto em `test_funcionais.py` e `test_http_controllers.py`.

**Estratégia:** Estes testes **não** usam a lógica de negócio real. Em vez disso, eles **substituem** (com `app.dependency_overrides`) os Serviços (ex: `get_user_service`) por "Stubs" ou "Mocks" (simuladores), isolando a camada da API para o teste.


### Teste da Aplicação e Rotas (Health Check)

Valida a configuração básica da API, o cliente de teste e o *endpoint* de "saúde" (`health check`) e, `test_funcionais.py`.

* **Fábrica de Aplicação (`app_factory`):**
    * É uma *fixture* do `pytest` que constrói a aplicação FastAPI (`create_app`) para os testes.
    * Ela usa `monkeypatch` para desativar conexões reais com o banco de dados (`mongo_manager`), garantindo que o teste seja focado apenas na camada web.
* **Verificação do Health Check:**
    * Garante que o *endpoint* `GET /api/health/` está funcionando e retorna o status `200 OK`, juntamente com os metadados corretos da aplicação (nome, ambiente).
    * *Função:* `test_health_endpoint_returns_environment_metadata`

### Teste de Fluxos HTTP (Stubs)

Simula requisições HTTP reais em `test_funcionais.py` (POST, GET, DELETE) e verifica se a API responde com os códigos de status e corpos JSON corretos, usando serviços simulados (Stubs).

* **Simulação de Sucesso (Caminho feliz):**
    * Substitui o `UserService` por um `SuccessfulUserService` (um dublê que sempre retorna sucesso).
    * Envia uma requisição `POST /api/users/` (para criar) e `DELETE /api/users/{id}` (para deletar).
    * Verifica se a API retorna os códigos de status corretos (`201 Created` e `204 No Content`) e se o JSON recebido está correto.
    * *Função:* `test_user_endpoints_support_post_and_delete`

* **Simulação de Erro (Não Encontrado):**
    * Substitui o `UserService` por um `NotFoundUserService` (um dublê que sempre lança `EntityNotFoundError`).
    * Envia uma requisição `GET /api/users/inexistente`.
    * Verifica se a API trata a exceção do serviço e a converte corretamente em uma resposta HTTP `404 Not Found`, contendo o JSON de erro esperado.
    * *Função:* `test_user_get_returns_404_and_error_message`

### Teste de Controladores HTTP (Mocks)

Valida módulos de controladores individuais em `test_http_controllers.py` (ex: `accounts_ctrl`, `transactions_ctrl`) criando uma aplicação FastAPI mínima e injetando *mocks* (`SimpleNamespace`).

* **Verificação de Serialização (Payload):** Garante que um payload JSON enviado (`POST /accounts/`) é recebido, deserializado e repassado corretamente ao *mock* do serviço.
    * *Função:* `test_accounts_create_http_success`
* **Verificação de Serialização (Query Params):** Garante que os parâmetros de query (filtros) em uma requisição `GET /transactions/` sejam corretamente recebidos e repassados ao *mock* do serviço.
    * *Função:* `test_transactions_list_http_applies_filters`
* **Tradução de Erros 400 (Validation):** Verifica se um `ValidationAppError` lançado pelo *mock* do serviço é traduzido em uma resposta HTTP `400 Bad Request`.
    * *Função:* `test_accounts_create_http_validation_error`
* **Tradução de Erros 404 (Not Found):** Verifica se um `EntityNotFoundError` lançado pelo *mock* do serviço é traduzido em uma resposta HTTP `404 Not Found`.
    * *Funções:* `test_accounts_get_http_not_found`, `test_transactions_delete_http_not_found`

---

## 6. Testes Não-Funcionais

**Objetivo:** Validar aspectos de qualidade da aplicação que não estão ligados à regra de negócio, como desempenho e escalabilidade.

### Testes de Performance (Benchmark)

**Objetivo:** Medir o desempenho em `test_user_service_benchmark.py` de operações específicas sob uma carga simulada para detectar regressões (perda de performance) ao longo do tempo.


* **Ferramenta:** `pytest-benchmark`
* **Estratégia:**
    * Um repositório "Stub" (`LargeDatasetRepository`) é criado para simular um banco de dados contendo um grande volume de dados (ex: 5000 usuários).
    * O `pytest-benchmark` executa a função de serviço (ex: `service.list_users()`) múltiplas vezes para medir o tempo médio de execução.
* **Funções de Teste:**
    * `test_list_users_performance_with_large_volume`: Faz o benchmark do `UserService.list_users` com 5000 usuários para garantir que a listagem de dados em larga escala permaneça eficiente.

---