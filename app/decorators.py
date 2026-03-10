def fence(func):
    def wrapper():
        print("-")
        func()
        print("+")
    return wrapper

@fence
def log():
    print("Hello Sushil")

log()

# Output
# -
# Hello Sushil
# +