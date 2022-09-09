"""
SOURCE: https://leetcode.com/problems/excel-sheet-column-title/
"""

def excel_num_to_col(columnNumber):
    result = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = columnNumber * 1

    while num:
        num -= 1
        result = alphabet[num % 26] + result
        num //= 26
    return result

print(excel_num_to_col(1)) # => "A"
print(excel_num_to_col(2)) # => "B"
print(excel_num_to_col(28)) # => "AB"
print(excel_num_to_col(701)) # => "ZY"
print(excel_num_to_col(2147483647)) # => "FXSHRXW"
