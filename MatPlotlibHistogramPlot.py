import matplotlib.pyplot as plt

def main():
    marks = [45,55,60,62,65,67,70,72,75,78,80,82,85,90,92]

    plt.hist(
        marks,              # Continuous data
        bins= 5,            # Number of groups
        edgecolor = "black",
        alpha = 0.8,        # Transparency       
        rwidth= 0.9         # Relative width of bar

    )

    plt.title ("Marvellous Histogram Plot")
    plt.xlabel ("Marks")
    plt.ylabel ("Frequecny")
    plt.show()    

if __name__ == "__main__":
    main()