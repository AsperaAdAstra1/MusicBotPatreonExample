# 🔐 Como Criar e Configurar seu Arquivo `.env`

Este guia explica, passo a passo, como criar o arquivo `.env` que guarda o token secreto do seu bot — sem ele, o bot não consegue se conectar ao Discord.

## O que é o `.env` e por que ele existe?

O `.env` é um arquivo de texto simples onde você guarda informações sensíveis (como senhas e tokens) **fora** do código principal. Isso existe por um motivo importante:

> Se você colocasse o token direto dentro do arquivo `.py` e depois subisse esse código para o GitHub (ou compartilhasse com alguém), qualquer pessoa poderia pegar seu token e controlar seu bot como se fosse você.

Separando o token num arquivo `.env`, você consegue compartilhar seu código livremente sem expor nada sensível — basta nunca subir o `.env` junto.

## Passo 1: Pegue o token do seu bot no Discord

1. Acesse [discord.com/developers/applications](https://discord.com/developers/applications) e faça login com sua conta do Discord
2. Clique em **"New Application"** no canto superior direito
3. Dê um nome para o seu bot e clique em **"Create"**
4. No menu lateral esquerdo, clique em **"Bot"**
5. Clique no botão **"Reset Token"** (ou **"View Token"**, se for a primeira vez)
6. Clique em **"Copy"** para copiar o token — ele só aparece uma vez, então copie e guarde num lugar seguro antes de sair da página

⚠️ **Esse token é como uma senha.** Qualquer pessoa que tiver ele pode controlar seu bot. Nunca poste ele em prints, chats ou repositórios públicos.

## Passo 2: Crie o arquivo `.env`

### No Windows

1. Abra a pasta do seu projeto (onde está o arquivo `.py` do bot)
2. Clique com o botão direito em uma área vazia → **Novo** → **Documento de Texto**
3. Renomeie o arquivo para `.env` — apague completamente o nome antigo e a extensão `.txt`, deixando só `.env`
4. O Windows vai perguntar se você tem certeza de mudar a extensão — clique em **"Sim"**

> **Dica:** se o Windows não deixar o arquivo ficar só com `.env` (sem nome antes do ponto), abra o Bloco de Notas, escreva o conteúdo do passo 3 abaixo, depois vá em **Arquivo → Salvar Como**, escolha o tipo **"Todos os Arquivos (*.*)"** e salve como `.env` na pasta do projeto.

### No Mac/Linux

Pelo terminal, dentro da pasta do projeto:

```bash
touch .env
```

Depois abra o arquivo com qualquer editor de texto (VS Code, nano, etc).

## Passo 3: Coloque o token dentro do arquivo

Abra o `.env` que você acabou de criar e escreva uma única linha, substituindo pelo seu token real (sem aspas, sem espaços antes ou depois do `=`):

```
DISCORD_TOKEN=cole_seu_token_aqui
```

Salve o arquivo.

## Passo 4: Confirme que está tudo certo

Sua pasta do projeto deve ter, no mínimo:

```
minha-pasta-do-bot/
├── BOTDISCORD.py
├── .env          ← seu arquivo com o token (nunca compartilhe!)
└── .gitignore    ← garante que o .env não vá pro GitHub
```

Se o seu `.gitignore` ainda não tiver essa linha, adicione:

```
.env
```

## Passo 5: Teste

Rode o bot normalmente:

```bash
python BOTDISCORD.py
```

Se aparecer `Bot conectado como <nome-do-seu-bot>` no terminal, o `.env` foi lido com sucesso e o token funcionou.

## Erros comuns

| Erro | Causa provável |
|---|---|
| `discord.errors.LoginFailure: Improper token has been passed` | Token errado, incompleto, ou com espaço extra colado por engano |
| O bot não conecta e não dá nenhum erro claro | O arquivo `.env` está com nome errado (ex: `.env.txt` em vez de `.env`) |
| `KeyError` ou `None` ao carregar o token | Faltou a linha `DISCORD_TOKEN=...` no arquivo, ou o nome da variável está diferente do que o código espera |

## Se você acidentalmente expôs seu token

Se você subiu o `.env` sem querer para o GitHub, ou colou o token em algum lugar público:

1. Volte no [Discord Developer Portal](https://discord.com/developers/applications)
2. Vá em **Bot → Reset Token**
3. Isso invalida o token antigo imediatamente e gera um novo
4. Atualize seu `.env` local com o novo token

Não tem problema nenhum resetar o token quantas vezes precisar — é rápido e resolve o problema na hora.
