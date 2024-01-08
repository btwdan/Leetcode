class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def splitListToParts(self, head, k):
        length = 0
        curr = head
        #Запускаем цикл для опередения длины списка
        while curr:
            length += 1
            curr = curr.next
        #Выясняем является ли k целочисленым делителем на длину списка
        size = length // k
        remainder = length % k
        #Заводим переменую для хранения результата
        res = []
        #Перекидываем ссылку на ервый элемент
        curr = head
        for i in range(k):
            res_head = curr
            part_length = size + (1 if i < remainder else 0)
            #Проходим по списку до нужного элемента
            for j in range(part_length - 1):
                if curr:
                    curr = curr.next
            #Обнуляем следующую ссылку и делаем слудующую ссылку головой
            if curr:
                next_node = curr.next
                curr.next = None
                curr = next_node
            #Заносим в итоговый массив ссылку
            res.append(res_head)

        return res