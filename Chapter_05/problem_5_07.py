def rain(colors) :
    colors.append("purple")
    colors = ["green", "blue"]
    return colors

rainbow = ["red", "orange"]
print(rain(rainbow))            # ["green", "blue"]

# ["red", "orange", "purple"]을 출력하고 싶으면

# def rain(colors) :
    # colors.append("purple")
    # colors = ["green", "blue"]

# rainbow = ["red", "orange"]
# rain(rainbow)
# print(rainbow)