#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    def add(num_list, max_num):
        carry = 0
        num_string = ""
        for i in range(-1, (-1 * max_num) - 1, -1):
            for num in num_list:
                if -1 * i <= len(num):
                    carry += int(num[i])
            num_string = str((carry % 10)) + num_string
            carry = carry // 10
        if carry > 0:
            num_string = str(carry) + num_string
        return (num_string)

    def sub(big_num, small_num):
        carry = 0
        result = ""
        for i in range(-1, (-1 * len(big_num)) - 1, -1):
            start = int(big_num[i]) + carry
            if len(small_num) == 0:
                end = 0
            if -1 * i <= len(small_num):
                end = int(small_num[i])
            else:
                end = 0
            if (start < end):
                result = str((10 + start) - end) + result
                carry = -1
            else:
                result = str(start - end) + result
                carry = 0
        return (result)

    def check_size(num):
        size = 0
        for i in range(-1, (-1 * len(num)) - 1, -1):
            a = (-1 * i) - 1
            size += (10**a * int(num[i]))
        return (size)
    pos_num = []
    neg_num = []
    if len(sys.argv) == 1:
        print("0")
    elif len(sys.argv) > 1:
        max_pos = 0
        max_neg = 0
        for i in sys.argv[1:]:
            if i[0] == "-":
                neg_num.append(i[1:])
                if len(i[1:]) >= max_neg:
                    max_neg = len(i[1:])
            else:
                pos_num.append(i)
                if len(i) >= max_pos:
                    max_pos = len(i)
        pos_string = add(pos_num, max_pos)
        neg_string = add(neg_num, max_neg)
        pos_size = check_size(pos_string)
        neg_size = check_size(neg_string)
        if pos_size >= neg_size:
            print("{}".format(sub(pos_string, neg_string)))
        else:
            print("-{}".format(sub(neg_string, pos_string)))