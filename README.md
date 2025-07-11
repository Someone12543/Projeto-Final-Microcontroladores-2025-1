# :pen: Projeto-Final-Microcontroladores-2025-1
O projeto possui como objetivo a criação de uma máquina de desenhar as imagens geradas por inteligência artifical (IA) através de um site e utiliza-se um arduino para controlar os motores na máquina CNC.

## :brain: Componentes utilizados
- 3 motores de passo;
- 1 arduino mega;
- 1 shield CNC;
- 3 servos;
- 2 fontes (uma para os motores outra para os servos).

## Esquemático do projeto
<img width="1155" height="757" alt="image" src="https://github.com/user-attachments/assets/9375232d-3d8f-42fb-81f9-4935b1c15885" /> <br/>

> [!Note]  
> Para os motores, alimente-os com 12 V. Para os servos, alimente-os com 5 V.

## Funcionamento
1. Para funcionar, tanto o frontend quanto o backend devem estar rodando ao mesmo tempo.
2. Após, abra-se o frontend no navegador e aparecerá uma tela de chat. Nela, você digita o que quer que a IA gere, de preferência em inglês, e clica "ENTER" ou na seta para enviar.
3. Enquanto a IA está gerando a imagem, fica carregando, e quando terminar de carregar é necessário scrollar até embaixo para ver o último resultado. 
4. Se você quiser editar a imagem gerada, clique no botão para **editar** e abrirá um pop-up para fazer tal. 
5. Quando estiver do seu agrado, clique em **salvar**, se estiver editando, ou em **enviar** se não fez nenhuma modificação na imagem.

# 📦 Projeto - Instruções de Execução

## 🛠️ Backend (API)

Para rodar o backend, siga os passos abaixo:

1. Abra o terminal na pasta `api`.

2. Crie um ambiente virtual:
   ```bash
   python3 -m venv venv
   ```

3. Ative o ambiente virtual:

   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```

   - **Linux/Mac**:
     ```bash
     source venv/bin/activate
     ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Execute o backend:
   ```bash
   python main.py
   ```

---

## 💻 Frontend

Para rodar o frontend, siga os passos abaixo:

1. Abra o terminal na pasta `frontend`.

2. Instale as dependências:
   ```bash
   npm install
   ```

3. Rode o projeto:
   ```bash
   npm run dev
   
