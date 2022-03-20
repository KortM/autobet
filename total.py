import math
from game_parser import get_command_stat, parse_command



class Total:

    def __init__(self):
        pass

    def count_raiting(self, games: dict) -> tuple:
        scored = []
        loose = []
        if len(games) < 5: return 'Расчет не возможен игр меньше 5'
        else:
            games = [i for i in games if i['score']]
            for count in range(5):
                print(games[::-1][count])
                scored.append(games[::-1][count]['score'][0])
                loose.append(games[::-1][count]['score'][1])
            scored.remove(max(scored))
            scored.remove(min(scored))
            raiting_attack = round((sum(scored) / len(scored)), 1)
            print(raiting_attack)
            loose.remove(max(loose))
            loose.remove(min(loose))
            raiting_defense = round((sum(loose) / len(loose)), 1)
            print(raiting_defense)

            return raiting_attack, raiting_defense
    
    def total(self, one_command, two_command):
        total_one = (one_command[0] + two_command[1]) - one_command[1]
        total_two = (two_command[0] + one_command[1]) - two_command[1]
        print(total_one, total_two)



    def total_home(self, games: dict) -> int:
        pass
    
    def total_2comand_away(self, games: dict) -> int:
        pass

    def total_min(self, games: dict) -> int:
        pass

    def total_max(self, games: dict) -> int:
        pass

    def total_avg(self, games: dict) -> int:
        '''Средний тотал на основании максимального и минимального расчета '''
        return (self.total_min + self.total_max) / 2


if __name__ == '__main__':
    t = Total()
    games = get_command_stat(parse_command('Барс'))
    games2 = get_command_stat(parse_command('Йокерит'))
    command_one = t.count_raiting(games)
    commmand_two = t.count_raiting(games2)
    t.total(command_one, commmand_two)
