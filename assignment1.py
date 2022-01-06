# Assignment. 
# In groups that are already in place please do the following assignments. 
# Create a function based programme in python that 
# ####calculates a final mark for a student.
#  Where a student is supposed to have 3 sets of tests.
#  Test 1 and Test 2 and coursework.
#  Only the best two  of the three are considered . 
# The average of the best two is calculated  and divided by 2. 

# Then the percentage of the average derived  is calculated and multiplied by 40. 
# The final test  result is out of 60 and  goes through the same process  of average calculation as the tests and is later added to the test results to come up with the final mark .
#  Write the name of the student and the  best two marks of a student on a text file, plus  the final test mark and the total mark. 
# For a user  to be able to access this information they should first input student  their details.  
# The system should also be able to write  on the excel too. This assignment is due Friday 31st December 2021.


def final_mark(test_1, test_2, course_work):
    # set contrucotur - set only data tye that is not ordered
    nums = set([test_1, test_2, course_work])
    smallest = min(nums) # not max (trollface :P)
    nums.remove(smallest)
    print("the two largest numbers are", ' and '.join(map(str, nums)))

    # access the two values 
    mark1 = list(nums)[0]
    mark2 = list(nums)[1]

    print(mark1)
    print(mark2)

    # get average 
    avg = (mark1 + mark2) / 2.0
    print(avg)





final_mark(70,80,60)
