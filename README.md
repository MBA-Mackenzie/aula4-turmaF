# Pipeline de Validação de Dados com Python & Pandas

### Aula prática - turma F: Engenharia de Dados Mackenzie

Este repositório contém um script automatizado para validação de qualidade de dados (Data Quality) estruturado em Python, utilizando a biblioteca **Pandas**. O objetivo principal é garantir a integridade dos dados contidos no arquivo `dados.csv` antes que eles sigam para as próximas etapas de uma pipeline de dados, simulando o comportamento de testes nativos de ferramentas modernas como o **dbt (data build tool)**.

O projeto conta com uma esteira de Integração Contínua (CI) via **GitHub Actions**, que executa automaticamente as validações a cada alteração no código ou nos dados.

---

## Estrutura do Projeto

* `validar_dados.py`: Script principal que contém as regras de negócio e os testes de qualidade de dados.
* `dados.csv`: Arquivo de entrada que será submetido aos testes de validação.
* `.github/workflows/pipeline.yml`: Configuração da esteira de CI do GitHub Actions.

---

## Regras de Validação (Testes de Qualidade)

O script `validar_dados.py` realiza quatro testes fundamentais sobre o conjunto de dados carregado:

1.  **Valores Negativos (`df['valor'] < 0`):** Garante que nenhuma linha possua valores numéricos negativos na coluna `valor`. Caso encontre, os registros problemáticos são listados.
2.  **IDs Únicos (`df['id'].duplicated()`):** Verifica a unicidade da coluna identificadora (`id`), impedindo duplicidade de registros.
3.  **Presença de Nomes (`df['nome'].isna()`):** Avalia se existem campos vazios ou nulos (NaN) na coluna identificadora de texto `nome`.
4.  **Consistência Financeira (`df['valor'].sum() < 0`):** Uma validação macro que impede que o balanço/soma total da coluna `valor` resulte em um saldo negativo.

---

## Como Executar Localmente

### Pré-requisitos
* Python 3.10 ou superior instalado.
* Biblioteca `pandas` instalada.

### Passo a Passo

1.  **Clone o repositório:**
    ```bash
    git clone <url-do-seu-repositorio>
    cd <nome-do-repositorio>
    ```

2.  **Instale as dependências:**
    ```bash
    pip install pandas
    ```

3.  **Prepare o arquivo de dados:**
    Certifique-se de que o arquivo `dados.csv` esteja na raiz do projeto com as colunas estruturadas (`id`, `nome`, `valor`).

4.  **Execute o script de validação:**
    ```bash
    python validar_dados.py
    ```

### Códigos de Saída (Exit Codes)
O script utiliza códigos de terminação padrão do sistema para se integrar perfeitamente com orquestradores e ferramentas de CI/CD:
* **`0` (Sucesso):** Todos os testes passaram. O terminal exibirá o total de registros, soma e média dos valores.
* **`1` (Falha):** Um ou mais testes falharam. Os erros serão detalhados no console e a pipeline será interrompida.

---

## Integração Contínua (GitHub Actions)

A pipeline automatizada está configurada no arquivo `.github/workflows/pipeline.yaml` e é disparada sob as seguintes condições:
* **Triggers:** Qualquer `push` ou `pull_request` direcionado para a branch `main`.

### Fluxo do Job (`validar_dados`)
O ambiente roda sobre o sistema operacional `ubuntu-latest` e executa os seguintes passos descritos visualmente abaixo:

1.  **Pegar o código (`actions/checkout@v3`):** Faz o clone do código do repositório dentro do ambiente virtual do GitHub Runner.
2.  **Instalar Python (`actions/setup-python@v4`):** Configura o ambiente com a versão `3.10` do Python.
3.  **Instalar pandas (`run: pip install pandas`):** Instala a biblioteca necessária para a manipulação e teste de dados.
4.  **Validar dados (`run: python validar_dados.py`):** Executa o script. Se o script retornar `exit 1`, o GitHub Actions marca o Job como **falho**, alertando o time de engenharia de dados imediatamente e bloqueando o merge de dados corrompidos.
   
---

## Autoria e Orientação

* **Responsável:** Profª. Debora Batista Paulo
* **Hashtag Oficial:** #profdeborapaulo
