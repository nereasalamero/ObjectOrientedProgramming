# Handling several custom errors
class ErrorNew(Exception):
    def __init__(self, *args: object):
        super().__init__(*args)
        self.message = args[0]
        self.code = args[1]

class ErrorValueNegative(Exception):
    def __init__(self, text, code):
        self.text = text
        self.code = code

class ErrorValuePositive(Exception):
    def __init__(self, text, code):
        self.text = text
        self.code = code

class Value:
    def __init__(self):
        pass

    def check_value(self, value):
        if value < 0:
            raise ErrorNew("Value is negative.", 128)
            # raise ErrorValueNegative("Value is negative.", 128)
        elif value > 0:
            raise ErrorValuePositive("Value is positive.", 256)
        else:
            print("Value is OK = ", value)


if __name__ == "__main__":
    v = Value()
    try:
        v.check_value(int(input("Enter the number zero (0): ")))
    except ErrorValueNegative as e:
        print("Error: ", e.text, "Code: ", e.code)
    except ErrorValuePositive as e:
        print("Error: ", e.text, "Code: ", e.code)
    except ErrorNew as e:
        print(e.message + " " + str(e.code))
    except ValueError as e:
        print("Error: ", e)
    else:
        print("No errors.")