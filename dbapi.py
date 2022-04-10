import json
import requests

base_url = 'https://fumgame.ir/api/'


def create_level(level, teamcode, starttime):
    data = {
        'level': level,
        'teamcode': str(teamcode),
        'starttime': starttime,
    }
    url = base_url + 'create_level.php'
    requests.post(url, data=data)


def create_team(name, code):
    data = {
        'name': str(bytes(name, 'utf-8'), 'utf-8'),
        'code': code
    }
    url = base_url + 'create_team.php'
    requests.post(url, data=data)


def create_player(teamcode, chatid, studentid, studyfield, phonenumber, username, name, leader, activate):
    data = {
        'teamcode': teamcode,
        'chatid': chatid,
        'studentid': studentid,
        'studyfield': str(bytes(studyfield, 'utf-8'), 'utf-8'),
        'phonenumber': phonenumber,
        'username': username,
        'name': str(bytes(name, 'utf-8'), 'utf-8'),
        'leader': leader,
        'activate': activate,
    }
    url = base_url + 'create_player.php'
    requests.post(url, data=data)


def get_levels():
    url = base_url + 'get_levels.php'
    x = requests.get(url)
    j = json.loads(str(x.text))
    return j


def get_teams():
    url = base_url + 'get_teams.php'
    x = requests.get(url)
    j = json.loads(str(x.text))
    return j


def get_players():
    url = base_url + 'get_players.php'
    x = requests.get(url)
    try:
        j = json.loads(str(x.text))
        return j
    except json.decoder.JSONDecodeError:
        print("خطا در دریافت اطلاعات")


def accept_player(pid):
    data = {
        'chatid': pid,
    }
    url = base_url + 'accept_player.php'
    requests.post(url, data=data)


def presence_player(pid):
    data = {
        'chatid': pid,
    }
    url = base_url + 'presence_player.php'
    requests.post(url, data=data)


def update_endtime_level(teamcode, endtime):
    data = {
        'teamcode': teamcode,
        'endtime': endtime,
    }
    url = base_url + 'update_endtime_level.php'
    requests.post(url, data=data)


def update_help1time_level(teamcode, level, help1time):
    data = {
        'teamcode': teamcode,
        'level': level,
        'help1time': help1time,
    }
    url = base_url + 'update_help1time_level.php'
    requests.post(url, data=data)


def update_help2time_level(teamcode, level, help2time):
    data = {
        'teamcode': teamcode,
        'level': level,
        'help2time': help2time,
    }
    url = base_url + 'update_help2time_level.php'
    requests.post(url, data=data)


def update_help3time_level(teamcode, help3time):
    data = {
        'teamcode': teamcode,
        'help3time': help3time,
    }
    url = base_url + 'update_help3time_level.php'
    requests.post(url, data=data)


# when the server is off, 'players' and 'teams' will be empty, then we ahve to fetch data from database
# and create team and thiere players again
def refetch_data(teams: list, players: list, levels: list, Team, Player, Level):
    teams.clear()
    players.clear()
    teamsjsons = get_teams()
    for tj in teamsjsons:
        if bool(int(tj['statuspay'])):
            nt = Team(str(bytes(tj['name'], 'utf-8'), 'utf-8'), int(tj['code']))
            nt.statuspay = bool(int(tj['statuspay']))
            teams.append(nt)
    playersjson = get_players()
    for pj in playersjson:
        if bool(int(pj['activate'])):
            p = Player(int(pj['teamcode']), int(pj['chatid']), pj['studentid'], str(bytes(pj['studyfield'], 'utf-8'), 'utf-8'),
                       pj['phone_number'], pj['username'], str(bytes(pj['fullname'], 'utf-8'), 'utf-8'))
            p.leader = bool(int(pj['leader']))
            p.activate = bool(int(pj['activate']))
            p.presence = bool(int(pj['presence']))
            players.append(p)
    levelsjson = get_levels()
    for lj in levelsjson:
        lev = Level(int(lj['level']), lj['teamcode'], lj['startTime'])
        lev.endtime = lj['endTime']
    for pl in players:
        tc = pl.teamcode
        for t in teams:
            if t.code == tc:
                t.members.append(pl)
