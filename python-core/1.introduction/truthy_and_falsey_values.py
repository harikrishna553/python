def demo(a):
    if a:
        print(f'{a} is evaluated to True')
    else:
        print(f'{a} is evaluated to False')

demo(0)
demo(0.0)
demo(1)

demo('')
demo('  ')

demo([])
demo([2, 3])

demo({})
demo({'x' : 123})

demo(None)
demo(True)