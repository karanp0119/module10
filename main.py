import matplotlib.pyplot as plt
from plotnine import *
from plotnine.data import diamonds


def main():
    x = [1, 3, 5, 7, 9]
    y = [6, 7, 9, 10, 12]

    plt.plot(x, y)
    plt.show()

    p = (ggplot(diamonds)  # What data to use
         + aes(x="price")  # What variable to use
         + geom_bar(size=20)  # Geometric object to use for drawing
         )
    print(p)


if __name__ == "__main__":
    main()
