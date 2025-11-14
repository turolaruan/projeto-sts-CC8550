# Simulação e Teste de Software (CC8550) – Descrição do Projeto

**Disciplina:** Simulação e Teste de Software (CC8550)  
---

## 1. Tema

O tema do projeto é livre, permitindo que a equipe escolha um domínio de interesse.

Exemplos de domínios sugeridos:

- Sistema de gerenciamento (biblioteca, estoque, tarefas, finanças pessoais)
- Aplicação de e-commerce simplificada
- Sistema de agendamento (consultas, reservas, eventos)
- Plataforma educacional (quiz, cursos, avaliações)
- Sistema de análise de dados (relatórios, dashboards)
- API REST para serviços diversos
- Sistema de recomendação
- Aplicação de monitoramento (clima, sensores, logs)

---

## 2. Características Técnicas Obrigatórias

### 2.1 Arquitetura e Estrutura

- **Modularização:** código organizado em módulos/pacotes distintos.  
- **Separação de responsabilidades:**  
  - Camada de apresentação  
  - Camada de lógica de negócio  
  - Camada de acesso a dados  
- **Injeção de dependências:** para facilitar testes com *mocks* e *stubs*.  
- **Uso de interfaces/classes abstratas:** para permitir substituição de implementações.

---

### 2.2 Funcionalidades Mínimas

- **5 operações CRUD** (Create, Read, Update, Delete) em diferentes entidades.  
- **3 regras de negócio complexas** que envolvam:
  - Validações com múltiplas condições  
  - Cálculos ou processamento de dados  
  - Interações entre diferentes entidades  
- **2 funcionalidades de consulta/busca** com filtros e ordenação.  
- **Tratamento de exceções personalizado** para diferentes cenários de erro.  
- **Validação de entrada de dados** com regras específicas.

---

### 2.3 Persistência de Dados

- Uso de banco de dados (**SQLite**, **PostgreSQL** ou **MongoDB**).  
- Implementação de camada de acesso a dados (padrão **Repository** ou **DAO**).  
- Possibilidade de usar *mock* do banco para testes.

---

### 2.4 Interface (Escolher pelo menos uma)

- **API REST:**  
  - Endpoints com Flask, FastAPI ou Django REST Framework  

**ou**

- **Interface CLI:**  
  - Linha de comando com menu interativo  

**ou**

- **Interface Web:**  
  - Frontend simples (HTML + templates)  

**ou**

- **Interface Gráfica:**  
  - Tkinter ou PyQt (opcional)

---

### 2.5 Requisitos Técnicos Específicos

- **Configuração externa:** usar arquivo de configuração (JSON, YAML ou `.env`).  
- **Logging:** implementar sistema de logs em diferentes níveis.  
- **Documentação de código:** *docstrings* em todas as funções e classes principais.  
- **Type hints:** anotações de tipo em funções e métodos.  
- **Manipulação de arquivos:** pelo menos uma funcionalidade que leia/escreva arquivos.

---

## 3. Requisitos de Testes

### 3.1 Testes Unitários (peso: 25%)

- Testar todas as funções e métodos isoladamente.  
- Usar **pytest** ou **unittest**.  
- **Mínimo de 30 casos de teste unitários.**  
- Cobrir casos:
  - Normais  
  - Extremos  
  - De erro  
- Uso de **fixtures** e parametrização.

---

### 3.2 Testes de Integração (peso: 20%)

- Testar interações entre módulos.  
- Testar integração com banco de dados.  
- Testar fluxos completos de funcionalidades.  
- **Mínimo de 10 testes de integração.**

---

### 3.3 Testes Funcionais (Caixa-Preta) (peso: 15%)

- Testar funcionalidades sem conhecer a implementação (foco em caixa-preta).  
- Focar em entradas e saídas esperadas.  
- Incluir testes de aceitação das regras de negócio.  
- **Mínimo de 8 cenários funcionais.**

---

### 3.4 Testes Estruturais (Caixa-Branca) (peso: 15%)

- Alcançar **mínimo de 80% de cobertura de código**.  
- Usar **pytest-cov** ou **coverage.py**.  
- Testar todos os caminhos críticos do código.  
- Incluir testes de cobertura de *branches*.  
- Gerar relatório de cobertura em **HTML**.

---

### 3.5 Testes de Mutação (peso: 10%)

- Usar **mutmut**.  
- Aplicar em pelo menos **3 módulos principais**.  
- Analisar taxa de mutantes mortos.  
- Documentar mutantes sobreviventes e justificar.

---

### 3.6 Testes Específicos por Tipo (peso: 15%)

Implementar **pelo menos 2** dos seguintes tipos de testes:

#### 3.6.1 Testes de API/REST (se aplicável)

- Testar endpoints com diferentes métodos HTTP.  
- Validar *status codes* e respostas JSON.  
- Usar `requests` ou `httpx` para testes.

#### 3.6.2 Testes de Exceções

- Verificar lançamento correto de exceções.  
- Testar mensagens de erro específicas.  
- Validar recuperação de erros.

#### 3.6.3 Testes com Mocks e Stubs

- Usar `unittest.mock` ou `pytest-mock`.  
- Isolar dependências externas (BD, APIs, arquivos).  
- Simular diferentes cenários de resposta.

#### 3.6.4 Testes de Performance/Carga

- Medir tempo de execução de operações críticas.  
- Testar comportamento com grandes volumes de dados.  
- Usar **pytest-benchmark**.

#### 3.6.5 Testes de Orientação a Objetos

- Testar herança e polimorfismo.  
- Validar encapsulamento.  
- Testar métodos abstratos e interfaces.

---

## 4. Estrutura do Projeto

O projeto deve ser estruturado de forma modular, seguindo boas práticas de arquitetura, separação de camadas, testes automatizados e documentação, atendendo todos os requisitos técnicos e de testes descritos acima.


    projeto/
    ├── src/                          # Código fonte da aplicação
    │   ├── controllers/              # Endpoints FastAPI
    │   ├── models/                   # Pydantic models e enums
    │   ├── repositories/             # Camada de acesso a dados (Mongo)
    │   ├── services/                 # Regras de negócio
    │   └── utils/                    # Utilidades (FileManager, logger, etc.)
    │
    ├── scripts/                      # Ferramentas auxiliares (ex.: generate_demo_data.py, CLI via scripts/cli.py)
    ├── tests/                        # Toda a suíte automatizada
    │   ├── fixtures/                 # Fábricas e repositórios em memória
    │   ├── unit/                     # Testes unitários
    │   ├── integration/              # Testes de integração (API + Mongo)
    │   ├── functional/               # Cenários caixa-preta/REST
    │   ├── structural/               # Testes estruturais/white-box
    │   ├── mutation/                 # Casos focados em mutação (mutmut)
    │   └── performance/              # Testes benchmark/tempo de execução
    │
    ├── docs/                         # Documentação do projeto
    │   ├── projeto.md                # Descrição do projeto
    │   ├── plano_testes.md           # Plano de testes
    │   └── relatorio_testes.md       # Relatório de execução
    │
    ├── config/                       # Arquivos de configuração
    ├── requirements.txt              # Dependências Python
    ├── pytest.ini                    # Configuração do pytest
    ├── .env.example                  # Exemplo de variáveis de ambiente
    └── README.md                     # Instruções do projeto
