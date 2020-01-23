import random
import time
import threading

#Основной класс, который включает в себя объекты Мама, Сын, Дочка
class MoneyWaster(threading.Thread):
    name = ""
    money = 0
    working = False
    #Функция генерирует рандомное время от 1го до 3х и выводит количество средств которое получил объект
    def work(self):
        global daddys_money
        while self.working:
            i = random.randint(1, 3)
            time.sleep(i)
            want = random.randint(500, 2000)
            if daddys_money >= want:
            	#Вывод в консоль при наличии средств у папы
                daddys_money -= want
                self.money += want
                if self.name != "сын":
                    print(self.name + " получила от папы " + str(want) + " грн, и теперь у нее " + str(
                        self.money) + " грн\n")
                else:
                    print(self.name + " получил от папы " + str(want) + " грн, и теперь у него " + str(
                        self.money) + " грн\n")

            else:
            	#Вывод в консоль при отсутствии средств у отца
                print(self.name + " хочет " + str(want) + " грн, но фигушки\n")
        time.sleep(3)
        #Вывод общей полученной саммы
        print(self.name + " говорит пока-пока с " + str(self.money) + " грн в кармане\n")


daddys_money = 100
#Инициализация объектов класса
mom = MoneyWaster()
mom.name = "мама"
daughter = MoneyWaster()
daughter.name = "дочь"
son = MoneyWaster()
son.name = "сын"
mom.working = True
daughter.working = True
son.working = True
#Содадние потоков
thread1 = threading.Thread(target=son.work)
thread2 = threading.Thread(target=mom.work)
thread3 = threading.Thread(target=daughter.work)
#Запуск потоков
thread1.start()
thread2.start()
thread3.start()
#Цикл, в котором отец получает по 1000 грн каждые 2 секунды
for i in range(10):
    time.sleep(2)
    daddys_money += 1000
    print("папа получил 1000 грн и теперь у него " + str(daddys_money) + " грн\n")
#Остановка метода working
mom.working = False
daughter.working = False
son.working = False
time.sleep(3)
print("папа денег больше не дает\n")
#Остановка потоков
thread1.join()
thread2.join()
thread3.join()
