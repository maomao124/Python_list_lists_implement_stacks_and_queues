"""
 * Project name(项目名称)：Python_list列表实现栈和队列
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/22 
 * Time(创建时间)： 12:14
 * Version(版本): 1.0
 * Description(描述)： Python list实现栈
 """

if __name__ == '__main__':
    # 定义一个空 list 当做栈
    stack = []
    stack.append(1)
    stack.append(2)
    stack.append("hello")
    print(stack)
    print("取一个元素：", stack.pop())
    print("取一个元素：", stack.pop())
    print("取一个元素：", stack.pop())

    input()
