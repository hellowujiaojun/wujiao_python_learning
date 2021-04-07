def main():

    '''

    '''
    # 创立一个空表
    list_null = []

    # 创立一个纯数字表
    list_num = [1,7,6,4,2]

    # 创立一个纯字符串表
    list_str = ['wujiao','jachin','laowang']

    # 创立一个混合表
    list_com = ["wujiao",123,3.14]

    # 测试insert功能
    list_com.insert(2,"jachin")
    print(list_com)

    # 测试append功能
    list_com.append(1996)
    print(list_com)

    # 测试extend功能
    list_com.extend(list_str)
    print(list_com)

    # 测试pop功能
    print(list_com.pop())

    # 测试sort功能
    list_num.reverse()
    print(list_num)
    list_copy = list_com.copy()
    list_com.pop()
    print(list_copy)


if __name__ == "__main__":
    main()
