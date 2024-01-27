def even_odd_filter(**kwargs):

    if 'odd' in kwargs.keys():
        kwargs['odd'] = [num for num in kwargs['odd'] if num % 2 != 0]
    if 'even' in kwargs.keys():
        kwargs['even'] = [num for num in kwargs['even'] if num % 2 == 0]

    return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
