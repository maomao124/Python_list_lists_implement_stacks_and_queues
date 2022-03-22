"""
 * Project name(项目名称)：Python_list列表实现栈和队列
 * Package(包名): 
 * File(文件名): test3
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/22 
 * Time(创建时间)： 12:15
 * Version(版本): 1.0
 * Description(描述)： collections模块实现栈和队列
 """

from collections import deque

if __name__ == '__main__':
    queueAndStack = deque()
    queueAndStack.append(1)
    queueAndStack.append(2)
    queueAndStack.append("hello")
    print(list(queueAndStack))
    # 实现队列功能，从队列中取一个元素，根据先进先出原则，这里应输出 1
    print(queueAndStack.popleft())
    # 实现栈功能，从栈里取一个元素，根据后进先出原则，这里应输出 hello
    print(queueAndStack.pop())
    # 再次打印列表
    print(list(queueAndStack))

    input()
