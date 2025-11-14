# Relatório de Testes

## Link do repositório: https://github.com/turolaruan/projeto-sts-CC8550

## Testes Unitários

### Escopo e abordagem

- `tests/unit/test_account_service.py`: cobre criação/remoção e leitura de contas, validando mensagens de erro para usuários inexistentes, filtros por proprietário e atualizações parciais.
- `tests/unit/test_budget_service.py`: garante regras de período, sobreposição e alertas de orçamento, além de validar operações auxiliares como `apply_expense`, `get_budget_for`, `summarize` e exclusão segura.
- `tests/unit/test_goal_service.py`: exercita fluxo completo de metas (criação, contribuições com/sem bloqueio, conclusão automática, remoção e validações de consistência entre usuário e conta).
- `tests/unit/test_transaction_service.py`: valida cenários isolados de criação de transações (receitas/despesas), checagem de budgets, filtros de busca, atualizações e remoção, usando repositórios em memória.
- `tests/unit/test_user_service.py`: cobre CRUD de usuários, tratamento de e-mails duplicados e remoção segura.
- Demais suites complementares (`test_file_manager`, `test_models_oop`, `test_report_service`, `test_services_with_mocks`, `test_settings`) validam utilitários isolados, serialização e integração com dependências mockadas.

### Quantitativo

| Métrica | Valor |
| --- | --- |
| Casos unitários coletados | **69** |
| Arquivos exercitados | 11 |
| Linhas de teste executadas | 69 (todas passaram) |

### Resultado da execução

Trecho relevante do `pytest` (modo estrito do `pytest-asyncio` em Python 3.10):

