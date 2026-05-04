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
print("练习2-1：最喜欢的数")
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
print(repr(raw_name))
stripped_name=raw_name.strip()
print(repr(stripped_name))
left_name=raw_name.lstrip()
print(repr(left_name))
right_name=raw_name.rstrip()
print(repr(right_name))



print("\n\n\n")
print(".26 python之禅")
print("import this")
print("Beautiful is better than ugly\n优美胜于丑陋")
print("Explice is better than complex\n明了胜于晦涩")
print("Simple is  better than complex\n简单胜于复杂")
print("complex is better than complicated\n复杂胜于繁杂")
print("Flat is better than nested\n扁平胜于嵌套")
print("Sparse os better than dense\n稀疏胜于密集")
print("Readability counts\n可读性至关重要")
print("Special caases aren't special enough to break the rule\n特例不足以违背规则")
print("Although practicality beats purity\n尽管实用性优先于纯粹")
print("Errors should never pass silently\n错误绝不悄然放过")
print("Unless explictly silence\n除非刻意静默处理")
print("In the face of ambiguity,refuse the temptation to guess\n面对歧义，切忌主观臆断")
print("There should be one --and preferable only one--obvious way to do it\n做事应有且最好只有一种显而易见的方式")
print("Although that way may not be obvious at first unless you're Dutch\n尽管这种方式起初未必显而易见，除非你是荷兰人")
print("Now is better than never\n行动胜于拖延")
print("Although never is often better than right now\n但草率行事不如永不行动")
print("If the implementation is hard to explain,it's a bad idea\n难以解释的实现，绝非好思路")
print("If the implementation is easy to explain,it may be a good idea\n易于阐释的实现，或许是好设计")
print("Namespaces are one honking great idea --let's do more of those\n命名空间简直绝妙，多多益善")
print("练习2-11 Python之禅")



print("\n\n\n")
print("第三章 列表简介")
print("3.1 列表是什么")
bicycles=['terk','cannondale','redline','specialized']
print(bicycles)



print("\n\n\n")
print("3.1.1访问列表元素")
bicycles=['trek','cannondale','rediline','specialized','hello']
print(bicycles[0])
print(bicycles[-5])#当然也可以反向索引
#print(bicycles[5])！！！列表的索引是从0开始的，这个超范围了！！！
print(bicycles[4])


print("\n\n\n")
print('下面这段代码可以帮助我理解python会使用最后一次赋值的那个列表')
cau=['理学院','工学院','食品学院','国际学院','资环学院','植保学院']
print("第一次复制后：",cau)
cau=['理学院','工学院','食品学院','国际学院','资环学院','植保学院','动物医学院','动物保护学院']
print("第二次赋值后：",cau)
print(cau[3])


bicycles=['trek','cannondale','redline','specialzed']
print(bicycles[0].title())
#print(bicycles[4])!!!这里就很好的解释了python是从最后一次赋值的那个列表开始赋值的


print("\n\n\n")
print("3.1.2 索引从0开始而不是从1开始")
bicycles=['trek','cannondale','redline','speciallized']
print(bicycles[1])
#print(biclcles[3])!!!!是bicycles不是biclcles!!!!
bicycles=['trek','cannondate','redline','speecialized']
print(bicycles[-1])



print("\n\n\n")
print("3.13 使用列表中的各个值")
bucycles=['trek','cannnondale','redine','specialized']
message=f"my first bicycle was a {bicycles[0].title()}."
print(message)



print("\n\n\n")
print("练习3-1 姓名")
names=['库尔班江','艾热提','古力先木','美迪娜']
Address=['myself','My father','My mother','My yonger sister']#Address:社交称呼
message="的名字是："
print(f"{Address[0]}{message}{names[0]},\n{Address[1]}{message}{names[1]},\n{Address[2]}{message}{names[2]},\n{Address[3]}{message}{names[3]}")




print("\n\n\n")
print('or')
names=['库尔班江','艾热提','古力先木','美迪娜']
ps=['艾尼','阿不力孜']
Address=['my','My father','My mother','My yonger sister']
message=['name is:','full name']
sentence_1=f"{Address[0]} {message[0]} {names[0]},my {message[1]} is {names[1]}"
sentence_2=f"{Address[1]} {message[0]} {names[1]},his {message[1]} is {ps[1]}"
sentence_3=f"{Address[2]} {message[0]} {names[2]},her {message[1]} is {ps[1]}"
sentence_4=f"{Address[3]} {message[0]} {names[3]},her {message[1]} is {names[1]}"
#print(sentence_1+'\n',sentence_2+'\n',sentence_3+'\n',sentence_4)！！！这样写前面会有空格，不是很好看
print(f"{sentence_1}\n{sentence_2}\n{sentence_3}\n{sentence_4}")



