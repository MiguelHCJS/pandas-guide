# Comandos para criar container de banco de dados

Util para abstrair a necessidade de instalar e configurar Banco de dados.

```bash
   docker pull postgres

   docker volume create [nome_do_volume]

   docker run -d --name [nome_do_container] -p 5433:5432 -e POSTGRES_PASSWORD=[sua_senha] -v [nome_do_volume]:/var/lib/postgresql/data postgres

   psql -h localhost -p 5432 -U postgres
```
