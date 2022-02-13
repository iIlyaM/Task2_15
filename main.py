from file import *


def shift(lst, steps):
    changed_lst = lst.copy()
    if steps < 0:
        steps = abs(steps)
        for i in range(len(changed_lst)):
            for j in range(steps):
                changed_lst[i].append(changed_lst[i].pop(0))
    else:
        for i in range(len(changed_lst)):
            for j in range(steps):
                changed_lst[i].insert(0, changed_lst[i].pop())
    return changed_lst


def read_answer(string: str):
    if string == 'y' or string == 'Y':
        return False
    elif string == 'n' or string == 'N':
        return True


def start_program():
    filename = input("Enter name of file: ")
    nums = read_file(filename)
    shifted_nums = shift(nums[0:-1], nums[-1][0])
    output_filename = input("Choose file for output: ")
    write_file(output_filename, shifted_nums)
    print("Terminate the program?\n Print y - yes or n - no")


def main():
    flag = True
    while flag:
        start_program()
        flag = read_answer(input())


if __name__ == '__main__':
    main()
