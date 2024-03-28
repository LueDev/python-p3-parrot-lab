# def deccy(func):
#     def wrapper(*args, **kwargs):
#         print("Before func call")
#         result = func(*args, **kwargs)
#         print("After func call")
#         return result
#     return wrapper

# @deccy
def parrot(stringy="Squawk!") -> str:
    print(stringy)
    return stringy

if __name__ == "__main__":
    print(parrot())