def foo():
    bar()

def bar():
    foo()

def main():
    print('foo...')
    foo()


if __name__ == '__main__':
    main()
