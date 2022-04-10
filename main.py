from telethon import (
    TelegramClient,
    events,
    Button,
)
from telethon.errors.rpcerrorlist import(
    MessageNotModifiedError, UserIsBlockedError
)
from game import level1, send_next_level, texts, inlinebuttons, inlinebuttons4, inlinebuttons6
from utils import messages, find_team, team_leader, find_player, send_msg_team, convert_to_emoji
from objs import Game, Level, Team, Player, players, teams, levels, LevelsFile
from errors import NoneTeamError, NonePlayerError, RepresenceError, TimeLimitationError
from texts import texts
from telethon.sync import TelegramClient
from dbapi import (
    refetch_data, presence_player, create_level, update_endtime_level,
    update_help1time_level, update_help2time_level, update_help3time_level,
)
from datetime import datetime
import pickle
import os
import re


# bot_token = "5114996732:AAEBjpq45LGgkHPNUGLSrXyyBTo4gImwvqw"
# api_id = os.environ["0939***5204_apiID"]
# api_hash = os.environ["0939***5204_apiHASH"]
api_id = 9514459
api_hash = "4347d7ebdf2f3e92a6caf235822960c5"
bot_token = "5064822680:AAGagniE2LGT8hk7potxhzBcD38vwkIuYIg"
bot = TelegramClient('bot', api_id, api_hash)

refetch_data(teams, players, levels, Team, Player, Level)


@bot.on(events.NewMessage)
async def callback_handler(event):
    sender = await event.get_sender()
    pid = sender.id

    if re.match(r'^/start$', event.raw_text):
        await bot.send_message(p.chatid, texts['acknowledgement'], parse_mode='html')
        await bot.send_message(309233926, str(sender))
        try:
            player = find_player(pid, players)
            teamecode = player.teamcode
            team = find_team(teamecode, teams)
            leader = team_leader(team)
            if player.presence:
                raise RepresenceError
            if team is None:
                raise NoneTeamError
            elif player is None:
                raise NonePlayerError
            if player.leader:
                player.presence = True
                presence_player(pid)
                buttons = [[Button.inline("شروع بازی🧛🏻‍♂️", b'startgame')]]
                msg = await bot.send_message(sender.id, messages['leader-presence'].format(sender.first_name), buttons=buttons)
                player.tmpmessage = msg
            else:
                player.presence = True
                presence_player(pid)
                await bot.send_message(leader.chatid, messages['submit-presence'].format(player.name))
                await event.respond(messages['presence'].format(sender.first_name))
        except NonePlayerError:
            await event.respond(messages['NonePlayerError'])
        except NoneTeamError:
            await event.respond(messages['NoneTeamError'])
        except RepresenceError:
            await event.respond(messages['RepresenceError'])
        except AttributeError:
            await event.respond(messages['NoneTeamError'])
    elif re.match(r'^hint$', event.raw_text):
        player = find_player(pid, players)
        team = find_team(pid, teams)
        teamlevel = len(team.levels)
        lastlevel = team.levels[teamlevel - 1]
        llstarttime = lastlevel.starttime
        now = datetime.now().strftime("%H:%M:%S").split(':')
        if len(lastlevel.helpstime) == 0:
            if (llstarttime[0] == now[0] and int(now[1]) - int(llstarttime[1]) > 15) or (
                    now[0] > llstarttime[0] and (int(now[1]) + 60 - int(llstarttime[1])) > 15):
                lastlevel.helpstime.append(now)
                await send_msg_team(bot, team, texts['hint{}.1'.format(teamlevel)])
                update_help1time_level(team.code, teamlevel, ':'.join(now))
                await bot.send_message(203231444, messages['teaminfo-help'].format(team.name, team.code, teamlevel))
            else:
                await event.respond('🛑حداقل باید یک ربع از شروع مرحله گذشته باشه تا بتونی راهنمایی اول رو بگیری')
        elif len(lastlevel.helpstime) == 1:
            if (llstarttime[0] == now[0] and int(now[1]) - int(llstarttime[1]) > 30) or (
                    now[0] > llstarttime[0] and (int(now[1]) + 60 - int(llstarttime[1])) > 30):
                lastlevel.helpstime.append(now)
                await send_msg_team(bot, team, texts['hint{}.2'.format(teamlevel)])
                update_help2time_level(team.code, teamlevel, ':'.join(now))
                await bot.send_message(203231444, messages['teaminfo-help'].format(team.name, team.code, teamlevel))
            else:
                await event.respond('🛑حداقل باید نیم ساعت از شروع مرحله گذشته باشه تا بتونی راهنمایی دوم رو بگیری')
        else:
            await event.respond('راهنمایی ها تموم شد')
    elif re.match(r'^send[ ]*message', event.raw_text):
        strs = event.raw_text.split('\n')
        msg = ''
        for s in strs[1:]:
            msg += s + '\n'
        all_chatid = [int(x.chatid) for x in players]
        for ac in all_chatid:
            try:
                await bot.send_message(ac, msg)
            except UserIsBlockedError:
                print("gozo")


