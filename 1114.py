class Foo:
    def __init__(self):
        self.p1, self.p2, self.p3 = 1, 0, 0

    def first(self, printFirst) -> None:
        while True:
            if self.p1 == 1:
                self.p1 -= 1
                break
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        while True:
            if self.p2 == 0:
                self.p2 += 1
                break

    def second(self, printSecond) -> None:
        while True:
            if self.p2 == 1:
                self.p2 -= 1
                break
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        while True:
            if self.p3 == 0:
                self.p3 += 1
                break

    def third(self, printThird) -> None:
        while True:
            if self.p3 == 1:
                self.p3 -= 1
                break
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        while True:
            if self.p1 == 0:
                self.p1 += 1
                break
