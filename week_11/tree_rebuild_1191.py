def find_root():
    global roots_consumed
    root = pre_order[roots_consumed]
    roots_consumed += 1
    return in_order.find(root)


def post_order(i, j):
    root_index = find_root()

    if root_index > i:
        post_order(i, root_index-1)
    if root_index < j:
        post_order(root_index+1, j)

    print(in_order[root_index], end='')


def tree_rebuild():
    global pre_order, in_order, roots_consumed
    while True:
        try:
            pre_order, in_order = input().split()
        except:
            break

        roots_consumed = 0
        post_order(0, len(pre_order)-1)
        print()


if __name__ == '__main__':
    tree_rebuild()
