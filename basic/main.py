classdata={'20222789':'马智臻'}
a=True
choice=0
while a:
    a=input("输入0退出 任意键继续\n")
    choice=input("输入1查询学号，2写入，3查询姓名\n")
    if choice=='1':
        name=input("请输入姓名\n")
        print([k for k,v in classdata.items() if v==name])
    if choice=='2':
        name=input("请输入姓名\n")
        num=input("请输入学号\n")     
        classdata[num]=name
        print("成功写入\n")
    if choice=='3':
        num=input("请输入学号\n")
        print(classdata.get(num))
    else:
        continue

    