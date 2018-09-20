unsorted_list = ['a', 'b', 'c', 'd', 'e', 0, 1, 0, 0, 'f', 'g', 'h', False, False,'i', 'j']
zero_list = []


def sorter(unsorted_list):
    for item in unsorted_list:
        if isinstance(item, int):
            if 0 in unsorted_list:
                unsorted_list.remove(0)
                zero_list.append(0)

    new_list = unsorted_list + zero_list
    print(new_list)


if __name__ == "__main__":
    sorter(unsorted_list)
