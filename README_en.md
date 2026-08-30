# 🎧 Discord Music Bot (SoundCloud + Online Radio)

Example Python bot that plays music from SoundCloud and online radio stations directly in a Discord voice channel. It also welcomes new members to the server.

> This project is an educational example, built to teach the basics of how to create a music bot. It's not the full production bot — it's a simplified version, made for people who are just getting started.

## What it does

- 🎵 Plays SoundCloud tracks from a search term or a direct link (`!tocar` / `!play`)
- 📻 Plays pre-configured online radio stations (`!radio`)
- 🛑 Stops the music and disconnects from the voice channel (`!parar` / `!stop`)
- 👋 Sends a welcome message to new server members
- ❓ Help command listing all available commands (`!ajuda` / `!help`)

> Note: commands are in Portuguese (`!tocar`, `!parar`, `!ajuda`) since this example was built for a Brazilian audience. Feel free to rename them in the code if you prefer English commands.

## Prerequisites

Before running the bot, you'll need:

1. **Python 3.10+** — [python.org](https://www.python.org/downloads/)
2. **FFmpeg** — the tool that converts audio into a format Discord can understand. [Download here](https://ffmpeg.org/download.html) and add it to your system PATH.
3. A **bot created in the Discord Developer Portal** with its access token in hand ([discord.com/developers/applications](https://discord.com/developers/applications))

## Installation

Clone the repository and install the dependencies:

```bash
git clone <your-repository-link>
cd <folder-name>
pip install discord.py yt-dlp python-dotenv PyNaCl
```

> **Important:** Discord now requires the DAVE encryption protocol for voice connections. If the bot throws a `4017` error when trying to join a voice channel, update the libraries:
> ```bash
> pip install -U discord.py
> pip install -U davey
> ```

## Configuration

1. Create a file called `.env` in the project root (use `.env.example` as a template)
2. Inside it, add your bot token:

```
DISCORD_TOKEN=your_token_here
```

⚠️ **Never share or upload the `.env` file to GitHub.** It's already listed in this project's `.gitignore` for safety.

## How to run

```bash
python BOTDISCORD.py
```

If everything is set up correctly, the terminal will show `Bot conectado como <bot-name>`.

## Available commands

| Command | What it does |
|---|---|
| `!tocar <name or link>` | Searches for and plays a track from SoundCloud |
| `!radio` | Lists the available radio stations |
| `!radio <name>` | Tunes in and plays a specific station |
| `!parar` | Stops the music and disconnects the bot from the voice channel |
| `!ajuda` | Shows all commands with examples |

## Adding new radio stations

At the top of `BOTDISCORD.py`, edit the `ESTACOES_RADIO` dictionary:

```python
ESTACOES_RADIO = {
    'lofi': 'https://coderadio-admin-v2.freecodecamp.org/listen/coderadio/radio.mp3',
    'your_station': 'direct-mp3-or-similar-stream-link',
}
```

**Heads up:** radio stream links go offline or change over time — that's just how internet radio works. If a station stops playing, that's usually the cause, not a bug in the bot. Check [radio-browser.info](https://www.radio-browser.info) for a community-maintained database of working stream URLs, and swap in a fresh one.

## Why SoundCloud instead of YouTube?

YouTube has Terms of Service restrictions around bots extracting audio from videos for shared playback. That's why this example uses SoundCloud, which has a more permissive policy for this kind of use.

## A note on things breaking

This is a good project to get used to something every programmer deals with: libraries and platforms change constantly. A working bot today can throw an error tomorrow after a `pip install --upgrade` or a platform-side change (like Discord's DAVE requirement). Reading the full error traceback and searching for the exact error message is a normal part of the process — not a sign something went wrong with you.

## Disclaimer

This code is for educational purposes. Adapt it, break it, study it, and use it however you like to learn — but keep an eye on each platform's Terms of Service before using it in production or sharing it publicly.
