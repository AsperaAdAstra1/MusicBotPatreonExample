# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------
#Bot exemplo  - musicas do soundcloud,rádio mensagens de bem-vindo e extras!!
# -----------------------------------------------------------------------------
#1. a ideia de botar um bot com música já é um pouco além do python básico!! por isso vamos precisar de ferramentas além das que já vem pre instaladas!!
#2. a parte da mensagem de boas vindas até que é bem simples de fazer
#3. ideias novas (tive a ideia de botar estações de rádio online, mas não sei se vai funcionar direito)
#4. o bot vai tocar músicas do soundcloud, porque o youtube tem muitas restrições(eu posso até ensinar a fazer um bot que toca do youtube, Mas apenas para uso pessoal, nunca para compartilhar com outras pessoas, porque o youtube não permite isso)!!!! talvez isso seja uma boa ideia!!!
ESTACOES_RADIO = {
    'lofi': 'https://coderadio-admin-v2.freecodecamp.org/listen/coderadio/radio.mp3',
    'synthwave': 'https://stream.nightride.fm/nightride.mp3',
    'chillhop': 'https://ice1.somafm.com/groovesalad-128-mp3',
    'jazz': 'http://tsfjazz.ice.infomaniak.ch/tsfjazz-high.mp3',
    # Você pode encontrar e adicionar mais estações de rádios como preferir só adiciona as ‘strings’ corretamente tipo 'açúcar': 'link da rádio'
}

# Biblioteca principal para interagir com o Discord
#pip install discord.py

# Biblioteca para baixar o áudio do YouTube
#pip install yt-dlp

# Biblioteca necessária para a criptografia de áudio do Discord
#pip install PyNaCl

#imports: imports necessários
import discord
from discord.ext import commands, tasks
import yt_dlp
from dotenv import load_dotenv
import os
import difflib  # biblioteca padrão do Python, já vem instalada -> usamos pra sugerir estações parecidas quando o usuário erra o nome
#instale o FFmpeg: https://ffmpeg.org/download.html!!!  é a ferramenta que o bot vai usar para processar o aúdio, e é o único programa extra que vamos utilizazr,além das bibliotecas python
# o FFmpeg trabalha em conjunto com a biblioteca yt-dlp para extrair o áudio dos vídeos do YouTube(ela entrega o aúdio de forma bruta, e o FFmpeg converte para um formato que o Discord consegue entender)

intents = discord.Intents.default()
intents.guilds = True
intents.voice_states = True
intents.messages = True
intents.message_content = True
intents.members = True  # Necessário para detectar membros que entram no servidor

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)#eu defini o prefixo como "!" mas você pode mudar
#isso significa que todos os comandos do bot vão começar com "!" (ex: !play)
#tambem desativei o comando de ajuda padrão do discord, porque eu vou fazer um personalizado

YDL_OPTIONS = {
    'format': 'bestaudio/best',
    'noplaylist': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}


@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')
    print('DJ dos crias!')# aqui você pode colocar qualquer mensagem que quiser é o status do bot a partir do momento que ele fica online
    print('---------------------------------------')


@bot.command(name='tocar', aliases=['play'])
async def tocar(ctx, *, search: str):
    """
    Comando para tocar uma música do SoundCloud.
    Uso: !tocar <nome da música e artista>
    """
    if not ctx.author.voice:
        await ctx.send("Você não está em um canal de voz para que eu possa entrar!")
        return

    canal_voz = ctx.author.voice.channel
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    if not voice_client:
        voice_client = await canal_voz.connect()
    elif voice_client.channel != canal_voz:
        await voice_client.move_to(canal_voz)

    if voice_client.is_playing():
        voice_client.stop()



    # Adicionamos uma mensagem de feedback para o usuário.
    await ctx.send(f'🔎 Procurando no SoundCloud por: `{search}`...')

    # Primeiro, definimos a consulta e as opções que vamos usar
    query = search
    ydl_opts_to_use = YDL_OPTIONS.copy()  # Usamos uma cópia para poder modificar

    if not search.startswith('http'):
        # Se não for um link, formatamos como uma busca no SoundCloud
        query = f"scsearch:{search}"
        # E permitimos que a busca retorne resultados de playlists
        ydl_opts_to_use['noplaylist'] = False

    # Agora, executamos a extração com as opções corretas
    try:
        with yt_dlp.YoutubeDL(ydl_opts_to_use) as ydl:
            info = ydl.extract_info(query, download=False)
            # Se a busca retornar uma lista ('entries'), pegamos o primeiro resultado
            if 'entries' in info:
                info = info['entries'][0]

    except Exception as e:
        # Adicionei um print para vermos o erro exato no terminal, o que ajuda muito!
        print(f"Ocorreu um erro no yt-dlp: {e}")
        await ctx.send(
            "Não consegui encontrar essa música no SoundCloud. Tente ser mais específico ou use um link direto.")
        return

    url = info['url']
    # Pegamos o título da música para informar o usuário. !!
    # Também pegamos o nome do artista ou do cara q upou para uma mensagem mais completa.
    titulo = info.get('title', 'Título desconhecido')
    artista = info.get('uploader', 'Artista desconhecido')

    await ctx.send(f'**Tocando agora do SoundCloud:** 🎵 `{titulo}` por `{artista}`')

    voice_client.play(discord.FFmpegPCMAudio(url))


# colocamos o comando parar pra poder desconectar o bot do canal de voz
@bot.command(name='parar', aliases=['stop'])
async def parar(ctx):
    """
    Comando para parar a música e desconectar o bot do canal de voz.
    Uso: !parar
    """
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    if voice_client and voice_client.is_connected():
        await voice_client.disconnect()
        await ctx.send("Música parada e eu saí do canal! 👋")
    else:
        await ctx.send("Eu não estou em nenhum canal de voz no momento.")

