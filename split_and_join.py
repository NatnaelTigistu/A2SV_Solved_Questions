def split_and_join(line):
    words = line.split()
    result = ""
    for word in words:
        result += (word + "-")
    return result[:-1:1]
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)