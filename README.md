# Sistema de Almoxarifado de Empréstimo de Ferramentas

![Imagem](https://github.com/Alex-Olv/Almoxarifado/blob/main/static/assets/unnamed_2_-removebg-preview.png)

Bem-vindo ao projeto de controle de empréstimo de ferramentas para obras!

## Índice

- [Funcionalidades](#funcionalidades)
- [Tecnologias utilizadas](#tecnologias-utilizadas)
- [Como instalar e rodar](#como-instalar-e-rodar)
- [Como contribuir](#como-contribuir)
- [Licença](#licença)
- [Colaboradores](#colaboradores)

## Funcionalidades

- Cadastro de ferramentas e materiais
- Registro de empréstimos e devoluções
- Controle de estoque em tempo real
- Relatórios de uso e movimentação
- Interface web responsiva e amigável (issues [#1](https://github.com/Alex-Olv/Almoxarifado/issues/1))
- Busca e filtros de itens (issues [#2](https://github.com/Alex-Olv/Almoxarifado/issues/2))
- Implementação de teste unitários para aplicação (issues [#3](https://github.com/Alex-Olv/Almoxarifado/issues/3))
-Usar o Docker na aplicação (issues [#4](https://github.com/Alex-Olv/Almoxarifado/issues/4))

## Tecnologias utilizadas

- **Back-end:** Python (Flask)
- **Banco de Dados:** MySQL
- **Front-end:** HTML5, CSS3

## Como instalar e rodar

1. Clone este repositório:
   ```bash
   git clone https://github.com/Alex-Olv/Almoxarifado.git
   cd Almoxarifado
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. **Suba um container MySQL usando Docker:**
   ```bash
   docker run --name almoxarifado-mysql -e MYSQL_ROOT_PASSWORD=senha_root -e MYSQL_DATABASE=almoxarifado -e MYSQL_USER=usuario -e MYSQL_PASSWORD=senha_usuario -p 3306:3306 -d mysql:8.0
   ```
   - Altere `senha_root`, `usuario` e `senha_usuario` conforme desejar.
   - O banco será acessível em `localhost:3306`.

5. **Configure as variáveis de ambiente do seu projeto** (exemplo para Flask):
   ```
   DB_HOST=localhost
   DB_PORT=3306
   DB_USER=usuario
   DB_PASSWORD=senha_usuario
   DB_NAME=almoxarifado
   ```

6. **Execute as migrações ou crie as tabelas** conforme a necessidade do seu projeto.

7. Execute a aplicação:
   ```bash
   flask run

## Como contribuir

1. Faça um fork deste repositório
2. Crie uma branch para sua feature ou correção (`git checkout -b feature/NovaFuncionalidade`)
3. Faça o commit de suas alterações (`git commit -m 'Adiciona nova funcionalidade'`)
4. Faça push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Colaboradores

- Alex Oliveira Curvo
- Silvio Medeiros Leite
- Victor Silva do Nascimento Reis






