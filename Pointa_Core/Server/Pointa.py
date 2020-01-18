import asyncio
import random
import math
import time


class Player:
    'Base Player Class'
    def __init__(self, key):
        self.key = key
        self.properties = {
            'hp': 100,
            'pt': 0,
            'def': 0
        }
        # 0 = atk, 1 = def, 2 = hel
        self.actions = {
            0: 0,
            1: 0,
            2: 0
        }

        self.temp = {}

    def action(self, data):
        self.actions = data

    def roundClear(self):
        self.properties['def'] = 0
        self.actions = {
            0: 0,
            1: 0,
            2: 0
        }

    def roll(self):
        self.temp['roll'] = random.randint(1, 12)
        self.properties['pt'] += self.temp['roll']
        return self.temp['roll']

    def damage(self, pt):
        self.temp['judge'] = random.randint(1, 12)

        if self.temp['judge'] in range(1, 6):
            self.temp['dmg'] = math.ceil((0.30 * pt ^ 2) * 0.5)
        elif self.temp['judge'] in range(6, 12):
            self.temp['dmg'] = math.ceil((0.30 * pt ^ 2))
        elif self.temp['judge'] == 12:
            self.temp['dmg'] = math.ceil((0.30 * pt ^ 2) * 1.5)

        self.temp['def'] = self.properties['def']

        self.properties['def'] = [
            0,
            self.properties['def'] - self.temp['dmg']
        ][
            self.properties['def'] > self.temp['dmg']
        ]

        self.temp['dmg'] = [
            0,
            self.temp['dmg'] - self.temp['def']
        ][
            self.temp['dmg'] > self.temp['def']
        ]

        self.properties['hp'] -= self.temp['dmg']

        return self.temp['judge']


class Pointa:
    'Base Game Emulator, Contains all Game Logics'
    def __init__(self, p1, p2):
        self.players = {
            p1.key: p1,
            p2.key: p2
        }
        self.round = {
            'num': 0,
            'phase': 0
        }
        self.actions = []
        self.temp = {}
        self.log = []

    def settleRound(self):
        # Step 0, Check if actions are avaliable
        for p in self.players.items():
            if sum(p.actions.items()) > p.properties['pt']:
                return p

        # Setp 1, Sort out the actions.
        for key, p in self.players:
            for action, value in p.actions:
                self.actions.append({
                    'own': key,
                    'action': action,
                    'value': value
                })
        self.actions.sort(key=lambda x: (x['value'], -x['action']))

        # Step 2, Take actions.
        for action in self.actions:
            self.players[action['own']].properties['pt'] -= action['value']

            if action['action'] == 0:  # Attack
                self.temp['target'] = sorted(
                    self.players.pop(action['own']).items())[0]
                self.logger(
                    action['own'],
                    'atkJudge',
                    self.temp['target'].damage(action['value'])
                )

            elif action['action'] == 1:  # Defense
                self.players[
                    action['own']
                ].properties[
                    'def'
                ] = (0.25 * action['value'] ^ 2)

            elif action['action'] == 2:  # Healing
                self.players[
                    action['own']
                ].properties[
                    'hp'
                ] = (0.35 * action['value'] ^ 2)

                if self.players[action['own']].properties['hp'] > 100:
                    self.players[action['own']].properties['hp'] = 100

        # Step 3, Clear the nums
        for p in self.players:
            p.roundClear()

    def gameStat(self):
        return {
            'Players': self.players.items(),
            'Round': self.round,
            'Log': self.log
        }

    def logger(self, actor, action, value):
        self.log.append(
            {
                'time': int(time.time()),
                'actor': actor,
                'action': action,
                'value': value
            }
        )

    async def main(self):
        self.round['num'] += 1
        self.logger('game', 'roundBegin', self.round['num'])

        # Phase 1
        self.round['phase'] = 1
        self.logger('game', 'phaseBegin', self.round)
        for key, p in self.players:
            self.logger(key, 'pointRolled', p.roll())

        # Phase 2
        self.round['phase'] = 2
        self.logger('game', 'phaseBegin', self.round)
        await asyncio.sleep(15)

        # Phase 3
        self.round['phase'] = 2
        self.logger('game', 'phaseBegin', self.round)
        self.settleRound()

        for key, p in self.players:
            if p.properties['hp'] < 1:
                return p

        self.main()
