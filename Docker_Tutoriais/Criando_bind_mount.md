# Criando um Bind Mount

### Sumário
- [Descrição](#descrição)
- [Prática](#prática)

---

### Descrição

Este artigo mostrará como criar um bind mount.


---

### Prática

Será mostrado como subir um container com um volume do tipo bind mount e baseado em uma imagem ubuntu.

```bash
# Criando o container com base ubuntu:
docker run -dit -v /meu-app:/app/exemplo --name container-com-bind-mount ubuntu
# Obs: O /meu-app é o diretório que ficará no docker host, caso ele não exista ele será criado.
# Obs2: O /app/exemplo é o diretório no container, caso ele não exista ele será criado.

# Mostrando que o diretório foi criado fora do container, e que ele ainda não possui nenhum arquivo:
ls -lh /meu-app/

docker exec -it container-com-bind-mount bash

# Mostrando que o diretório foi criado dentro do container, e que ele ainda não possui nenhum arquivo:
ls -lh /app/exemplo/

# Criando três arquivos dentro do container
touch /app/exemplo/arquivo{1..3}.txt

ls -lh /app/exemplo/

exit

# Mostrando que os três arquivos estão disponíveis também fora do container:
ls -lh /meu-app/

# Criando um arquivo fora do container:
touch /meu-app/arquivo4.txt

# Mostrando que agora o diretório possui quatro arquivos:
ls -lh /meu-app/

docker exec -it container-com-bind-mount bash

# Mostrando que dentro do container também possui quatro arquivos:
ls -lh /app/exemplo/

exit

# Criando um segundo container para mostrar que o contéudo mapeado via bind mount estará disponível, foi mudado apenas o diretório que fica dentro do container:
docker run -dit -v /meu-app:/app/exemplo2 --name container-com-bind-mount2 ubuntu

docker exec -it container-com-bind-mount2 bash

# Mostrando que os quatro arquivos também estão disponíveis neste novo container:
ls -lh /app/exemplo2/

exit

# Excluindo o diretório e os arquivos que estavam sendo usado para o bind mount:
rm -rf /meu-app

# Diretório criado para mostrar uma nova de criação de volume do tipo bind mount, pois ao usar a opção --mount, se o diretório já não existir será exibido um erro em tela e o container não será criado:
mkdir /meu-novo-app

# Criando um terceiro container para mostrar que é possível criar de outra maneira um volume do tipo bind mount:
docker run -dit --mount type=bind,source=/meu-novo-app,target=/novoapp/exemplo3 --name container-com-bind-mount3 ubuntu

# Criando um arquivo fora do container:
touch /meu-novo-app/arquivo1.txt

docker exec -it container-com-bind-mount3 bash

# Provando que o arquivo está recém criado está disponível dentro do container:
ls -lh /novoapp/exemplo3/

# Criando um arquivo dentro do container:
touch /novoapp/exemplo3/arquivo2.txt

# Provando que os dois arquivos recém criados estão disponíveis fora do container:
ls -lh /meu-novo-app
```

---
