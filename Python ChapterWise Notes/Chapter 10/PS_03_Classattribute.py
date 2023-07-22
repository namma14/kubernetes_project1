class new:
    a = "nachiketa"
    def abc(self):
        print(self.a)
    @staticmethod
    def greet():
        print("Hello Programmers")

naya = new()
naya.a = 0
new.a = "nabhay"
print(naya.a)
print(new.a)
naya.abc()
naya.greet()