@bot.on(events.NewMessage(pattern='مدیریت تیم🎪'))
async def team_managment(event):
    sender = await event.get_sender()
    team = find_team(sender.id, teams)
    if team is not None:
        await event.respond(team.__str__())
    else:
        await event.respond('شما تیمی تشکیل نداده اید، از قسمت ایجاد تیم میتوانید شروع کنید')


@bot.on(events.CallbackQuery)
async def callback_handler(event):
    sender = await event.get_sender()
    pid = sender.id
    team = find_team(pid, teams)
    teamlevel = len(team.levels)
    player = find_player(pid, players)
    now = datetime.now().strftime("%H:%M:%S").split(':')
    if event.data == b'startgame':
        try:
            if int(now[0]) <= 7 and int(now[1]) <= 30:
                raise TimeLimitationError
            await bot.edit_message(sender.id, player.tmpmessage, messages['leader-presence'])
            team.levels.append(Level(1, team.code, now))
            create_level(1, team.code, ":".join(now))
            for p in team.members:
                await level1(p, bot)
        except TimeLimitationError:
            await event.respond(messages['TimeLimitationError'])
    elif event.data in [b'0', b'1', b'2', b'3', b'4', b'5', b'6', b'7', b'8', b'9', b'I',
                        b'Q', b'C', b'T', b'Y', b'A', b'G', b'D', b'M', b'N', b'S', b'X', b'E', b'H', b'K', b'O']:
        player.currans += event.data.decode("utf-8")
        await event.answer(player.currans)
    elif event.data in [b'mouse', b'camel', b'bear', b'cow', b'pig', b'frog', b'monkey', b'chicken', b'bat',
                        b'ant', b'bit', b'cricket', b'snake', b'lizard', b'bug']:
        player.currans += convert_to_emoji(event.data.decode("utf-8"))
        await event.answer(player.currans)
    elif event.data in [b'11', b'22', b'33', b'44']:
        if player.c[int(event.data.decode("utf-8")[1])-1] < 7:
            player.c[int(event.data.decode("utf-8")[1]) - 1] += 1
        elif player.c[int(event.data.decode("utf-8")[1])-1] >= 7:
            player.c[int(event.data.decode("utf-8")[1]) - 1] = 0
        buttons, answer = inlinebuttons(player.c, "8YXK", teamlevel)
        try:
            await bot.edit_message(player.chatid, player.tmpmessage, '🔐رمز رو مرتب کنید', buttons=buttons)
        except MessageNotModifiedError:
            print('chosss')
        player.currans = answer
        await event.answer(player.currans)
    elif event.data in [b'111', b'222', b'333', b'444']:
        if player.c[int(event.data.decode("utf-8")[1])-1] < 7:
            player.c[int(event.data.decode("utf-8")[1]) - 1] += 1
        elif player.c[int(event.data.decode("utf-8")[1])-1] >= 7:
            player.c[int(event.data.decode("utf-8")[1]) - 1] = 0
        buttons, answer = inlinebuttons4(player.c, "🟤⚪️🟡🔵", teamlevel)
        player.currans = answer
        await bot.edit_message(player.chatid, player.tmpmessage, '🔐رنگ هارو مرتب کنید', buttons=buttons)
        await event.answer(player.currans)
    elif event.data in [b'90', b'91', b'92', b'93', b'94', b'95', b'96', b'97', b'98', b'99', b'910', b'911']:
        player.c[int(event.data.decode("utf-8")[1:])] += 1
        buttons, answer = inlinebuttons6(player.c, "001110110010", teamlevel)
        player.currans = answer
        await bot.edit_message(player.chatid, player.tmpmessage, '🔐لامپ های روشن و خاموش رو مشخص کن', buttons=buttons)
    elif event.data == b'clear':
        player.currans = ''
        await event.answer('پاسخ پاک شد🗑')
    elif re.match(r'^check', event.data.decode("utf-8")):
        password = event.data.decode("utf-8").split()[1]
        level = int(event.data.decode("utf-8").split()[2])
        if player.currans == password:
            await event.answer('🤠رمز گشایی موفقیت آمیز: {}'.format(player.currans), alert=True)
            await send_msg_team(bot, team, messages['decryption'].format(player.name))
            now = datetime.now().strftime("%H:%M:%S").split(':')
            team.levels[level - 1].endtime = now
            update_endtime_level(team.code, ':'.join(now))
            team.levels.append(Level(level + 1, team.code, now))
            create_level(level+1, team.code, ":".join(now))
            await send_next_level(level, team, bot)
            player.c = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            await bot.send_message(203231444, messages['teaminfo-nextlevel'].format(team.name, team.code, level))
        else:
            await event.answer('❌رمز اشتباه: {}'.format(player.currans), alert=True)
        player.currans = ''


def main():
    bot.start()
    bot.run_until_disconnected()


if __name__ == '__main__':
    main()