```
=============================================================================================== test session starts ===============================================================================================
platform linux -- Python 3.10.12, pytest-8.2.2, pluggy-1.6.0 -- /home/ruan/Documentos/FEI/8_Semestre/projeto-sts-CC8550/.venv/bin/python3
cachedir: .pytest_cache
benchmark: 4.0.0 (defaults: timer=time.perf_counter disable_gc=False min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
rootdir: /home/ruan/Documentos/FEI/8_Semestre/projeto-sts-CC8550
configfile: pytest.ini
plugins: cov-5.0.0, anyio-4.11.0, benchmark-4.0.0, asyncio-0.23.6
asyncio: mode=strict
collected 69 items                                                                                                                                                                                                

tests/unit/test_account_service.py::TestAccountService::test_create_account_missing_user_raises PASSED                                                                                                      [  1%]
tests/unit/test_account_service.py::TestAccountService::test_create_account_requires_existing_user PASSED                                                                                                   [  2%]
tests/unit/test_account_service.py::TestAccountService::test_delete_account_missing_raises PASSED                                                                                                           [  4%]
tests/unit/test_account_service.py::TestAccountService::test_delete_account_removes_entry PASSED                                                                                                            [  5%]
tests/unit/test_account_service.py::TestAccountService::test_get_account_missing_raises PASSED                                                                                                              [  7%]
tests/unit/test_account_service.py::TestAccountService::test_get_account_returns_entry PASSED                                                                                                               [  8%]
tests/unit/test_account_service.py::TestAccountService::test_list_accounts_returns_only_user_entries PASSED                                                                                                 [ 10%]
tests/unit/test_account_service.py::TestAccountService::test_update_account_success PASSED                                                                                                                  [ 11%]
tests/unit/test_account_service.py::TestAccountService::test_update_nonexistent_account_raises PASSED                                                                                                       [ 13%]
tests/unit/test_budget_service.py::TestBudgetService::test_apply_expense_beyond_limit_raises PASSED                                                                                                         [ 14%]
tests/unit/test_budget_service.py::TestBudgetService::test_apply_expense_within_limit_updates_spent PASSED                                                                                                  [ 15%]
tests/unit/test_budget_service.py::TestBudgetService::test_create_budget_invalid_period_raises PASSED                                                                                                       [ 17%]
tests/unit/test_budget_service.py::TestBudgetService::test_create_budget_rejects_overlapping_periods PASSED                                                                                                 [ 18%]
tests/unit/test_budget_service.py::TestBudgetService::test_delete_budget_missing_raises PASSED                                                                                                              [ 20%]
tests/unit/test_budget_service.py::TestBudgetService::test_delete_budget_returns_true PASSED                                                                                                                [ 21%]
tests/unit/test_budget_service.py::TestBudgetService::test_get_budget_for_returns_matching_period PASSED                                                                                                    [ 23%]
tests/unit/test_budget_service.py::TestBudgetService::test_get_budget_returns_entry PASSED                                                                                                                  [ 24%]
tests/unit/test_budget_service.py::TestBudgetService::test_get_missing_budget_raises PASSED                                                                                                                 [ 26%]
tests/unit/test_budget_service.py::TestBudgetService::test_list_budgets_returns_all_for_user PASSED                                                                                                         [ 27%]
tests/unit/test_budget_service.py::TestBudgetService::test_summarize_returns_budget_status PASSED                                                                                                           [ 28%]
tests/unit/test_budget_service.py::TestBudgetService::test_summarize_returns_budget_summary PASSED                                                                                                          [ 30%]
tests/unit/test_budget_service.py::TestBudgetService::test_update_budget_changes_limit PASSED                                                                                                               [ 31%]
tests/unit/test_budget_service.py::TestBudgetService::test_update_budget_missing_raises PASSED                                                                                                              [ 33%]
tests/unit/test_file_manager.py::TestFileManager::test_export_transactions_creates_csv PASSED                                                                                                               [ 34%]
tests/unit/test_goal_service.py::TestGoalService::test_apply_contribution_completes_goal PASSED                                                                                                             [ 36%]
tests/unit/test_goal_service.py::TestGoalService::test_apply_contribution_missing_account PASSED                                                                                                            [ 37%]
tests/unit/test_goal_service.py::TestGoalService::test_apply_contribution_respects_locked_amount PASSED                                                                                                     [ 39%]
tests/unit/test_goal_service.py::TestGoalService::test_apply_contribution_with_lock_releases_funds PASSED                                                                                                   [ 40%]
tests/unit/test_goal_service.py::TestGoalService::test_create_goal_requires_existing_account PASSED                                                                                                         [ 42%]
tests/unit/test_goal_service.py::TestGoalService::test_create_goal_with_mismatched_user_raises PASSED                                                                                                       [ 43%]
tests/unit/test_goal_service.py::TestGoalService::test_create_goal_without_account_raises PASSED                                                                                                            [ 44%]
tests/unit/test_goal_service.py::TestGoalService::test_delete_goal_missing_raises PASSED                                                                                                                    [ 46%]
tests/unit/test_goal_service.py::TestGoalService::test_delete_goal_releases_locked_amount PASSED                                                                                                            [ 47%]
tests/unit/test_goal_service.py::TestGoalService::test_get_goal_missing_raises PASSED                                                                                                                       [ 49%]
tests/unit/test_goal_service.py::TestGoalService::test_list_goals_returns_user_entries PASSED                                                                                                               [ 50%]
tests/unit/test_goal_service.py::TestGoalService::test_update_goal_changes_name PASSED                                                                                                                      [ 52%]
tests/unit/test_goal_service.py::TestGoalService::test_update_goal_missing_raises PASSED                                                                                                                    [ 53%]
tests/unit/test_models_oop.py::TestModelsOOP::test_budget_model_status_property_uses_polymorphism PASSED                                                                                                    [ 55%]
tests/unit/test_models_oop.py::TestModelsOOP::test_budget_summary_derives_remaining_amount PASSED                                                                                                           [ 56%]
tests/unit/test_models_oop.py::TestModelsOOP::test_goal_model_completes_when_target_reached PASSED                                                                                                          [ 57%]
tests/unit/test_report_service.py::TestReportService::test_report_service_exports_transactions PASSED                                                                                                       [ 59%]
tests/unit/test_services_with_mocks.py::TestServicesWithMocks::test_report_service_handles_file_manager_failure PASSED                                                                                      [ 60%]
tests/unit/test_services_with_mocks.py::TestServicesWithMocks::test_report_service_uses_file_manager PASSED                                                                                                 [ 62%]
tests/unit/test_services_with_mocks.py::TestServicesWithMocks::test_transaction_service_handles_repository_errors_with_mock PASSED                                                                          [ 63%]
tests/unit/test_services_with_mocks.py::TestServicesWithMocks::test_transaction_service_propagates_goal_service_errors PASSED                                                                               [ 65%]
tests/unit/test_settings.py::TestSettings::test_settings_reads_env PASSED                                                                                                                                   [ 66%]
tests/unit/test_transaction_service.py::TestTransactionService::test_create_expense_with_locked_funds_raises PASSED                                                                                         [ 68%]
tests/unit/test_transaction_service.py::TestTransactionService::test_create_transaction_missing_user_raises PASSED                                                                                          [ 69%]
tests/unit/test_transaction_service.py::TestTransactionService::test_create_transaction_updates_balance_and_budget PASSED                                                                                   [ 71%]
tests/unit/test_transaction_service.py::TestTransactionService::test_delete_transaction_missing_raises PASSED                                                                                               [ 72%]
tests/unit/test_transaction_service.py::TestTransactionService::test_delete_transaction_removes_entry PASSED                                                                                                [ 73%]
tests/unit/test_transaction_service.py::TestTransactionService::test_get_budget_helper_returns_none_for_income PASSED                                                                                       [ 75%]
tests/unit/test_transaction_service.py::TestTransactionService::test_get_budget_helper_skips_when_requested PASSED                                                                                          [ 76%]
tests/unit/test_transaction_service.py::TestTransactionService::test_get_transaction_missing_raises PASSED                                                                                                  [ 78%]
tests/unit/test_transaction_service.py::TestTransactionService::test_get_transaction_returns_entry PASSED                                                                                                   [ 79%]
tests/unit/test_transaction_service.py::TestTransactionService::test_income_transaction_increases_balance PASSED                                                                                            [ 81%]
tests/unit/test_transaction_service.py::TestTransactionService::test_list_transactions_returns_entries PASSED                                                                                               [ 82%]
tests/unit/test_transaction_service.py::TestTransactionService::test_search_transactions_filters_by_category PASSED                                                                                         [ 84%]
tests/unit/test_transaction_service.py::TestTransactionService::test_update_transaction_changes_description PASSED                                                                                          [ 85%]
tests/unit/test_transaction_service.py::TestTransactionService::test_update_transaction_missing_raises PASSED                                                                                               [ 86%]
tests/unit/test_user_service.py::TestUserService::test_create_user_persists_and_returns_user PASSED                                                                                                         [ 88%]
tests/unit/test_user_service.py::TestUserService::test_create_user_with_duplicate_email_raises PASSED                                                                                                       [ 89%]
tests/unit/test_user_service.py::TestUserService::test_delete_user_missing_raises PASSED                                                                                                                    [ 91%]
tests/unit/test_user_service.py::TestUserService::test_delete_user_removes_entry PASSED                                                                                                                     [ 92%]
tests/unit/test_user_service.py::TestUserService::test_get_user_returns_entry PASSED                                                                                                                        [ 94%]
tests/unit/test_user_service.py::TestUserService::test_get_user_with_invalid_id_raises PASSED                                                                                                               [ 95%]
tests/unit/test_user_service.py::TestUserService::test_list_users_returns_all PASSED                                                                                                                        [ 97%]
tests/unit/test_user_service.py::TestUserService::test_update_user_changes_fields PASSED                                                                                                                    [ 98%]
tests/unit/test_user_service.py::TestUserService::test_update_user_not_found_raises PASSED                                                                                                                  [100%]

=============================================================================================== 69 passed in 0.23s ================================================================================================

```

