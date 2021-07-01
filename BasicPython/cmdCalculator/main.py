import optparse


class Calculator:

    def addition(self):
        print("Addition")

    def subtraction(self):
        pass

    def multiplication(self):
        pass

    def division(self):
        pass


def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-o", "--oper", dest="operation",
                      help="Operation for Addition,Subtraction,Multiplication,Division")
    return parser.parse_args()


(value, arguments) = get_args()
oper = value.operation
calc = Calculator()
if oper[0].lower() == 'a':
    calc.addition()
elif oper[0].lower() == 's':
    calc.subtraction()
elif oper[0].lower() == 'm':
    calc.multiplication()
elif oper[0].lower() == 'd':
    calc.division()
