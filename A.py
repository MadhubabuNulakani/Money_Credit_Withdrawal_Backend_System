class A:
    def f(self):
        if self.retry < 3:
            try:
                  num =int(input())
            except  Exception as e:
                self.retry += 1
                print(f" hi ")
                self.f()
                print(f"Hello..")
            print(f"num is : {num} ")
obj=A()
obj.retry=0
obj.f()
          