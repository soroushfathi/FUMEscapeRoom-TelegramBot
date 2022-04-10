messages = {
    'start': 'ربات محل برگزاری مسابقه اتاق فرار آنلاین خوش اومدی\nلطفا با لینک مخصوص تیمت حضور خودتو ثبت کن',
    'leader-presence': '🧙🏻‍♂️: خب، {} حضورت به عنوان سرگروه ثبت شد\n'
                       'هر کدوم از هم تیمی هات ک استارت رو بزنن پیامش حضورش برات میاد\n'
                       '🔮هر وقت زمان مسابقه(ساعت 11) شروع شد میتونی شروع بازی رو بزنی🪄 \n'
                       '‼️دقت کن تا وقتی شروع نکنی هم تیمی هات هم نمیتونن شروع کنن🎃 خوش بگذه',
    'submit-presence': '🙋🏻‍♂️هم تیمی با نام \"{}\" حضورش رو ثبت کرد',
    'presence': '🧙🏻‍♂️:صبح بخیر {}🖐🏻 پیام ثبت حضورت برای سرگروه ارسال شد'
                '📤 هروقت مسابقه رو شروع کنه شما هم میتونین شروع کنین🎛\n💣گود لاک',
    'decryption': 'ایول✌🏻 \"{}\" قفل رو باز کرد🤠 بریم ادامه ماجرا...(تا چند ثانیه دیگه سوالا ارسال میشه⏳)',
    'NonePlayerError': 'شما در تیمی عضو نیستید، یا توسط سرگروه تایید نشده اید\n'
                       'در صورت بروز مشکل با پشتیبانی هماهنگ کنید',
    'NoneTeamError': 'تیمی پیدا نشد🤷🏻‍♂️ این مشکل میتونه از عدم پرداخت باشه یا اینکه تیم شما تایید نشده\n'
                     'در صورت بروز مشکل با پشتیبانی هماهنگ کنید',
    'RepresenceError': '⚠️شما قبلا حضورتون رو ثبت کردین',
    'TimeLimitationError': 'محدودیت زمان⛔️ مسابقه هنوز شروع نشده',
    'teaminfo-nextlevel': '🔸تیم \"{}\"، با کد {}، به مرحله {} رفت',
    'teaminfo-help': '🔸تیم \"{}\"، با کد {}، در مرحله {} راهنمایی گرفت',
}


def find_team(cid, teams):
    for t in teams:
        for p in t.members:
            if p.chatid == cid:
                return t
    return None


def find_player(cid, players):
    for p in players:
        if p.chatid == cid:
            return p
    return None


def team_leader(team):
    for p in team.members:
        if p.leader:
            return p
    return None


async def send_msg_team(bot, team, msg):
    for p in team.members:
        await bot.send_message(p.chatid, msg)


def convert_to_emoji(asci):
    emdic = {
        'mouse': '🐭',
        'camel': '🐪',
        'bear': '🐻',
        'cow': '🐮',
        'pig': '🐷',
        'frog': '🐸',
        'monkey': '🐵',
        'chicken': '🐔',
        'bat': '🦇',
        'ant': '🐜',
        'bit': '🦟',
        'cricket': '🦗',
        'snake': '🐍',
        'lizard': '🦎',
        'bug': '🐛',
    }
    return emdic[asci]
