
def template(param):
    """параметризованный декоратор"""

    def _template(old_function):

        def new_function(*args, **kwargs):
            ...  # код до вызова исходной функции
            print(f'параметр равен {param}')  # можем использовать параметр
            print('Декоратор до функции')
            result = old_function(*args, **kwargs)
            print('Декоратор после функции')
            ...  # код после вызова исходной функции
            return result

        return new_function

    return _template


@template(param=42)
def hello_world():
    return print('Hello World')

hello_world()
