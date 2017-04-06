import math


class Heap(object):
    def __init__(self, get_val=None, max_heap=False):
        self.data = list()

        if get_val is None:
            self.get_key = Heap._self_val
        else:
            self.get_key = get_val

        if max_heap:
            self.heap_compare = Heap._max_heap_compare
        else:
            self.heap_compare = Heap._min_heap_compare

    @staticmethod
    def _self_val(value):
        return value

    @staticmethod
    def _max_heap_compare(current_value, parent_value):
        return current_value > parent_value

    @staticmethod
    def _min_heap_compare(current_value, parent_value):
        return current_value < parent_value

    def add(self, value):
        self.data.append(value)
        self.heapify_up()

    @staticmethod
    def get_left_child(idx):
        return 2 * idx + 1

    @staticmethod
    def get_right_child(idx):
        return 2 * idx + 2

    @staticmethod
    def get_parent(idx):
        return int(round(math.floor(idx - 1) / 2))

    def swap(self, child_idx, parent_idx):
        self.data[child_idx], self.data[parent_idx] = self.data[parent_idx], self.data[child_idx]

    def heapify_up(self):
        done = False
        current_idx = int(len(self.data) - 1)
        current_value = self.get_key(self.data[current_idx])

        while not done and current_idx > 0:
            parent_idx = Heap.get_parent(current_idx)
            parent_value = self.get_key(self.data[parent_idx])

            if self.heap_compare(current_value, parent_value):
                self.swap(current_idx, parent_idx)
                current_idx = parent_idx
            else:
                done = True

    def heapify_down(self):
        done = False
        current_idx = 0
        child_idx = 1

        # swap the head and the tail
        self.swap(len(self.data) - 1, 0)

        return_data = self.data.pop()

        while not done and child_idx < len(self.data):
            current_value = self.get_key(self.data[current_idx])
            child_value = self.get_key(self.data[child_idx])

            # if right child exists
            if len(self.data) > child_idx + 1 and self.heap_compare(self.get_key(self.data[child_idx]), child_value):
                child_value = self.get_key(self.data[child_idx])
                child_idx += 1

            if self.heap_compare(child_value, current_value):
                self.swap(current_idx, child_idx)
                current_idx = child_idx
                child_idx = Heap.get_left_child(current_idx)
            else:
                done = True

        return return_data

    def pop(self):
        return self.heapify_down()

    def __str__(self):
        out = []

        dlen = len(self.data)
        for i in range(0, len(self.data)):
            iv = str(self.get_key(self.data[i]))
            lci = str(Heap.get_left_child(i))
            rci = str(Heap.get_right_child(i))
            lcv = ""
            rcv = ""

            if int(lci) < dlen:
                lcv = str(self.get_key(self.data[int(lci)]))
            if int(rci) < dlen:
                rcv = str(self.get_key(self.data[int(rci)]))

            out.append("[{0}]: {1} ([{2}]: {3}) <--> ([{4}]: {5})".format(i, iv, lci, lcv, rci, rcv))
        return '\n'.join(out)

if __name__ == "__main__":
    h = Heap()

    h.add(2)

    h.add(7)
    h.add(12)

    h.add(4)
    h.add(6)
    h.add(13)
    h.add(11)

    print str(h)
    h.add(8)
    print '-----------------'
    print str(h)

    print '-----------------'
    print h.pop()
    print str(h)