from twitchio.ext import commands
from settings import BOT_OATH_TOKEN, BOT_NICKNAME, TARGET_CHANNEL
import winsound
from mongo import pay_xp_coins, add_click, get_xp_data
from lexicon import decline_count


class Bot(commands.Bot):
    """
    Главный и единственный класс бота.
    На нейминг фантазии не хватило.
    """

    def __init__(self):
        super().__init__(
            irc_token=BOT_OATH_TOKEN,
            client_id=BOT_NICKNAME,
            nick=BOT_NICKNAME,
            prefix="!",
            initial_channels=[TARGET_CHANNEL],
        )

    async def event_ready(self):
        print(f"Ready | {self.nick}")

    async def event_message(self, message):
        print(message.author.name, ":", message.content)
        pay_xp_coins(message.author)
        await self.handle_commands(message)

    # TODO: !xp, !give, !money, !charge, !bob
    @commands.command(name="hello")
    async def my_command(self, ctx):
        await ctx.send(f"Hello {ctx.author.name}!")

    @commands.command(name="help")
    async def help(self, ctx):
        await ctx.send(
            "За активность в чате начисляется опыт и минералы. Используй накопления для звуковых команд во "
            "время стрима. На стадии бета-тестирования доступны следующие команды: !click !lvl !tank !clap "
            "!shame."
        )

    @commands.command(name="click")
    async def click(self, ctx):
        clicks = add_click()
        await ctx.send("За сегодня кликнули {} {}".format(clicks, decline_count(clicks)))

    @commands.command(name="lvl")
    async def display_level(self, ctx):
        xp_data = get_xp_data(ctx.author.name)
        await ctx.send(
            "{} уровень {}, опыт {}/{}. Счет в банке {} минералов.".format(
                ctx.author.name.capitalize(),
                xp_data["lvl"],
                xp_data["xp"],
                xp_data["xp_for_level"],
                xp_data["coins"],
            )
        )

    @commands.command(name="clap")
    async def clap(self, ctx):
        play_sound("sound/clap.wav")

    @commands.command(name="shame")
    async def shame(self, ctx):
        play_sound("sound/shame.wav")

    @commands.command(name="tank")
    async def tank(self, ctx):
        play_sound("sound/tank.wav")


def play_sound(path):
    winsound.PlaySound(path, winsound.SND_FILENAME)


bot = Bot()
bot.run()
