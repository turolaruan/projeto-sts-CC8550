# Projeto: Sistema de Finanças Pessoais (API REST)

### Disciplina: CC8550 - Simulação e Teste de Software
### Professor: Luciano Rossi

### Objetivo
O presente projeto tem como objetivo atender às exigências solicitadas pelo professor Luciano Rossi para a matéria CC8550.

O grupo escolheu o tema **Sistema de Finanças Pessoais**, com o objetivo de construir uma **API REST** para gerenciamento financeiro, focando em arquitetura em camadas, regras de negócio complexas e ampla cobertura de testes.

---

## 📋 Critérios de avaliação do sistema

### 1. Arquitetura e Estrutura
1.  **Modularização:** Código organizado em módulos/pacotes distintos.
2.  **Separação de responsabilidades:** Camadas de apresentação, lógica de negócio e acesso a dados.
3.  **Injeção de dependências:** Para facilitar testes com mocks e stubs.
4.  **Uso de interfaces/classes abstratas:** Para permitir substituição de implementações.

### 2. Funcionalidades Mínimas
* **5 operações CRUD** (Create, Read, Update, Delete) em diferentes entidades.
* **3 regras de negócio complexas** que envolvam:
    * Validações com múltiplas condições.
    * Cálculos ou processamento de dados.
    * Interações entre diferentes entidades.
* **2 funcionalidades de consulta/busca** com filtros e ordenação.
* **Tratamento de exceções personalizado** para diferentes scenários de erro.
* **Validação de entrada de dados** com regras específicas.

### 3. Persistência de Dados
* Uso de banco de dados (SQLite, PostgreSQL ou MongoDB).
* Implementação de camada de acesso a dados (**Repository Pattern** ou **DAO**).
* Possibilidade de usar **mock do banco** para testes.

### 4. Interface
Implementar pelo menos uma das opções (escolha do grupo em negrito):
* **API REST: Endpoints com Flask, FastAPI ou Django REST Framework.**
* Interface CLI: Linha de comando com menu interativo.
* Interface Web: Frontend simples (HTML + templates).
* Interface Gráfica: Tkinter ou PyQt (opcional).

### 5. Requisitos Técnicos Específicos
* **Configuração externa:** Usar arquivo de configuração (JSON, YAML ou `.env`).
* **Logging:** Implementar sistema de logs em diferentes níveis.
* **Documentação de código:** Docstrings em todas as funções e classes principais.
* **Type hints:** Anotações de tipo em funções e métodos.
* **Manipulação de arquivos:** Pelo menos uma funcionalidade que leia/escreva arquivos.

---

## Requisitos de Teste e critério de avaliação

### Testes Unitários (Peso: 25%)
* Testar todas as funções e métodos isoladamente.
* Usar `pytest` ou `unittest`.
* Mínimo de **30 casos de teste unitários**.
* Cobrir casos normais, extremos e de erro.
* Uso de `fixtures` e parametrização.

### Testes de Integração (Peso: 20%)
* Testar interações entre módulos.
* Testar integração com banco de dados.
* Testar fluxos completos de funcionalidades.
* Mínimo de **10 testes de integração**.

### Testes Funcionais (Caixa-Preta) (Peso: 15%)
* Testar funcionalidades sem conhecer a implementação.
* Focar em entradas e saídas esperadas.
* Incluir testes de aceitação das regras de negócio.
* Mínimo de **8 cenários funcionais**.

### Testes Estruturais (Caixa-Branca) (Peso: 15%)
* Alcançar mínimo de **80% de cobertura de código**.
* Usar `pytest-cov` ou `coverage.py`.
* Testar todos os caminhos críticos do código.
* Incluir testes de cobertura de *branches* (desvios).
* Gerar relatório de cobertura em HTML.

### Testes de Mutação (Peso: 10%)
* Usar `mutmut`.
* Aplicar em pelo menos 3 módulos principais.
* Analisar taxa de mutantes mortos.
* Documentar mutantes sobreviventes e justificar.

### Testes Específicos por Tipo (Peso: 15%)
Implementar pelo menos **2 dos seguintes**:

* **Testes de API/REST** (se aplicável):
    * Testar endpoints com diferentes métodos HTTP.
    * Validar *status codes* e respostas JSON.
    * Usar `requests` ou `httpx` para testes.
* **Testes de Exceções**:
    * Verificar lançamento correto de exceções.
    * Testar mensagens de erro específicas.
    * Validar recuperação de erros.
* **Testes com Mocks e Stubs**:
    * Usar `unittest.mock` ou `pytest-mock`.
    * Isolar dependências externas (BD, APIs, arquivos).
    * Simular diferentes cenários de resposta.
* **Testes de Performance/Carga**:
    * Medir tempo de execução de operações críticas.
    * Testar comportamento com grandes volumes de dados.
    * Usar `pytest-benchmark`.
* **Testes de Orientação a Objetos**:
    * Testar herança e polimorfismo.
    * Validar encapsulamento.
    * Testar métodos abstratos e interfaces.