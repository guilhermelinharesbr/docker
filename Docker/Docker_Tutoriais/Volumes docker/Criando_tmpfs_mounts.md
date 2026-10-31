# Criando Tmpfs Mounts

### Sumário
- [Descrição](#descrição)
- [Prática](#prática)

---

### Descrição

Os _Docker Volumes_ e _Bind Mounts_ permitem compartilhar arquivos entre a máquina host e o container, possibilitando a persistência de dados mesmo após a interrupção do container.

Se você estiver executando o Docker no Linux, terá uma terceira opção: **tmpfs mounts**. Ao criar um container com um tmpfs mount, o container pode criar arquivos fora da camada gravável do container.

Ao contrário de _Docker Volumes_ e _Bind Mounts_, um _tmpfs mount_ é temporároa e persiste apenas na memória do host. Quando o container é interrompido, o tmpfs mount é removido e os arquivos gravados nele não serão persistidos.

Como o tmpfs armazena dados na memória, esse uso é contabilizado no limite de memória do cgroup do container (--memory / Compose mem_limit). Definir um tamanho de tmpfs grande (ou montar o tmpfs no host) não fornece RAM extra ao container além desse limite, preencher a montagem ainda pode causar um erro de falta de memória (OOM) no container. As métricas de memória do container incluem o uso do tmpfs; consulte as métricas de tempo de execução. As montagens tmpfs são mais adequadas para casos em que você não deseja que os dados persistam na máquina host ou dentro do container. Isso pode ser necessário por motivos de segurança ou para proteger o desempenho do container quando seu aplicativo precisa gravar um grande volume de dados de estado não persistentes.

---

### Prática

Será mostrado como é o funcionamento do tmpfs mount.

```bash
# Criando um container que usa tmpfs mount e este diretório dentro do container terá o nome de meu-app, e tem como base uma imagem ubuntu:
docker run -dit --tmpfs=/meu-app --name cont-com-tmpfs-mount ubuntu

docker exec -it cont-com-tmpfs-mount bash

# Visto que o diretório /meu-app é um diretório com permissões de diretório temporário, como o /tmp:
ls -lh 

touch /meu-app/arquivo1.txt

# Mostrando que o arquivo foi criado:
ls -lh /meu-app/

exit

# Ao parar o container e iniciar ele novamente o diretório /meu-app para de ser do tipo temporário e os arquivos que estivessem dentro terão sido excluídos:
docker container stop cont-com-tmpfs-mount

docker container start cont-com-tmpfs-mount

docker exec -it cont-com-tmpfs-mount bash

# Visto que o diretório /meu-app deixou de ser um diretório temporário:
ls -lh

# Mostrando que o arquivo de nome arquivo1.txt não existe mais:
ls -lh /meu-app/

exit

# Criando de uma segunda forma um container que usa tmpfs mount e este diretório dentro do container terá o nome de meu-app2, e tem como base uma imagem ubuntu:
docker run -dit --mount type=tmpfs,destination=/meu-app2 --name cont-com-tmpfs-mount2 ubuntu
```

---
