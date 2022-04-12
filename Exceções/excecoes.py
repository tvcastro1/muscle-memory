def validador(x):
    a = 50
    try:
        a += x
    except Exception as e:
        print(f'{e}')
    else:
        return a
    finally:
        if isinstance(x, int):
            print('Vai rodar!!')
        else:
            print('Vai dar pau!')




print(validador('a'))
