def choose_class(name):
    if name == 'foo':
        class Foo:
            pass

        return Foo
    else:
        class Bar:
            pass

        return Bar


my_class = choose_class('foo')  # Foo
print(my_class)
my_class = choose_class('bar')  # Bar
print(my_class)
