def opt():
    return " 1- Count Digits \n 2- Find Max \n 3- Count Tags \n 4- Count Normalized Columns \n 5- Recursive Binary Search \n 6- Recursive Binary Search on 2d Matrix \n 7- Exit \n"
#1
def countDigits(cDigits):
    return(len(cDigits))
#2
def findMax(lstUser):
    if (len(lstUser) == 0):
        return None
    temp = lstUser.pop()
    userMax = findMax(lstUser)
    if(userMax is not None and userMax > temp):
        return userMax
    else:
        return temp
#3
def countTags(html, tag):
    count = 0
    open_tag = "<" + tag + ">"
    close_tag = "</" + tag + ">"
    start_index = 0
    while True:
        open_index = html.find(open_tag, start_index)
        if open_index == -1:
            break
        close_index = html.find(close_tag, open_index)
        if close_index == -1:
            break
        count += 1
        start_index = close_index + len(close_tag)
    return count
#4
def calculateMean(column):
        total = sum(column)
        return total / len(column)
def calculateStdDev(column, mean):
        sqDiff = sum((x - mean) ** 2 for x in column)
        variance = sqDiff / len(column)
        return variance ** 0.5
def countNormalizedColumns(matrix, col, count):
    if col == len(matrix[0]):
        return count
    column = [row[col] for row in matrix]

    mean = calculateMean(column)
    stdDev = calculateStdDev(column, mean)

    if abs(mean) < 1e-9 and abs(stdDev - 1) < 1e-9:
        count += 1

    return countNormalizedColumns(matrix, col + 1, count)

#5
def binarySearch(lst, item, low, high):
    if low > high:
        return -1
    #akhadna nos list w amelnela assign lal mid
    mid = (low + high) // 2
    print("the middle is at position", mid, "its value is", lst[mid])
    
    if lst[mid] == item:
        return mid
    elif lst[mid] > item:
        print("now", mid, "is the new high, it has the value", lst[mid])
        return binarySearch(lst, item, low, mid - 1)
    else:
        print("now", mid, "is the new low, it has the value", lst[mid])
        return binarySearch(lst, item, mid + 1, high)
#6
def search2dRecursive(matrix, item, row, col):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return -1
    
    if matrix[row][col] == item:
        return (row, col)
    elif matrix[row][col] < item:
        # Search right
        return search2dRecursive(matrix, item, row, col + 1)
    else:
        # Search up
        return search2dRecursive(matrix, item, row - 1, col)

def main():
    
    print(opt())
    choice = int(input("choose what option do U want: "))

    while (choice != 7):
        ############## choice 1 ########################
        if(choice == 1):
            #count digits
            cDigits = str(input("Enter the number you want to count: "))
            print(countDigits(cDigits),"\n")
        ############## choice 2 ########################
        elif (choice == 2):
            lst = []
            while True:
                userIn = int(input("Enter your numbers and when you done enter (-1): "))
                if(userIn >= 0):
                    lst.append(userIn)
                else:
                    break

            result = findMax(lst)
            if (result is not None):
                print("The max is: ",result)
            else:
                print("empty list")
        ############## choice 3 ########################
        elif (choice == 3):
            html = """
            <html>
            <head>
            <title>My Website</title>
            </head>
            <body>
            <h1>Welcome to my website!</h1>
            <p>Here you'll find information about me and my hobbies.</p>
            <h2>Hobbies</h2>
            <ul>
            <li>Playing guitar</li>
            <li>Reading books</li>
            <li>Traveling</li>
            <li>Writing cool h1 tags</li>
            </ul>
            </body>
            </html>
            """

            tag = input("Enter the tag you want to count: ")
            resultTag=  countTags(html, tag)
            print(f"The number of '{tag}' tags is:", resultTag)

        ############## choice 4 ########################
        elif (choice == 4):
            #count Normalized columns
            matrix = [
                [-1.2649110640673518, 5.123451, 43],
                [-0.6324555320336759, 5.13123123, 4334],
                [0.0, 6.1543453, 125879],
                [0.6324555320336759, 0.1231235709, 123544],
                [1.2649110640673518, 9.1543524234, 55676]
                ]
            resultMatrix = countNormalizedColumns(matrix, 0, 0)
            print("The count Normalized columns:", resultMatrix)
        ############## choice 5 ########################
        elif (choice == 5):
            #recursive binary search
            lstUser2 = []
            while True:
                userIn = int(input("Enter your numbers and when you done enter (-1): "))
                if(userIn > 0):
                    lstUser2.append(userIn)
                else:
                    break
            rbs = int(input("Enter the index you want to find : "))
            result = binarySearch(lstUser2, rbs, 0, len(lstUser2) - 1)
            if result != -1:
                print("Item found at index:", result)
            else:
                print("Item not found")
        ############## choice 6 ########################
        elif (choice == 6):
            #Recursive binary search on 2d matrix
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))

            matrix = []
            print("Enter the elements of the matrix:")
            for i in range(rows):
                row = list(map(int, input().split()))
                matrix.append(row)
    
            rbs = int(input("Enter the value you want to find: "))
            result = search2dRecursive(matrix, rbs, rows - 1, 0)
    
            if result != -1:
                print("Item found at position:", result)
            else:
                print("Item not found")
        ############## choice 7 ########################
        else:
            print("Wrong choice please choose option between 1 -> 7")

        print(opt())
        choice = int(input("choose what option do U want: "))
    quit()

main()


