import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def ReadCSV():
    print("The Covid19 data analysis of December 2020 India by CSV")
    df = pd.read_csv("C:\\Users\\Divyansh\\Desktop\\covid project.csv")
    print(df)


def BarPlot():
    df = pd.read_csv("C:\\Users\\Divyansh\\Desktop\\covid project.csv")
    st = df['State/UT']
    cnf = df['Confirmed']
    rc = df['Recovered']
    dth = df['Deaths']
    ac = df['Active']
    plt.xlabel("state")
    plt.xticks(rotation='vertical')

    while True:
        print("Select Specific Bar Plot as given below:")
        print("Press 1 to print the data for State vs Confirmed Cases")
        print("Press 2 to print the data for State vs Recovered Cases")
        print("Press 3 to print the data for State vs Death Cases")
        print("Press 4 to print the data for State vs Active Cases")
        print("Press 5 to print all data in one Bar Plot")
        print("Press 6 to Go to Main Menu")

        op = int(input("Enter your Choice:"))

        if op == 1:
            plt.ylabel("Confirmed Cases")
            plt.title("State wise Confirmed Cases")
            plt.bar(st, cnf)
            plt.show()
        elif op == 2:
            plt.ylabel("Recovered Cases")
            plt.title("State wise Recovered Cases")
            plt.bar(st, rc)
            plt.show()
        elif op == 3:
            plt.ylabel("Death Cases")
            plt.title("State wise Death Cases")
            plt.bar(st, dth)
            plt.show()
        elif op == 4:
            plt.ylabel("Active Cases")
            plt.title("State wise Active Cases")
            plt.bar(st, ac)
            plt.show()
        elif op == 5:
            ind = np.arange(len(st))
            width = 0.2
            plt.bar(ind, cnf, width, label="State wise Confirmed Cases")
            plt.bar(ind + 0.3, rc, width, label="State wise Recovered Cases")
            plt.bar(ind + 0.6, dth, width, label="State wise Death Cases")
            plt.bar(ind + 0.9, ac, width, label="State wise Active Cases")
            plt.legend()
            plt.show()
        elif op == 6:
            print("\nMain Menu")
            break
        else:
            print("Invalid Input")


def lineChart():
    df = pd.read_csv("")
    st = df['State/UT']
    cnf = df['Confirmed']
    rc = df['Recovered']
    dth = df['Deaths']
    ac = df['Active']
    plt.xlabel("state")
    plt.xticks(rotation='vertical')

    while True:
        print("Select Specific Line Chart as given below:")
        print("Press 1 to print the data for State vs Confirmed Cases")
        print("Press 2 to print the data for State vs Recovered Cases")
        print("Press 3 to print the data for State vs Death Cases")
        print("Press 4 to print the data for State vs Active Cases")
        print("Press 5 to to print all data in one Line Chart")
        print("Press 6 to Go to Main Menu")

        op = int(input("Enter your Choice:"))

        if op == 1:
            plt.ylabel("Confirmed Cases")
            plt.title("State wise Confirmed Cases")
            plt.plot(st, cnf)
            plt.show()
        elif op == 2:
            plt.ylabel("Recovered Cases")
            plt.title("State wise Recovered Cases")
            plt.plot(st, rc)
            plt.show()
        elif op == 3:
            plt.ylabel("Death Cases")
            plt.title("State wise Death Cases")
            plt.plot(st, dth)
            plt.show()
        elif op == 4:
            plt.ylabel("Active Cases")
            plt.title("State wise Active Cases")
            plt.plot(st, ac)
            plt.show()
        elif op == 5:
            plt.ylabel("number of cases")
            plt.plot(st, cnf, label="state wise confirmed cases")
            plt.plot(st, rc, label="state wise recoverd  cases")
            plt.plot(st, dth, label="state wise death ")
            plt.plot(st, ac, label="state wise active cases")
            plt.legend()
            plt.show()
        elif op == 6:
            print("\nMain Menu")
            break
    else:
        print("Invalid Input")


def specific_col():
    print("The Table consist of 4 colums: 1.Recovered , 2.Active ,3.Confirmed and 4.Deaths")
    print("To enter again in main menu TYPE Go to Main menu")
    while True:
        op = str(input("Enter the specific column to display:"))
        if op == "Recovered":
            print("Reading specific column from specific file")
            df = pd.read_csv("C:\\Users\\Divyansh\\Desktop\\covid project.csv", usecols=['State/UT', 'Recovered'],
                             index_col=0)
            print(df)
        elif op == "Active":
            print("Reading specific column from specific file")
            df = pd.read_csv("C:\\Users\\Divyansh\\Desktop\\covid project.csv", usecols=['State/UT', 'Active'],
                             index_col=0)
            print(df)
        elif op == "Confirmed":
            print("Reading specific column from specific file")
            df = pd.read_csv("C:\\Users\\Divyansh\\Desktop\\covid project.csv", usecols=['State/UT', 'Confirmed'],
                             index_col=0)
            print(df)
        elif op == "Deaths":
            print("Reading specific column from specific file")
            df = pd.read_csv("C:\\Users\\Divyansh\\Desktop\\covid project.csv", usecols=['State/UT', 'Deaths'],
                             index_col=0)
            print(df)
        elif op == "Go to Main menu":
            print("\nMain Menu")
            break
        else:
            print("Invalid Input")


def main_menu():
    while True:
        print("1.The Covid19 data analysis of December 2020 India by CSV")
        print("===============================================")
        print("Data Visualization of The Covid19 data")
        print("2.Bar Plot")
        print("3.Line Chart")
        print("===============================================")
        print("Apply Data Manipulation in the records of CSV File")
        print("4.Read the specific columns")
        print("5.Exit the Program")

        opt = int(input("enter your choice="))
        if opt == 1:
            ReadCSV()
        elif opt == 2:
            BarPlot()
        elif opt == 3:
            lineChart()
        elif opt == 4:
            specific_col()
        elif opt == 5:
            print("Thanks for being with us!!")
            break
        else:
            print("Invalid Input")


main_menu()


