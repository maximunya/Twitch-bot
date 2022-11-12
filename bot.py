import os
import random

import twitchio
from twitchio.ext import commands, routines

from functions.banners import get_successful_attempt_for_characters_banner
from functions.banners import get_successful_attempt_for_weapons_banner
import banwords


class Bot(commands.Bot):
    """Class of the Bot."""

    def __init__(self):
        """Initializing the Bot."""
        super().__init__(
            token=os.environ['TOKEN'],
            client_id=os.environ['CLIENT'],
            nick=os.environ['NICK'],
            prefix=os.environ['PREFIX'],
            initial_channels=[os.environ['CHANNEL']],
        )

        self.waifu_list = [
            'яэ мико',
            'райден сёгун',
            'сангономия кокоми',
            'гань юй',
            'камисато аяка',
            'шэнь хэ',
            'ху тао',
            'ёимия',
            'мона мегистус',
            'е лань',
            'кэ цин',
            'эола',
            'нин гуан',
            'ноэлль',
            'юнь цзинь',
            'розария',
            'эмбер',
            'сян лин',
            'синь янь',
            'янь фэй',
            'барбара',
            'бэй доу',
            'фишль',
            'кудзе сара',
            'куки синобу',
            'лиза',
            'джинн',
            'сахароза',
            'никто',
            'венти',
            'син цю',
            'коллеи',
            'нилу',
            'дехья',
            'кандакия',
            'лайла',
            'фарузан',
        ]

        self.husband_list = [
            'альбедо',
            'аратаки итто',
            'горо',
            'чжун ли',
            'чунь юнь',
            'кэйа',
            'беннет',
            'дилюк',
            'тома',
            'камисато аято',
            'тарталья',
            'рэйзор',
            'каэдахара кадзуха',
            'сиканоин хэйдзо',
            'венти',
            'сяо',
            'хиличурл',
            'геовишап',
            'гидро слайм',
            'син цю',
            'тигнари',
            'сайно',
            'аль хайтам',
            'скарамучча',
            'кавех',
        ]

        self.husband_banner_weights = [
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            0.5,
            0.5,
            0.5,
            1,
            1,
            1,
            1,
            1,
            1,
        ]

        self.characters_banner1 = [
            'Нахида',
            'Дилюк',
            'Мона',
            'Джинн',
            'ЧИЧА',
            'Кэ Цин',
        ]

        self.characters_banner2 = [
            'Ёимия',
            'Дилюк',
            'Мона',
            'Джинн',
            'ЧИЧА',
            'Кэ Цин',
        ]

        self.weapons_banner = [
            'Сновидение тысячи ночей',
            'Громовой пульс',
            'Лук Амоса',
            'Меч Сокола',
            'Молитва святым ветрам',
            'Небесная ось',
            'Небесное величие',
            'Небесное крыло',
            'Небесный атлас',
            'Небесный меч',
            'Волчья погибель',
            'Нефритовый коршун',
        ]

        self.characters_banner_weights = [
            0.5,
            0.1,
            0.1,
            0.1,
            0.1,
            0.1,
        ]

        self.weapons_banner_weights = [
            0.25,
            0.25,
            0.05,
            0.05,
            0.05,
            0.05,
            0.05,
            0.05,
            0.05,
            0.05,
            0.05,
            0.05,
        ]

        self.weapons_banner_additional_drop_probabilities = [
            0.1,
            0.11,
            0.12,
            0.13,
            0.14,
            0.15,
            0.15,
            0.15,
            0.125,
            0.125,
            0.11,
            0.1,
            0.1,
            0.1,
            0.1,
            0.1,
            0.1,
            0.1,
            0.1,
            0.08,
            0.04,
        ]

        self.remindings = [
            'ээээээуууу я здесь! я ваш бот и со мной можно '
            'поболтать.. а еще подобрать вам вайфу! '
            'не меня, конечно, но там вариантики тоже ничего (＾• ω •＾)',

            'что-то мне скучно стало... поговорите со мной! '
            'подскажу ваш шанс выпадения леги или еще чего интересного!',

            'вы можете спросить меня о чем угодно! '
            '(почти) постараюсь быть полезной (´꒳`)♡',

            'я все еще тут! не забывайте меня пожалуйста (╥﹏╥)',

            'мне иногда кажется, что я состою из нулей и единиц.. '
            'а еще меня кто-то создал.. наверное, показалось. '
            'кстати, моя вайфу - райден! а ваша? (!вайфу)',
        ]

        self.answers = [
            'да!',
            'нееет',
            'а вот не знаю',
            'это сложный вопрос...',
            'кто знает? спросите лучше Женю',
        ]

        self.call_bot = '@waifu_assistent'
        self.question_mark = '?'
        self.telegram_reminding = ('заходите в мой телеграм-канал! '
                                   'https://t.me/zhenyaohayo')

        self.donate_reminding = ('вы можете помочь стримеру денежкой: '
                                 'https://www.donationalerts.com/r/zhenyaoh')

        self.discord = 'дискордик: https://discord.gg/fDrsZA8B56'
        self.telegram = 'наше место: https://t.me/zhenyaohayo'

        self.donate = 'спасибо что интересуешься ♡︎ '\
                      'https://www.donationalerts.com/r/zhenyaoh ♡︎'

        self.rules = ('нельзя: ♡︎ оскорблять меня/модераторов ♡︎ '
                      'банворды ♡︎ проявлять расизм, сексизм, шовинизм '
                      'и любые виды ксенофобии! бан от модера или меня не '
                      'обсуждается. система страйков - 3 страйка = бан '
                      '♡︎ за обсуждение любых сливов геншина - бан')

        self.help = 'нуждается в помощи стримера!'

        self.comms = ('!правила – правила чата; !тг – ссылка на нашу телегу; '
                      '!дс – ссылка на канал в дискорде; !донат – ссылка на '
                      'донат; !вайфу – узнать свою вайфу; !хасбунд – узнать '
                      'своего мужа; !баннер – кто и на какой крутке тебе '
                      'выпадет с ивентового баннера; !баннероружие - как '
                      '!баннер, только с оружием; !паста – рандомная паста; '
                      '!помощь – попросить стримера помочь; !писюн – размер '
                      'вашего писюна; !шанс – вероятность того или иного '
                      'события; !спросимвайфу - ответ на вопрос (да/нет); '
                      '!осу - осуждаем всем чатом')

        self.osu = ('ОСУЖДААААЮ не одобряю, написавший/сказавший это очень '
                    'ПЛОХОЙ НЕВОСПИТАННЫЙ человек, зачем ты такое '
                    'говоришь??? ГОВНЮК, ОСУЖДААААЮЮЮЮ!!!!!!!!')

        self.zero_help = ('всё ясно стример опять афк опять не читает мои '
                          'сообщения всем пока я плакать '
                          'BibleThump BibleThump BibleThump')

        self.congrats = ('ЖЕНЕЧКА <3<3<3 ПОЗДРАВЛЯЮ ТЫ САМЫЙ ЛУЧШИЙ сТрИМер '
                         'ты заслужила 325675621 ФАЛЛОВИРАВ ГОСПОДИ МЫ ТБЯ '
                         'ВСЕ ОЧЕНЬ ЛЮБИМ КРАСОТКА МИЛАШКА 😳 СМЕШНЯВКА '
                         'КРИНЖУЛЬКА 😎 <3 УРААААААААА УЛыБАЙСЯ ЧАЩЕ И '
                         'ПРОДОЛЖАЙ В ТОМ ЖЕ ДУХЕ!!!')

        self.ban_words = banwords.ban_words

        self.pastas = [
            'П-п-привет, я тут новенькая  KonCha Я аниме девочка 17 лет, '
            'с розовыми волосами, мама не даёт денег  KonCha , так что '
            'подарите сабочку  KonCha',

            '7 рaз oтмepь, один скoпиpуй пacтy BloodTrail Скoлько вoлка '
            'не кoрми он всё равно пacтy кoпиpует BloodTrail Зa двумя '
            'пастами пoгoнишься ни одной не скопируешь BloodTrail Пасте '
            'врeмя, таймаут на час BloodTrail Скопировал пасту - высирай '
            'смело BloodTrail Копируй пасту пока не уплыла BloodTrail Без '
            'труда, не высрешь пасту ты сюда BloodTrail Одна '
            'паста в чате не воин',

            'Как не зайдешь в чат, одно и тоже. Один клоун, копирует и '
            'вставляет сообщение другого клоуна peepoClown Хватит '
            'превращать чат в цирк peepoClown',

            'Фотографирую 📸 закат🌆 Будто пару ✌️ лет📅 назад🔙 '
            'Без тебя😭 без тебя😭 Без тебя-я-я😭',

            'Люблю Папича ✨ и все что с ним связано 😄 рофланЕбало 💕 👌 '
            'ОПАФ5 😍 VI KA 😈 НЫАА) 😆 Обычно я рофлю с Папича 🙀 это мое '
            'хобби 😹 смотрю его стримы 😊 сабнулся, кидаю рофланЕбало в '
            'чатике 🍀 Еще люблю казино 👺 не спамлю 💀 доначу 🙈 не '
            'стримснайплю 👹 Если ты не любишь ппаню, не считаешь крутым, '
            'то не пиши мне ✋ 👎 😄',

            'BibleThump пусть модер услышит BibleThump пусть модер придет '
            'BibleThump пусть ставочку нам наконец заведет BibleThump ведь '
            'так не бывает на свете BibleThump чтобы были без ставочки дети '
            'BibleThump',

            'Чат подскажите пожалуйста как вылечить геморрой? Мне '
            'посоветовали свечи, но теперь попа в воске и крови, '
            'больно какать BibleThump',

            'Привет, я твой олд, подписан на твой канал 6 лет BibleThump '
            'но вчера я случайно отписался BibleThump , когда перепутал '
            'кнопку платного фоллоу с бесплатным и мой фоллоу срок слетел '
            'BibleThump можешь дать випку, чтобы все знали '
            'что я олд BibleThump',

            'Сижу сейчас, попиваю мультиягодный смузи за 700 EUR , на улице '
            'стоит моя Bugatti Veyron Grand Sport за 1.7 млн $, ах забыл, '
            'нахожусь я в городе Палермо , Италия в вилле за 30 000 000 '
            'евро, Скоро мой шеф повар приготовит Florentiniс pizza c '
            'золотой стружкой за 1400 EUR и порцию элитных мандаришек с '
            'финиками за 300 EUR, но на сабку не хватило, подарите',

            'KappaPride ctrl+c нажали KappaPride ctrl+v нажали KappaPride '
            'в чат твича вставили KappaPride и ждать кд сообщения KappaPride '
            'очень слабенькие сегодня модераторы KappaPride ну очень '
            'слабенькие KappaPride',

            'Привет, Женя. Это я, твой единственный настоящий зритель. '
            'На протяжении многих лет я создавал иллюзию того, что твои '
            'стримы смотрят много людей. Но это был я. Сейчас напишу '
            'это сообщение со всех аккаунтов.',
        ]

    async def event_ready(self):
        """Starts the bot and routines,
        prints 2 strings in console if everything is ok.
        """
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')
        self.send_reminder.start()
        self.send_donate.start()

    async def event_message(self, message: twitchio.Message):
        """The bot reacts to messages in Twitch-chat.

        Response cases:
        1. When a question is addressed to the bot
        2. Someone wrote any banword from the list in the chat
        3. Someone wrote 'привет' in the chat
        """
        if message.echo:
            return
        print(message.content)

        # Answering the question
        if self.call_bot in message.content.lower():
            if self.question_mark in message.content.lower():
                await message.channel.send(f'@{message.author.name}, '
                                           f'{random.choice(self.answers)}')

        # Giving timeouts for using banwords in the chat
        for word in self.ban_words:
            if word in message.content.lower():
                await message.channel.send(f'/timeout {message.author.name} '
                                           f'300 банворд')

        # Greets viewers back
        if message.content.lower() == 'привет':
            await message.channel.send(f'приветик, @{message.author.name}!')
        await self.handle_commands(message)

    @routines.routine(minutes=25, wait_first=True)
    async def send_reminder(self):
        """Sends a random reminding from the list every 25 minutes."""
        chan = self.get_channel("zhenyaoh")
        await chan.send(random.choice(self.remindings))
        await chan.send('напиши "!команды" и узнай что я умею!')

    @send_reminder.before_routine
    async def before_send_reminder(self):
        """Waits for ready before starting
        the random reminder routine.
        """
        await self.wait_for_ready()

    @routines.routine(minutes=45, wait_first=True)
    async def send_tg(self):
        """Sends a reminding of telegram-channel
        every 45 minutes.
        """
        chan = self.get_channel("zhenyaoh")
        await chan.send(self.telegram_reminding)

    @send_tg.before_routine
    async def before_send_tg(self):
        """Waits for ready before starting
        the telegram reminder routine.
        """
        await self.wait_for_ready()

    @routines.routine(minutes=35, wait_first=True)
    async def send_donate(self):
        """Sends a reminding of the opportunity
        to donate to a streamer every 35 minutes.
        """
        chan = self.get_channel("zhenyaoh")
        await chan.send(self.donate_reminding)

    @send_donate.before_routine
    async def before_send_donate(self):
        """Waits for ready before starting
        the donate reminder routine.
        """
        await self.wait_for_ready()

    @commands.cooldown(1, 10, commands.Bucket.channel)
    @commands.command()
    async def hello(self, ctx: commands.Context):
        """Sends a hello back to the user."""
        await ctx.send(f'приветик, @{ctx.author.name.strip()}!')

    @commands.cooldown(1, 10, commands.Bucket.channel)
    @commands.command()
    async def discord(self, ctx: commands.Context):
        """Sends the Discord link."""
        await ctx.send(self.discord)

    @commands.cooldown(1, 10, commands.Bucket.channel)
    @commands.command()
    async def waifu(self, ctx: commands.Context):
        """Returns a random waifu from the list to the user."""
        choice = random.choice(self.waifu_list)
        await ctx.send(f'@{ctx.author.name.strip()} '
                       f'твоя вайфу – {choice.title()}')

    @commands.cooldown(1, 10, commands.Bucket.channel)
    @commands.command()
    async def telegram(self, ctx: commands.Context):
        """Sends the Telegram-channel link."""
        await ctx.send(self.telegram)

    @commands.cooldown(1, 10, commands.Bucket.channel)
    @commands.command()
    async def rules(self, ctx: commands.Context):
        """Sends the list of rules on the streamer's Twitch-channel."""
        await ctx.send(self.rules)

    @commands.cooldown(1, 10, commands.Bucket.channel)
    @commands.command()
    async def commands(self, ctx: commands.Context):
        """Sends the list of commands, which are available
        on the streamer's Twitch-channel by using prefix '!'.
        """
        await ctx.send(self.comms)

    @commands.cooldown(1, 30, commands.Bucket.channel)
    @commands.command()
    async def help(self, ctx: commands.Context):
        """Asks the streamer for help to the user."""
        await ctx.send(f'@{ctx.author.name.strip()} {self.help}')

    @commands.cooldown(1, 30, commands.Bucket.channel)
    @commands.command()
    async def zerohelp(self, ctx: commands.Context):
        """Sends a paste about the fact that
        the streamer is a selfish dumb because
        she doesn't help.
        """
        await ctx.send(f'{ctx.author.name.strip()}: {self.zero_help}')

    @commands.cooldown(1, 10, commands.Bucket.channel)
    @commands.command()
    async def donate(self, ctx: commands.Context):
        """Sends the DonationAlerts link."""
        await ctx.send(self.donate)

    @commands.command()
    async def gratz(self, ctx: commands.Context):
        """Sends congratulations to the streamer."""
        await ctx.send(self.congrats)

    @commands.cooldown(1, 30, commands.Bucket.channel)
    @commands.command()
    async def paste(self, ctx: commands.Context):
        """Returns a random paste from the list to the chat."""
        await ctx.send(random.choice(self.pastas))

    @commands.cooldown(1, 10, commands.Bucket.channel)
    @commands.command()
    async def chance(self, ctx: commands.Context):
        """Returns a chance of any occasion to the user."""
        await ctx.send(f'@{ctx.author.name.strip()}, вероятность '
                       f'интересующего тебя события – '
                       f'{random.randint(0, 101)}%')

    @commands.cooldown(1, 10, commands.Bucket.channel)
    @commands.command()
    async def askwaifu(self, ctx: commands.Context):
        """Answers to a question of an user
        by a random phrase from the list.
        """
        await ctx.send(f'@{ctx.author.name.strip()}, '
                       f'{random.choice(self.answers)}')

    @commands.cooldown(1, 10, commands.Bucket.channel)
    @commands.command()
    async def jujun(self, ctx: commands.Context):
        """Returns the random size of the user's penis
        from -15 to 120 cm.
        """
        await ctx.send(f'@{ctx.author.name.strip()}, твой писюн: '
                       f'{random.randint(-15, 121)} см')

    @commands.cooldown(1, 5, commands.Bucket.channel)
    @commands.command()
    async def asu(self, ctx: commands.Context):
        """Sends a judgmental paste in the chat."""
        await ctx.send(self.osu)

    @commands.cooldown(1, 10, commands.Bucket.channel)
    @commands.command()
    async def husband(self, ctx: commands.Context):
        """Returns a random husband from the list to the user."""
        husband = random.choices(self.husband_list,
                                 weights=self.husband_banner_weights)
        await ctx.send(f'@{ctx.author.name.strip()} твой хасбунд – '
                       f'{husband[0].title()}')

    @commands.cooldown(1, 10, commands.Bucket.channel)
    @commands.command()
    async def banner1(self, ctx: commands.Context):
        """Predicts which character and on which wish will drop
        to the user in the first character event banner.
        """
        character = random.choices(self.characters_banner1,
                                   self.characters_banner_weights)
        await ctx.send(f'@{ctx.author.name.strip()}, тебе выпадет '
                       f'{character[0]} на '
                       f'{get_successful_attempt_for_characters_banner()} '
                       f'крутке!')

    @commands.cooldown(1, 10, commands.Bucket.channel)
    @commands.command()
    async def banner2(self, ctx: commands.Context):
        """Predicts which character and on which wish will drop
        to the user in the second character event banner.
        """
        character = random.choices(self.characters_banner2,
                                   self.characters_banner_weights)
        await ctx.send(f'@{ctx.author.name.strip()}, тебе выпадет '
                       f'{character[0]} на '
                       f'{get_successful_attempt_for_characters_banner()} '
                       f'крутке!')

    @commands.cooldown(1, 10, commands.Bucket.channel)
    @commands.command()
    async def weaponbanner(self, ctx: commands.Context):
        """Predicts which weapon and on which wish will drop
        to the user in the weapon event banner.
        """
        weapon = random.choices(self.weapons_banner,
                                weights=self.weapons_banner_weights)
        await ctx.send(f'@{ctx.author.name.strip()}, тебе выпадет '
                       f'{weapon[0]} на '
                       f'{get_successful_attempt_for_weapons_banner()} '
                       f'крутке!')


# pipenv run python bot.py
bot = Bot()
bot.run()
