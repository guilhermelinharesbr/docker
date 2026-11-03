# Docker NETWORK CREATE

### Sumário
- [Descrição](#descrição)
- [Sintaxe](#sintaxe)
- [Opções](#opções)
- [Exemplos](#exemplos)

---

### Descrição

O **docker network create** cria uma nova rede. O parâmetro `--driver` aceita os drivers **bridge** ou **overlay**, que são os drivers de rede integrados. Se for instalado um driver de rede de terceiros ou um driver personalizado, também pode especificá-lo aqui. Se não especificar a opção **--driver**, o comando criará automaticamente uma rede bridge. Ao instalar o Docker Engine, uma rede bridge é criada automaticamente. Essa rede corresponde à _docker0 bridge_, na qual o Docker Engine tradicionalmente se baseia. Quando inicia-se um novo container com `docker container run`, ele se conecta automaticamente a essa rede bridge. Não pode remover essa rede bridge padrão, mas pode criar novas usando o comando `docker network create`.

---

### Sintaxe

docker **network create** [OPTIONS] NETWORK

---

### Opções

As opções podem ser vistas por meio do comando `docker network create --help` sendo elas:

- **-d**, **--driver** -> configura o driver para gerenciar a rede.

---

### Exemplos

Ex. Criando uma rede com driver bridge de nome minha-rede:
```bash
docker network create --driver bridge minha-rede
```


---