A suíte unitária roda em ~0.23 s e não apresentou falhas. Os testes estão organizados por classe/método para isolar regras de negócio específicas, garantindo feedback rápido antes de executar suites mais pesadas (funcionais, integração, etc.).

## Testes de Integração

### Escopo e abordagem

- `tests/integration/test_integracao.py` valida fluxos ponta a ponta usando o app FastAPI real com dependências trocadas por repositórios em memória, exercitando rotas HTTP.
- Cenários contemplam interações entre controladores/serviços/repositórios e regras de banco de dados (como sums/locks simulados): criação/atualização de usuários e contas, budgets com detecção de sobreposição, buscas paginadas de transações e relatórios CSV.
- Fluxos completos de metas e transações (com e sem objetivos, e com bloqueio de saldo) garantem que ajustes em contas e budgets aconteçam de forma coordenada.
- Endpoints críticos (DELETE, PUT, GET com filtros) são validados com respostas HTTP específicas (204, 404, 409) garantindo aderência aos contratos REST e ao schema persistido.

### Quantitativo

| Métrica | Valor |
| --- | --- |
| Casos de integração coletados | **12** |
| Endpoints cobertos | `/users`, `/accounts`, `/budgets`, `/transactions`, `/goals`, `/reports` |
| Tempo médio de execução | 0.38 s |

### Resultado da execução

