# def popular_words (text, words):
#     text_words = text.lower().split()
#     count_world = {}
#     for word in words:
#         count_world[word] = text_words.count(word)
#
#     return count_world
#
#
# assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
# print('OK')


# def difference(*args):
#     result = 0
#     for x in args:
#         result = round(max(args) - min(args), 2)
#
#     return result
#
#
#
# assert difference(1, 2, 3) == 2, 'Test1'
# assert difference(5, -5) == 10, 'Test2'
# assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
# assert difference() == 0, 'Test4'
# print('OK')


