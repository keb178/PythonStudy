#2026年4月24日，我将我的旧的学习方式抛弃了，我想看看我能不能在5月1日之前把这本书学完
name="库尔班江"
print(name.title())#我不知道是什么原理，但是我还是敲出来并运行了
name="banana"
print(name.title())
name="apple"
print(name.upper())
name="CAU"
print(name.lower())


first_name='kuerbanjiang'
middle_name='·'
last_name='aireti'
full_name=f"{first_name} {middle_name} {last_name}"
print(full_name)


first_name='库尔班江'
middle_name='·'
last_name='艾热提'
full_name=f"{first_name} {middle_name} {last_name}"
print(full_name)


first_name='ada'
last_name="lovelace"
full_name=f"{first_name} {last_name}"
print(f"Hello,{full_name.title()}!")


first_name='ada'
last_name="lovelace"
full_name=f"{first_name} {last_name}"
print(f"Hello,{full_name.title()}！")
#message=f"Hello,{full_name.title}"出问题了！！！

message=f"Hello,{full_name.title()}!"#没写（），没写！，以后要注意
print(message)
print("\n")

#空白
print("python")
print("\tpython")
print("\n\n")#打印单独的\n确实可以起到换行的作用，我这里写了两个，换了两次行
print("Languages:\npython\nc\njavaScript")
print("\n\n")

#在编写时的空白行不影响最后编译后结果
#删除空白
favorite_language='python                           .'
print(favorite_language,"\n")
print(f"{favorite_language.upper().rstrip('.')}")#在括号里加上'.'就可以去掉我所打的句号
print()#我的猜测是这样子打印出来的是空白，又因为这行代码占了一行，所以就可以展现换行符\n的表现了
cleaned=favorite_language.rstrip('.')
print(repr(favorite_language))#repr可以显示空白是否去除
print()


favorite_language='C++ '
print(favorite_language)
favorite_language=favorite_language.rstrip()
print(favorite_language)
favorite_language
print()
#剔除字符串右边的空白


haowan="java        "
#haowan=haowan.restrip()出错了！！！是rstrip(),不是restrip()
haowa=haowan.rstrip()
print(haowa)
print(repr(haowa))



print()
print('\n\n\n')



#2026-4-27
message="One of python's strengths is its diverse community"
print(message)
#message='One of python's strengths is its diverse community'当我们的字符串中包括单引号或者说撇号时，我们要记得字符串外面一定要用双引号
#print(message)
print("\n\n\n")



print('练习2-3')
name="库尔班江·艾热提"
title="would you like to learn some python today"
print(f"Hello{name} ,{title}?")


print("\n\n\n")
print("练习2-4")
first_name='Ku er ban jiang'
middle_name='·'                       
last_name='Ai re ti'
full_name=f"{first_name} {middle_name} {last_name}"
#print("我的名字：",full_name)  三令五申说在字符串中加变量时要么用逗号','要么用'+'隔开！！！
#print("我的名字（大写版本）：" full_name.upper())
#print("我的名字(首字母大写版本):"full_name.title())
print("我的名字：",full_name)
print("我的名字(小写版本)：",full_name.lower())
print("我的名字（大写版本）：",full_name.upper())
print("我的名字（首字母大写版本）：",full_name.title())#还没完
print(f"我的名字{full_name}\t 我的名字（小写版本）:{full_name.lower()}\t 我的名字（大写版本）:{full_name.upper()}\t 我的名字（首字母大写版本）：{full_name.title()}")



print("\n\n\n")
print("练习2-5")
人名="玩机器machine"
玩机器的名言="'这真别玩了，我无语了，这真流脓了Device!'"
print(f"{人名.title()} said:{玩机器的名言}")
name="alber einstein"
中文翻译="爱因斯坦"
Famous_Quotes="Imagination is moreimportant than knowledge"
名人名言="想象力比知识更重要"
print(f"{name.title()}({中文翻译}) said: {Famous_Quotes.title()}!({名人名言})")



print("\n\n\n")
print("练习2-7")
name="\t\t\tkuerbanjiang\t\t\t"
print(repr(name))
print(repr(name.lstrip()))
print(repr(name.rstrip()))
print(repr(name.strip()))



print("\n\n\n")
print("2.4数")
print("整数")
name=2+3
print(name)
name=3-2
print(name)
name=2*3
print(name)
name=3/2
print(name)
name=3**2
print(name)
name=3**3
print(name)
name=10**6
print(name)
name=2+3*4
print(name)
name=(2+3)*4
print(name)



print("\n\n\n")
print("浮点数")
name=0.1+0.1
print(name)
name=0.2+0.2
print(name)
name=2*0.1
print(name)
name=2*0.2
print(name)
name=0.5*0.8
print(name)
name=0.1*0.2
print(name)
name=0.2+0.1
print(name)
name=3*0.1
print(name)



