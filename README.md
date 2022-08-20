
## Documentação da API

### Retorna todos os itens

```http
  GET /pessoas
```

### Retorna uma pessoa buscando por id

```http
  GET /pessoas/${id}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `int` | **Obrigatório**. O ID da pessoa que você quer |


### Retorna todas as pessoas buscando por um nome específico

```http
  GET /pessoas/nome/${nome}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `nome`      | `string` | **Obrigatório**. O Nome das pessoas que você quer |


### Cria pessoa e salva no banco

```http
  POST /pessoas
```

```json
Request Body:

    {
        "name": string,
        "idade": int	
    }
```