```
=============================================================================================== test session starts ===============================================================================================
platform linux -- Python 3.10.12, pytest-8.2.2, pluggy-1.6.0 -- /home/ruan/Documentos/FEI/8_Semestre/projeto-sts-CC8550/.venv/bin/python3
cachedir: .pytest_cache
benchmark: 4.0.0 (defaults: timer=time.perf_counter disable_gc=False min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
rootdir: /home/ruan/Documentos/FEI/8_Semestre/projeto-sts-CC8550
configfile: pytest.ini
plugins: cov-5.0.0, anyio-4.11.0, benchmark-4.0.0, asyncio-0.23.6
asyncio: mode=strict
collected 12 items                                                                                                                                                                                                

tests/integration/test_integracao.py::TestIntegrationFlows::test_account_delete_endpoint_removes_account PASSED                                                                                             [  8%]
tests/integration/test_integracao.py::TestIntegrationFlows::test_budget_creation_overlap_returns_conflict PASSED                                                                                            [ 16%]
tests/integration/test_integracao.py::TestIntegrationFlows::test_budget_summary_endpoint PASSED                                                                                                             [ 25%]
tests/integration/test_integracao.py::TestIntegrationFlows::test_get_missing_user_returns_404_with_json PASSED                                                                                              [ 33%]
tests/integration/test_integracao.py::TestIntegrationFlows::test_goal_contribution_flow PASSED                                                                                                              [ 41%]
tests/integration/test_integracao.py::TestIntegrationFlows::test_goal_delete_releases_locked_amount PASSED                                                                                                  [ 50%]
tests/integration/test_integracao.py::TestIntegrationFlows::test_report_endpoint_generates_payload PASSED                                                                                                   [ 58%]
tests/integration/test_integracao.py::TestIntegrationFlows::test_transaction_search_returns_inserted_items PASSED                                                                                           [ 66%]
tests/integration/test_integracao.py::TestIntegrationFlows::test_transaction_with_goal_wrong_type_returns_conflict PASSED                                                                                   [ 75%]
tests/integration/test_integracao.py::TestIntegrationFlows::test_update_nonexistent_account_returns_404 PASSED                                                                                              [ 83%]
tests/integration/test_integracao.py::TestIntegrationFlows::test_user_and_account_flow PASSED                                                                                                               [ 91%]
tests/integration/test_integracao.py::TestIntegrationFlows::test_user_update_endpoint PASSED                                                                                                                [100%]

=============================================================================================== 12 passed in 0.38s ================================================================================================

```

Os testes demonstram que os fluxos completos – desde criação de usuário até geração de relatório – funcionam com os repositórios reais (Motor/Mongo substituído por memória), garantindo que camadas conversem corretamente antes de subir ambientes com banco externo.

## Testes Funcionais (Caixa-Preta)

### Escopo e abordagem

- `tests/functional/test_funcionais.py` trata o sistema como uma “caixa-preta”: cada caso prepara apenas as entradas/requests HTTP e valida as saídas esperadas (status code, payloads e efeitos em recursos).
- Focamos em validar regras de negócio e aceitação do usuário: limites de orçamento, validações de valores negativos, fluxo completo de metas, relatórios com totais corretos e geração de arquivos, além de mensagens de erro 4xx.
- O ambiente utiliza o app FastAPI real com dependências trocadas por repositórios em memória, simulando integrações com banco sem depender de infraestrutura externa.

### Cenários exercitados

| CT | Cenário / Entrada | Saída esperada | Aprovado/Reprovado |
| --- | --- | --- | --- |
| CT01 | Criar conta apontando para `user_id` inexistente. | POST `/accounts` responde 404 com detalhe “User not found for account creation”. | Aprovado |
| CT02 | Usuário com orçamento mensal tenta registrar despesa que ultrapassa o limite. | Primeira despesa aceita (201), segunda retorna 409 contendo “Budget…”. | Aprovado |
| CT03 | Buscar transações aplicando faixa de valores (min=100, max=200). | GET `/transactions/search` devolve apenas lançamentos dentro da faixa (lista de 1 item). | Aprovado |
| CT04 | Registrar transação com valor negativo. | POST `/transactions` rejeita com 422 (validação). | Aprovado |
| CT05 | Contribuir em uma meta até atingir o alvo. | GET `/goals/{id}` retorna `status=completed` após contribuições. | Aprovado |
| CT06 | Gastar 90% do orçamento de comida. | `/budgets/summary/{user}` apresenta status `warning`/`exceeded`. | Aprovado |
| CT07 | Solicitar exportação de relatório. | GET `/reports/transactions/{user}` devolve 200 com caminho `.csv` e totalizações. | Aprovado |
| CT08 | Conferir totais do relatório com lançamentos existentes. | Campos `total_expenses` e `total_income` batem com os lançamentos criados. | Aprovado |

