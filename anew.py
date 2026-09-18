import string
import traceback

metaslash = 1

def printNames():
    global neal, michele, eric
    neal = 'neal'
    michele = 'michele'
    eric = 5
    # Bug: 'eric' is an integer (5), but the format string uses '%(eric)d' 
    # Wait, %d works for integers. Let's look closer at the scope/name bugs.
    print("Local values: %(neal)s %(michele)s %(eric)d" % locals())

class Nothing:
    def init(self, value):  # Bug: Should be __init__ instead of init
        self.value = value

    def printValue(self):
        print(self.value)

def tryToDoSomething(value):
    try:
        if not value:
            raise (RuntimeError, "Hey, there's no value")
        printNames()
    except:
        traceback.print_exc()

useless = Nothing(5)
print('a useless value is:', useless.value)  # This will crash because __init__ was never called properly to set self.value
