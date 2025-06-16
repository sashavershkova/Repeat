def first_uncommon(matrix, n):
    # Your implementation here!

    freq_dict = {}

    for tup in matrix:
        for char in tup:
            freq_dict[char] = freq_dict.get(char, 0) + 1
    
    for k, v in freq_dict.items():
        if v < n:
            return k



matrix_1 = (
    ('u','e','r','e', ' ', 'e'),
    ('d', 'z', 'o', 'b', 'i', 'v'),
    ('n',),
    ('w', 'g', 'q', ' ', '5', 'g', 'w'),
    ('r',),
    ('y', 'e'),
    ('u', 'a', 'u', 't')
)
assert first_uncommon(matrix_1, 2) == 'd'
assert first_uncommon(matrix_1, 3) == 'r'
assert first_uncommon(matrix_1, 4) == 'u'

matrix_2 = (
    ('💜',),
)
assert first_uncommon(matrix_2, 2) == '💜'
assert first_uncommon(matrix_2, 525600) == '💜'

print("All tests passed! Discuss time and space complexity if time remains!")

# print(first_uncommon(matrix_1, 3))