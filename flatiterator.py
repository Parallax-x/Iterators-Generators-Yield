class FlatIterator:

    def __init__(self, list_of_list: list):
        self.list_of_list = list_of_list
        self.cursor = -1
        self.len_list = len(list_of_list)

    def __iter__(self):
        self.cursor += 1
        self.nest_cursor = -1
        return self

    def __next__(self):
        self.nest_cursor += 1
        self.len_list_in_list = len(self.list_of_list[self.cursor])
        if self.nest_cursor == self.len_list_in_list:
            self.__iter__()
            self.nest_cursor += 1
        if self.cursor == self.len_list:
            raise StopIteration
        item = self.list_of_list[self.cursor][self.nest_cursor]
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]