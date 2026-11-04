# Criando imagem Docker no padrão OCI

### Sumário
- [Descrição](#descrição)
- [Endereços na Web](#endereços-na-web)

---

### Descrição

Será mostrado como criar uma imagem Docker usando o padrão da OCI (Open Container Initiative).

---

### Prática

```bash
# Criando o diretório do projeto:
mkdir -p /oci
cd /oci
```

Criando o Dockerfile:
```bash
vim Dockerfile
```
```dockerfile
# Conteúdo
FROM alpine:3.18
RUN apk add --no-cache curl
# Mantém o container rodando indefinidamente em segundo plano
CMD ["sleep", "infinity"]
```

```bash
# Fazendo o build da imagem usando o builx
docker buildx build -t minha-imagem-oci:1.0.0 --output type=oci,dest=minha-imagem-oci-1.0.0.tar .
# Obs: O "type=oci": Força a exportação estritamente no formato de layout de imagem OCI (com manifestos, camadas e o arquivo oci-layout na raiz).
# Obs2: dest=minha-imagem-oci.tar: Salva o resultado diretamente em um arquivo compactado tarball compatível com OCI.
```

```bash
# Para inspecionar o interior do arquivo tar para confirmar a estrutura padrão da OCI (que inclui o arquivo oci-layout, index.json e a pasta blobs):
tar -tf minha-imagem-oci-1.0.0.tar
# Foi possível vem os arquivos abaixo:
# blobs/
# blobs/sha256/
# blobs/sha256/23c7c93f800fa3dac858ad13b988289844c3cd151dcfaad42a310b10bc3b0072
# blobs/sha256/29e57413c4e1a738c0349966ca484fc75b7f9874237878ed179f1e3d05aa5786
# blobs/sha256/44cf07d57ee4424189f012074a59110ee2065adfdde9c7d9826bebdffce0a885
# blobs/sha256/60f4acc5ee1f9b375ca52d52c8160c15301441315bd222bac2419430af311148
# index.json
# oci-layout
```

Testando a imagem, usando a ferramenta skopeo:
```bash
apt install skopeo
skopeo copy oci:minha-imagem-oci-1.0.0.tar docker-daemon:minha-imagem-oci:1.0.0
# Obs: O Skopeo é uma ferramenta de linha de comando de código aberto, leve e sem daemon, usada para manipular, inspecionar, copiar e assinar imagens de contêineres e repositórios remotos.
```

Sudindo o coantainer com base na imagem padrão OCI:
```bash
docker run --rm minha-imagem-oci:latest
```


---