### Quantitativo

| Métrica | Valor |
| --- | --- |
| Casos funcionais coletados | **8** |
| Foco | Entradas/saídas (HTTP) e aceitação das regras de negócio |
| Tempo médio de execução | 0.31 s |

### Resultado da execução

```
=============================================================================================== test session starts ===============================================================================================
platform linux -- Python 3.10.12, pytest-8.2.2, pluggy-1.6.0 -- /home/ruan/Documentos/FEI/8_Semestre/projeto-sts-CC8550/.venv/bin/python3
cachedir: .pytest_cache
benchmark: 4.0.0 (defaults: timer=time.perf_counter disable_gc=False min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
rootdir: /home/ruan/Documentos/FEI/8_Semestre/projeto-sts-CC8550
configfile: pytest.ini
plugins: cov-5.0.0, anyio-4.11.0, benchmark-4.0.0, asyncio-0.23.6
asyncio: mode=strict
collected 8 items                                                                                                                                                                                                 

tests/functional/test_funcionais.py::TestFunctionalScenarios::test_account_creation_with_invalid_user_returns_404 PASSED                                                                                    [ 12%]
tests/functional/test_funcionais.py::TestFunctionalScenarios::test_budget_status_reaches_warning PASSED                                                                                                     [ 25%]
tests/functional/test_funcionais.py::TestFunctionalScenarios::test_goal_completion_flow PASSED                                                                                                              [ 37%]
tests/functional/test_funcionais.py::TestFunctionalScenarios::test_report_generation_returns_file PASSED                                                                                                    [ 50%]
tests/functional/test_funcionais.py::TestFunctionalScenarios::test_report_totals_match_transactions PASSED                                                                                                  [ 62%]
tests/functional/test_funcionais.py::TestFunctionalScenarios::test_transaction_negative_amount_validation PASSED                                                                                            [ 75%]
tests/functional/test_funcionais.py::TestFunctionalScenarios::test_transaction_search_with_amount_filters PASSED                                                                                            [ 87%]
tests/functional/test_funcionais.py::TestFunctionalScenarios::test_user_cannot_exceed_budget PASSED                                                                                                         [100%]

================================================================================================ 8 passed in 0.31s ================================================================================================
```

A suíte garante que as principais funcionalidades observáveis pelo usuário final respondem com os códigos HTTP esperados e respeitam as regras descritas nos requisitos.

### Cobertura e relatórios

- Comando executado: `pytest --cov=src --cov-report=term --cov-report=html`.
- Resultado agregado: **91 %** de cobertura de código (acima do mínimo de 80 %), incluindo branches críticos nos controllers/serviços exercitados pelos cenários de negócio.
- Relatório navegável disponível em `htmlcov/index.html`, utilizado para inspecionar linhas/branches faltantes e priorizar novos testes (estruturais e unitários) para fechar lacunas nos repositórios.

## Testes Estruturais (Caixa-Branca)

### Escopo e abordagem

- Suites `tests/structural/` examinam internamente providers, repositórios, utils e versionamento, utilizando fakes para simular o MongoDB e garantir execução de todos os ramos (create/list/update/delete, filtros, agregações e exceções).
- Foco em cobertura de branches: `TransactionRepository.search/total_by_type`, helpers de serialização, cache do cliente Mongo, configuração de logger e resolução de dependências (`get_*_service`).
- Relatórios de cobertura: `pytest --cov=src --cov-report=term --cov-report=html` (mesmo comando das outras suites), assegurando ≥80 % e disponibilizando inspeção via `htmlcov/index.html`.

### Quantitativo

| Métrica | Valor |
| --- | --- |
| Casos estruturais coletados | **15** |
| Módulos englobados | Dependências, repositórios, utils e versionamento |
| Tempo médio de execução | 0.09 s |

### Resultado da execução

