import pickle
from telethon import Button
from objs import levels
from texts import texts


async def level1(player, bot):
    infile = open('level1.pkl', 'rb')
    fileobj = pickle.load(infile)
    fileslist = fileobj.files
    password = "193410"
    # password = "100110011001"
    async with bot.action(player.chatid, 'file'):
        await bot.send_file(player.chatid, file=fileslist[0])
        await bot.send_message(player.chatid, texts['level1.1'])
        await bot.send_file(player.chatid, file=fileslist[1], caption='🏛موزه دانشگاه فردوسی بیست اسفند\n🚶🏻‍♂️بریم ببینیم چ خبره...')
        await bot.send_file(player.chatid, file=fileslist[2])
        await bot.send_file(player.chatid, file=fileslist[3], caption=texts['level1.2'])
        await bot.send_file(player.chatid, file=[fileslist[5], fileslist[4]], caption=texts['level1.3'])
        await bot.send_file(player.chatid, file=fileslist[6], caption=texts['level1.4'])
    infile.close()
    msg = await answer1(bot, player.chatid, password, 1)
    # msg = await answer6(bot, player.chatid, password, 9)
    player.tmpmessage = msg


async def level2(player, bot):
    infile = open('level2.pkl', 'rb')
    fileobj = pickle.load(infile)
    fileslist = fileobj.files
    password = "1353"
    async with bot.action(player.chatid, 'file'):
        await bot.send_file(player.chatid, file=fileslist[0], caption=texts['level2.1'])
        await bot.send_file(player.chatid, file=[fileslist[1], fileslist[2]], caption=texts['level2.2'])
        await bot.send_file(player.chatid, file=fileslist[3], caption=texts['level2.3'])
        await bot.send_file(player.chatid, file=fileslist[4])
        await bot.send_file(player.chatid, file=[fileslist[5], fileslist[6], fileslist[7], fileslist[8], fileslist[9]], caption=texts['level2.4'])
        await bot.send_message(player.chatid, texts['level2.5'])
    infile.close()
    msg = await answer1(bot, player.chatid, password, 2)
    player.tmpmessage = msg


async def level3(player, bot):
    infile = open('level3.pkl', 'rb')
    fileobj = pickle.load(infile)
    fileslist = fileobj.files
    password = "57932864"
    async with bot.action(player.chatid, 'document'):
        await bot.send_file(player.chatid, file=fileslist[0])
        # await bot.send_file(player.chatid, file=fileslist[1])
        await bot.send_file(player.chatid, file=[fileslist[2], fileslist[3]], caption=texts['level3.1'])
        await bot.send_file(player.chatid, file=fileslist[4], caption=texts['level3.2'])
        await bot.send_file(player.chatid, file=fileslist[5], caption=texts['level3.3'])
    infile.close()
    msg = await answer1(bot, player.chatid, password, 3)
    player.tmpmessage = msg


async def level4(player, bot):
    infile = open('level4.pkl', 'rb')
    fileobj = pickle.load(infile)
    fileslist = fileobj.files
    password = "1914715"
    async with bot.action(player.chatid, 'document'):
        # await bot.send_file(player.chatid, file=fileslist[0])
        await bot.send_file(player.chatid, file=fileslist[1], caption='سال ۱۳۴۰ تاسیس دانشکده علوم')
        await bot.send_file(player.chatid, file=fileslist[2], caption='یک ساختمونی اینجا در حال ساخته🧱 چقدر شبیه انگاریوم دانشگاس...')
        await bot.send_file(player.chatid, file=fileslist[3], caption=texts['level4.1'])
        await bot.send_file(player.chatid, file=fileslist[4], caption='یک فلش پیدا کردم زدم اینجا داخلش یه فایله💾 قفل عدد 7 رقمی میخواد ازمون')
        await bot.send_file(player.chatid, file=fileslist[5])
    infile.close()
    msg = await answer1(bot, player.chatid, password, 4)
    player.tmpmessage = msg


async def level5(player, bot):
    infile = open('level5.pkl', 'rb')
    fileobj = pickle.load(infile)
    fileslist = fileobj.files
    password = "QDQAQC"
    async with bot.action(player.chatid, 'document'):
        await bot.send_file(player.chatid, file=fileslist[0], caption='📚سال ۱۳۴۷ تاسیس کتابخانه')
        await bot.send_file(player.chatid, file=[fileslist[1], fileslist[2], fileslist[3]],
                            caption='نگهبانی ۳ تا کتاب بهم داده گفت داری میری پایین اینا هم ببر😒')
        await bot.send_message(player.chatid, 'برم پایین ببینم چه خبره🚶🏻‍♂️قفل هم ۶ حرف شده')
    infile.close()
    msg = await answer2(bot, player.chatid, password, 5)
    player.tmpmessage = msg


