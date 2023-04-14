from twitchio.ext import commands, routines
import twitchio
from config import *
from datetime import datetime

now = datetime.now().strftime('%Y%m%d_%H%M%S')
filepath = 'chat_logs/' + now + '.txt'
f = open(filepath, 'x')

class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(token=TWITCH_BOT_TOKEN, prefix='!', initial_channels=TWITCH_CHANNELS,
                         case_insensitive=True)

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

        await bot.wait_for_ready()
        channel = bot.get_channel(TWITCH_CHANNELS[0])
        await channel.send('Beep Boop')

    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...

        if message.echo:
            return
        
        elif message.content[0] == '!':
            msg = str(message.timestamp)[:19] + ' |*| ' + message.author.name + ': ' + message.content
            print(msg)
            log = open(filepath, 'a')
            log.write(msg + '\n')
            log.close()
        
        else:
            # Print the contents of our message to console...
            msg = str(message.timestamp)[:19] + ' | ' + message.author.name + ': ' + message.content
            print(msg)
            log = open(filepath, 'a')
            log.write(msg + '\n')
            log.close()
            


        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Here we have a command hello, we can invoke our command with our prefix and command name
        # e.g ?hello
        # We can also give our commands aliases (different names) to invoke with.

        # Send a hello back!
        # Sending a reply back to the channel is easy... Below is an example.
        await ctx.send(f'Hello {ctx.author.name}!')


bot = Bot()
bot.run()
# bot.run() is blocking and will stop execution of any below code here until stopped or closed.