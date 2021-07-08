from typing import Any


class stack:

    __stack = []

    def push(self, data) -> None:
        """
        Занесение элемента в стек. Размер увеличивается на единицу, элемент становится вершиной
        """
        self.__stack.append(data)
    
    def pop(self) -> Any:
        """
        Извлечь элемент, являющийся вершиной стека и умнешьить размер на единицу
        """
        try:
            item = self.__stack[-1]
        except IndexError:
            return
        
        self.__stack.__delitem__(-1)
        
        return item

    def peek(self) -> Any:
        """
        Получить значение элемента, находящегося на вершине стека, не нарушая его целостности
        """
        try:
            return self.__stack[-1]
        except IndexError:
            return

    def empty(self) -> bool:
        """
        Предикат истинен, когда стек пуст
        """
        return not bool(self.__stack.__len__())

    def destroy(self) -> None:
        """
        Разрушить стек
        """
        del self

    def __str__(self) -> str:
        """
        Метод печати стека
        """
        return self.__stack.__str__()