# Docker HUB

### Sumário
- [Descrição](#descrição)
- [Links úteis](#links-úteis)
- [Outros Container Registries](#outros-container-registries)

---

### Descrição

O **Docker Hub** simplifica o desenvolvimento com o maior container registry do mundo para armazenar, gerenciar e compartilhar imagens Docker. Ao se integrar perfeitamente às suas ferramentas, ele aumenta a produtividade e garante a implantação, distribuição e acesso confiáveis ​​a aplicativos em containeres. Também fornece aos desenvolvedores imagens e recursos pré-construídos para acelerar os fluxos de trabalho de desenvolvimento.

Principais recursos do Docker Hub:

- Repositórios públicos ilimitados
- Repositórios privados
- Webhooks para automatizar fluxos de trabalho
- Integrações com GitHub e Bitbucket
- Builds simultâneos e automatizados
- Conteúdo confiável com imagens seguras e de alta qualidade

Além da interface gráfica, pode-se interagir com o Docker Hub usando a API do Docker Hub, a ferramenta experimental Docker Hub CLI ou o servidor Docker Hub MCP para integrações com agentes de IA.

---

### Links úteis

- [Docker Hub site](https://hub.docker.com/)
- [Docker Hub documentação](https://docs.docker.com/docker-hub/)

---

### Outros Container Registries

Além do Docker Hub existem outros Container Registries, entre eles:

- [Amazon Elastic Container Registry (ECR)](https://aws.amazon.com/pt/ecr/) -> Armazene, compartilhe e implante facilmente seu software de contêiner em qualquer lugar. É o padrão da indústria para ambientes corporativos que rodam na nuvem da AWS. Oferece alta segurança, integração nativa com o IAM para controle de acesso restrito e escaneamento automático de vulnerabilidades em tempo real nas imagens.
- [Azure Container Registry](https://azure.microsoft.com/en-in/products/container-registry) -> Um registro de imagens Docker e Open Container Initiative (OCI), com suporte para todos os artefatos OCI. Perfeito para ambientes que rodam em servidores Windows/Linux na Azure ou integrados ao AKS (Azure Kubernetes Service). Possui recursos avançados de replicação geográfica entre regiões e webhooks para automação
- [GitHub Packages (GHCR)](https://docs.github.com/pt/packages/learn-github-packages/introduction-to-github-packages) -> uma boa opção para quem já usa o GitHub para versionar código, pois facilita a criação de pipelines de CI/CD automatizadas (GitHub Actions) para build e push direto. Oferece controle granular de permissões por repositório ou organização.
- [GitLab Container Registry](https://docs.gitlab.com/user/packages/container_registry/) -> O registro nativo embutido nas ferramentas de DevOps do GitLab. Ideal para equipes que utilizam o GitLab CI/CD. Cada projeto do GitLab pode ter seu próprio registro de containers vinculado de forma transparente, simplificando a autenticação e o versionamento das imagens junto ao código-fonte.
- [Google Artifact Registry)](https://docs.cloud.google.com/artifact-registry/docs?hl=pt-br) -> é o serviço de armazenamento de artefatos do Google Cloud Platform (subcessor do antigo Google Container Registry). Totalmente integrado ao GCP e ao Kubernetes (GKE). Suporta não apenas imagens OCI/Docker, mas também pacotes de linguagens (como npm, Maven, Python), com forte criptografia e gerenciamento global de redes.
- [Harbor](https://goharbor.io/) -> Um registry enterprise de código aberto pode-se instalar e gerenciar na sua infraestrutura própria (on-premise). Se uma empresa não quiser depender de nuvens públicas nem do Docker Hub, o Harbor oferece uma interface web completa, suporte a múltiplos tenants, replicação de imagens entre servidores, controle de acesso baseado em papéis (RBAC) e segurança com antivírus/Clair integrado.
- [Red Hat Quay.io](https://www.redhat.com/en/technologies/cloud-computing/quay) -> Um registry robusto focado em segurança e gerenciamento avançado, mantido pela Red Hat. Muito conhecido por suas ferramentas avançadas de análise de segurança, varredura profunda de vulnerabilidades por CVE em camadas de imagens e suporte a políticas rígidas de acesso corporativo.

---
