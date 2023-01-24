from typing import List


def generate(numRows: int) -> List[List[int]]:

    res = [[1]]

    numRowsToCreate = numRows-1

    for i in range(numRowsToCreate):

        temp = [0] + res[-1] + [0]  # the trick

        row = []

        numValuesToCreate = len(res[-1])+1

        for j in range(numValuesToCreate):

            row.append(temp[j]+temp[j+1])

        res.append(row)

    return res


"""
Initialize the res list with the first value appended. It will be the same in every case.
Iterate through the numRows - 1, minus 1 because want the remaining rows.
The trick is to append 0 at each end of the new row.
After that iterate over new row length, where length of last row +1
Append current value + the next value, hnce temp[j] + temp[j+1] or 0+1 so on and so forth
Append to new row.
Append to result list 
"""

print(generate(5))
