# def my_function():
#     global msg
#     msg = "Hello"
#     print(msg)
#     #namespace local
#     return None
#
# my_function()
# print(msg)


def my_function():
    def my_second_function():
        print(f"functia mea secundara: {msg}")
        return None

    msg = "Hello"

    my_second_function()
    print(f"functia mea principala: {msg}")

    return None

my_function()