# comando para tocar rádio online
# você pode adicionar mais estações ao dicionário ESTACOES_RADIO no início do código

@bot.command(name='radio')
async def radio(ctx, *, nome_estacao: str = None):
    """Sintoniza e toca uma estação de rádio online."""

    if nome_estacao is None:
        # Se o usuário não digitar um nome, lista as estações disponíveis!!! nao sei se vou botar isso no help do bot tbm
        lista_estacoes = "\n".join(f"- `{nome}`" for nome in ESTACOES_RADIO.keys())
        embed_lista = discord.Embed(
            title="📻 Estações de Rádio Disponíveis",
            description=f"Para tocar, use `!radio <nome>`.\n\n{lista_estacoes}",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed_lista)
        return

    # Procura o nome da estação no nosso dicionário (converte para minúsculas para facilitar)
    nome_busca = nome_estacao.lower().strip()
    estacao_url = ESTACOES_RADIO.get(nome_busca)

    if not estacao_url:
        # Não achou exato -> tenta sugerir a estação mais parecida (corrige erro de digitação tipo "chilhop" -> "chillhop")
        nomes_disponiveis = list(ESTACOES_RADIO.keys())
        sugestoes = difflib.get_close_matches(nome_busca, nomes_disponiveis, n=1, cutoff=0.6)

        if sugestoes:
            sugestao = sugestoes[0]
            await ctx.send(
                f"Não encontrei a rádio `{nome_estacao}`. Você quis dizer `{sugestao}`? "
                f"Digite `!radio {sugestao}` para tocar, ou `!radio` para ver todas as opções."
            )
        else:
            lista_estacoes = ", ".join(f"`{nome}`" for nome in nomes_disponiveis)
            await ctx.send(
                f"Não encontrei a rádio `{nome_estacao}`. Estações disponíveis: {lista_estacoes}."
            )
        return
    #voltei aqui porque as radios tinham saído do ar e eu ainda não tinha upado o bot kkk, deixei um aviso falando pra reescrever o código caso as rádios caiam. os softwares são atualizados sempre. por isso se você QUISER PROGRAMAR tem q se acostumar com as coisas funcionando num dia e no outro não. vai atualizar pip no cmd e quebrar e ler o prompt todo, já se acostuma!

    # O resto do código é muito parecido com o que já temos
    if not ctx.author.voice:
        await ctx.send("Você precisa estar num canal de voz para eu sintonizar a rádio!")
        return

    canal_voz = ctx.author.voice.channel
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    if not voice_client:
        voice_client = await canal_voz.connect()
    elif voice_client.channel != canal_voz:
        await voice_client.move_to(canal_voz)

    if voice_client.is_playing():
        voice_client.stop()

    await ctx.send(f"Sintonizando na rádio: **{nome_busca.capitalize()}**... 🎶")

    # Usamos FFmpeg diretamente com o link do stream da rádio
    # before_options com reconexão: se o stream cair um instante, o FFmpeg tenta reconectar sozinho
    # em vez de simplesmente travar o áudio no bot
    ffmpeg_reconnect_options = '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5'
    voice_client.play(discord.FFmpegPCMAudio(estacao_url, before_options=ffmpeg_reconnect_options))

#  comando padrão de ajuda, que mostra os comandos disponíveis
@bot.command(name='ajuda', aliases=['help'])
async def ajuda(ctx):
    """Mostra esta mensagem de ajuda."""
    # Primeiro, criamos o objeto Embed. O título e a descrição são a base.
    embed_ajuda = discord.Embed(
        title="🎧 Ajuda do Bot de Música 🎧",
        description="Olá! Eu sou um bot de música que toca faixas diretamente do SoundCloud.",
        color=discord.Color.orange()  # Você pode escolher outras cores, como .blue(), .green(), .purple()
    )
    embed_ajuda.set_thumbnail(url="https://i.imgur.com/N3ce5uC.png")
    # Agora, adicionamos "campos" (Fields) para cada comando, explicando o que fazem.
    # O parâmetro 'inline=False' faz com que cada campo ocupe uma linha inteira, deixando mais organizado.
    embed_ajuda.add_field(
        name="`!tocar` ou `!play`",
        value="Busca e toca uma música do SoundCloud no canal de voz em que você está.\n**Exemplo:** `!tocar justice genesis`",
        inline=False
    )

    embed_ajuda.add_field(
        name="`!parar` ou `!stop`",
        value="Para a música que está a tocar e me desconecta do canal de voz.",
        inline=False
    )

    embed_ajuda.add_field(
        name="`!ajuda` ou `!help`",
        value="Mostra esta mensagem detalhada sobre todos os comandos.",
        inline=False
    )

    embed_ajuda.add_field(
        name="`!radio(nome da estação)`",
        value="Sintoniza e toca uma estação de rádio online. Digite `!radio` para ver a lista de estações disponíveis.",
        inline=False
    )

    # Por fim, podemos adicionar um rodapé para dar um toque final.
    embed_ajuda.set_footer(text="Bot criado para a comunidade do Patreon!")

    # Enviamos a mensagem para o canal. Note que usamos 'embed=embed_ajuda'.
    await ctx.send(embed=embed_ajuda)
# aqui fora dos comandos das musicas vamos botar o comando pra ele saudar os novos membros do  servidor  !!
@bot.event
async def on_member_join(member):
    canal = discord.utils.get(member.guild.text_channels, name='geral') # Altere para o nome do canal desejado
    if canal:
        await canal.send(f"Bem-vindo(a) ao servidor, {member.mention}! 🎉")#você pode personalizar a mensagem como quiser


# Lembre-se de colocar o seu token aqui.
load_dotenv()
TOKEN =os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)