async def level6(player, bot):
    infile = open('level6.pkl', 'rb')
    fileobj = pickle.load(infile)
    fileslist = fileobj.files
    password = "8YXK"
    async with bot.action(player.chatid, 'document'):
        # await bot.send_file(player.chatid, file=fileslist[0])
        await bot.send_file(player.chatid, file=[fileslist[1], fileslist[2]], caption=texts['level6.1'])
        await bot.send_file(player.chatid, file=fileslist[3], caption=texts['level6.2'])
        await bot.send_message(player.chatid, texts['level6.3'])
    infile.close()
    msg = await answer3(bot, player.chatid, password, 6)
    player.tmpmessage = msg


async def level7(player, bot):
    infile = open('level7.pkl', 'rb')
    fileobj = pickle.load(infile)
    fileslist = fileobj.files
    password = "🔵🟡⚪️🟤"
    async with bot.action(player.chatid, 'document'):
        # await bot.send_file(player.chatid, file=fileslist[0])
        await bot.send_file(player.chatid, file=fileslist[0], caption=texts['level7.1'])
        await bot.send_file(player.chatid, file=fileslist[1], caption=texts['level7.2'])
        await bot.send_file(player.chatid, file=fileslist[2], caption=texts['level7.3'])
        # await bot.send_message(player.chatid, texts['level7.4'])
    infile.close()
    msg = await answer4(bot, player.chatid, password, 7)
    player.tmpmessage = msg


async def level8(player, bot):
    infile = open('level8.pkl', 'rb')
    fileobj = pickle.load(infile)
    fileslist = fileobj.files
    password = "🦇🐵🦟🐪"
    async with bot.action(player.chatid, 'document'):
        await bot.send_file(player.chatid, file=[fileslist[0], fileslist[1]], caption=texts['level8.1'])
        await bot.send_file(player.chatid, file=[fileslist[2], fileslist[3], fileslist[4], fileslist[5], fileslist[6],
                                                 fileslist[7], fileslist[8]], caption=texts['level8.1'])
        await bot.send_file(player.chatid, file=fileslist[9], caption='پشت یکی از درها اینو چسبونده بودن. قفل شبیهشو تو پیام بعدی میفرستم')
        # await bot.send_message(player.chatid, texts['level7.4'])
    infile.close()
    msg = await answer5(bot, player.chatid, password, 8)
    player.tmpmessage = msg


async def level9(player, bot):
    infile = open('level9.pkl', 'rb')
    fileobj = pickle.load(infile)
    fileslist = fileobj.files
    password = "001110110010"
    async with bot.action(player.chatid, 'document'):
        # await bot.send_file(player.chatid, file=fileslist[0])
        await bot.send_file(player.chatid, file=[fileslist[1], fileslist[2], fileslist[3], fileslist[4]], caption=texts['level9.1'])
        await bot.send_message(player.chatid, texts['level9.2'])
        await bot.send_file(player.chatid, file=[fileslist[5], fileslist[6], fileslist[7], fileslist[8], fileslist[9],
                                                 fileslist[10]], caption=texts['level9.3'])
    infile.close()
    msg = await answer6(bot, player.chatid, password, 9)
    player.tmpmessage = msg


async def answer1(bot, pid, password, level):
    buttons = [
        [
            Button.inline('1️⃣', b'1'),
            Button.inline('2️⃣', b'2'),
            Button.inline('3️⃣', b'3'),
        ], [
            Button.inline('4️⃣', b'4'),
            Button.inline('5️⃣', b'5'),
            Button.inline('6️⃣', b'6'),
        ], [
            Button.inline('7️⃣', b'7'),
            Button.inline('8️⃣', b'8'),
            Button.inline('9️⃣', b'9'),
        ], [
            Button.inline('🗑', b'clear'),
            Button.inline('0️⃣', b'0'),
            Button.inline('✅', 'check ' + password + ' ' + str(level)),
        ]
    ]
    msg = await bot.send_message(pid, '🔐رمز را وارد کنید', buttons=buttons)
    return msg


