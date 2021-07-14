## **Table of Contents**
- [E10 - Kenzie Serie](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/3a_e_01_kenzie_serie.html&ref=master#mcetoc_1f4uinjti1) 
  - [Objetivo](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/3a_e_01_kenzie_serie.html&ref=master#mcetoc_1f4uinjti2)
  - [Preparativos](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/3a_e_01_kenzie_serie.html&ref=master#mcetoc_1f4uinjti3)
- [Exemplos de entrada e saída](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/3a_e_01_kenzie_serie.html&ref=master#mcetoc_1f5tee5tf1)
- [Kenzie Serie](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/3a_e_01_kenzie_serie.html&ref=master#mcetoc_1f4uinjti1) 
  - [Database](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/3a_e_01_kenzie_serie.html&ref=master#mcetoc_1f5eg5m2j0)
- [Rotas](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/3a_e_01_kenzie_serie.html&ref=master#mcetoc_1f5eg5m2j1) 
  - [Rota /series](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/3a_e_01_kenzie_serie.html&ref=master#mcetoc_1f5eg5m2j2)
  - [Rota /series](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/3a_e_01_kenzie_serie.html&ref=master#mcetoc_1f5eg5m2j4)
  - [Rota /series/](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/3a_e_01_kenzie_serie.html&ref=master#mcetoc_1f5ei3hp56)
- [Entregáveis ](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/3a_e_01_kenzie_serie.html&ref=master#mcetoc_1egvoav555j)
  - [Repositório ](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/3a_e_01_kenzie_serie.html&ref=master#mcetoc_1egvrpv6k1l4)
- [Critérios de aceitação ](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/3a_e_01_kenzie_serie.html&ref=master#mcetoc_1eh146n6m3)
# **E10 - Kenzie Serie**
Para essa entrega você criará um sistema para armazenamento e criação de series.


## **Objetivo**
Essa atividade foi elaborada para trabalhar seus conhecimentos de Flask e PostgreSQL.


## **Preparativos**
Você deverá seguir a seguinte estrutura de pastas:

├── app

│   ├── \_\_init\_\_.py

│   ├── services

│   │   └── \_\_init\_\_.py

│   └── views

│       └── \_\_init\_\_.py

├── .gitignore

└── requirements.txt



**OBS:** Siga os **endpoints,** **status code**, **assinatura da função** e as especificações da **database** como o esperado se não irá perder nota.

**Nota:** Os retornos **NÃO** precisam seguir na mesma ordem apresentada.


# **Exemplos de entrada e saída**
Todos os exemplos de entrada e saída estão nesse [link](https://gitlab.com/cauanf/3a_kenzie_serie).


# **Kenzie Serie**
## **Database**
Você deverá criar sua base seguindo o seguinte padrão abaixo:

- **NOME DA TABELA: ka\_series**
- **id:  BIGSERIAL, PRIMARY KEY**
- **serie: VARCHAR(100), NOT NULL, UNIQUE**
- **seasons: INTEGER, NOT NULL**
- **released\_date: DATE, NOT NULL**
- **genre: VARCHAR(50), NOT NULL**
- **imdb\_rating: FLOAT, NOT NULL**


# **Rotas**
## **Rota /series**
- Especificações da rota: 
  - Assinatura da função: 
    - **create()**
  - Deverá aceitar o método: 
    - **POST**
  - Rotina deverá ser: 
    - **Criação da tabela** no seu banco de dados caso ela não exista.
    - **Inserção** da série que foi mandada pela requisição na **tabela** do seu banco de dados.
    - Os valores de **serie** e **genre** deverá ser salvo no formato de título.
  - Retorno: 
    - Um **dicionário** com as informações pessadas pela requisição.
    - Status code **201**.


## **Rota /series**
- Especificações da rota: 
  - Assinatura da função: 
    - **series()**
  - Deverá aceitar o método: 
    - **GET**
  - Rotina deverá ser: 
    - **Seleção** de todos os dados da tabela.
  - Retorno: 
    - Caso haja dados na tabela deverá retornar:  
      - Uma **lista** de **dicionários** com o resultado da **seleção** feita.
      - Status code **200**.
    - Caso **não** haja dados na tabela deverá retornar: 
      - Uma **lista** vazia.
      - Status code **200**.
    - Caso a tabela não exista: 
      - Deverá **fazer a criação da tabela**.
      - E retornará uma **lista** vazia
      - Status code **200**


## **Rota /series/<int:serie\_id>**
- Especificações da rota: 
  - Assinatura da função: 
    - **select\_by\_id()**
  - Deverá aceitar o método: 
    - **GET**
  - Rotina deverá ser: 
    - **Seleção** de um dado da tabela filtrado pelo **id**.
  - Retorno: 
    - Caso haja dados na tabela deverá retornar:  
      - Um **dicionário** de **dicionário** com o resultado da **seleção** feita.
      - Status code **200**.
    - Caso **não** haja dados na tabela ou **não exista** o respectivo **id** deverá retornar: 
      - Um **dicionário**.
      - Status code **404**.
    - Caso a tabela não exista: 
      - Deverá **fazer a criação da tabela**.
      - E retornar um **dicionário**.
      - Status code **404**
-----
# **Entregáveis** 
## **Repositório** 
- Link do **repositório** do **GitLab** 
- **Código fonte:** 
  - Diretório **app**. 
- **Privacidade** 
  - Incluir **ka-br-out-2020-correcoes** como reporter. 
### -----
# **Critérios de aceitação** 

|**Pts** |**Dado** |**Quando** |**É esperado** |
| :-: | :-: | :-: | :-: |
|**0.5**|**database**|**dado o formato**|**que siga o formato**|
|**1.5**|**rota /series**|**feito a requisição na rota**|**siga o esperado**|
|**1.5**|**rota /series**|**feito a requisição na rota**|**siga o esperado**|
|**1.5**|**rota /series/<int:serie\_id>**|**feito a requisição na rota**|**siga o esperado**|
**Boa diversão!! 😉**






