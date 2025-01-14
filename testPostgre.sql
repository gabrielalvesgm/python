-- Criação do banco de dados
CREATE DATABASE ecommerce;

-- Conectando ao banco de dados
\c ecommerce;

-- Criando a tabela Usuarios
CREATE TABLE Usuarios (
    id SERIAL PRIMARY KEY,            -- Identificador único
    nome VARCHAR(100) NOT NULL,       -- Nome do usuário
    email VARCHAR(150) UNIQUE NOT NULL -- Email do usuário
);

-- Criando a tabela Produtos
CREATE TABLE Produtos (
    id SERIAL PRIMARY KEY,                      -- Identificador único
    produto_nome VARCHAR(150) NOT NULL UNIQUE,  -- Nome do produto
    produto_preco NUMERIC(10, 2) NOT NULL CHECK (produto_preco > 0) -- Preço positivo
);

-- Criando a tabela Orders (Pedidos)
CREATE TABLE Orders (
    id SERIAL PRIMARY KEY,               -- Identificador único do pedido
    user_id INTEGER NOT NULL REFERENCES Usuarios(id) ON DELETE CASCADE -- FK para Usuarios
);

-- Tabela intermediária Orders_Produtos para muitos-para-muitos
CREATE TABLE Orders_Produtos (
    id SERIAL PRIMARY KEY,               -- Identificador único
    order_id INTEGER NOT NULL REFERENCES Orders(id) ON DELETE CASCADE, -- FK para Orders
    produto_id INTEGER NOT NULL REFERENCES Produtos(id) ON DELETE CASCADE, -- FK para Produtos
    quantidade INTEGER NOT NULL CHECK (quantidade > 0) -- Quantidade deve ser positiva
);

-- Inserindo dados na tabela Usuarios
INSERT INTO Usuarios (nome, email) VALUES ('Gabriel', 'LGabrielAlvesgm@gmail.com');
INSERT INTO Usuarios (nome, email) VALUES ('Julia', 'JuliaVitoria2004@gmail.com');

-- Inserindo dados na tabela Produtos
INSERT INTO Produtos (produto_nome, produto_preco) VALUES ('Sapato', 200.00);
INSERT INTO Produtos (produto_nome, produto_preco) VALUES ('Calça', 175.00);
INSERT INTO Produtos (produto_nome, produto_preco) VALUES ('Camiseta', 135.00);

-- Criando pedidos na tabela Orders
INSERT INTO Orders (user_id) VALUES (1); -- Pedido para Gabriel
INSERT INTO Orders (user_id) VALUES (2); -- Pedido para Julia

-- Associando produtos aos pedidos na tabela Orders_Produtos
-- Pedido 1 (Gabriel): 1 Sapato, 2 Camisetas
INSERT INTO Orders_Produtos (order_id, produto_id, quantidade) VALUES (1, 1, 1);
INSERT INTO Orders_Produtos (order_id, produto_id, quantidade) VALUES (1, 3, 2);

-- Pedido 2 (Julia): 1 Calça
INSERT INTO Orders_Produtos (order_id, produto_id, quantidade) VALUES (2, 2, 1);

-- Consultas SQL

-- Consulta 1: Exibir pedidos e seus clientes
SELECT 
    Orders.id AS PedidoID,
    Usuarios.nome AS Cliente,
    SUM(Produtos.produto_preco * Orders_Produtos.quantidade) AS TotalPedido
FROM 
    Orders
JOIN 
    Usuarios ON Orders.user_id = Usuarios.id
JOIN 
    Orders_Produtos ON Orders.id = Orders_Produtos.order_id
JOIN 
    Produtos ON Orders_Produtos.produto_id = Produtos.id
GROUP BY 
    Orders.id, Usuarios.nome;

-- Consulta 2: Exibir produtos de cada pedido
SELECT 
    Orders.id AS PedidoID,
    Usuarios.nome AS Cliente,
    Produtos.produto_nome AS Produto,
    Orders_Produtos.quantidade AS Quantidade,
    Produtos.produto_preco AS PreçoUnitário,
    (Produtos.produto_preco * Orders_Produtos.quantidade) AS TotalProduto
FROM 
    Orders
JOIN 
    Usuarios ON Orders.user_id = Usuarios.id
JOIN 
    Orders_Produtos ON Orders.id = Orders_Produtos.order_id
JOIN 
    Produtos ON Orders_Produtos.produto_id = Produtos.id;