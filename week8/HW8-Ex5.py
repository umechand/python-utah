

# Exercise #5 “Abstract classes” (10 points)
# Part 1:

class Box:
    def add(self, *items):
        raise NotImplementedError()

    def empty(self):
        raise NotImplementedError()

    def count(self):
        raise NotImplementedError()

class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class ListBox(Box):
    def __init__(self):
        self._items = []

    def add(self, *items):
        self._items.extend(items)

    def empty(self):
        items = self._items
        self._items = []
        return items

    def count(self):
        return len(self._items)

class DictBox(Box):
    def __init__(self):
        self._items = {}

    def add(self, *items):
        self._items.update(dict((i.name, i) for i in items))

    def empty(self):
        items = list(self._items.values())
        self._items = {}
        return items

    def count(self):
        return len(self._items)

# Part 2:

# Part 2:

def repack_boxes(*boxes):
    items = []

    for box in boxes:
        items.extend(box.empty())

    while items:
        for box in boxes:
            try:
                box.add(items.pop())
            except IndexError:
                break

box1 = ListBox()
for i in range(20):
    item = Item(str(i), i)
    box1.add(item)

box2 = ListBox()
for i in range(9):
    item = Item(str(i), i)
    box2.add(item)

box3 = DictBox()
for i in range(5):
    item = Item(str(i), i)
    box3.add(item)

repack_boxes(box1, box2, box3)

print(box1.count())
print(box2.count())
print(box3.count())
