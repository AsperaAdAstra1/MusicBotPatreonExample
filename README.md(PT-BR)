# 🎧 Bot de Música para Discord (SoundCloud + Rádio Online)

Bot de exemplo em Python que toca músicas do SoundCloud e estações de rádio online direto em um canal de voz do Discord. Também dá as boas-vindas a novos membros do servidor.

> Este projeto é um exemplo educacional, feito para ensinar os conceitos básicos de como criar um bot de música. Não é o bot completo usado em produção — é uma versão simplificada, pensada para quem está começando.

## O que ele faz

- 🎵 Toca músicas do SoundCloud a partir de um nome de busca ou link direto (`!tocar` / `!play`)
- 📻 Toca estações de rádio online pré-configuradas (`!radio`)
- 🛑 Para a música e desconecta do canal de voz (`!parar` / `!stop`)
- 👋 Envia mensagem de boas-vindas para novos membros do servidor
- ❓ Comando de ajuda com todos os comandos disponíveis (`!ajuda` / `!help`)

## Pré-requisitos

Antes de rodar o bot, você precisa ter instalado:

1. **Python 3.10+** — [python.org](https://www.python.org/downloads/)
2. **FFmpeg** — ferramenta que converte o áudio para um formato que o Discord entende. [Baixe aqui](https://ffmpeg.org/download.html) e adicione ao PATH do seu sistema.
3. Um **bot criado no Discord Developer Portal** com o token de acesso em mãos ([discord.com/developers/applications](https://discord.com/developers/applications))

## Instalação

Clone o repositório e instale as dependências:

```bash
git clone <link-do-seu-repositorio>
cd <nome-da-pasta>
pip install discord.py yt-dlp python-dotenv PyNaCl
```

> **Importante:** o Discord passou a exigir o protocolo de criptografia DAVE para conexões de voz. Se o bot der erro `4017` ao tentar entrar em um canal de voz, atualize as bibliotecas:
> ```bash
> pip install -U discord.py
> pip install -U davey
> ```

## Configuração

1. Crie um arquivo chamado `.env` na raiz do projeto (use o `.env.example` como base)
2. Dentro dele, adicione seu token do bot:

```
DISCORD_TOKEN=seu_token_aqui
```

⚠️ **Nunca compartilhe ou suba o arquivo `.env` para o GitHub.** Ele já está listado no `.gitignore` deste projeto por segurança.

## Como rodar

```bash
python BOTDISCORD.py
```

Se tudo estiver certo, o terminal vai mostrar `Bot conectado como <nome-do-bot>`.

## Comandos disponíveis

| Comando | O que faz |
|---|---|
| `!tocar <nome ou link>` | Busca e toca uma música do SoundCloud |
| `!radio` | Lista as estações de rádio disponíveis |
| `!radio <nome>` | Sintoniza e toca uma estação específica |
| `!parar` | Para a música e desconecta o bot do canal de voz |
| `!ajuda` | Mostra todos os comandos com exemplos |

## Adicionando novas estações de rádio

No topo do arquivo `BOTDISCORD.py`, edite o dicionário `ESTACOES_RADIO`:

```python
ESTACOES_RADIO = {
    'lofi': 'http://stream.lofi.live/radio',
    'sua_estacao': 'link-direto-do-stream-mp3-ou-similar',
}
```

## Por que SoundCloud e não YouTube?

O YouTube tem restrições de Termos de Serviço para bots que extraem áudio de vídeos para reprodução compartilhada. Por isso este exemplo usa o SoundCloud, que tem uma política mais permissiva para esse tipo de uso.

## Aviso

Este código é para fins educacionais. Adapte, quebre, estude e use como quiser para aprender — mas fique de olho nos Termos de Serviço de cada plataforma antes de usar em produção ou compartilhar publicamente.
