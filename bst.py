class BSTNode:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None

class BookBST:
    def __init__(self):
        self.root = None

    def insert(self, book):
        self.root = self._insert(self.root, book)

    def _insert(self, node, book):
        if not node:
            return BSTNode(book)
        if book.title < node.book.title:
            node.left = self._insert(node.left, book)
        else:
            node.right = self._insert(node.right, book)
        return node

    def inorder(self):
        books = []
        self._inorder(self.root, books)
        return books

    def _inorder(self, node, books):
        if node:
            self._inorder(node.left, books)
            books.append(node.book)
            self._inorder(node.right, books)

    def search_by_title(self, title):
        return self._search(self.root, title)

    def _search(self, node, title):
        if not node:
            return None
        if title == node.book.title:
            return node.book
        elif title < node.book.title:
            return self._search(node.left, title)
        else:
            return self._search(node.right, title)
