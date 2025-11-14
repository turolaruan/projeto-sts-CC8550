Fixtures de dados utilizados pelos testes automatizados.

Cada arquivo JSON representa uma entidade de domínio com campos alinhados aos
modelos Pydantic do projeto. Os timestamps estão em ISO 8601 e valores
monetários são strings numéricas para preservar a precisão decimal.

Arquivos disponíveis:

| Arquivo            | Conteúdo                                                      |
|--------------------|---------------------------------------------------------------|
| `users.json`       | Usuários base com moedas padrão diferentes.                   |
| `accounts.json`    | Contas vinculadas aos usuários das fixtures.                  |
| `categories.json`  | Categorias de receita e despesa (inclui hierarquia).          |
| `budgets.json`     | Orçamentos mensais associados a categorias de despesa.        |
| `transactions.json`| Transações de exemplo (receita, despesa e transferência).     |

Utilize o utilitário `tests.fixtures.loaders` para carregar os dados em testes,
por exemplo:

```python
from tests.fixtures import load_fixture, load_models
from src.models.account import Account

raw_accounts = load_fixture("accounts")
account_models = load_models("accounts", Account)
```

Adicione novos arquivos seguindo a mesma convenção para manter os testes
consistentes.
