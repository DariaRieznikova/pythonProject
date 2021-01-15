# змінні оточення
def globVar(res=None):
    def setRes(val):
        nonlocal res
        res = val

    def getRes():
        return res

    return setRes, getRes


setResult, getResult = globVar({})
sizeCell = 100
