def sort_colors(colors):
    red = 0
    white = 0
    blue = len(colors) -1

    for _ in range(len(colors)):
        if colors[white] == 0:
            colors[white], colors[red] = colors[red], colors[white]
            red += 1
            white += 1
        
        elif colors[white] == 1:
            white += 1
        
        else:
            colors[white], colors[blue] = colors[blue], colors[white]
            blue -= 1
    
    return colors


# TEST CASES

print(sort_colors(colors=[2, 2, 1, 1, 0])) # => [0, 1, 1, 2, 2]

print(sort_colors(colors=[2, 2, 0, 1, 2, 2, 0, 2])) # => [0, 0, 1, 2, 2, 2, 2, 2]

print(sort_colors(colors=[0, 0, 1, 0, 1, 1, 1, 2, 1, 2])) # => [0, 0, 0, 1, 1, 1, 1, 1, 2, 2]