# Entrypoint

---

### Definição

O ENTRYPOINT é uma instrução utilizada em um Dockerfile que define o _comando principal_ e _executável fixo_ que será executado sempre que um container for iniciado a partir daquela imagem.

Pode-se pensar nele como o "programa principal" do seu container. Se for criada uma imagem para rodar um script em Python, por exemplo, o ENTRYPOINT garante que o interpretador Python será acionado por padrão, impedindo que o container feche imediatamente após iniciar.

---

### Prática


![entrypoint_ubuntu.png](./images/Entrypoint/entrypoint_ubuntu.png)

Mostra

---