async def answer2(bot, pid, password, level):
    buttons = [
        [
            Button.inline('Q', b'Q'),
            Button.inline('C', b'C'),
            Button.inline('T', b'T'),
        ], [
            Button.inline('Y', b'Y'),
            Button.inline('A', b'A'),
            Button.inline('G', b'G'),
        ], [
            Button.inline('D', b'D'),
            Button.inline('M', b'M'),
            Button.inline('N', b'N'),
        ], [
            Button.inline('🗑', b'clear'),
            Button.inline('S', 'S'),
            Button.inline('✅', 'check ' + password + ' ' + str(level)),
        ]
    ]
    msg = await bot.send_message(pid, '🔐رمز رو مرتب کنید', buttons=buttons)
    return msg


async def answer3(bot, pid, password, level):
    col1 = [Button.inline('H', b'11'), Button.inline('N', b'11'),
            Button.inline('M', b'11'), Button.inline('8', b'11'),
            Button.inline('E', b'11'), Button.inline('2', b'11'),
            Button.inline('5', b'11'), Button.inline('9', b'11')]
    col2 = [Button.inline('V', b'22'), Button.inline('D', b'22'),
            Button.inline('K', b'22'), Button.inline('T', b'22'),
            Button.inline('5', b'22'), Button.inline('7', b'22'),
            Button.inline('Y', b'22'), Button.inline('X', b'22')]
    col3 = [Button.inline('K', b'33'), Button.inline('G', b'33'),
            Button.inline('S', b'33'), Button.inline('I', b'33'),
            Button.inline('P', b'33'), Button.inline('3', b'33'),
            Button.inline('1', b'33'), Button.inline('X', b'33')]
    col4 = [Button.inline('O', b'44'), Button.inline('P', b'44'),
            Button.inline('B', b'44'), Button.inline('A', b'44'),
            Button.inline('2', b'44'), Button.inline('5', b'44'),
            Button.inline('K', b'44'), Button.inline('0', b'44')]
    buttons = [[col1[0], col2[0], col3[0], col4[0]], [Button.inline('بررسی✅', 'check ' + password + ' ' + str(level))]]
    msg = await bot.send_message(pid, '🔐رمز را مرتب کنید', buttons=buttons)
    return msg


def inlinebuttons(c, password, level):
    col1 = [Button.inline('H', b'11'), Button.inline('N', b'11'),
            Button.inline('M', b'11'), Button.inline('8', b'11'),
            Button.inline('E', b'11'), Button.inline('2', b'11'),
            Button.inline('5', b'11'), Button.inline('9', b'11')]
    col11 = ['H', 'N', 'M', '8', 'E', '2', '5', '9']
    col2 = [Button.inline('V', b'22'), Button.inline('D', b'22'),
            Button.inline('K', b'22'), Button.inline('T', b'22'),
            Button.inline('5', b'22'), Button.inline('7', b'22'),
            Button.inline('Y', b'22'), Button.inline('X', b'22')]
    col22 = ['V', 'D', 'K', 'T', '5', '7', 'Y', 'X']
    col3 = [Button.inline('K', b'33'), Button.inline('G', b'33'),
            Button.inline('S', b'33'), Button.inline('I', b'33'),
            Button.inline('P', b'33'), Button.inline('3', b'33'),
            Button.inline('1', b'33'), Button.inline('X', b'33')]
    col33 = ['K', 'G', 'S', 'I', 'P', '3', '1', 'X']
    col4 = [Button.inline('O', b'44'), Button.inline('P', b'44'),
            Button.inline('B', b'44'), Button.inline('A', b'44'),
            Button.inline('2', b'44'), Button.inline('5', b'44'),
            Button.inline('K', b'44'), Button.inline('0', b'44')]
    col44 = ['O', 'P', 'B', 'A', '2', '5', 'K', '0']
    buttons = [[col1[c[0]], col2[c[1]], col3[c[2]], col4[c[3]]], [Button.inline('بررسی✅', 'check ' + password + ' ' + str(level))]]
    answer = col11[c[0]] + col22[c[1]] + col33[c[2]] + col44[c[3]]
    return buttons, answer


