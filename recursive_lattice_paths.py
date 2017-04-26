cache = {}


def crawl(x, y, max_x, max_y, number_paths=0):
    if (x,y) in cache:
        return number_paths + cache[(x,y)]
    if x == max_x and y == max_y:
        return number_paths + 1

    number_this_branch = 0
    if x < max_x:
        number_this_branch += crawl(x+1, y, max_x, max_y, number_paths)
    if y < max_y:
        number_this_branch += crawl(x, y+1, max_x, max_y, number_paths)
    cache[(x,y)] = number_this_branch
    return number_paths + number_this_branch

print(crawl(0,0,20,20))