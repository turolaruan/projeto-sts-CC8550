# Relatório de Testes

## Testes de Mutação (Mutmut)

### Configuração e comandos

- Ferramenta: `mutmut 2.4.0`
- Suites exercitadas: `pytest` (modo estrito do `pytest-asyncio`)
- Escopo dos módulos mutados:
  - `src/services/account_service.py`
  - `src/services/budget_service.py`
  - `src/services/transaction_service.py`
- Comandos executados:
  ```bash
  pytest
  mutmut run \
    --runner "python3 -m pytest" \
    --paths-to-mutate src/services/account_service.py \
    --paths-to-mutate src/services/budget_service.py \
    --paths-to-mutate src/services/transaction_service.py \
    --tests-dir tests
  mutmut results
  mutmut result-ids killed
  mutmut result-ids survived
  ```

### Métricas gerais

| Métrica | Valor |
| --- | --- |
| Mutantes gerados | 139 |
| Mutantes mortos | 39 |
| Mutantes sobreviventes | 100 |
| Taxa de mutantes mortos | **28.06 %** |

### Cobertura por módulo

| Módulo | Situação | Observações |
| --- | --- | --- |
| `src/services/account_service.py` | 0 sobreviventes | Todos os mutantes gerados para a camada de contas foram mortos pelos novos testes assíncronos. |
| `src/services/budget_service.py` | 0 sobreviventes | Cenários de criação, unicidade e remoção segura garantiram 100 % de mutantes mortos. |
| `src/services/transaction_service.py` | 100 sobreviventes | Mutantes restantes concentram-se em fluxos ainda não exercitados (listagem, atualização, deleção e mensagens). |

### Mutantes sobreviventes e justificativas

Os 100 mutantes sobreviventes estão restritos a `src/services/transaction_service.py`. Eles se agrupam em quatro categorias principais:

1. **Alterações apenas em mensagens/contexto de erro** — Exemplos: linhas `47-71`, `108-170` e `260-269` trocam rótulos como `"account"` por `"XXaccountXX"`. Como asserções atuais validam somente o tipo da exceção (`ValidationAppError`/`EntityNotFoundError`), testar texto traria pouco valor e tornaria o suite frágil a refactors de UX.
2. **Filtragem em `list_transactions` (`78-106`)** — Mutantes que trocam o dicionário de filtros (`filters = {}` → `filters = None`, chaves renomeadas, retorno `None`). Ainda não existem testes cobrindo esse método porque ele é um simples repasse para o repositório; reproduzir as consultas implicaria duplicar a lógica de persistência ou criar fakes complexos.
3. **Fluxo de atualização (`115-164`)** — Mutantes como o ID 70 (troca de `**updates` por `*updates`) demonstram que `update_transaction` não foi exercitado. Cobrir esse caminho exige montar cenários com transações persistidas, budgets e deltas positivos/negativos — item planejado para a próxima iteração, pois envolve mocks adicionais do repositório.
4. **Operações de deleção e agregações (`165-220`)** — Alguns mutantes trocam o retorno do repositório ou o cálculo de `adjusted_total`. Embora tenhamos validado o estouro de orçamento na criação, ainda faltam casos que forçam alterações pós-criação (update/delete) para cobrir integralmente `_ensure_budget_allows` e `_apply_balance_delta` em todos os tipos de transação.

### Próximos passos recomendados

1. Adicionar testes dedicados para `TransactionService.list_transactions` validando o dicionário de filtros em diferentes combinações.
2. Criar uma suíte específica para `TransactionService.update_transaction`, cobrindo:
   - Atualização apenas de metadados (sem delta financeiro).
   - Atualização de valor que dispara `amount_delta` tanto positivo quanto negativo.
   - Tentativa de atualização vazia (já coberta indiretamente, mas pode validar mensagem).
3. Exercitar `delete_transaction` e `_apply_balance_delta` para transações de **transferência**, garantindo que dois ajustes de saldo ocorram.
4. Manter a estratégia de não validar textos de erro (mutantes apenas de string) e focar nos comportamentos observáveis ao usuário. Para esses casos, a justificativa acima permanece válida e documentada.
