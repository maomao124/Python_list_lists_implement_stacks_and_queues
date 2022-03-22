"""
 * Project name(项目名称)：Python_list列表实现栈和队列
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/22 
 * Time(创建时间)： 12:09
 * Version(版本): 1.0
 * Description(描述)： list实现队列
 """

if __name__ == '__main__':
    # 定义一个空列表，当做队列
    queue = []
    # 向列表中插入元素
    queue.insert(0, 1)
    queue.insert(0, 2)
    queue.insert(0, "hello")
    print(queue)
    print("取一个元素：", queue.pop())
    print("取一个元素：", queue.pop())
    print("取一个元素：", queue.pop())

    queue = []
    queue.insert(len(queue), 1)
    queue.insert(len(queue), 2)
    queue.insert(len(queue), 3)
    print(queue)
    print(queue.pop(0))
    print(queue)
    print(queue.pop(0))
    print(queue)
    print(queue.pop(0))

    input()