```
c=============================================================================================== test session starts ===============================================================================================
platform linux -- Python 3.10.12, pytest-8.2.2, pluggy-1.6.0 -- /home/ruan/Documentos/FEI/8_Semestre/projeto-sts-CC8550/.venv/bin/python3
cachedir: .pytest_cache
benchmark: 4.0.0 (defaults: timer=time.perf_counter disable_gc=False min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
rootdir: /home/ruan/Documentos/FEI/8_Semestre/projeto-sts-CC8550
configfile: pytest.ini
plugins: cov-5.0.0, anyio-4.11.0, benchmark-4.0.0, asyncio-0.23.6
asyncio: mode=strict
collected 15 items                                                                                                                                                                                                

tests/structural/test_dependencies.py::TestDependencyProviders::test_report_service_builds_file_manager PASSED                                                                                              [  6%]
tests/structural/test_dependencies.py::TestDependencyProviders::test_repository_providers_use_database_dependency PASSED                                                                                    [ 13%]
tests/structural/test_dependencies.py::TestDependencyProviders::test_service_providers_bind_dependencies PASSED                                                                                             [ 20%]
tests/structural/test_repositories.py::TestAbstractRepository::test_create_and_get_by_id PASSED                                                                                                             [ 26%]
tests/structural/test_repositories.py::TestAbstractRepository::test_list_filters_and_exists PASSED                                                                                                          [ 33%]
tests/structural/test_repositories.py::TestAbstractRepository::test_update_and_delete PASSED                                                                                                                [ 40%]
tests/structural/test_repositories.py::TestTransactionRepository::test_search_applies_filters_and_sorting PASSED                                                                                            [ 46%]
tests/structural/test_repositories.py::TestTransactionRepository::test_total_by_type_aggregates_values PASSED                                                                                               [ 53%]
tests/structural/test_utils.py::TestDatabaseHelpers::test_get_client_is_cached PASSED                                                                                                                       [ 60%]
tests/structural/test_utils.py::TestDatabaseHelpers::test_get_database_returns_named_database PASSED                                                                                                        [ 66%]
tests/structural/test_utils.py::TestSerializerHelpers::test_serialize_document_converts_object_ids PASSED                                                                                                   [ 73%]
tests/structural/test_utils.py::TestLoggerConfiguration::test_logger_configures_once_and_binds_name PASSED                                                                                                  [ 80%]
tests/structural/test_version_module.py::TestVersionAccess::test_returns_default_when_package_missing PASSED                                                                                                [ 86%]
tests/structural/test_version_module.py::TestVersionAccess::test_returns_installed_version PASSED                                                                                                           [ 93%]
tests/structural/test_version_module.py::TestVersionAccess::test_unknown_attribute_raises PASSED                                                                                                            [100%]

=============================================================================================== 15 passed in 0.09s ================================================================================================

```

Esses testes exercitam explicitamente ramos internos, garantindo que métodos de infraestrutura se comportem corretamente antes de serem usados por serviços/rotas.

### Cobertura e relatórios

- Comando: `pytest --cov=src --cov-report=term --cov-report=html`.
- Cobertura global: **91 %** (linhas + branches), superando o mínimo de 80 %. O relatório HTML (`htmlcov/index.html`) evidencia que os ramos críticos dos repositórios/utilitários foram exercitados e sinaliza apenas trechos residuais (principalmente budgets/goals) para futuras iterações.

