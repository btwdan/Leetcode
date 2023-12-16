class MyStack(object):
    
    def __init__(self):
        self._quit = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self._quit.append(x)

        

    def pop(self):
        """
        :rtype: int
        """
        for i in range(len(self._quit) - 1):
            self.push(self._quit.popleft())
        return self._quit.popleft()
        

    def top(self):
        """
        :rtype: int
        """
        return self._quit[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self._quit) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()