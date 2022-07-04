class Ide:
    def functionalities(self):
        funcs=["create","delete","rename"]
        return funcs


class Pycharm(Ide):
    def functionalities(self):
       func=super().functionalities()
       func.append("execute")
       func.append("debug")
       return func


py=Pycharm()
print(py.functionalities())

