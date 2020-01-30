# Inputs
LOGIN_SERVER = u'Enter Server URI > '
LOGIN_USERNAME = u'Enter Your Username > '
MENU_SELECT = u'Choose your operation by number > '
INVITE = u'Enter the ID of the player you want to invite > '
ACTION = u'Enter the value of action {ACTION} > '

# Outputs Normal
WAIT = u'Waiting'
GAME_START = u'Your match against {name} created! Game is about to begin!'
MENU = u'''----------------Welcome to Pointa! Your ID is {key}----------------
    ---- [0] Invite
    ---- [1] Wait for invitation
    ---- [2] Quit
'''
ROUND_BEGIN = u'\n----------------Round {num} Begin----------------'
ROLLED = u'{name}Rolled{num}Points！'
ATK_JUDGE = u'{name}did atk judge，rolled{num}points！Cause{dmg}damages！'
STATUS = u'''\n---- {name} 's Status' ----
    - HP: {HP}
    - DEF: {DEF}
    - PT: {PT}
'''
PLAYER_KILLED = u'{name} Dead'
GAME_END = u'Game Over！{lose} loses！'
GAME_END_EQUAL = u'Game Over！Draw！'
ACTIONS_HEAD = u'\n-------Round {num} Action Summary-------'

ACTION_ATK = '{name} used {num} points to ATK，rolled {judge} points as judgement.'
ACTION_DEF = '{name} used {num} to DEF'
ACTION_HEL = '{name} used {num} to HEL'

PHASE_2 = 'You have only 15 secs to finish the operation!'

# Outputs Errors
TIMEOUT_BAD = u'Timeout or Bad Input!'
REQUEST_ERROR = u'Requested failed…… Code is{code}'
QUIT = u'Press Ctrl+C to quit……'
BAD_INPUT = u'Bad Input!'
INVITE_404 = u'Player not found.'