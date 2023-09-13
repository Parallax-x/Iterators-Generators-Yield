from flatiterator import FlatIterator, test_1
from flatgenerator import flat_generator, test_2
from flatiterator_1 import FlatIterator1, test_3
from flatgenerator_1 import flat_generator_1, test_4

list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

if __name__ == '__main__':
    for item in FlatIterator(list_of_lists_1):
        print(item, end=', ')
    test_1()
    print('')
    for item in flat_generator(list_of_lists_1):
        print(item, end=', ')
    test_2()
    print('')
    for item in FlatIterator1(list_of_lists_2):
        print(item, end=', ')
    test_3()
    print('')
    for item in flat_generator_1(list_of_lists_2):
        print(item, end=', ')
    test_4()
