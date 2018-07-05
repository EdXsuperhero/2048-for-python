# made by Edison Shi
# copyright by Edison Shi
# just a little game for everyone to play.
import random

# these are some helper functions for the game.
def merge_left(v):
    v = exclude_zero(v)
    for i in range(3):
        if v[i] == v[i+1]:
            v[i] = str(int(v[i])*2)
            v[i+1] = '0'
    return exclude_zero(v)

def merge_right(v):
    return merge_left(v[::-1])[::-1]

def exclude_zero(v):
    '''get a list of items that keep zeros on the right
    '''
    res = []

    for i in range(len(v)):
        item = v[i]
        if item != '0':
            res.append(item)
    while len(res) != len(v):
        res.append('0')
    return res




class Vector:
    ''' the row vector of the matrix'''
    def __init__(self, a='0', b='0', c='0', d='0'):
        self._content = [a, b, c, d]
    def merge_left(self):
        self._content = merge_left(self._content)
    def merge_right(self):
        self._content = merge_right(self._content)

class Matrix:
    ''' a matrix for the body of the game'''
    def __init__(self):
        self._vectors = [Vector(), Vector(), Vector(), Vector()]
        self._flag = True

    def __str__(self):
        res = ''
        for v in self._vectors:
            for entry in v._content:
                res += (entry + ' ')
            res = res[:-1]
            res += '\n'
        return res[:-1]

    # add 2 randomly to a Vector.
    def add(self):
        idx_set = self.get_idx_set()
        if len(idx_set) != 0 and self._flag:
            random_point = random.randint(0, len(idx_set)-1)
            idx = idx_set[random_point]
            ran_int = random.randint(1,2)
            self._vectors[idx[0]]._content[idx[1]] = str(ran_int*2)
        else:
            self._flag = False

    def get_idx_set(self):
        '''get a list of index of zero entries.
        '''
        idx_set = []
        idx_1 = -1
        for v in self._vectors:
            idx_1 += 1
            for i in range(4):
                if v._content[i] == '0':
                    idx_2 = i
                    idx_set.append((idx_1,idx_2))
        return idx_set

    def transpose(self):
        cols = []
        col = []
        for i in range(4):
            for v in self._vectors:
                col.append(v._content[i])
            cols.append(Vector(col[0], col[1], col[2], col[3]))
            col.clear()
        self._vectors = cols

class Game():
    ''' the game of 2048'''
    def __init__(self):
        self._body = Matrix()
        self._body.add()
        self._body.add()


    def action_left(self):
        temp_body = str(self._body)
        for row in self._body._vectors:
            row.merge_left()
        if temp_body != str(self._body):
            self._body.add()

    def action_right(self):
        temp_body = str(self._body)
        for row in self._body._vectors:
            row.merge_right()
        if temp_body != str(self._body):
            self._body.add()

    def action_up(self):
        body_to_check = str(self._body)
        self._body.transpose()
        for row in self._body._vectors:
            row.merge_left()
        self._body.transpose()
        if body_to_check != str(self._body):
            self._body.add()

    def action_down(self):
        body_to_check = str(self._body)
        self._body.transpose()
        for row in self._body._vectors:
            row.merge_right()
        self._body.transpose()
        if body_to_check != str(self._body):
            self._body.add()

if __name__ == '__main__':

    #print('\n=======\n')

    #a = Game()
    #print('start the game:')
    #print(a._body)

    #print('\n=======\n')
    #a.action_left()
    #print('do action left:')
    #print(a._body)

    #print('\n=======\n')
    #a.action_right()
    #print('do action right:')
    #print(a._body)

    #print('\n=======\n')
    #a.action_left()
    #print('do action left again:')
    #print(a._body)

    #print('\n=======\n')
    #a.action_up()
    #print('do action up:')
    #print(a._body)

    #print('\n=======\n')
    #a.action_down()
    #print('do action down:')
    #print(a._body)


    game = Game()
    print("enter 'ok' to start the game")
    if str(input()) == 'ok':
        print('\n=======')
        print(game._body)
        print('=======\n')
        while game._body._flag:
            action = str(input("please give a direction: 'w', 'a', 's', 'd'\n"))
            if action in ['w', 'a', 's', 'd']:
                if action == 'w':
                    game.action_up()
                elif action == 'a':
                    game.action_left()
                elif action == 's':
                    game.action_down()
                else:
                    game.action_right()
                print('\n=======')
                print(game._body)
                print('=======\n')
