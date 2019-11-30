from twitchio.ext import commands
from settings import OATH_TOKEN, NICK, CHAN

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(irc_token=OATH_TOKEN, client_id=NICK, nick=NICK, prefix='!',
                         initial_channels=[CHAN])

    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Ready | {self.nick}')

    async def event_message(self, message):
        print(message.author.name, ':', message.content)
        await self.handle_commands(message)

    # Commands use a decorator...
    @commands.command(name='test')
    async def my_command(self, ctx):
        await ctx.send(f'Hello {ctx.author.name}!')


bot = Bot()
bot.run()