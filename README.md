# Haven v2

This is a reboot of the Haven discord bot.

[![Add to Discord](https://img.shields.io/badge/Add%20to%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/oauth2/authorize?client_id=1506465698124267552)

| Environment Variable | Description | Required |
| ----------- | ----------- | ----------- |
| `DISCORD_TOKEN` | The token to log into your Discord Application | Yes |
| `KAT_API_URL` | The url of the API used to fetch cat images | No |

| Config | Description | Default Value |
| ----------- | ----------- | ----------- |
| `prefix` | The prefix the bot will listen for when using text commands | `h.` |
| `log_level` | The level of logging that should be printed to console | `INFO` |
| `ping_errors` | Option to ping the bot owner | `false` |
| `error_channel` | The discord channel the bot should forward errors to | `123456789` | 
| `bot_owner` | The ID of the bot owner, used for various things. Example: The user to ping in the error channel, if enabled. | `123456789` |

## Requirements

```
discord.py
python-dotenv
pyyaml
PyNaCl
davey
```

*Note: You can remove PyNaCl & davey, they are optional and not necessary to the application.*

## Issues & Bug Reports

Want to report an issue? Please use the Issues section. All issues submitted in this repository will be reviewed regularly.