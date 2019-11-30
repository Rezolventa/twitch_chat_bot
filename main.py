from twitchio.ext import commands
from settings import OATH_TOKEN, NICK, CHAN, SUPER_USER
import winsound
from mongo import pay_xp_coins, add_click, get_xp_data
from lexicon import raz_raza

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(irc_token=OATH_TOKEN, client_id=NICK, nick=NICK, prefix='!',
                         initial_channels=[CHAN])

    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Ready | {self.nick}')

    async def event_message(self, message):
        print(message.author.name, ':', message.content)
        pay_xp_coins(message.author)
        await self.handle_commands(message)

    # TODO: !xp, !give, !money, charging_minerals
    @commands.command(name='hello')
    async def my_command(self, ctx):
        await ctx.send(f'Hello {ctx.author.name}!')

    @commands.command(name='help')
    async def help(self, ctx):
        await ctx.send('На стадии бета-тестирования доступны следующие команды: !money !clap !shame')

    @commands.command(name='click')
    async def click(self, ctx):
        clicks = add_click()
        await ctx.send('За сегодня кликнули {} {}'.format(clicks, raz_raza(clicks)))

    @commands.command(name='lvl')
    async def display_level(self, ctx):
        xp_data = get_xp_data(ctx.author.name)
        await ctx.send('{} уровень {}, опыт {}/{}. Счет в банке {} минералов.'.format(ctx.author.name.capitalize(), xp_data['lvl'], xp_data['xp'], xp_data['xp_for_level'], xp_data['coins']))

    @commands.command(name='clap')
    async def clap(self, ctx):
        playsound('sound/clap.wav')

    @commands.command(name='shame')
    async def shame(self, ctx):
        playsound('sound/shame.wav')

    @commands.command(name='tank')
    async def shame(self, ctx):
        playsound('sound/tank.wav')

def playsound(path):
    winsound.PlaySound(path, winsound.SND_FILENAME)

bot = Bot()
bot.run()