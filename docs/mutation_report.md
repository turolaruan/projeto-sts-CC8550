# Relatório de Testes de Mutação

## Estratégia

- Ferramenta: [`mutmut`](https://github.com/boxed/mutmut).
- Runner customizado para acelerar o ciclo por serviço:
  - `AccountService`: `python3 -m pytest tests/unit/test_services.py -k AccountServiceTest`
  - `BudgetService`: `python3 -m pytest tests/unit/test_services.py -k BudgetServiceTest`
  - `TransactionService`: `python3 -m pytest tests/unit/test_services.py -k TransactionServiceTest`
- Para cada serviço o `setup.cfg` foi ajustado provisoriamente em `[mutmut]` >
  `paths_to_mutate` e `runner`, seguido de `rm -f .mutmut-cache` e `mutmut run`.
- Saídas completas foram armazenadas em `tests/mutation/mutmut_<serviço>.txt` e os
  agregados no `tests/mutation/mutmut_summary.json`.

## Resultados

| Serviço                     | Mutantes | Mortos | Sobreviventes | Kill rate |
|-----------------------------|---------:|-------:|--------------:|----------:|
| `src/services/account_service.py`      | 81 | 32 | 49 | 39.5 % |
| `src/services/budget_service.py`       | 62 | 25 | 37 | 40.3 % |
| `src/services/transaction_service.py`  | 139 | 69 | 70 | 49.6 % |

> O `mutmut` encerra com código de saída `2` quando há mutantes sobreviventes,
> por isso os comandos foram executados manualmente (não dentro do fluxo do CI).

## Mutantes sobreviventes e ações sugeridas

### AccountService

Sobreviventes concentram-se em:
- Mensagens/`context` dos `ValidationAppError`/`EntityNotFoundError`.
- Montagem do dicionário de filtros em `list_accounts`.
- Guard-clauses nas validações de saldo mínimo.

**Plano**
1. Criar testes que validem o conteúdo de `context` ao disparar exceções (não
   apenas o tipo da exceção).
2. Exercitar `list_accounts` verificando o payload enviado ao repositório com
   `AsyncMock.assert_awaited_once_with(...)` para cada filtro.
3. Adicionar casos em que `minimum_balance` é atualizado para garantir que a
   comparação `balance < new_min` continue sendo exercitada.

### BudgetService

Sobreviventes cobrem filtros de `list_budgets` e mensagens/contexto das exceções.
Como os testes atuais apenas verificam o retorno (lista vazia/non-vazia) muitas
mutações passando a ignorar filtros não são percebidas.

**Plano**
1. Adicionar `assert_awaited_once_with` para o repositório ao chamar
   `list_budgets`, cobrindo combinações de `user_id`, `category_id`, `year` e
   `month`.
2. Exercitar `delete_budget` com `exists_for_category` retornando `False` para
   validar o caminho "feliz" e com valores diferentes para garantir que o
   `context` das exceções seja validado.
3. Acrescentar testes de integração para a rota `/budgets/` garantindo os erros
   `409` e `400` com as mensagens originais.

### TransactionService

Mutantes sobreviventes estão ligados à validação de transferências (`transfer_account_id`),
regras de categorias por tipo de transação e montagem dos filtros de
`list_transactions`.

**Plano**
1. Adicionar testes que validem o `context` das `ValidationAppError` em
   `_ensure_budget_allows` e `_validate_category_for_transaction`.
2. Criar cenários unitários específicos para `list_transactions` verificando o
   dicionário passado ao repositório (especialmente filtros de data e
   `transaction_type`).
3. Exercitar `_apply_balance_delta` com `TransactionType.TRANSFER` cobrindo o
   caminho em que `transfer_account_id` falta (mutantes que removem o `raise`
   sobreviveram).

## Como repetir os experimentos

Para cada serviço:

```bash
# 1. Ajuste temporariamente a seção [mutmut] em setup.cfg
cat <<'EOF' > temp-mutmut.cfg
[mutmut]
paths_to_mutate = src/services/<arquivo>.py
backup = False
runner = python3 -m pytest tests/unit/test_services.py -k <NomeDoTestCase>
tests_dir = tests/
EOF

# 2. Substitua a seção original (por exemplo usando `python3 - <<'PY'` ...)
# ou edite setup.cfg manualmente com os valores acima.

rm -f .mutmut-cache
mutmut run
mutmut results > tests/mutation/mutmut_<serviço>.txt
```

Finalize restaurando o `setup.cfg` original (`paths_to_mutate = src` e
`runner = python3 -m pytest`).

Os arquivos `tests/mutation/mutmut_*.txt` e `tests/mutation/mutmut_summary.json`
servem como baseline para acompanhar futuras melhorias de cobertura.
