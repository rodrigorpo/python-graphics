import matplotlib.pyplot as plt


def main():
    print("Generation numbers")
    list_x, list_y = generatePoints()
    writeFile(list_x, list_y)
    draw_graph(list_x, list_y)


# noinspection PyPep8Naming
def writeFile(x, y):
    f = open("graphic.txt", "w+")
    for i in x:
        f.write(str(i) + "==>" + str(y[i]) + "\n")
    f.close()


def draw_graph(x, y):
    plt.plot(x, y)
    plt.ylabel('Y axis')
    plt.xlabel('X axis')
    plt.show()


def generatePoints():
    list_x = list(range(-20, 20))
    list_y = []
    for i in list_x:
        y = i*i*i + i * i + 2 * i + 200
        list_y.append(y)
    return list_x, list_y


if __name__ == "__main__":
    main()