print("\n\n\n")
print("练习3-2:问候语")
message_1="开心一点！"
message_2="下班没"
message_3="吃饭没"
message_4="你是最棒的！！！"
ps=['艾尼','阿不力孜','我想对我/他/她说：']
sentence_5=f"{sentence_1},{ps[2]} {message_1}"
sentence_6=f"{sentence_2},{ps[2]} {message_2}"
sentence_7=f"{sentence_3},{ps[2]} {message_3}"
sentence_8=f"{sentence_4},{ps[2]} {message_4}"
print(f"{sentence_5}\n{sentence_6}\n{sentence_7}\n{sentence_8}")



print("\n\n\n")
print("练习3-3：自己的列表")
Main_mode_of_commuting=['汽车','摩托车','小电驴','地铁','公交车']
Favorite_brand=['奔驰','杜卡迪','雅迪','15号线','10路车']
message=['我最喜欢的','品牌','线路']
'''
sentence_1=f"{message[0],Main_mode_of_commuting[0],message[1]:,Favorute_branf[0]}"
sentence_2=f"{message[0],Main_mode_of_commuting[1],message[1]:,Favorute_branf[1]}"
sentence_3=f"{message[0],Main_mode_of_commuting[2],message[1]:,Favorute_branf[2]}"
sentence_4=f"{message[0],Main_mode_of_commuting[3],message[1]:,Favorute_branf[3]}"
sentence_5=f"{message[0],Main_mode_of_commuting[4],message[1]:,Favorute_branf[4]}"
print(f"{sentence_1}\n{sentence_2}\n{sentence_3}\n{sentence_4}\n{sentence_5}\n")
1.是Favorite_brand,不是Favorute_branf  
2.冒号，逗号，空格作为普通字符放在花括号外面，花括号里面只放入变量！！！
'''
#sentence_1=f"{message[0]},{Main_mode_of_commuting[0]},{message[1]}:,{Favorute_branf[0]}"
#又他妈的犯了：是Favorite_brand!!!
sentence_1=f"{message[0]}{Main_mode_of_commuting[0]}{message[1]}:{Favorite_brand[0]}"
sentence_2=f"{message[0]}{Main_mode_of_commuting[1]}{message[1]}:{Favorite_brand[1]}"
sentence_3=f"{message[0]}{Main_mode_of_commuting[2]}{message[1]}:{Favorite_brand[2]}"
sentence_4=f"{message[0]}{Main_mode_of_commuting[3]}{message[2]}:{Favorite_brand[3]}"
sentence_5=f"{message[0]}{Main_mode_of_commuting[4]}{message[2]}:{Favorite_brand[4]}"
print(f"{sentence_1}\n{sentence_2}\n{sentence_3}\n{sentence_4}\n{sentence_5}")



print("\n\n\n")
print("3.2 修改，添加和删除元素")
print("3.2.1 修改列表元素")
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0]='ducati'
print(motorcycles)



print("\n\n\n")
print("3.2.2 在列表中添加元素")
print("01 在列表末尾添加元素")
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)


motorcycles=[]
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)



print('\n\n\n')
print("02 在列表中插入元素")
motorcycles=['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)



print("\n\n\n")
print("3.2.3 从列表中删除元素")
print("01 使用del语句删除元素")
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)



print('\n\n\n')
print("02.使用pop()删除元素")
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
#popped_motorcycles=motorcycles.pop!!!!不加括号的话python以为我们在这个变量里存的是pop这个方法而不是执行pop()这个方法后的结果
popped_motorcycles=motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)


motorcycles=['honda','yamaha','suzuki']
last_owned=motorcycles.pop()
print(f"The last motorcycles I owend was a{last_name}.")



print("\n\n\n")
print("03.弹出列表中任何位置处的元素")
motorcycles=['honda','yamaha','suzuki']
first_owned=motorcycles.pop(0)
print(f"The first motorcycles I owend was a {first_owned.title()}.")



print('\n\n\n')
print("04.根据值删除元素")
motorcycles=['honda','yamaha','suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

motorcycles=['honda','yamaha','suzuki','ducati']
print(motorcycles)
too_expensive='ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")



print('\n\n\n')
print("练习3-4：嘉宾名单")
name=['熊大','熊二','光头强','翠花','蹦蹦','吉吉国王','毛毛']
message=['你好','我想邀请你来参加我的晚宴','这个是我所邀请的人员名单']



print("\n\n\n")
print("2026年5月3日23：17，今天请假一天，不想学")
print("等会打完csgo写")