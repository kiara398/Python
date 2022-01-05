
#! Assignment to handle test results.

import heapq
import xlsxwriter

def test():
    name = input("Please input your name: ")
    print("This is the MUK Test Portal follow the prompts below to assess your tests.")

    test1 = int(input("Input your Test 1 Results: "))
    test2 = int(input("Input your Test 2 Results: "))
    coursework = int(input("Input your Coursework Results: "))
    exam = int(input("Input your Final Exam results: "))
    results = [test1, test2, coursework]
    print(results)

    #? Getting the largest 2 values
    highest_marks = heapq.nlargest(2, results)
    print("Highest Mark: ",highest_marks)

    #? Getting the average of the two values
    average = sum(highest_marks)/len(highest_marks)
    print("Average: ",average)

    #? Getting percentage of average out of 40
    percentage = average/100*40

    #? Getting the percentage of the final exam
    final = exam/100*60

    #? Getting the final courseunit results
    course_unit = percentage + final
    print("CourseWrok: ",course_unit)

    print(name,",Thank you for using the portal. Have a Happy New Year.")

    #? Writing the results in a txt file
    with open('test.txt', 'a') as f:
        f.writelines(name)
        f.write('\n')
        f.writelines("This is a list of the highest marks in the three tests:")
        f.write(str(highest_marks))
        f.write('\n')
        f.writelines("This is the final course unit result:")
        f.writelines(str(course_unit))
        f.write('\n')
        f.write("================================================================")
        f.write('\n')
        f.close()

    #? Writing to Excel File
    workbook = xlsxwriter.Workbook('test.xlsx')
    worksheet = workbook.add_worksheet()

    row = 0
    col = 0

    #* Writing to worksheet
    for i in range(1):
        worksheet.write(row, col, name)
        worksheet.write(row, col+1, str(highest_marks))
        worksheet.write(row, col+2, str(course_unit))
        row += 1
    workbook.close()

test()