print("\n\n\n")
print("2.4整数和浮点数")
name=4/2
print(name)
name_1=1+2.0
name_2=1+2
#print(f"整数+浮点数：{name_1}\n 整数+整数：{name_2.lstrip()}")!!!是letrip(),不是letrip()
print(f"整数+浮点数：{name_1}\n整数+整数：{name_2}")



print("\n\n\n")
print("2.4.4数字中的下划线")
universe_age=14_000_000_000#univer_age豆包给我的翻译是宇宙年龄
print(universe_age)


print("\n\n\n")
print("2.4.5 同时给多个变量赋值")
x,y,z=0,0,0
print(x,y,z)
x,y,z=0.0,0.0,0.0000000000000
print(x,y,z)



print("\n\n\n")
print("2.4.6常量")
MAX_CONNECTTONS=5000#MAX_CONNECTTONS:最大连接数
print(MAX_CONNECTTONS)
MAX_CONNECTTONS=1
print(MAX_CONNECTTONS)#常量大写只是一个约定成俗的约定，其实他还是变量


#test
MAX_CONNECTIONS = 5000  # 约定为常量，不改它
print(MAX_CONNECTIONS)
# 如果需要测试其他值，定义一个新变量
current_test_value = 1
print(current_test_value)



print("\n\n\n")
print("练习2-8 ：数字8")
jiafa=3+5
jianfa=10-2
chengfa=4*2
chufa=16/2
print(jiafa)
print(jianfa)
print(chengfa)
print(chufa)#在涉及除法时，python就自动的进入带小数点的世界了



print("\n\n\n")
print("练习2-9：最喜欢的数")
#love_numver,talk,=21,我最喜欢的数字!!!是lover_number不是love_numver;而且talk后面不要带逗号
love_number,talk=21,"我最喜欢的数字是："
print(f"{talk}{love_number}")



print("\n\n\n")
print("2.5 注释")
print("2.5.1 如何编写注释")
#向大家问好
print("Hello python people")
#在python中我们可以使用#键将#键后面一行的内容都注释掉，或者说会被python解释器忽略掉
#当然我们想忽略掉更多行时，我们可以使用''''''和"""""""来注释掉，在开头放上三个，在最后放上三个


print('\n\n\n')
print('2.5.2该编写什么样的注释')
#编写注释的主要目的是阐述代码要做什么，以及是如何做的。在开发项目期间，你对各个部分如何协同工作了如指掌，但过段时间后，有些细节你可能不记得了。当然，你总是可以通过研究代码来确定各个部分的工作原理，但通过编写注释以清晰的自然语言对解决方案进行概述，可节省很多时间。
# 要成为专业程序员或与其他程序员合作，就必须编写有意义的注释。当前，大多数软件是合作编写的，编写者可能是同一家公司的多名员工，也可能是众多致力于同一个开源项目的人员。训练有素的程序员都希望代码中包含注释，因此你最好从现在开始就在程序中添加描述性注释。作为新手，最值得养成的习惯之一就是在代码中编写清晰、简洁的注释。
# 如果不确定是否要编写注释，就问问自己：在找到合理的解决方案之前，考虑了多个解决方案吗？如果答案是肯定的，就编写注释对你的解决方案进行说明吧。相比回过头去再添加注释，删除多余的注释要容易得多。从现在开始，本书的示例都将使用注释来阐述代码的工作原理。



print('\n\n\n')
print('练习2-10：添加注释')
print("第一个程序：")
MAX_FILE_SIZE_MB=500
name_A="喜羊羊"
name_B="灰太狼"
File_size_A=200.0#是这里的小坑吗？
#不是这里的坑
File_size_B=750
status_1="Enabled Status"#status:状态,Enabled Status;允许状态
status_2="Disabled Status"#Disabled Status:禁用状态
#！！！是让我做一个可以自动判断状态的程序，而不是像现在一样手动定义状态！！！
'''
print(f"{name_A}的文件大小是：{File_size_A}\nUpload Status:{status_1}")#Upload Status:上传状态
#print(f"{name_B}的文件大小是：{File_size_A}\nUpload Status:{status_2}")！！！name_B的文件大小是File_size_B,粗心了！！！
print(f"{name_B}的文件大小是：{File_size_B}\nUpload Status:{status_2}")
'''
print(f"{name_A}的文件大小是：{File_size_A}MB\nUpload Status:{status_1 if File_size_A<=MAX_FILE_SIZE_MB else status_2}")
#当然我们也可以做到真正的自动化，就像下面的：
print(f"{name_A}的文件大小是：{File_size_A}MB\n上传状态：{'允许' if File_size_A <=MAX_FILE_SIZE_MB else '拒绝'}")
print("\n")
print(f"{name_B}的文件大小是：{File_size_B}MB\nUpload Status:{status_1 if File_size_B<=MAX_FILE_SIZE_MB else status_2}")
#or
print(f"{name_B}的文件大小是：{File_size_B}MB\n上传状态：{'允许' if File_size_B <=MAX_FILE_SIZE_MB else '拒绝'}")


print("第二个程序")
raw_name="\t\n Zhang san  \n\t"
print(raw_name)
stripped_name.