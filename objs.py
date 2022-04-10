teams = []
players = []
levels = []


class Game:
    def __init__(self, name):
        self.name = name
        self.levels = []


class LevelsFile:
    def __init__(self, password):
        self.password = password
        self.files = []


class Level:
    def __init__(self, level, teamcode, starttime):
        self.level = level
        self.teamcode = teamcode
        self.starttime = starttime
        self.endtime = None
        self.helpstime = []

    def __str__(self):
        return 'مرحله {}= زمان شروع: {}. زمان پایان: {}. راهنمایی ها: {}'.format(
            self.level, self.starttime, self.endtime, self.helpstime)


class Team:
    def __init__(self, name: str, code: int):
        self.name = name
        self.code = code
        self.members = []
        self.levels = []
        self.memberscount = len(self.members)
        self.statuspay = False
        self.score = 0

    def __str__(self):
        s = '\n'.join(map(str, self.members))
        le = None
        for p in self.members:
            if p.leader:
                le = p
                break
        return '🎛نام تیم: {}\n🀄️کد تیم: {}\n👤سرگروه:\n {}\n👥اعضا:\n{}\n'.format(self.name, self.code, le, s)


class Player:
    def __init__(self, tc, ci, si, sf, phn, un, n):
        self.teamcode = tc
        self.chatid = ci
        self.studentid = si
        self.studyfield = sf
        self.phonenumber = phn
        self.username = un
        self.name = n
        self.currans = ''
        self.tmpmessage = None
        self.leader = False
        self.activate = False
        self.presence = False
        self.c = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def __str__(self):
        return '➖نام: {}، آیدی: {}، شماره دانشجویی: {}، رشته تحصیلی: {}، شماره: {}'.format(
            self.name, self.username, self.studentid, self.studyfield, self.phonenumber
        )
