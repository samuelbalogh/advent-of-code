""" Part one """

from collections import defaultdict



class BotManager(object):
    def __init__(self, instructions):
        self.bots = []
        self.outputs = defaultdict(list)
        self.instructions = instructions

    def initialize(self):
        with open(self.instructions) as data:
            while True:
                try:
                    line = next(data)
                    if line.startswith('bot'):
                        bot_number = line.split(' ')[1].strip()
                        low_target_type = line.split(' ')[5].strip()
                        low_target = line.split(' ')[6].strip()
                        high_target_type = line.split(' ')[10].strip()
                        high_target = line.split(' ')[11].strip()
                        bot = Bot(bot_number, low_target_type, low_target, high_target_type, high_target)
                        self.bots.append(bot)
                except StopIteration:
                    break

    def start_working(self):
        with open(self.instructions) as data:
            while True:
                try:
                    line = next(data)
                    if line.startswith('value'):
                        value = line.split(' ')[1].strip()
                        bot_id = line.split(' ')[5].strip()
                        bot = self.get_bot_by_id(bot_id)
                        bot.add_chip(value)
                except StopIteration:
                    break
        self.next_bot_with_two_chips().pass_on_chips()

    def get_all_bots(self):
        return self.bots

    def get_number_of_bots(self):
        return len(self.bots)

    def get_all_bot_info(self):
        for i in [bot.__dict__ for bot in self.bots]:
            print(i)

    def get_output_info(self):
        return self.outputs

    def next_bot_with_two_chips(self):
        try:
            return [bot for bot in self.bots if len(bot.chips) == 2][0]
        except IndexError:
            return

    def get_orders(self):
        with open(self.instructions) as data:
            orders = [line.strip() for line in data.readlines() if line.startswith('bot')]
        return orders

    def get_bot_by_id(self, number):
        for bot in self.bots:
            if bot.number == number:
                return bot

    def get_output_by_id(self, idx):
        return self.outputs[idx]

    def add_chip_to_output(self, idx, chip):
        self.outputs[idx].append(chip)


class Bot(object):
    """ Represent a bot """
    def __init__(self, number, low_target_type, give_low_to, high_target_type, give_high_to):
        self.number = number
        self.low_target_type = low_target_type
        self.give_low_to = give_low_to
        self.high_target_type = high_target_type
        self.give_high_to = give_high_to
        self.dispatched_all_chips = False
        self.chips = []

    @property
    def low(self):
        return min(self.chips) if self.chips else []

    @property
    def high(self):
        return max(self.chips) if self.chips else []


    def add_chip(self, chip):
        self.chips.append(int(chip))


    def pass_on_chips(self):
        if 17 in self.chips and 61 in self.chips:
            print('--------')
            print('--------')
            print(self.number)
            print('--------')
            print('--------')
        types = [self.low_target_type, self.high_target_type]
        low_chip = self.low
        high_chip = self.high
        self.chips = []
        for type in range(len(types)):
            if type == 0:
                if types[type]== 'output':
                    bot_manager.get_output_by_id(self.give_low_to).append(low_chip)
                elif types[type] == 'bot':
                    bot_manager.get_bot_by_id(self.give_low_to).add_chip(low_chip)
            elif type == 1:
                if types[type]== 'output':
                    bot_manager.get_output_by_id(self.give_high_to).append(high_chip)
                elif types[type] == 'bot':
                    bot_manager.get_bot_by_id(self.give_high_to).add_chip(high_chip)
        if len(bot_manager.get_bot_by_id(self.give_low_to).chips) == 2:
            bot_manager.get_bot_by_id(self.give_low_to).pass_on_chips()
        if len(bot_manager.get_bot_by_id(self.give_high_to).chips) == 2:
            bot_manager.get_bot_by_id(self.give_high_to).pass_on_chips()

global bot_manager
bot_manager = BotManager('input')
bot_manager.initialize()
bot_manager.start_working()

""" Part two """

product = 1
for i in range(3):
    product *= bot_manager.outputs[str(i)][0]
print(product)
