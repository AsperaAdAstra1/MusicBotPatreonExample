# 🔐 How to Create and Configure Your `.env` File

This guide walks you through, step by step, how to create the `.env` file that holds your bot's secret token — without it, the bot can't connect to Discord.

## What is `.env` and why does it exist?

`.env` is a simple text file where you store sensitive information (like passwords and tokens) **outside** of your main code. This exists for an important reason:

> If you put the token directly inside the `.py` file and later uploaded that code to GitHub (or shared it with someone), anyone could grab your token and control your bot as if they were you.

By keeping the token in a separate `.env` file, you can freely share your code without exposing anything sensitive — as long as you never upload the `.env` along with it.

## Step 1: Get your bot's token from Discord

1. Go to [discord.com/developers/applications](https://discord.com/developers/applications) and log in with your Discord account
2. Click **"New Application"** in the top right corner
3. Give your bot a name and click **"Create"**
4. In the left side menu, click **"Bot"**
5. Click the **"Reset Token"** button (or **"View Token"**, if this is your first time)
6. Click **"Copy"** to copy the token — it only shows once, so copy and store it somewhere safe before leaving the page

⚠️ **This token is like a password.** Anyone who has it can control your bot. Never post it in screenshots, chats, or public repositories.

## Step 2: Create the `.env` file

### On Windows

1. Open your project folder (where the bot's `.py` file lives)
2. Right-click on an empty area → **New** → **Text Document**
3. Rename the file to `.env` — completely delete the old name and the `.txt` extension, leaving just `.env`
4. Windows will ask if you're sure you want to change the extension — click **"Yes"**

> **Tip:** if Windows won't let the file end up with just `.env` (nothing before the dot), open Notepad, write the content from Step 3 below, then go to **File → Save As**, choose **"All Files (*.*)"** as the type, and save it as `.env` in the project folder.

### On Mac/Linux

From the terminal, inside the project folder:

```bash
touch .env
```

Then open the file with any text editor (VS Code, nano, etc).

## Step 3: Put the token inside the file

Open the `.env` file you just created and write a single line, replacing it with your actual token (no quotes, no spaces before or after the `=`):

```
DISCORD_TOKEN=paste_your_token_here
```

Save the file.

## Step 4: Confirm everything is set up correctly

Your project folder should have, at minimum:

```
my-bot-folder/
├── BOTDISCORD.py
├── .env          ← your file with the token (never share this!)
└── .gitignore    ← makes sure .env doesn't get pushed to GitHub
```

If your `.gitignore` doesn't have this line yet, add it:

```
.env
```

## Step 5: Test it

Run the bot normally:

```bash
python BOTDISCORD.py
```

If you see `Bot conectado como <your-bot-name>` in the terminal, the `.env` was read successfully and the token worked.

## Common errors

| Error | Likely cause |
|---|---|
| `discord.errors.LoginFailure: Improper token has been passed` | Wrong or incomplete token, or an extra space pasted in by accident |
| The bot doesn't connect and no clear error shows up | The `.env` file has the wrong name (e.g. `.env.txt` instead of `.env`) |
| `KeyError` or `None` when loading the token | Missing the `DISCORD_TOKEN=...` line in the file, or the variable name doesn't match what the code expects |

## If you accidentally exposed your token

If you uploaded `.env` to GitHub by mistake, or pasted the token somewhere public:

1. Go back to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Go to **Bot → Reset Token**
3. This immediately invalidates the old token and generates a new one
4. Update your local `.env` with the new token

There's no harm in resetting the token as many times as you need — it's quick and fixes the problem right away.
