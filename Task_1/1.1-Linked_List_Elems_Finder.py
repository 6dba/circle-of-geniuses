import time
from typing import Any

class Node:

	def __init__(self, data=None, next=None) -> None:
		"""
		Узел
		"""
		self.data = data
		self.next = next


class LinkedList:

	def __init__(self) -> None:
		"""
		Инициализация списка
		"""
		self.first = None
		self.last = None
		self.length = 0


	def __getitem__(self, attr) -> Any:
		"""
		Получение элемента по индексу
		"""
		if not isinstance(attr, int):
			raise TypeError(f'list indices must be integers, not {type(attr)} ')

		if attr >= self.length or attr < -1:
			raise IndexError('list index out of range')
		
		if attr == -1:
			return self.last.data

		if self.length != 0:
			length = 0

			while self.first:
				
				if attr == length:
					return self.first.data
					
				length += 1
				self.first = self.first.next


	def __str__(self) -> str:
		"""
		Метод печати списка
		"""
		if self.length == 0:
			return '[]'

		# Если существует, но только 1 элемент
		if self.first and self.first.next == None:
			return '[' + str(self.first.data) + ']'

		out = '[' 
		while self.first.next != None:
			out += str(self.first.data) + ', '
			self.first = self.first.next 
			
			if self.first.next == None:
				out += str(self.first.data)
		return out + ']'


	def clear(self) -> None:
		"""
		Очистка списка
		"""
		self.__init__()


	def append(self, data) -> None:
		"""
		Метод добавления элемента в список
		"""
		self.length += 1

		if self.first == None:
			self.first = self.last = Node(data=data, next=None)
		else:
			self.last.next = self.last = Node(data=data, next=None)
	

	def finder(self, sought) -> float:
		"""
    	Поиск элементов в односвязном списке путем перебора.
    	Средняя выч. сложность - Θ(n)
    	"""
		start_time = time.perf_counter()

		if self.length != 0:
			while self.first:
				if self.first.data == sought:
					break
				self.first = self.first.next
		return time.perf_counter() - start_time


list = LinkedList()

for num in range(10):
	list.append(num)

# Допустим, что искомый элемент, оказался первым
print("Поиск перебором. Сложность - Θ(1): ", list.finder(1))
	
# Элемента не оказалось
print("Поиск перебором. Сложность - Θ(N): ", list.finder(666))

# Аналогично поиску перебором в массиве, у нас получилось константное время обращения (Θ(1)) в первом паттерне поиска
# из-за того, что нужный элемент оказался первым
# Время доступа сопоставимо со временем в варианте с массивом
# Также, полный перебор списка (Θ(N)) оказался затратнее. Время на выполнение незначительно превышает
# аналогичную операцию с массивом, будем считать, что увеличение времени - есть дополнительная обработка реализации Linked List

# В связном списке, как и в массиве временная сложность поиска - O(N), ускоряют процесс поиска только частные случаи
# на подобие того, как нужный нам элемент оказался первым