```
Name                                                     Stmts   Miss Branch BrPart  Cover   Missing
----------------------------------------------------------------------------------------------------
src/__init__.py                                              9      0      2      0   100%
src/controllers/__init__.py                                 10      0      0      0   100%
src/controllers/accounts.py                                 22      0      0      0   100%
src/controllers/budgets.py                                  25      5      0      0    80%   32, 39, 50, 60-61
src/controllers/dependencies.py                             32      0      0      0   100%
src/controllers/goals.py                                    22      2      0      0    91%   32, 50
src/controllers/reports.py                                   9      0      0      0   100%
src/controllers/transactions.py                             28      5      0      0    82%   40, 79, 90, 100-101
src/controllers/users.py                                    22      3      0      0    86%   29, 54-55
src/main.py                                                 33      5      0      0    85%   23-25, 46, 50
src/models/__init__.py                                       4      0      0      0   100%
src/models/entities.py                                      82      0      4      0   100%
src/models/enums.py                                         18      0      0      0   100%
src/models/schemas.py                                       64      0      0      0   100%
src/repositories/__init__.py                                 7      0      0      0   100%
src/repositories/accounts.py                                18      7      0      0    61%   22, 27-32, 37-42
src/repositories/base.py                                    43      2      0      0    95%   71-73
src/repositories/budgets.py                                 22     10      0      0    55%   22-30, 35-40, 45-47, 61-78
src/repositories/goals.py                                   23     10      0      0    57%   23-28, 33-38, 43-44, 49-50
src/repositories/transactions.py                            39      0     18      8    86%   25->31, 27->29, 29->31, 31->33, 33->39, 35->37, 37->39, 39->41
src/repositories/users.py                                   11      2      0      0    82%   22-23
src/services/__init__.py                                     8      0      0      0   100%
src/services/accounts.py                                    32      0      8      0   100%
src/services/budgets.py                                     44      0     12      0   100%
src/services/exceptions.py                                   4      0      0      0   100%
src/services/goals.py                                       56      0     22      1    99%   59->61
src/services/reports.py                                     11      0      0      0   100%
src/services/transactions.py                                68      2     30      2    96%   47, 49
src/services/users.py                                       31      0      8      0   100%
src/utils/__init__.py                                        5      0      0      0   100%
src/utils/database.py                                       12      0      0      0   100%
src/utils/file_manager.py                                   26      0      4      0   100%
src/utils/logger.py                                         19      0      2      0   100%
src/utils/serializers.py                                    11      0      6      1    94%   14->16
tests/__init__.py                                           97     77     14      2    22%   17-20, 26, 32-111, 122-142
tests/conftest.py                                           60     14      0      0    77%   65, 73, 108-109, 121-128, 133-134
tests/fixtures/__init__.py                                   1      0      0      0   100%
tests/fixtures/factories.py                                 51      0      0      0   100%
tests/fixtures/memory_repositories.py                      126     21     54     13    78%   31, 41, 64, 72->71, 86, 92, 112, 120, 136, 139-140, 149, 155, 160, 174, 180, 185-190
tests/functional/__init__.py                                 0      0      0      0   100%
tests/functional/test_funcionais.py                        126      0      2      0   100%
tests/integration/__init__.py                                0      0      0      0   100%
tests/integration/test_integracao.py                       150      0      0      0   100%
tests/mutation/test_mutacao.py                              52      0      0      0   100%
tests/mutation/test_mutmut_guard.py                          6      1      2      1    75%   14
tests/performance/test_transaction_search_benchmark.py      14      0      2      0   100%
tests/structural/__init__.py                                 0      0      0      0   100%
tests/structural/test_dependencies.py                       51      0      2      0   100%
tests/structural/test_repositories.py                      153      5     28      6    94%   56, 62, 70, 87, 100, 123->125
tests/structural/test_utils.py                              52      0      0      0   100%
tests/structural/test_version_module.py                     24      0      0      0   100%
tests/test_discovery.py                                     13      7      4      0    35%   15-23
tests/unit/test_account_service.py                          58      0      4      0   100%
tests/unit/test_budget_service.py                           85      0      6      0   100%
tests/unit/test_file_manager.py                             20      0      2      0   100%
tests/unit/test_goal_service.py                             86      0      4      0   100%
tests/unit/test_models_oop.py                               20      0      2      0   100%
tests/unit/test_report_service.py                           24      0      2      0   100%
tests/unit/test_services_with_mocks.py                      63      0      0      0   100%
tests/unit/test_settings.py                                 18      0      2      0   100%
tests/unit/test_transaction_service.py                      93      0      4      0   100%
tests/unit/test_user_service.py                             53      0      4      0   100%
----------------------------------------------------------------------------------------------------
TOTAL                                                     2366    178    254     34    91%

```

## Testes Específicos por Tipo

### Testes de API/REST

- `tests/functional/test_funcionais.py` e `tests/integration/test_integracao.py` realizam chamadas HTTP reais (via `httpx.ASGITransport`) contra as rotas FastAPI (`/users`, `/accounts`, `/budgets`, `/transactions`, `/goals`, `/reports`).
- Cada cenário valida códigos 2xx/4xx apropriados e o payload retornado, garantindo conformidade com o contrato REST exposto ao usuário final.

### Testes de Exceções

- Suites unitárias de serviços (`test_account_service`, `test_budget_service`, `test_goal_service`, `test_transaction_service`, `test_user_service`) verificam `NotFoundError`, `BusinessRuleError` e `ValidationError`.
- `tests/structural/test_dependencies.py` e `tests/structural/test_utils.py` asseguram que a infraestrutura (providers/logger/serializers) propaga exceções com mensagens adequadas.

### Testes com Mocks e Stubs

- `tests/unit/test_services_with_mocks.py` usa `MagicMock/AsyncMock` para simular repositórios e observar `TransactionService`/`ReportService` em isolamento.
- `tests/fixtures/memory_repositories.py` atua como camada stub para MongoDB, permitindo que suites funcionais/integradas controlem os dados sem depender de I/O real.

### Testes de Performance/Carga

