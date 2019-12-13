import pandas as pd
import calendar

# Read the user selection of newspaper
data = pd.read_csv('user.csv')
df = pd.DataFrame(data)
ls = df.iloc[0]

# Read pre-defined prices of newspapers
expenses = pd.read_csv('expenses.csv')
ex = pd.DataFrame(expenses)


# Calender function for counting the number of days of a 7 days of a week of a particular month and year
def calender(y, m):
    cal = calendar.Calendar()
    l1 = []

    for week in cal.monthdays2calendar(y, m):
        for d in week:
            if d[0] != 0:
                l1.append(d[1])
    count_list = [l1.count(0), l1.count(1), l1.count(2), l1.count(3), l1.count(4), l1.count(5), l1.count(6)]
    return count_list


# To calculate total expenses of a  user for the newspaper/newspapers selected
def expenses(ls, b):
    sum_list = []
    for i in range(5):
        if ls[i] == 1:
            temp = ex.iloc[i]
            for i in range(7):
                sum_list.append(temp[i] * b[i])
    expense = sum(sum_list)
    return expense


b = calender(2019, 12)
total_expense = expenses(ls, b)
print(total_expense)
