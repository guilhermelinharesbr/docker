# Docker ENGINE

### Sumário
- [Descrição](#descrição)
- [Fonte de Pesquisa](#fonte-de-pesquisa)

---

### Descrição

O **Docker Engine** é o principal ambiente de execução de containeres de código aberto que cria e gerencia containeres, constrói imagens e fornece a API do Docker. Ele funciona em Linux, Windows e macOS, servindo como base para o Docker Desktop e instalações independentes do Docker em servidores.

O Docker Engine é uma tecnologia de containeres de código aberto para construir e conteinerizar seus aplicativos. O Docker Engine atua como um aplicativo cliente-servidor com:

- Um servidor com um processo _daemon_ de longa duração, o **dockerd**.
- APIs que especificam interfaces que os programas podem usar para se comunicar com o daemon do Docker e instruí-lo.
- Um cliente de interface de linha de comando (CLI), o docker.

A CLI usa as APIs do Docker para controlar ou interagir com o daemon do Docker por meio de scripts ou comandos diretos da CLI. Muitos outros aplicativos Docker usam a API e a CLI subjacentes. O daemon cria e gerencia objetos do Docker, como imagens, containeres, redes e volumes.

O Docker Engine é composto:
- **dockerd** -> É o grande processo servidor que roda em segundo plano no seu sistema operacional. Ele é o verdadeiro "motor" e gerencia todo o ciclo de vida dos objetos do Docker. É o dockerd que recebe os comandos (via API ou CLI), gerencia imagens, redes, volumes e coordena a criação dos containers.
- **Docker Engine API** -> é uma API RESTful exposta pelo Daemon do Docker (dockerd). Como ela segue o padrão HTTP, qualquer linguagem de programação (Python, Node.js, Go, Shell Script com curl) ou ferramenta externa pode conversar diretamente com o motor do Docker para criar containers, gerenciar imagens, inspecionar redes e monitorar recursos sem precisar passar pela CLI tradicional.
- **CLI Docker** -> É a interface de linha de comando (docker run, docker ps, docker build) onde digita-se no terminal. Ela não gerencia containers diretamente; o único papel da CLI é traduzir os seus comandos em requisições HTTP e enviá-las para a API do Docker Daemon.
- **containerd** -> Por baixo dos panos, o Docker Daemon não fala diretamente com o kernel do Linux para criar o container do zero. Ele delega essa tarefa pesada para o containerd. O containerd é um daemon de nível inferior (industry-standard container runtime) responsável por gerenciar o ciclo de vida completo do container: supervisão de processos, armazenamento de imagens, transferência, montagem de sistemas de arquivos e execução.
- **runc** -> Se o containerd é o gerente, o runc é o executor final. Ele é uma ferramenta leve e especializada em apenas uma coisa: interagir diretamente com os recursos do kernel do Linux (Namespaces, Cgroups e SELinux) para efetivamente criar, iniciar e matar o processo isolado (o container). O runc segue rigorosamente as especificações da OCI (Open Container Initiative).
- **Bibliotecas de Rede e Armazenamento (Libnetwork e Plugins)**:
    - Libnetwork: É o subsistema responsável por criar e gerenciar a infraestrutura de rede dos containers (redes bridge, overlay, macvlan), garantindo o isolamento e a comunicação entre eles.
    - Gerenciadores de Volume: Módulos que permitem que o Docker monte e gerencie volumes persistentes (armazenamento local ou drivers para nuvem) para que os dados sobrevivam ao ciclo de vida do container.

---

### Fonte de Pesquisa

- [Docker Engine](https://docs.docker.com/engine/)

---