async def answer4(bot, pid, password, level):
    col1 = [Button.inline('🔴', b'111'), Button.inline('🟠', b'111'),
            Button.inline('🟡', b'111'), Button.inline('⚫️', b'111'),
            Button.inline('🟢', b'111'), Button.inline('🟤', b'111'),
            Button.inline('🔵', b'111'), Button.inline('⚪️', b'111')]
    col2 = [Button.inline('🔴', b'222'), Button.inline('🟠', b'222'),
            Button.inline('🟡', b'222'), Button.inline('⚫️', b'222'),
            Button.inline('🟢', b'222'), Button.inline('🟤', b'222'),
            Button.inline('🔵', b'222'), Button.inline('⚪️', b'222')]
    col3 = [Button.inline('🔴', b'333'), Button.inline('🟠', b'333'),
            Button.inline('🟡', b'333'), Button.inline('⚫️', b'333'),
            Button.inline('🟢', b'333'), Button.inline('🟤', b'333'),
            Button.inline('🔵', b'333'), Button.inline('⚪️', b'333')]
    col4 = [Button.inline('🔴', b'444'), Button.inline('🟠', b'444'),
            Button.inline('🟡', b'444'), Button.inline('⚫️', b'444'),
            Button.inline('🟢', b'444'), Button.inline('🟤', b'444'),
            Button.inline('🔵', b'444'), Button.inline('⚪️', b'444')]
    buttons = [[col1[0], col2[0], col3[0], col4[0]], [Button.inline('بررسی✅', 'check ' + password + ' ' + str(level))]]
    msg = await bot.send_message(pid, '🔐رنگ هارو مرتب کنید', buttons=buttons)
    return msg


def inlinebuttons4(c, password, level):
    col1 = [Button.inline('🔴', b'111'), Button.inline('🟠', b'111'),
            Button.inline('🟡', b'111'), Button.inline('⚫️', b'111'),
            Button.inline('🟢', b'111'), Button.inline('🟤', b'111'),
            Button.inline('🔵', b'111'), Button.inline('⚪️', b'111')]
    col11 = ['🔴', '🟠', '🟡', '⚫️', '🟢', '🟤', '🔵', '⚪️']
    col2 = [Button.inline('🔴', b'222'), Button.inline('🟠', b'222'),
            Button.inline('🟡', b'222'), Button.inline('⚫️', b'222'),
            Button.inline('🟢', b'222'), Button.inline('🟤', b'222'),
            Button.inline('🔵', b'222'), Button.inline('⚪️', b'222')]
    col22 = ['🔴', '🟠', '🟡', '⚫️', '🟢', '🟤', '🔵', '⚪️']
    col3 = [Button.inline('🔴', b'333'), Button.inline('🟠', b'333'),
            Button.inline('🟡', b'333'), Button.inline('⚫️', b'333'),
            Button.inline('🟢', b'333'), Button.inline('🟤', b'333'),
            Button.inline('🔵', b'333'), Button.inline('⚪️', b'333')]
    col33 = ['🔴', '🟠', '🟡', '⚫️', '🟢', '🟤', '🔵', '⚪️']
    col4 = [Button.inline('🔴', b'444'), Button.inline('🟠', b'444'),
            Button.inline('🟡', b'444'), Button.inline('⚫️', b'444'),
            Button.inline('🟢', b'444'), Button.inline('🟤', b'444'),
            Button.inline('🔵', b'444'), Button.inline('⚪️', b'444')]
    col44 = ['🔴', '🟠', '🟡', '⚫️', '🟢', '🟤', '🔵', '⚪️']
    buttons = [[col1[c[0]], col2[c[1]], col3[c[2]], col4[c[3]]], [Button.inline('بررسی✅', 'check ' + password + ' ' + str(level))]]
    answer = col11[c[0]] + col22[c[1]] + col33[c[2]] + col44[c[3]]
    return buttons, answer


async def answer6(bot, pid, password, level):
    col0 = [Button.inline('💡', b'90'), Button.inline(' ', b'90')]
    col1 = [Button.inline('💡', b'91'), Button.inline(' ', b'91')]
    col2 = [Button.inline('💡', b'92'), Button.inline(' ', b'92')]
    col3 = [Button.inline('💡', b'93'), Button.inline(' ', b'93')]
    col4 = [Button.inline('💡', b'94'), Button.inline(' ', b'94')]
    col5 = [Button.inline('💡', b'95'), Button.inline(' ', b'95')]
    col6 = [Button.inline('💡', b'96'), Button.inline(' ', b'96')]
    col7 = [Button.inline('💡', b'97'), Button.inline(' ', b'97')]
    col8 = [Button.inline('💡', b'98'), Button.inline(' ', b'98')]
    col9 = [Button.inline('💡', b'99'), Button.inline(' ', b'99')]
    col10 = [Button.inline('💡', b'910'), Button.inline(' ', b'910')]
    col11 = [Button.inline('💡', b'911'), Button.inline(' ', b'911')]
    buttons = [
        [col0[0], col1[0], col2[0], col3[0], col4[0], col5[0]],
        [col6[0], col7[0], col8[0], col9[0], col10[0], col11[0]],
        [Button.inline('بررسی✅', 'check ' + password + ' ' + str(level))]
    ]
    msg = await bot.send_message(pid, '🔐لامپ های روشن و خاموش رو مشخص کن', buttons=buttons)
    return msg


