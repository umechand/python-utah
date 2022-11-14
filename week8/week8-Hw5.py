
# PART -1

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
    # TODO: create a new variable called items and set it equal to _items.
    # TODO: set the private variable _items to a new list, this will make _items empty again.
    # TODO: return the new items variable.

    def count(self):
        return len(self._items)
        # TODO: Create a return statement to return the length of the items.


class DictBox(Box):
    def __init__(self):
        self._items = {}

    def add(self, *items):
        self._items.update(dict((i, i) for i in items))

    def empty(self):
        items = list(self._items.values())
        self._items = {}
        return items
    # TODO: create a new variable and set it equal to the dictionary values. (A new list, not a new dictionary using self._items.values())
    # TODO: set the private variable _items to a new dictionary to make it empty.
    # TODO: return the new variable.

    def count(self):
        return len(self._items)

# TODO: Create a return statement to return the length of the items.


#PART-2

import math

def repack_boxes(*boxes):
    items = []

    # get all the items from each box, save it to a new variable called items, then empty the boxes.
    for box in boxes:
        items.extend(box.empty())

    # now we have all of the items in each box inside one list, traverse the list of items.

    div = len(items) / len(boxes)
    start = 0
    end = math.floor(div)
    total_boxes = len(boxes)
    box_num = 1

    # for each box passed in, add an item to box, remove the item from the item list as its added to the box.
    # if we pass in 3 boxes to this function, that means we'll add 3 items to the boxes and remove those items
    # from the list on each pass within the for loop.
    for box in boxes:
        try:
            if box_num < total_boxes:
                box.add(*items[start:end])
                start = end
                end = end + math.floor(div)
                box_num = box_num + 1
            else:
                end = end + 1
                box.add(*items[start:end])
        # TODO: for each box in boxes: box.add(items.pop())
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
