class FlatIterator1:

    def __init__(self, list_of_list: list):
        self.stack = []
        self.list_of_list = list_of_list
        self.cursor = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor >= len(self.list_of_list):
            if self.stack:
                self.list_of_list, self.cursor = self.stack.pop()
                return next(self)
            else:
                raise StopIteration
        item = self.list_of_list[self.cursor]
        self.cursor += 1

        if type(item) is not list:
            return item
        else:
            self.stack.append((self.list_of_list, self.cursor))
            self.list_of_list = item
            self.cursor = 0
            return next(self)


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator1(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator1(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
