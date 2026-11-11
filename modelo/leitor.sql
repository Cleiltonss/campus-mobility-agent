-- Usuário do agente: só lê.
--
-- Um usuário novo nasce sem permissão nenhuma; o GRANT concede só o válido
-- (SELECT). DELETE, UPDATE, DROP e TRUNCATE não precisam ser listados: o que
-- não foi concedido é recusado pelo banco.
--
-- A senha não fica neste arquivo (o repositório é público). Ela vem da
-- variável `senha` do psql:
--
--   docker compose exec -T database psql -U alfred -d transportes \
--     -v ON_ERROR_STOP=1 -v senha="$AGENTE_SENHA" < leitor.sql

CREATE ROLE agent LOGIN PASSWORD :'senha';
GRANT SELECT ON ALL TABLES IN SCHEMA public TO agent;

-- Teto de tempo por consulta para quem entra como agent, de onde for
-- (também no psql). Um SELECT só de leitura ainda trava o banco: um JOIN do
-- fato com ele mesmo sem condição dá 2,7 milhões x 2,7 milhões de linhas.
ALTER ROLE agent SET statement_timeout = '5s';
