class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def binaryTreePaths(self, root):
        def dfs(node, path, paths):
            if node is None:
                return

            path.append(str(node.val))                      # Добавляем значение текущего узла в текущий путь

            if node.left is None and node.right is None:    # Проверяем, является ли текущий узел листом
                paths.append("->".join(path))               # Если да, то добавляем текущий путь в список путей
            else:
                dfs(node.left, path, paths)                 # Рекурсивно обходим левое поддерево
                dfs(node.right, path, paths)                # Рекурсивно обходим правое поддерево

            path.pop()                                      # Удаляем текущий узел из текущего пути (возвращаемся на уровень выше)
    
        paths = []
        dfs(root, [], paths)                                # Вызываем вспомогательную функцию dfs для обхода дерева
        return paths