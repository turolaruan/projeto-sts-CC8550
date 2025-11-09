# Simulação e Teste de Software (CC8550) — Descrição do Projeto
**Curso:** Ciência da Computação — Centro Universitário FEI  
**Professor:** Prof. Luciano Rossi  
**Semestre:** 2º Semestre de 2025

---

## Tema
O tema é livre, permitindo que a equipe escolha um domínio de interesse. Exemplos:
- Sistema de gerenciamento (biblioteca, estoque, tarefas, finanças pessoais)
- Aplicação de e-commerce simplificada
- Sistema de agendamento (consultas, reservas, eventos)
- Plataforma educacional (quiz, cursos, avaliações)
- Sistema de análise de dados (relatórios, dashboards)
- API REST para serviços diversos
- Sistema de recomendação
- Aplicação de monitoramento (clima, sensores, logs)

---

## Projeto

### Arquitetura e Estrutura
- **Modularização:** código organizado em módulos/pacotes distintos  
- **Separação de responsabilidades:** camadas de apresentação, lógica de negócio e acesso a dados  
- **Injeção de dependências:** para facilitar testes com *mocks* e *stubs*  
- **Interfaces/classes abstratas:** para permitir substituição de implementações

### Funcionalidades Mínimas
- **CRUD:** pelo menos 5 operações CRUD em diferentes entidades
- **Regras de negócio (3 no mínimo)** envolvendo:
  - Validações com múltiplas condições
  - Cálculos ou processamento de dados
  - Interações entre diferentes entidades
- **Consultas/busca (2 no mínimo):** com filtros e ordenação
- **Tratamento de exceções:** personalizado para diferentes cenários de erro
- **Validação de entrada:** com regras específicas

### Persistência de Dados
- Uso de banco de dados (**SQLite**, **PostgreSQL** ou **MongoDB**)
- Implementação de camada de acesso a dados (**Repository Pattern** ou **DAO**)
- Possibilidade de usar *mock* do banco para testes

### Interface (implementar pelo menos uma)
- **API REST:** endpoints com Flask, FastAPI ou Django REST Framework
- **Interface CLI:** linha de comando com menu interativo
- **Interface Web:** frontend simples (HTML + templates)
- **Interface Gráfica:** Tkinter ou PyQt (opcional)

### Requisitos Técnicos Específicos
- **Configuração externa:** arquivo de configuração (JSON, YAML ou `.env`)
- **Logging:** sistema de logs em diferentes níveis
- **Documentação de código:** *docstrings* em funções e classes principais
- **Type hints:** anotações de tipo em funções e métodos
- **Manipulação de arquivos:** ao menos uma funcionalidade que leia/escreva arquivos

### Preparação do Banco de Dados MongoDB
- Ajuste as variáveis de ambiente em `.env` (copie de `.env.example` se necessário)
- Para subir uma instância local rapidamente, execute `docker-compose up -d`
- Execute `python3 -m src.database.setup` para criar coleções e índices exigidos pelo sistema

---

## Requisitos de Testes

### Testes Unitários (peso: 25%)
- Testar funções e métodos isoladamente
- Usar **pytest** ou **unittest**
- **Mínimo de 30 casos** de teste unitários
- Cobrir casos normais, extremos e de erro
- Uso de **fixtures** e **parametrização**

### Testes de Integração (peso: 20%)
- Testar interações entre módulos
- Testar integração com banco de dados
- Testar fluxos completos de funcionalidades
- **Mínimo de 10** testes de integração

### Testes Funcionais — Caixa-Preta (peso: 15%)
- Testar sem conhecer a implementação
- Foco em entradas e saídas esperadas
- Incluir testes de aceitação das regras de negócio
- **Mínimo de 8** cenários funcionais

### Testes Estruturais — Caixa-Branca (peso: 15%)
- **Cobertura mínima de 80%** de código
- Usar **pytest-cov** ou **coverage.py**
- Testar caminhos críticos do código
- Incluir cobertura de **branches**
- Gerar relatório de cobertura em **HTML**

### Testes de Mutação (peso: 10%)
- Usar **mutmut**
- Aplicar em pelo menos **3 módulos principais**
- Analisar taxa de mutantes mortos
- Documentar mutantes sobreviventes e justificar

### Testes Específicos por Tipo (peso: 15%) — Implementar **pelo menos 2**:
**Testes de API/REST (se aplicável)**
- Testar endpoints com diferentes métodos HTTP
- Validar *status codes* e respostas JSON
- Usar `requests` ou `httpx` para testes

**Testes de Exceções**
- Verificar lançamento correto de exceções
- Testar mensagens de erro específicas
- Validar recuperação de erros

**Testes com Mocks e Stubs**
- Usar `unittest.mock` ou `pytest-mock`
- Isolar dependências externas (BD, APIs, arquivos)
- Simular diferentes cenários de resposta

**Testes de Performance/Carga**
- Medir tempo de execução de operações críticas
- Testar comportamento com grandes volumes de dados
- Usar **pytest-benchmark**

**Testes de Orientação a Objetos**
- Testar herança e polimorfismo
- Validar encapsulamento
- Testar métodos abstratos e interfaces

---

## Créditos
- **Professor:** Prof. Luciano Rossi  
- **Disciplina:** Simulação e Teste de Software (CC8550) — FEI