- Arquivo: `tests/performance/test_transaction_search_benchmark.py`.
- Resultado (benchmark do `pytest-benchmark`):

```
test_transaction_search_benchmark  mean 531 µs (OPS ≈ 1.88 Kops/s, 1 130 rounds, 1.62 s totais)
```

- O teste mede a busca filtrada de transações após inserir 200 registros sintéticos, monitorando regressões de latência.

### Testes de Orientação a Objetos

- `tests/unit/test_models_oop.py` valida propriedades derivadas (`BudgetModel.status`, `GoalModel` completando ao atingir a meta) e comportamentos polimórficos.
- `tests/unit/test_goal_service.py` e `tests/unit/test_transaction_service.py` exercitam colaboração entre objetos (serviços → repositórios → modelos), garantindo encapsulamentos e invariantes de domínio.

## Testes de Mutação (Mutmut)

### Visão geral

- **Ferramenta:** `mutmut 2.4.0`
- **Módulos-alvo:** `src/services/accounts.py`, `src/services/budgets.py`, `src/services/transactions.py`
- **Execução:** `mutmut run --runner "python3 -m pytest tests/mutation"`

### Métricas

| Métrica | Valor |
| --- | --- |
| Mutantes gerados | **81** |
| Mutantes mortos 🎉 | **58** |
| Mutantes sobreviventes 🙁 | **23** |
| Mutation score (inicial/final) | **71.6 %** |

### Cobertura por módulo

| Módulo | Situação | Comentário |
| --- | --- | --- |
| `src/services/accounts.py` | 0 sobreviventes | Validação de donos de contas e erros 404 matou todos mutantes deste módulo. |
| `src/services/budgets.py` | 7 sobreviventes | Condições de período e mensagens de excesso de limite ainda possuem lacunas de teste. |
| `src/services/transactions.py` | 16 sobreviventes | Fluxos de contribuição para metas e validações de categoria/balanço carecem de cenários direcionados. |

### Tipos de mutantes sobreviventes

1. **Lógica/contorno (7 mutantes)** — Exemplos:
   - ID 36 (`BudgetService._validate_period`): o mutante substituiu `>=` por `>`, permitindo orçamentos com `start == end`.
   - IDs 54/62/69 (`TransactionService`): faltam testes para contribuições em metas e para categorias vazias.
   - ID 57 (`TransactionService`): ausência de caso onde o saldo disponível é exatamente igual ao valor da transação.
   - IDs 34/35 (`BudgetService`): mutantes alteraram a fórmula do erro de limite excedido sem que houvesse assert na mensagem.

2. **Exceções com mensagens ignoradas (16 mutantes)** — IDs 8, 13, 16, 19, 23, 28, 31, 37, 45, 48, 50, 58, 65, 73, 78, 81. Todos alteram apenas o texto de `NotFoundError`/`BusinessRuleError` em services de contas, budgets e transações. Como os testes verificam somente o tipo da exceção via `assertRaises`, a alteração passa despercebida.

### Quantidade de testes de mutação

- `mutmut` executou os 81 cenários automaticamente; não há “testes manuais” adicionais além da suíte apontada pelo runner.

### Resultado do comando

```
-- summary --
tool: mutmut
total: 81
killed: 58
survived: 23
score: 71.6 %
```

### Justificativas e próximos passos

- **Categoria lógica:** requer criação de novos testes unitários focando em:
  1. Orçamentos com `period_start == period_end`.
  2. Transações que consomem todo o saldo disponível.
  3. Fluxo de contribuição (`goal_id` preenchido) e validação de categorias vazias.
- **Categoria mensagens:** reforçar os testes existentes para validar também o conteúdo da mensagem (capturando a exceção e usando `assertIn`), apenas onde o texto agrega valor para o usuário; manter documentação caso opte-se por não validar mensagens cosméticas.

Essas ações devem elevar o mutation score acima do patamar atual e garantir que as regressões sutis fiquem cobertas.

## Conclusão

O plano de testes cobre toda a pirâmide de qualidade: suites unitárias e estruturais asseguram os invariantes internos; funcionais e integradas exercitam regras de negócio via HTTP; testes específicos validam exceções, OOP, mocks/stubs e performance (com busca mantendo ~531 µs). A instrumentação de cobertura atinge 91 % e o mutation score de 71,6 % evidencia lacunas claras, já mapeadas para evolução. Com esses insumos, o time possui visibilidade sobre a saúde da aplicação e um roadmap objetivo para fortalecer ainda mais a confiabilidade da Finance Manager API.
