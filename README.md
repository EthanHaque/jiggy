# Jiggy

![License](https://img.shields.io/github/license/EthanHaque/jiggy)
![Issues](https://img.shields.io/github/issues/EthanHaque/jiggy)
![Stars](https://img.shields.io/github/stars/EthanHaque/jiggy)

## Overview

**Jiggy** is a Discord bot created for the Princeton University Robotics Club.

## Table of Contents

- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)

## Installation

To get started with **Jiggy**, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/EthanHaque/jiggy.git
    ```
2. Navigate to the project directory:
    ```bash
    cd jiggy
    ```
3. Install the dependencies:
    ```bash
    pip install .
    ```
### Using Nix

If you are using Nix, you can set up the environment by running:
```bash
nix develop --no-pure-eval
```

## Setup

### Configuring the `.env` File
This project uses a `.env` file to manage environment variables. Follow these steps to set it up:

1. Locate the `.env-example` file in the root of the repository.
2. Create a new `.env` file based on `.env-example`:
   ```bash
   cp .env-example .env
   ```
3. Open the `.env` file and fill in the required values. Each variable in `.env-example` is described briefly:
   - `DISCORD_TOKEN`: The token for your Discord bot.
   - `SERVER_IP`: The server IP (and optional specified port) the Minecraft server is running on.
   - `SERVER_MINECRAFT_VERSION`: What version(s) of minecraft the server supports.

### Setting Up a Discord Bot

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click **New Application** and give your application a name.
3. Under the "Bot" section:
   - Copy the **Bot Token** by clicking **Reset Token** (store it securely).
4. Set the required permissions for your bot:
   - Go to the **OAuth2** > **URL Generator** section.
   - Select the `bot` scope and `applications.commands` scope.
   - Assign the `Send Messages` bot permission.
   - Use the generated URL to invite your bot to your server.

### Finalizing the Setup

After creating the bot and obtaining the token:
1. Paste the token into the `DISCORD_TOKEN` field in your `.env` file.
2. Ensure all other required `.env` variables are populated correctly.
3. Save the `.env` file.

You're all set to run the project with your Discord bot!

## Usage

Here's how you can use **Jiggy**:

```bash
python -m jiggy
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

If you have any questions, feel free to contact us:

- **Ethan Haque** - [ethanhaque@princeton.edu](mailto:ethanhaque@princeton.edu)
- GitHub: [EthanHaque](https://github.com/EthanHaque)
