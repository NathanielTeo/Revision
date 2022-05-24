import statistics

def main():
    display_main_menu()
    numlist=get_user_input()
    avg=calc_average(numlist)
    print(avg)
    minmax=find_min_max(numlist)
    print(minmax)
    sort=sort_temperature(numlist)
    print(sort)
    median=calc_median_temperature(numlist)
    print(median)


def display_main_menu():
    print("display_main_menu")


def get_user_input():
    print("get_user_input")
    x = input("Enter Numbers with a ',' in between the numbers : ")
    temps=x.split(',')
    temps2=[]
    for y in range(len(temps)):
        floatnum=float(temps[y])
        temps2.append(floatnum)

    return temps2

    
def calc_average(x):
    print("calculate average")
    total=0
    for y in range(len(x)):
        total=total+x[y]
    answer=total/len(x)
    return answer


def find_min_max(x):
    print("find min max")
    minmax=[]
    minimum=x[0]
    maximum=x[0]
    for y in range(len(x)):
        if x[y]<minimum:
            minimum=x[y]
    minmax.append(minimum)

    for y in range(len(x)):
        if x[y]>maximum:
            maximum=x[y]
    minmax.append(maximum)
    return minmax


def sort_temperature(x):
    print("sort temperature")
    x.sort()
    return x

def calc_median_temperature(x):
    print("Calculate Median Temperature")
    median=statistics.median(x)
    return median

if __name__ == '__main__':
    main()
