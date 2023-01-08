from bot import client, get_env_or_exit
import abacus
import hello
import joined
import report
import text


token = get_env_or_exit('DISCORD_TOKEN')
print("token", token)
client.run(token)