def inlinebuttons6(c, password, level):
    col0 = [Button.inline('💡', b'90'), Button.inline(' ', b'90')]
    col1 = [Button.inline('💡', b'91'), Button.inline(' ', b'91')]
    col2 = [Button.inline('💡', b'92'), Button.inline(' ', b'92')]
    col3 = [Button.inline('💡', b'93'), Button.inline(' ', b'93')]
    col4 = [Button.inline('💡', b'94'), Button.inline(' ', b'94')]
    col5 = [Button.inline('💡', b'95'), Button.inline(' ', b'95')]
    col6 = [Button.inline('💡', b'96'), Button.inline(' ', b'96')]
    col7 = [Button.inline('💡', b'97'), Button.inline(' ', b'97')]
    col8 = [Button.inline('💡', b'98'), Button.inline(' ', b'98')]
    col9 = [Button.inline('💡', b'99'), Button.inline(' ', b'99')]
    col10 = [Button.inline('💡', b'910'), Button.inline(' ', b'910')]
    col11 = [Button.inline('💡', b'911'), Button.inline(' ', b'911')]
    colans = ['0', '1']
    buttons = [
        [col0[c[0] % 2], col1[c[1] % 2], col2[c[2] % 2], col3[c[3] % 2], col4[c[4] % 2], col5[c[5] % 2]],
        [col6[c[6] % 2], col7[c[7] % 2], col8[c[8] % 2], col9[c[9] % 2], col10[c[10] % 2], col11[c[11] % 2]],
        [Button.inline('بررسی✅', 'check ' + password + ' ' + str(level))]
    ]
    answer = ''
    for i in c:
        answer += colans[i % 2]
    return buttons, answer


async def answer5(bot, pid, password, level):
    buttons = [
        [
            Button.inline('🐭', b'mouse'), Button.inline('🐪', b'camel'), Button.inline('🐻', b'bear'), Button.inline('🐮', b'cow'),
        ], [
            Button.inline('🐷', b'pig'), Button.inline('🐸', b'frog'), Button.inline('🐵', b'monkey'), Button.inline('🐔', b'chicken'),
        ], [
            Button.inline('🦇', b'bat'), Button.inline('🐜', b'ant'), Button.inline('🦟', b'bit'), Button.inline('🦗', b'cricket'),
        ], [
            Button.inline('🐍', b'snake'), Button.inline('🦎', b'lizard'), Button.inline('🐛', b'bug'), Button.inline('✅', 'check ' + password + ' ' + str(level)),
        ]
    ]
    msg = await bot.send_message(pid, '🔐رمز را وارد کنید', buttons=buttons)
    return msg


async def send_next_level(level, team, bot):
    if level == 1:
        for p in team.members:
            await bot.delete_messages(p.chatid, p.tmpmessage)
            await level2(p, bot)
    elif level == 2:
        for p in team.members:
            await bot.delete_messages(p.chatid, p.tmpmessage)
            await level3(p, bot)
    elif level == 3:
        for p in team.members:
            await bot.delete_messages(p.chatid, p.tmpmessage)
            await level4(p, bot)
    elif level == 4:
        for p in team.members:
            await bot.delete_messages(p.chatid, p.tmpmessage)
            await level5(p, bot)
    elif level == 5:
        for p in team.members:
            await bot.delete_messages(p.chatid, p.tmpmessage)
            await level6(p, bot)
    elif level == 6:
        for p in team.members:
            await bot.delete_messages(p.chatid, p.tmpmessage)
            await level7(p, bot)
    elif level == 7:
        for p in team.members:
            await bot.delete_messages(p.chatid, p.tmpmessage)
            await level8(p, bot)
    elif level == 8:
        for p in team.members:
            await bot.delete_messages(p.chatid, p.tmpmessage)
            await level9(p, bot)
    elif level == 9:
        for p in team.members:
            await bot.delete_messages(p.chatid, p.tmpmessage)
            await bot.send_message(p.chatid, texts['congratulation'], link_preview=False)
            await bot.send_message(p.chatid, texts['acknowledgement'], parse_mode='html')
            await bot.send_message(p.chatid, texts['endmsg'], link_preview=False)
