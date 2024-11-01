import threading
import time

print('"За честь и отвагу"')
print('-----------------')

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.duration = 0
        self.enemies = 100

    def battle(self, name, power):
        self.power = power
        while self.enemies > 0:
            time.sleep(1)
            self.enemies -= power
            self.duration += 1
            print(f'{name} сражается {self.duration} дней(дня)..., осталось {self.enemies} войнов')


    def run(self):
        print(f'{self.name}, на нас напали!')
        self.battle(self.name, self.power)
        print(f'{self.name} одержал победу спустя {self.duration} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')

