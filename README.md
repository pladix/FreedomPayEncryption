# 🔐 FreedomPay - Sistema de Criptografia de Cartão de Crédito para Gateway

## Sobre o Projeto

**FreedomPay** é um sistema seguro de criptografia para números de cartão de crédito e outros dados sensíveis. Utiliza **RSA com chave pública** para garantir a proteção das informações enviadas.

Os dados são processados através da seguinte rota:

```
http://localhost:5555/encrypt?card=(numero do cartao)&expirationDate=1225&securityCode=123&postalCode=10080
```

Após a requisição, os dados são criptografados e retornam no formato `cardData`, semelhante a este:

```json
{
  "cardData": "Cef9zvFcVRTx5Oz2nym48A+T3gA65avKmUgFgP26o0/8Gp99HoIPqeKhoSoSH3se0QLh7n+7KHTZs+QZ0IH6/GCSZG5ietyEjT/fVBn0uXoH93vlWmAhlSsTlOPxT6piy9WHwja9wexkOUAp/YsGskAhvZUYYSu7rqQ4X1W6y7NK2/5i4O+SnDiEZGIs+VZuPcq/lmOfGMyfcSlE33ZikOV3nN2xBx6JwyuR844WBf8SE9+A6HiJqCI8ggYiM1nirqP36lLiAfJLw4g89ZR+pRlVMhgZPEziBXsvU2RlZzYsZGEodAlPVZ6nRnGJ5lvNmBIZvzcFWS+SHb3Dy5MjDA=="
}
```

## 🚀 Tecnologias Utilizadas

- **Python**
- **RSA Encryption**

## 📥 Instalação no Windows

1. Certifique-se de ter o **Python** instalado.
2. No terminal, execute o seguinte comando para instalar as dependências:
   ```sh
   pip3 install -r requirements.txt
   ```
3. Para iniciar o projeto manualmente, utilize:
   ```sh
   py app.py
   ```
4. Alternativamente, você pode usar o **arquivo `iniciar.bat`**, que instalará as dependências e iniciará o projeto automaticamente.

## 🛠 Contribuições & Feedback

Caso tenha sugestões, encontre **bugs** ou precise de suporte, entre em contato!

📩 **Contato:** [t.me/pladixoficial](https://t.me/pladixoficial)

