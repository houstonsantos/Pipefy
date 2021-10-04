# API GraphQL Pipefy

<p align="center">
    <img src="https://media2.giphy.com/media/1iv9rfagDFWE5CP8Im/200w.gif">
</p>

Deixo um pouco de uma experiência onde em um projeto realizei a integração do Pipefy com um ERP, e com Elastc Stack (Elasticsearch, Kibana e Logstash). Aqui realizei testes da API usando Python, posteriormente tranferir esse conhecimento para dentro do Logstash usnado o plugin http.

## O que é GraphQL?

* A linguagem de consulta de dados GraphQL é:

    * Uma especificação. A especificação determina a validade do esquema no servidor API. O esquema determina a validade das chamadas do cliente.

    * Fortemente tipado. O esquema define um sistema de tipo de API e todos os relacionamentos de objeto.

    * Introspectivo. Um cliente pode consultar o esquema para obter detalhes sobre o esquema.

    * Hierárquico. A forma de uma chamada GraphQL reflete a forma dos dados JSON que ela retorna. Os campos aninhados permitem consultar e receber  apenas os dados especificados em uma única viagem de ida e volta.

    * Uma camada de aplicativo. GraphQL não é um modelo de armazenamento ou uma linguagem de consulta de banco de dados. O gráfico se refere a estruturas de gráfico definidas no esquema, onde os nós definem objetos e as arestas definem relacionamentos entre os objetos. A API percorre e retorna os dados do aplicativo com base nas definições do esquema, independentemente de como os dados são armazenados.

>Quer saber mais da [API](https://developers.pipefy.com/reference/what-is-graphql) e [Pipefy Developers](https://api-docs.pipefy.com/reference/overview/Card/).