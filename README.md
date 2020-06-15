# Discord bot that forwards your zimbra webmail to your discord server

![](https://img.shields.io/badge/webmail2discord-1.0.0-brightgreen.svg )

__(For National Institute of Technology, Rourkela students only!)__


## How to use:
- Clone the repository
- Edit the config.py file to add your discord webhook and zauthtoken
- Run the `webmail2discord.py` file

__In long run you might want to use a server to keep the script running 24x7__
*(Use heroku or AWS instance for free hosting)*

## How to get your discord webhook
- Go to the setting of a room in a discord server
- Go to `webhook`
- Click on `Add webhook`

## How to get your zauthtoken (For mozilla users only!):
- Login to your zimbra webmail with your respective credentials
- Press `F12` key to open developer console
- Click on network tab
- Click on the existing network connection in the list below
- Right click on it and copy it as cURL
- Open an editor and paste
- Look for `zauthtoken=`

__Never share your webhook or zauthtoken with anyone__

