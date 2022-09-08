"""
SOURCE: https://leetcode.com/problems/excel-sheet-column-number/
Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

"""

def excel_col_to_number(s):
    result = 0
    char_values = [i for i in range(1, 27)]
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    char_map = dict(zip(letters, char_values))
    
    for char in s:
        result = result * 26 + char_map[char]
    return result

   
print(excel_col_to_number("A")) # => 1 
print(excel_col_to_number("B")) # => 2 
print(excel_col_to_number("AA")) # => 27 
print(excel_col_to_number("AB")) # => 28 
print(excel_col_to_number("ZY")) # => 701 
print(excel_col_to_number("FXSHRXW")) # => 2147483647
