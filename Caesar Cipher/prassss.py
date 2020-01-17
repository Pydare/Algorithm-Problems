def finish(*args):
    print('The list of all the players would be ',*args)

finish('boy','girl','man','woman')

def start(**kwargs):
    for key,value in kwargs.items():
        print('I just want to do it {}, or never {}'.format(key,value))


start(boy='Dare',girl='Frances',man='George',woman='Frin')