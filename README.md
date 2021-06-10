# Desafio Mercos Backend

### Como inicializar o projeto local

1. Necessário versão `Python >= 3.6`
2. Necessário versão `Mysql >= 8.0`
3. Executar comando `pip install -r requirements.txt`
4. Executar o comando `python manage.py migrate`

Para iniciar o servidor execute o comando `python manage.py runserver`. <br>
Pronto, agora a API está no ar 🚀 

<br>

> Obs: Você também pode acessar a aplicação pelo link: http://vendas-mercos.herokuapp.com/

---

### Como popular o banco de dados local

Já com o Mysql instalado na máquina, será necessário executar os seguintes comandos no terminal do Mysql.

#### Populando Clientes:

```
INSERT INTO clientes_cliente (nome, excluido, ultima_alteracao)
VALUES ('Daarth Vader', false, '2021-06-09 10:16:00');

INSERT INTO clientes_cliente (nome, excluido, ultima_alteracao)
VALUES ('Obi-Wan Kenobi', false, '2021-06-09 10:16:00');

INSERT INTO clientes_cliente (nome, excluido, ultima_alteracao)
VALUES ('Luke Skywalker', false, '2021-06-09 10:16:00');

INSERT INTO clientes_cliente (nome, excluido, ultima_alteracao)
VALUES ('Imperador Palpatine', false, '2021-06-09 10:16:00');

INSERT INTO clientes_cliente (nome, excluido, ultima_alteracao)
VALUES ('Han Solo', false, '2021-06-09 10:16:00');
```

#### Populando Produtos:

```
INSERT INTO produtos_produto (nome, preco_tabela, multiplo, excluido, ultima_alteracao)
VALUES ('Millenium Falcon', 550000.00, null, false, '2021-06-09 10:16:00');

INSERT INTO produtos_produto (nome, preco_tabela, multiplo, excluido, ultima_alteracao)
VALUES ('X-Wing', 60000.00, 2, false,  '2021-06-09 10:16:00');

INSERT INTO produtos_produto (nome, preco_tabela, multiplo, excluido, ultima_alteracao)
VALUES ('Super Star Destroyer', 4570000.00, null, false,  '2021-06-09 10:16:00');

INSERT INTO produtos_produto (nome, preco_tabela, multiplo, excluido, ultima_alteracao)
VALUES ('TIE Fighter', 75000.00, 2, false,  '2021-06-09 10:16:00');

INSERT INTO produtos_produto (nome, preco_tabela, multiplo, excluido, ultima_alteracao)
VALUES ('Lightsaber', 6000.00, 5, false,  '2021-06-09 10:16:00');

INSERT INTO produtos_produto (nome, preco_tabela, multiplo, excluido, ultima_alteracao)
VALUES ('DLT-19 Heavy Blaster Rifle', 5800.00, null, false, '2021-06-09 10:16:00');

INSERT INTO produtos_produto (nome, preco_tabela, multiplo, excluido, ultima_alteracao)
VALUES ('DL-44 Heavy Blaster Pistol', 1500.00, 10, false,  '2021-06-09 10:16:00');
```

---

Dessa forma, você já pode clonar o projeto do [Frontend](https://github.com/lauraziebarth/vendas-frontend) e fazer os pedidos 👩‍💻
