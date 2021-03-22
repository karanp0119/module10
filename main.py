import matplotlib.pyplot as plt
from plotnine import *
from plotnine.data import diamonds


def main():
    x = [1, 3, 5, 7, 9]
    y = [6, 7, 9, 10, 12]

    plt.plot(x, y)
    plt.show()

    p = (ggplot(diamonds)
         + aes(x="price")
         + geom_bar(size=20)
         )
    print(p)


if __name__ == "__main__":
    main()
