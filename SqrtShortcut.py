import pickle
import math

_n_max = 10000
_path = "./roots.txt"


class Roots(object):
    def __init__(self, read=True):
        if read:
            root_file = open(_path)
            self.sqrt_table = pickle.load(root_file)
            root_file.close()
            self.sqrt_table_len = len(self.sqrt_table)
        else:
            self.calc_sqrt_table()

    def calc_sqrt_table(self):
        self.sqrt_table = list()

        for i in range(1, _n_max + 1):
            self.sqrt_table.append(math.sqrt(i))

        self.sqrt_table_len = len(self.sqrt_table)

    def write_sqrt_table(self):
        root_file = open(_path, 'w')
        pickle.dump(self.sqrt_table, root_file)
        root_file.close()

    def get(self, x):
        if x < 0:
            x *= -1

        if x < self.sqrt_table_len:
            return self.sqrt_table[int(round(x)) - 1]
        else:
            return None

if __name__ == "__main__":
    roots = Roots(read=False)
    roots.write_sqrt_table()

    roots2 = Roots()

    for v in roots2.sqrt_table:
        print(v)
