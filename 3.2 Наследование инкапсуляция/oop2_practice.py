{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "-"
    }
   },
   "source": [
    "# ООП-2\n",
    "\n",
    "Булыгин Олег:  \n",
    "* [LinkedIn](linkedin.com/in/obulygin)  \n",
    "* [Мой канал в ТГ по Python](https://t.me/pythontalk_ru)\n",
    "* [Чат канала](https://t.me/pythontalk_chat)\n",
    "* [Блог в Телетайпе](https://teletype.in/@pythontalk)\n",
    "* [PythonTalk на Кью](https://yandex.ru/q/loves/pythontalk/)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "-"
    }
   },
   "source": [
    "### Инкапсуляция\n",
    "\n",
    "Инкапсуляция заключается в том, что данные скрыты за пределами определения объекта. Это позволяет разработчикам создавать удобный интерфейс взаимодействия и защитить данные от внешних источников."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true,
    "slideshow": {
     "slide_type": "-"
    }
   },
   "outputs": [],
   "source": [
    "class Character:\n",
    "    def __init__(self, name, power, energy=100, hands=2):\n",
    "        self.name = name\n",
    "        self.power = power\n",
    "        self.energy = energy\n",
    "        self.backpack = [] \n",
    "        self.hands = hands\n",
    "    \n",
    "    def eat(self, food):\n",
    "        if self.energy < 100:\n",
    "            self.energy += food\n",
    "        else:\n",
    "            print('Not hungry')\n",
    "        \n",
    "    \n",
    "    def do_exercise(self, hours):\n",
    "        if self.energy > 0:\n",
    "            self.energy -= hours * 2\n",
    "            self.power += hours * 2\n",
    "        else:\n",
    "            print('Too tired')\n",
    "    \n",
    "    def change_alias(self, new_alias):\n",
    "        self.alias = new_alias\n",
    "\n",
    "    def beat_up(self, foe):\n",
    "        if not isinstance(foe, Character): \n",
    "            return\n",
    "        if foe.power < self.power:\n",
    "            foe.status = 'defeated'\n",
    "            self.status = 'winner'\n",
    "        else:\n",
    "            print('Retreat!')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "scrolled": true,
    "slideshow": {
     "slide_type": "-"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[]\n"
     ]
    }
   ],
   "source": [
    "peter = Character('Peter Parker', 80)\n",
    "print(peter.backpack)\n",
    "peter.do_exercise(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "-"
    }
   },
   "source": [
    "Реализуем защищенную переменную и метод"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "scrolled": true,
    "slideshow": {
     "slide_type": "-"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Spider-Man\n",
      "[]\n"
     ]
    }
   ],
   "source": [
    "# реализуем защищенную переменную и метод\n",
    "class Character:\n",
    "    def __init__(self, name, power, energy=100, hands=2):\n",
    "        self.name = name\n",
    "        self.power = power\n",
    "        self.energy = energy\n",
    "        self._backpack = [] \n",
    "        self.hands = hands\n",
    "    \n",
    "    def eat(self, food):\n",
    "        if self.energy < 100:\n",
    "            self.energy += food\n",
    "        else:\n",
    "            print('Not hungry')\n",
    "    \n",
    "    def do_exercise(self, hours):\n",
    "        if self.energy > 0:\n",
    "            self.energy -= hours * 2\n",
    "            self.power += hours * 2\n",
    "        else:\n",
    "            print('Too tired')\n",
    "    \n",
    "    def _change_alias(self, new_alias):\n",
    "        self.alias = new_alias\n",
    "    \n",
    "    def beat_up(self, foe):\n",
    "        if not isinstance(foe, Character): \n",
    "            return\n",
    "        if foe.power < self.power:\n",
    "            foe.status = 'defeated'\n",
    "            self.status = 'winner'\n",
    "        else:\n",
    "            print('Retreat!')\n",
    "            \n",
    "    \n",
    "\n",
    "peter = Character('Peter Parker', 80)\n",
    "peter._change_alias('Spider-Man')\n",
    "print(peter.alias)\n",
    "print(peter._backpack)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "На самом деле, технические для интерпретатора это не имеет никакого значения. Это просто соглашение, согласно которому, такие атрибуты и методы не стоит использовать за рамками класса и дочерних классов."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Двойное подчеркивание в начале имени атрибута/метода дает большую защиту: атрибут становится недоступным по этому имени вне самого класса."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'Character' object has no attribute '__change_alias'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[0;32m/tmp/ipykernel_32787/358707266.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     36\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     37\u001b[0m \u001b[0mpeter\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mCharacter\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'Peter Parker'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m80\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 38\u001b[0;31m \u001b[0mpeter\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__change_alias\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'Spider-Man'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     39\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mpeter\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__backpack\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mAttributeError\u001b[0m: 'Character' object has no attribute '__change_alias'"
     ]
    }
   ],
   "source": [
    "# реализуем приватную переменную и метод\n",
    "\n",
    "class Character:\n",
    "    def __init__(self, name, power, energy=100, hands=2):\n",
    "        self.name = name\n",
    "        self.power = power\n",
    "        self.energy = energy\n",
    "        self.__backpack = [] \n",
    "        self.hands = hands\n",
    "    \n",
    "    def eat(self, food):\n",
    "        if self.energy < 100:\n",
    "            self.energy += food\n",
    "        else:\n",
    "            print('Not hungry')\n",
    "        \n",
    "    \n",
    "    def do_exercise(self, hours):\n",
    "        if self.energy > 0:\n",
    "            self.energy -= hours * 2\n",
    "            self.power += hours * 2\n",
    "        else:\n",
    "            print('Too tired')\n",
    "    \n",
    "    def __change_alias(self, new_alias):\n",
    "        self.alias = new_alias\n",
    "\n",
    "    def beat_up(self, foe):\n",
    "        if not isinstance(foe, Character): \n",
    "            return\n",
    "        if foe.power < self.power:\n",
    "            foe.status = 'defeated'\n",
    "            self.status = 'winner'\n",
    "        else:\n",
    "            print('Retreat!')\n",
    "\n",
    "peter = Character('Peter Parker', 80)\n",
    "peter.__change_alias('Spider-Man')\n",
    "print(peter.__backpack)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['_Character__change_alias',\n",
       " '__class__',\n",
       " '__delattr__',\n",
       " '__dict__',\n",
       " '__dir__',\n",
       " '__doc__',\n",
       " '__eq__',\n",
       " '__format__',\n",
       " '__ge__',\n",
       " '__getattribute__',\n",
       " '__gt__',\n",
       " '__hash__',\n",
       " '__init__',\n",
       " '__init_subclass__',\n",
       " '__le__',\n",
       " '__lt__',\n",
       " '__module__',\n",
       " '__ne__',\n",
       " '__new__',\n",
       " '__reduce__',\n",
       " '__reduce_ex__',\n",
       " '__repr__',\n",
       " '__setattr__',\n",
       " '__sizeof__',\n",
       " '__str__',\n",
       " '__subclasshook__',\n",
       " '__weakref__',\n",
       " 'beat_up',\n",
       " 'do_exercise',\n",
       " 'eat']"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dir(Character)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Но и это можно обойти при помощи прямого указания класса."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Spider-Man\n",
      "[]\n"
     ]
    }
   ],
   "source": [
    "peter = Character('Peter Parker', 80)\n",
    "peter._Character__change_alias('Spider-Man')\n",
    "print(peter.alias)\n",
    "print(peter._Character__backpack)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Таким образом, реализация инкапсуляции в Python носит формальный характер и работает только на уровне соглашения.\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Наследование"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "0\n",
      "100\n",
      "2\n",
      "Pew-Pew!\n"
     ]
    }
   ],
   "source": [
    "# и сразу реализуем множественное наследование!\n",
    "\n",
    "class Character:\n",
    "    name = ''\n",
    "    power = 0\n",
    "    energy = 100\n",
    "    hands = 2\n",
    "\n",
    "class Spider:\n",
    "    power = 0\n",
    "    energy = 50\n",
    "    hands = 8\n",
    "    \n",
    "    def webshoot(self):\n",
    "        print('Pew-Pew!')\n",
    "\n",
    "        \n",
    "class SpiderMan(Character, Spider):\n",
    "    pass\n",
    "\n",
    "# class SpiderMan(Spider, Character):\n",
    "#     pass\n",
    "\n",
    "peter_parker = SpiderMan()\n",
    "print(peter_parker.name)\n",
    "print(peter_parker.power)\n",
    "print(peter_parker.energy)\n",
    "print(peter_parker.hands)\n",
    "peter_parker.webshoot()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Линеаризация способ представления дерева (графа, дерева) в линейную модель (плоскую структуру, список) для определения порядка наследования."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[<class '__main__.SpiderMan'>, <class '__main__.Character'>, <class '__main__.Spider'>, <class 'object'>]\n"
     ]
    }
   ],
   "source": [
    "print(SpiderMan.mro())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Peter Parker\n",
      "100\n",
      "80\n",
      "2\n",
      "90\n",
      "100\n"
     ]
    }
   ],
   "source": [
    "class Character:\n",
    "    # перенесем все в init\n",
    "     def __init__(self, name, power, energy=100, hands=2):\n",
    "        self.name = name\n",
    "        self.power = power\n",
    "        self.energy = energy\n",
    "        self.hands = hands\n",
    "    \n",
    "\n",
    "class Spider:\n",
    "    def __init__(self, power, energy=50, hands=8):\n",
    "        self.power = power\n",
    "        self.energy = energy\n",
    "        self.hands = hands\n",
    "        \n",
    "    def webshoot(self):\n",
    "        print('Pew-Pew!')\n",
    "\n",
    "        \n",
    "    \n",
    "class SpiderMan(Character, Spider):\n",
    "    def turn_spider_sense(self):\n",
    "        self.energy -= 10\n",
    "        self.power += 20\n",
    "\n",
    "              \n",
    "        \n",
    "peter_parker = SpiderMan('Peter Parker', 80)\n",
    "print(peter_parker.name)\n",
    "print(peter_parker.energy)\n",
    "print(peter_parker.power)\n",
    "print(peter_parker.hands)\n",
    "peter_parker.turn_spider_sense()\n",
    "print(peter_parker.energy)\n",
    "print(peter_parker.power)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Полиморфизм\n",
    "\n",
    "Полиморфизм позволяет методам с одинаковыми именами реализовывать разную функциональность для разных классов (в т.ч. дочерних)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Changing position\n"
     ]
    }
   ],
   "source": [
    "# добавим в наши родительские классы новые методы\n",
    "\n",
    "class Character:\n",
    "    def __init__(self, name, power, energy=100, hands=2):\n",
    "        self.name = name\n",
    "        self.power = power\n",
    "        self.energy = energy\n",
    "        self.hands = hands\n",
    "\n",
    "    def move(self):\n",
    "        print('Changing position')\n",
    "\n",
    "        \n",
    "class Spider:\n",
    "    def __init__(self, power, energy=50, hands=8):\n",
    "        self.power = power\n",
    "        self.energy = energy\n",
    "        self.hands = hands\n",
    "    \n",
    "    def webshoot(self):\n",
    "        print('Pew-Pew!')\n",
    "    \n",
    "    def move(self):\n",
    "        self.webshoot()\n",
    "        print('Changing position')\n",
    "\n",
    "        \n",
    "    \n",
    "class SpiderMan(Character, Spider):\n",
    "    def turn_spider_sense(self):\n",
    "        self.energy -= 10\n",
    "        self.power += 20\n",
    "\n",
    "peter_parker = SpiderMan('Peter Parker', 80)\n",
    "peter_parker.move()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pew-Pew!\n",
      "Moving on 3 square\n"
     ]
    }
   ],
   "source": [
    "class Character:\n",
    "    def __init__(self, name, power, energy=100, hands=2):\n",
    "        self.name = name\n",
    "        self.power = power\n",
    "        self.energy = energy\n",
    "        self.hands = hands\n",
    "\n",
    "    def move(self):\n",
    "        print('Moving on 2 squares')\n",
    "\n",
    "        \n",
    "class Spider:\n",
    "    def __init__(self, power, energy=50, hands=8):\n",
    "        self.power = power\n",
    "        self.energy = energy\n",
    "        self.hands = hands\n",
    "    \n",
    "    def webshoot(self):\n",
    "        print('Pew-Pew!')\n",
    "    \n",
    "    def move(self):\n",
    "        self.webshoot()\n",
    "        print('Moving on 1 square')\n",
    "\n",
    "        \n",
    "    \n",
    "class SpiderMan(Character, Spider):\n",
    "    \n",
    "    def turn_spider_sense(self):\n",
    "        self.energy -= 10\n",
    "        self.power += 20\n",
    "    \n",
    "    def move(self):\n",
    "        self.webshoot()\n",
    "        print('Moving on 3 square')\n",
    "\n",
    "        \n",
    "peter_parker = SpiderMan('Peter Parker', 80)\n",
    "peter_parker.move()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "А теперь хотим создам инвентарь нашему игровому персонажу"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[]\n"
     ]
    }
   ],
   "source": [
    "class Character:\n",
    "    def __init__(self, name, power, energy=100, hands=2):\n",
    "        self.name = name\n",
    "        self.power = power\n",
    "        self.energy = energy\n",
    "        self.hands = hands\n",
    "\n",
    "    def move(self):\n",
    "        print('Moving on 2 squares')\n",
    "\n",
    "        \n",
    "class Spider:\n",
    "    def __init__(self, power, energy=50, hands=8):\n",
    "        self.power = power\n",
    "        self.energy = energy\n",
    "        self.hands = hands\n",
    "    \n",
    "    def webshoot(self):\n",
    "        print('Pew-Pew!')\n",
    "    \n",
    "    def move(self):\n",
    "        self.webshoot()\n",
    "        print('Moving on 1 square')\n",
    "\n",
    "        \n",
    "    \n",
    "class SpiderMan(Character, Spider):\n",
    "    # такой вариант допустимый, но зачем нам перезаписывать инициализацию,\n",
    "    # которая полностью совпадает с родителем?\n",
    "    def __init__(self, name, power, energy=100, hands=2):\n",
    "        self.name = name\n",
    "        self.power = power\n",
    "        self.energy = energy\n",
    "        self.hands = hands\n",
    "        self.backpack = []\n",
    "    \n",
    "    def turn_spider_sense(self):\n",
    "        self.energy -= 10\n",
    "        self.power += 20\n",
    "\n",
    "    def move(self):\n",
    "        self.webshoot()\n",
    "        print('Moving on 3 square')\n",
    "\n",
    "        \n",
    "peter_parker = SpiderMan('Peter Parker', 100)\n",
    "print(peter_parker.backpack)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Функция super() можно получить доступ к унаследованным методам, которые были перезаписаны в дочернем классе."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[]\n",
      "80\n",
      "100\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "class Character:\n",
    "    def __init__(self, name, power, energy=100, hands=2):\n",
    "        self.name = name\n",
    "        self.power = power\n",
    "        self.energy = energy\n",
    "        self.hands = hands\n",
    "\n",
    "    def move(self):\n",
    "        print('Moving on 2 squares')\n",
    "\n",
    "class Spider:\n",
    "    def __init__(self, power, energy=50, hands=8):\n",
    "        self.power = power\n",
    "        self.energy = energy\n",
    "        self.hands = hands\n",
    "    \n",
    "    def webshoot(self):\n",
    "        print('Pew-Pew!')\n",
    "    \n",
    "    def move(self):\n",
    "        self.webshoot()\n",
    "        print('Moving on 1 square')   \n",
    "    \n",
    "class SpiderMan(Character, Spider):\n",
    "    # мы полностью наследуем от родителя инициализацию и добавляем новый атрибут для экземпляра\n",
    "    def __init__(self, name, power):\n",
    "        super().__init__(name, power)\n",
    "        self.backpack = []\n",
    "        \n",
    "    def turn_spider_sense(self):\n",
    "        self.energy -= 10\n",
    "        self.power += 20\n",
    "\n",
    "    def move(self):\n",
    "        self.webshoot()\n",
    "        print('Moving on 3 square')\n",
    "\n",
    "\n",
    "peter_parker = SpiderMan('Peter Parker', 80)\n",
    "print(peter_parker.backpack)\n",
    "print(peter_parker.power)\n",
    "print(peter_parker.energy)\n",
    "print(peter_parker.hands)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "No web!\n"
     ]
    }
   ],
   "source": [
    "class Character:\n",
    "    def __init__(self, name, power, energy=100, hands=2):\n",
    "        self.name = name\n",
    "        self.power = power\n",
    "        self.energy = energy\n",
    "        self.hands = hands\n",
    "\n",
    "    def move(self):\n",
    "        print('Moving on 2 squares')\n",
    "\n",
    "        \n",
    "class Spider:\n",
    "    def __init__(self, power, energy=50, hands=8):\n",
    "        self.power = power\n",
    "        self.energy = energy\n",
    "        self.hands = hands\n",
    "    \n",
    "    def webshoot(self):\n",
    "        print('Pew-Pew!')\n",
    "    \n",
    "    def move(self):\n",
    "        self.webshoot()\n",
    "        print('Moving on 1 square')   \n",
    "    \n",
    "    \n",
    "class SpiderMan(Character, Spider):\n",
    "    def __init__(self, name, power):\n",
    "        super().__init__(name, power)\n",
    "        self.backpack = []\n",
    "        \n",
    "    def turn_spider_sense(self):\n",
    "        self.energy -= 10\n",
    "        self.power += 20\n",
    " \n",
    "    # наш персонаж не может пользоваться паутиной, если ее нет! попробуем исправить\n",
    "    # где ошибка?\n",
    "    def webshoot(self):\n",
    "        if 'web' in self.backpack:\n",
    "            self.webshoot() \n",
    "        else:\n",
    "            print('No web!')\n",
    "\n",
    "    def move(self):\n",
    "        self.webshoot()\n",
    "        print('Moving on 3 square')\n",
    "\n",
    "\n",
    "\n",
    "peter_parker = SpiderMan('Peter Parker', 80)\n",
    "peter_parker.webshoot()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "ename": "RecursionError",
     "evalue": "maximum recursion depth exceeded",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mRecursionError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[0;32m/tmp/ipykernel_32787/336789318.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0mpeter_parker\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mbackpack\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'web'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mpeter_parker\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwebshoot\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m/tmp/ipykernel_32787/159286754.py\u001b[0m in \u001b[0;36mwebshoot\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m     37\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mwebshoot\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     38\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0;34m'web'\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mbackpack\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 39\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwebshoot\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     40\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     41\u001b[0m             \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'No web!'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "... last 1 frames repeated, from the frame below ...\n",
      "\u001b[0;32m/tmp/ipykernel_32787/159286754.py\u001b[0m in \u001b[0;36mwebshoot\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m     37\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mwebshoot\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     38\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0;34m'web'\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mbackpack\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 39\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwebshoot\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     40\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     41\u001b[0m             \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'No web!'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mRecursionError\u001b[0m: maximum recursion depth exceeded"
     ]
    }
   ],
   "source": [
    "peter_parker.backpack.append('web')\n",
    "peter_parker.webshoot()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "No web!\n",
      "Pew-Pew!\n"
     ]
    }
   ],
   "source": [
    "class Character:\n",
    "    def __init__(self, name, power, energy=100, hands=2):\n",
    "        self.name = name\n",
    "        self.power = power\n",
    "        self.energy = energy\n",
    "        self.hands = hands\n",
    "\n",
    "    def move(self):\n",
    "        print('Moving on 2 squares')\n",
    "\n",
    "        \n",
    "class Spider:\n",
    "    def __init__(self, power, energy=50, hands=8):\n",
    "        self.power = power\n",
    "        self.energy = energy\n",
    "        self.hands = hands\n",
    "    \n",
    "    def webshoot(self):\n",
    "        print('Pew-Pew!')\n",
    "    \n",
    "    def move(self):\n",
    "        self.webshoot()\n",
    "        print('Moving on 1 square')   \n",
    "    \n",
    "    \n",
    "class SpiderMan(Character, Spider):\n",
    "    def __init__(self, name, power):\n",
    "        super().__init__(name, power)\n",
    "        self.backpack = []\n",
    "        \n",
    "    def turn_spider_sense(self):\n",
    "        self.energy -= 10\n",
    "        self.power += 20\n",
    "    \n",
    "    # исправляем\n",
    "    def webshoot(self):\n",
    "        if 'web' in self.backpack:\n",
    "            super().webshoot() \n",
    "        else:\n",
    "            print('No web!')\n",
    "\n",
    "    def move(self):\n",
    "        self.webshoot()\n",
    "        print('Moving on 3 square')\n",
    "\n",
    "        \n",
    "peter_parker = SpiderMan('Peter Parker', 80)\n",
    "peter_parker.webshoot()\n",
    "peter_parker.backpack.append('web')\n",
    "peter_parker.webshoot()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Можем ли наследовать что-то не от родителя по mro, а от другого родителя?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "90\n"
     ]
    },
    {
     "ename": "AttributeError",
     "evalue": "'Character' object has no attribute 'status'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[0;32m/tmp/ipykernel_32787/3986917366.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     61\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     62\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0menemy\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mhealth\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 63\u001b[0;31m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0menemy\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstatus\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m: 'Character' object has no attribute 'status'"
     ]
    }
   ],
   "source": [
    "# добавим родительским классам атаку и проверим, как будет наследоваться\n",
    "\n",
    "class Character:\n",
    "    def __init__(self, name, power, energy=100, hands=2):\n",
    "        self.name = name\n",
    "        self.power = power\n",
    "        self.energy = energy\n",
    "        self.hands = hands\n",
    "\n",
    "    def move(self):\n",
    "        print('Moving on 2 squares')\n",
    "    \n",
    "    def attack(self, foe):\n",
    "        foe.health -= 10\n",
    "        \n",
    "        \n",
    "class Spider:\n",
    "    def __init__(self, power, energy=50, hands=8):\n",
    "        self.power = power\n",
    "        self.energy = energy\n",
    "        self.hands = hands\n",
    "    \n",
    "    def webshoot(self):\n",
    "        print('Pew-Pew!')\n",
    "    \n",
    "    def move(self, foe):\n",
    "        self.webshoot()\n",
    "        print('Moving on 1 square')   \n",
    "        \n",
    "    def attack(self, foe):\n",
    "        foe.status = 'stunned'\n",
    "    \n",
    "    \n",
    "class SpiderMan(Character, Spider):\n",
    "    def __init__(self, name, power):\n",
    "        super().__init__(name, power)\n",
    "        self.backpack = []\n",
    "        \n",
    "    def turn_spider_sense(self):\n",
    "        self.energy -= 10\n",
    "        self.power += 20\n",
    "    \n",
    "    def webshoot(self):\n",
    "        if 'web' in self.backpack:\n",
    "            super().webshoot() \n",
    "        else:\n",
    "            print('No web!')\n",
    "\n",
    "    def move(self):\n",
    "        self.webshoot()\n",
    "        print('Moving on 3 square')\n",
    "        \n",
    "\n",
    "\n",
    "        \n",
    "peter_parker = SpiderMan('Peter Parker', 80)\n",
    "enemy = Character('Some Enemy', 10)\n",
    "enemy.health = 100\n",
    "\n",
    "peter_parker.attack(enemy)\n",
    "\n",
    "print(enemy.health)\n",
    "print(enemy.status)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "90\n",
      "stunned\n"
     ]
    }
   ],
   "source": [
    "# сделаем у дочернего класса свою атаку\n",
    "\n",
    "class Character:\n",
    "    def __init__(self, name, power, energy=100, hands=2):\n",
    "        self.name = name\n",
    "        self.power = power\n",
    "        self.energy = energy\n",
    "        self.hands = hands\n",
    "\n",
    "    def move(self):\n",
    "        print('Moving on 2 squares')\n",
    "    \n",
    "    def attack(self, foe):\n",
    "        foe.health -= 10\n",
    "        \n",
    "        \n",
    "class Spider:\n",
    "    def __init__(self, power, energy=50, hands=8):\n",
    "        self.power = power\n",
    "        self.energy = energy\n",
    "        self.hands = hands\n",
    "    \n",
    "    def webshoot(self):\n",
    "        print('Pew-Pew!')\n",
    "    \n",
    "    def move(self):\n",
    "        self.webshoot()\n",
    "        print('Moving on 1 square')   \n",
    "        \n",
    "    def attack(self, foe):\n",
    "        foe.status = 'stunned'\n",
    "    \n",
    "    \n",
    "class SpiderMan(Character, Spider):\n",
    "    def __init__(self, name, power):\n",
    "        super().__init__(name, power)\n",
    "        self.backpack = []\n",
    "        \n",
    "    def turn_spider_sense(self):\n",
    "        self.energy -= 10\n",
    "        self.power += 20\n",
    "    \n",
    "    def webshoot(self):\n",
    "        if 'web' in self.backpack:\n",
    "            super().webshoot() \n",
    "        else:\n",
    "            print('No web!')\n",
    "\n",
    "    def move(self):\n",
    "        self.webshoot()\n",
    "        print('Moving on 3 square')\n",
    "        \n",
    "    # делаем классу свою атаку   \n",
    "    def attack(self, foe):\n",
    "        super().attack(foe)\n",
    "        Spider.attack(self, foe)\n",
    "        \n",
    "\n",
    "peter_parker = SpiderMan('Peter Parker', 80)\n",
    "enemy = Character('Some Enemy', 10)\n",
    "enemy.health = 100\n",
    "peter_parker.attack(enemy)\n",
    "\n",
    "print(enemy.health)\n",
    "print(enemy.status)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Магические методы – это общий термин, относящийся к \"специальным\" методам классов, для которых нет единого определения, поскольку их применение разнообразно. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "И мы также можем перегрузить эти магические методы"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n",
      "True\n",
      "<__main__.SpiderMan object at 0x7f52504722e0>\n",
      "<__main__.SpiderMan object at 0x7f5250472520>\n"
     ]
    }
   ],
   "source": [
    "class Character:\n",
    "    def __init__(self, name, power, energy=100, hands=2):\n",
    "        self.name = name\n",
    "        self.power = power\n",
    "        self.energy = energy\n",
    "        self.hands = hands\n",
    "\n",
    "    def move(self):\n",
    "        print('Moving on 2 squares')\n",
    "    \n",
    "    def attack(self, foe):\n",
    "        foe.health -= 10\n",
    "        \n",
    "        \n",
    "class Spider:\n",
    "    def __init__(self, power, energy=50, hands=8):\n",
    "        self.power = power\n",
    "        self.energy = energy\n",
    "        self.hands = hands\n",
    "    \n",
    "    def webshoot(self):\n",
    "        print('Pew-Pew!')\n",
    "    \n",
    "    def move(self):\n",
    "        self.webshoot()\n",
    "        print('Moving on 1 square')   \n",
    "        \n",
    "    def attack(self, foe):\n",
    "        foe.status = 'stunned'\n",
    "    \n",
    "    \n",
    "class SpiderMan(Character, Spider):\n",
    "    def __init__(self, name, power):\n",
    "        super().__init__(name, power)\n",
    "        self.backpack = []\n",
    "        \n",
    "    def turn_spider_sense(self):\n",
    "        self.energy -= 10\n",
    "        self.power += 20\n",
    "    \n",
    "    def webshoot(self):\n",
    "        if 'web' in self.backpack:\n",
    "            super().webshoot() \n",
    "        else:\n",
    "            print('No web!')\n",
    "\n",
    "    def move(self):\n",
    "        self.webshoot()\n",
    "        print('Moving on 3 square')\n",
    "        \n",
    "    def attack(self, foe):\n",
    "        super().attack(foe)\n",
    "        Spider.attack(self, foe)\n",
    "        \n",
    "#     добавим возможность сравнения персонажей \n",
    "    def __lt__(self, other):\n",
    "        if not isinstance(other, Character):\n",
    "            print('Not a Character!')\n",
    "            return\n",
    "        return self.power < other.power\n",
    "    \n",
    "#     def __str__(self):\n",
    "#         res = f'Имя: {self.name}\\nСила персонажа = {self.power}'\n",
    "#         return res\n",
    "    \n",
    "    \n",
    "peter_parker = SpiderMan('Peter Parker', 80)\n",
    "miles_morales = SpiderMan('Miles Morales', 85)\n",
    "\n",
    "print(peter_parker < miles_morales)\n",
    "# и даже \"больше\" будет работать!\n",
    "print(peter_parker > miles_morales)\n",
    "print(peter_parker.__lt__(miles_morales))\n",
    "\n",
    "print(peter_parker)\n",
    "print(miles_morales)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "celltoolbar": "Slideshow",
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": false,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
