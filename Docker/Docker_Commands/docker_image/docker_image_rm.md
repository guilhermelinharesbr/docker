# Docker IMAGE RM

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Apelidos](#apelidos)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker image rm** remove uma ou mais imagens.

Para remover uma imagem é importante certifica-se que não tenha um container em execução ou parado, caso exista só será possível remover a imagem após remover o container ou forçar a remoção da imagem com a opção -f.

---

### Sintaxe

docker **image rm** [OPTIONS] IMAGE [IMAGE...]

---

### Apelidos

- docker **image remove** 
- docker **rmi**

---

### Opções

As opções podem ser vistas por meio do comando `docker rmi --help` sendo elas:

- **-f**, **--force** -> Força a remoção da imagem.

---

### Exemplos

Ex Remove a imagem de nome node:
```bash
docker image rm node
```

--

Ex2 Remove a imagem de nome hello-world passando a tag latest, muito útil para quando se tem várias versões de uma mesma imagem:
```bash
docker image rm hello-world:latest
```

--

Ex3. força a remoção da imagem de nome ubuntu, mesmo que ela tenha algum container em execução:
```bash
docker image rm -f ubuntu 
```

--

Ex4. o primeiro comando feito é o de dentro do parênteses ele lista as imagens docker e depois o resultado é jogado para o comando de fora do parenteses, que ele remove as imagens não utilizadas: 
```bash
docker image rm $(docker image ls -q)
ou
docker image rm $(docker image list -q)
ou
docker image rm $(docker images -q)   
```

---
