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



print('\n\n\n')
print("2026年5月6日请个假，实在不想学东西了")


'''
print("\n\n\n")
#import os
#os.system('cls')!!!这两行代码能够把控制台的历史记录清理干净
print("练习3—4：嘉宾名单")
name=['熊大','熊二','光头强','翠花','蹦蹦','吉吉国王','毛毛']
message="你好，我想邀请你来参加我的晚宴，这个是我所邀请的人员名单："
#print(f"{name[0]} {message[0]},{message[1]},{message[2]}:{name}")!!!这行代码是对的但就是有点不好看，所以我们要用到下面的方法.join来解决他
beautiful_name_list='，'.join(name)
print(f"{name[0]:6} {message}{beautiful_name_list}")#{name[0]:5}这个:5是在固定名字的宽度为5 
#print(f"{naem[1]} {message}{beautiful_name_list}")!!!是name不是naem!!!
print(f"{name[1]:6} {message}{beautiful_name_list}")
print(f"{name[2]:6} {message}{beautiful_name_list}")
print(f"{name[3]:6} {message}{beautiful_name_list}")
print(f"{name[4]:6} {message}{beautiful_name_list}")
print(f'{name[5]:6} {message}{beautiful_name_list}')
#print(f"{name[6]} {message}{beautiful_naem_list}")!!！这里也是，是name不是naem!!!
print(f"{name[6]:6} {message}{beautiful_name_list}")



print('\n\n\n')
print("练习3-5：修改嘉宾名单：")
'''
name_linshi="李老板"
name=['熊大','熊二','光头强','翠花','蹦蹦','吉吉国王','毛毛']
print(f"{name[0]:6} 你好，很抱歉{name[3]}无法到来了，所以我们临时邀请了{name_linshi}")
print("邀请人员名单")
'''
name=['熊大','熊二','光头强','翠花','蹦蹦','吉吉国王','毛毛']
regrets=name.pop(3)
new_name='李老板'
name.insert(3,new_name)
beautiful_name_list=','.join(name)
print(f"你好{name[0]},在刚刚的邀请人员中{regrets}无法来到晚宴，不过{name[3]}说可以来,\n所以最新的名单为{beautiful_name_list}")



print("\n\n\n")
print("练习3-6：添加嘉宾")
print("大家好我刚找到了一个更大的餐桌，可以容纳更多的嘉宾，所以我又邀请了：")
name.insert(0,'niko')
name.insert(3,'jee')
name.append('devise')
print(name)



print('\n\n\n')
print("练习3-7：缩减名单")
name=['熊大','熊二','光头强','翠花','蹦蹦','吉吉国王','毛毛']
'''


print('\n\n\n')
print('回来了，重新把事情搞完')
print('练习3-4：嘉宾名单')
#这几个练习我看能不能将他们穿起来
name=['熊大','熊二','光头强','翠花','蹦蹦','吉吉国王','毛毛']
message='你好，我想邀请你参加晚宴'
print(f"{name[0]},{message}")
print(f"{name[1]},{message}")
print(f"{name[2]},{message}")
print(f"{name[3]},{message}")
print(f"{name[4]},{message}")
print(f"{name[5]},{message}")
print(f"{name[6]},{message}")



print('\n\n\n')
print('练习3-5：修改嘉宾名单')
name_1=['涂涂','萝卜头']
message_1=f'很抱歉{name[0]}和{name[1]}来不了了，不过{name_1[0]}和{name_1[1]}愿意来，所以晚宴名单更新为：'
name[0]=name_1[0]
name[1]=name_1[1]
print(f'{name[0]},{message}')
print(f'{name[1]},{message}')
print(f'{name[2]},{message_1}{name}')
print(f'{name[3]},{message_1}{name}')
print(f'{name[4]},{message_1}{name}')
print(f'{name[5]},{message_1}{name}')
print(f'{name[6]},{message_1}{name}')



print('\n\n\n')
print('练习3-6：添加嘉宾')
name.append('肥波')
name.insert(0,'老鳄')
name.insert(4,'拖拖')
name.insert(5,'铁掌大师')
print(f'大家好我找到了更大的桌子，所以我又邀请了三个人,它们分别是:{name[0]},{name[4]},{name[5]},{name[10]}')
print(f"大家好，最新的晚宴名单为：{name}")

print(len(name))#列表长度

print('\n\n\n')
print('练习3-7：缩减名单')
print(name)
print('抱歉各位因为新购买的桌子无法及时送达，因此只能邀请两名嘉宾')
name.insert(0,'很抱歉我无法邀请你参加晚宴了')
name_2=name.pop()
print(f'{name_2},{name[0]}')
name_2=name.pop()
print(f'{name_2},{name[0]}')
name_2=name.pop()
print(f'{name_2},{name[0]}')
name_2=name.pop()
print(f"{name_2},{name[0]}")
name_2=name.pop()
print(f'{name_2},{name[0]}')
name_2=name.pop()
print(f'{name_2},{name[0]}')
name_2=name.pop()
print(f"{name_2},{name[0]}")
name_2=name.pop()
print(f'{name_2},{name[0]}')
name_2=name.pop()
print(f"{name_2},{name[0]}")
print(f"{name[1]},你好，你仍然在邀请名单里")
print(f"{name[2]},你好，你仍然在邀请名单里")
print(name)
del name[0]
del name[0]
del name[0]
print(name)


'''
print('\n\n\n')
print('3.3组织列表')
print('3.3.1使用方法sort()对列表永久排序')
cars=['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)



print('\n\n\n')
print('3.3.2 使用函数sorted()对列表临时排序')
cars=['bmw','audi','toyota','subaru']
print('Here is the original list:')
print(cars)
print('\nHere is the sorted list:')
print(sorted(cars))
print('\nHere is the original list again:')
print(cars)



print('\n\n\n')
print('3.3.3 倒着打印列表')
cars=['bmw','audi','toyota','subaru']
print(cars)
cars.reverse()
print(cars)



print('\n\n\n')
print('3.3.4 确定列表长度')
car=['bmw','audi','toyota','subaru']
len(cars)
print(len(cars))



print('\n\n\n')
print('练习3-8：放眼世界')
didian=['beijin','hami','xingxilan','beiji','nanji','yingdunixiya','aodaliya']
print(didian)
#sorted(didian)!!!!sorted()是一个有返回值的函数,我们不能光调用不去接这个返回值
#print(didian)
print(sorted(didian))
#sorted(reverse=True.didain) ！！！reverse=True是sorted函数的一个参数，必须放在括号里用逗号隔开 ❌ 拼写也错了，是 didian
# print(didian)
sorted(didian,reverse=True)
print(didian)
#didian.reverse=True!!!!reverse() 是一个方法。它直接对原列表进行操作，不产生新列表，也没有返回值给你。你不需要用等号去赋值，直接调用它就行。
#print(didian)
didian.reverse()
print(didian)
#didian.reverse=True
#print(didian)
#didian.sort()
#print(didian)
#didian.sort()
#print(didian)
'''
#这块学的有点问题，我重新搞一下






print('\n\n\n')
print('3.3 组织列表')
print('3.3.1 使用方法sort()对列表永久排序')
cars=['bmw','audi','toyota','subaru']
cars.sort()#sort()是方法，是对列表进行永久的修改
print(cars)



cars=['bmw','audi','toyota','subaru']
cars.sort(reverse=True)#rever=True是参数，不过对于列表的修改时永久的,这里的永久的意思是在代码里他就变成升序排列的了，并不只是在显示时是升序的
print(cars)#而且reverse=True的意思是“在排序时，把结果反转”，也就是将列表按照降序排序
#测试看我要是再搞一个reverse=True会不会变回来
#cars.sort(reversed=True)！！！时reverse=True不是reversed

#cars.sort(reverse=True)#因为在前面cars这个列表已经变成降序排列的了所以这次就不会起作用了
#print(cars)
#当然想要变回来的话就直接用方法sort()升序排列就行了
cars.sort()
print(cars)



print('\n\n\n')
print('3.3.2 使用函数sorted()对列表临时排序')#使用函数sorted()不会对原来的列表产生改变，只会在显示时显示改变后的结果
cars=['bmw','audi','toyota','subaru']
print("Here is the original list:")#没用函数sorted()时的样子
print(cars)
print("\nHere is the sorted list:")#用了函数sorted()时的样子
print(sorted(cars))
print("\nHere is the original list again:")#证明cars列表没有变
print(cars)

#要是想要与字母顺序相反的顺序显示列表，也可以向函数sorted()传递参数reverse=True
print(sorted(cars,reverse=True))
print(cars)
#测试一下看传递参数reverse=True后，列表会不会变
print(cars)#看来没有变



print('\n\n\n')
print('3.3.3 倒着打印列表')
cars=['bmw','audi','toyota','subaru']
print(cars)
cars.reverse()#reverse()是方法不是函数,并且reverse()并不是按照降序的方法排列元素，只是将列表元素的排列顺序反转过来
print(cars)
#需要注意的是方法reverse()是和方法sort()一样永久改变的，不过可以随时恢复到原来的排列顺序
#当然如果我们想要改回来的话再用一个reverse()就行
cars.reverse()
print(cars)




print('\n\n\n')
print('3.3.4 确定列表的长度')
cars=['bmw','audi','toyota','subaru']
print(len(cars))#通过函数len()可以快速的知道列表的长度



print('\n\n\n')
print('练习3-8：放眼世界')
didian=['beijin','hami','beiji','yingguo','xingxilan','nanji']
print(didian)

print(sorted(didian))
print(didian)

print(sorted(didian,reverse=True))
print(didian)

didian.reverse()
print(didian)

didian.reverse()
print(didian)

didian.sort()
print(didian)

didian.sort(reverse=True)
print(didian)



print('\n\n\n')
print('练习3-9：晚餐嘉宾')
print(len(name))



print('\n\n\n')
print('练习3-10：尝试使用各个函数')
meishi=['pisa','hanbao','guoyourou','jiaozi','huogou','kaorou']
youxi=['cs2','arma3','apex','qunxing']
#对meishi列表使用
print(meishi)

meishi.sort()
print(meishi)

meishi.sort(reverse=True)
print(meishi)

meishi.sort()
print(meishi)

print(sorted(meishi))
print(meishi)

print(sorted(meishi,reverse=True))
print(meishi)

meishi.reverse()
print(meishi)
meishi.reverse()
print(meishi)

print(len(meishi))

#对yousi列表使用
print(youxi)

youxi.sort()
print(youxi)

youxi.sort(reverse=True)
print(youxi)

youxi.sort()
print(youxi)

print(sorted(youxi))
print(youxi)
print(sorted(youxi,reverse=True))
print(youxi)

youxi.reverse()
print(youxi)
youxi.reverse()
print(youxi)

print(len(youxi))
#3.3结束



print('\n\n\n')
print('3.4 使用列表时避免索引错误')
motorcycles=['honda','yamaha','suzuki']
#print(motorcycles[3])!!!这个列表里面只有三个元素，没有第四个元素，这会触发索引错误

#当然当我们想要访问最后一个元素时我们就可以使用索引-1
motorcycles=['honda','yamaha','suzuki']
print(motorcycles[-1])

#当然，当列表为空时我们这样访问就会出错
motorcycles=[]
#print(motorcycles[-1])!!!



print('\n\n\n')
print('练习3-11：有意引发错误')
# 假设这是AETS系统中“大模型时代”的几个关键里程碑事件
ai_events = ['Transformer提出', 'GPT-3发布', 'ChatGPT发布', 'Agent原型出现', '工业AI Agent萌芽']

# 1. 你的任务：有意引发一个索引错误 (IndexError)
# 目前列表中有几个事件？试着去访问一个根本不存在的索引。
# 把你的代码写在下面：
print(len(ai_events))
#print(ai_events[5])！！！我这里模拟的是在前面看到这个列表的长度为5后想要访问最后一个索引时忘记-1的错误
# 2. 解释一下：你看到的错误信息写的是什么？它告诉了你哪些重要信息？
# （用注释回答）
'''
发生异常: IndexError    索引错误
list index out of range     列表索引超出范围
  File "D:\visual studio\vscode\PythonStudy\2026\.vscode\python_learn.py", line 921, in <module>
    print(ai_events[5])#我这里模拟的是在前面看到这个列表的长度为5后想要访问最后一个索引时忘记-1的错误
          ~~~~~~~~~^^^
IndexError: list index out of range      索引错误：列表索引超出范围

'''



          

# 3. 修复错误（只用一行代码，不要手动数）
# 用 len() 函数配合 f-string，打印一句话，展示最后一个里程碑是什么。
# 提示：最后一个事件的索引等于 len(列表) - 1
# 把你的代码写在下面：
#修复代码
print(ai_events[4])
print(f"ai_events列表的长度为{len(ai_events)},最后一个历程杯为：{ai_events[4]}")



print('练习题升级版：')
ai_events = ['Transformer提出', 'GPT-3发布', 'ChatGPT发布', 'Agent原型出现', '工业AI Agent萌芽']

# 为每个事件增加一个风险描述
risks = ['算力需求激增', '商业化路径不清晰', '伦理与监管空白', '多步推理不可靠', '物理世界安全挑战']

# 任务：用一行代码，打印出一个清晰展示某个事件及其对应风险的句子。
# 目标事件是你列表中的“倒数第二个”里程碑，这样能避开最后一个，考验你对中间位置的索引操作。
# 提示：倒数第二个的索引 = 总长度 - 2，但不要手动数，用 len()
# （把你的一行代码写在下面）
#print(f"ai_events的列表长度为{len(ai_events)},risks的列表长度为{len(risks)},{ai_events[3]}的风险为：{risks[3]}")
#不用数的方式：
print(f"ai_events的列表长度为:{len(ai_events)},risks的列表长度为{len(risks)},{ai_events[len(ai_events)-2]}的风险为：{risks[len(risks)-2]}")



print('\n\n\n')
print('3.5 小结')
print('这一章我没怎么记住，就是总是想不来这个增加元素用哪一个，删除用哪一个，想不起来怎么拼，这一章未来需要加强')



print('\n\n\n')
print('第4章 操作列表')
print('4.1 遍历整个列表')
magicians=['alice','david','carolina']
for magician in magicians:
    print(magician)



print('\n\n\n')
print('4.1.1深入研究循环')



print('\n\n\n')
print('4.1.2 在for循环中执行更多的操作')
magicians=['alice','david','carolina']
for magician in magicians:
    print(f"{magician.title()},that was a great trick!")

magicians=['alice','david','carolina']
for magician in magicians:
    print(f"{magician.title()},that was a great trick")
    print(f"I can not wait to see your next trick,{magician.title()}.\n")



print('\n\n\n')
print('4.13 在for循环结束后执行一些操作')
magicians=['alice','david','carolina']
for magician in magicians:
    print(f"{magician.title()},that was a great trick!")
    print(f"I can not wait to see your next trick,{magician.title()}.\n")
print("Thank you,everyone.That was a great magic show!")



print('\n\n\n')
print('4.2 避免缩进错误')

print('4.2.1 忘记缩进')
magicians=['alice','david','carolina']
for magician in magicians:
#print(magician)!!!没有缩进
    print(magician)



print('\n\n\n')
print('4.2.2 忘记缩进额外的代码行')
magicians=['alice','david','carolina']
for magician in magicians:
    print(f"{magician.title()},that was a great trick!")
print(f"I can not wait to see your next trick,{magician.title()}.\n")#不对



print("等会有比赛要看，请个假^=^")



print('\n\n\n')
print('4.2.3 不必要的缩进')
message="Hello python world!"
#        print(message)！！！因为在这里print不是循环的部分，所以Python会报错，需要注意!!!
print('\n\n\n')
print('4.2.4 循环后不必要的缩进')
magicians=['alice','david','carolina']
for magician in magicians:
    print(f"{magician.title()},that was a great trick!")
    print(f"I can not wait to see your next trick,{magician.title()}\n")
print("That you everyone,that was a great magic show!")
#这块有问题，但是不知道为什么我的vpn连不上了，今天也心不在焉的，先停一下



print('\n\n\n')
print('4.2.5 遗漏了冒号')
magicians=['alice','david','carolina']
#for magician in magicians！！！不要忘记加冒号：！！！
#   print(magician)



print('\n\n\n')
print('练习4-1：比萨')
pizzas=['荔枝披萨','板栗披萨','草莓巧克力披萨']
for pizza in pizzas:
    #print(f"我很喜欢吃{pizzas}")!!!注意我这里用的是pizzas是列表的全部了，正确用法应该是pizza
    print(f"我很喜欢吃{pizza}")
print('I really love pizza!')



print('\n\n\n')
print('练习4-2：动物')
animals=['dog','cat','rabbit']
for animal in animals:
    print(f"A {animal} would make a great pet")
print('Any of these animals would make a gret pet')



print('\n\n\n')
print('4.3 创建数值列表')
print('4.3.1 使用函数range()')
for value in range(1,5):
    print(value)


print('\n\n\n')
for value in range(1,6):
    print(value)



print('\n\n\n')
print('4.3.2 使用range()创建数字列表')
numbers=list(range(1,6))#!!!注意list()是函数，range()是参数,函数需要东西承接
print(numbers)


#指定步长
print('\n\n\n')
even_numbers=list(range(2,11,2))#！！！第二个2是步长！！！
print(even_numbers)



print('\n\n\n')
print('前十个整数的平方')
squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)


#当然也可以将中间变量square()去掉
squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)



print('\n\n\n')
print('4.3.3 对数字列表执行简单的执行统计')
#for digits in range(0,10**2):
#    print(digits)
#print(min(range))!!!range是python的内置函数名，不是我所创建的列表，想要这样写的话：print(min(range(0,10**2)))
#print(min(digits))!!!digits是整数不是列表，这样写会报错
numbers =list(range(0,10**2))
for digits in numbers:
    print(digits)
print(f"numbers列表中的最小数是{min(numbers)}")
print(f"numbers列表中的最大数是{max(numbers)}")
print(f"numbers列表中的最大数和最小数的总和是{sum(numbers)}")




print('\n\n\n')
print('4.3.4 列表解析')
squares=[value**2 for value in range(1,11)]
print(squares)



print('\n\n\n')
print('练习4-3：数到20')
#lianxi_4_3=[value,for value in range(1,21)]！！！for前面的表达式和for关键字之间不能有任何的标点符号
#print(value)!!!deepseek说这个是一个泄露干扰
lianxi_4_3=[value for value in range(1,21)]
print(lianxi_4_3)
for lianxi4_3 in lianxi_4_3:
    print(lianxi4_3)

print('\n\n\nor')
lianxi_4_3=list(range(1,21))#我可以关注一下海象运算符:=
for lianxi4_3 in lianxi_4_3:
    print(lianxi4_3)


'''
print('\n\n\n')
print("练习4-4：一百万")
lianxi_4_4=list(range(1,1000001))
for lianxi4_4 in lianxi_4_4:
    print(lianxi4_4)
'''


print('\n\n\n')
print('练习4-5：一百万求和')
lianxi_4_5=list(range(1,1000001))
print(min(lianxi_4_5))
print(max(lianxi_4_5))
print(sum(lianxi_4_5))



print('\n\n\n')
print('练习4-6：奇数')
a=list(range(1,21,2))
for b in a:
    print(b)



print('\n\n\n')
print('练习4-7：3的倍数：')
a=list(range(3,31,3))
for c in a:
    #print(c/2)!!!注意审题!!!
     print(c)



print('\n\n\n')
print('练习4-8：立方')
a=list(range(1,11))
for b in a:
    #print(b,':'b**3)！！！在':'和b**3之间缺了个,!!!
    print(b,':',b**3)



print('\n\n\n')
print('练习4-9:立方解析：')
a=[b**3 for b in range(1,11)]
print(a)
print("今天就到这里吧！")



print('\n\n\n')
print('4.4 使用列表的一部分')
print('4.4.1 切片')
players=['charles','martina','michael','florence','eli']
print(players[0:3])


players=['cherles','martina','michael','florence','eli']
print(players[1:4])


players=['cherles','martina','michael','florence','eli']
print(players[:4])


players=['cherles','martina','michael','florence','eli']
print(players[2:])


players=['cherles','martina','michael','florence','eli']
print(players[-3:])



print('\n\n\n')
print('4.4.2 遍历切片')
players=['cherles','martina','michael','florence','eli']
print("Here are first three players on my team:")
for player in players[1:3]:
    print(player.title())

print(players[0:3])



print('\n\n\n')
print('4.4.3 复制列表')
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]
print('My favorite foods are:')
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#text：当我们复制列表时也可以这样做
a=my_foods
#print(a)



my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)

print("\nMy frend's favorite foods are:")
print(friend_foods)
print(a)#这里没有出来的原因时：我这里用的my_foods是新的列表，不是前面一个my_foods


#我前面使用a=my_foods的用法的错误之处
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
#在这里我赋值给friend_foods的ice cream会出现在my_foods的原因是，我在最开始创建了一个贴着my_foods的盒子
#但是后面我又在这个盒子上加了一个名为“friend_foods”的标签，所以我添加给friend_foods的ice cream会出现在
#打印my_foods的结果中



print('\n\n\n')
print('练习4-10:切片')
my_foods=['pizza','falafel','carrot cake','炸鸡','汉堡','过油肉拌面','宫保鸡丁','饺子']
print("The first three items in list are:")
for my_food in my_foods[:3]:
    print(my_food.title())
print("\nThree items from the middle of the are:")
for my_food in my_foods[2:6]:
    print(my_food.title())
print("\nThe last three items in the list are:")
for my_food in my_foods[-3:]:
    print(my_food.title())



print('\n\n\n')
print('练习4-11：你的比萨，我的比萨')
#friend_pizzas=my_food[:]!!!这里要注意不能用my_food因为这样的话创建的副本是my_food得了，而不是my_foods的！！！
friend_pizzas=my_foods[:]
my_foods.append('荔枝比萨')
#friend_foods.append('板栗比萨')！！！是friend_pizzas！！！
friend_pizzas.append('板栗比萨')
print("My favorite pizzas are:")
for my_food in my_foods[:]:
    print(my_food.title())
#print("My frend's favorite pizza are:")!!!要在MY frend's的前面加上\n要不然会看起来很乱!!! 
print("\nMy frend's favorite pizza are:")
#for friend_pizza in friend_foods:!!!这里有好几处错误：1.是friend_pizzas,而不是friend_foods 2.而且我们要加上[:]要不然他鬼知道要怎么搞
for friend_pizza in friend_pizzas:
    print(friend_pizza.title())



print('\n\n\n')
print("练习4-12：使用多个循环")
my_foods=['pizza','falsfel','carrot cake']
for my_food in my_foods:
    print(my_food.title())
print("没搞懂他想要干什么")



print('\n\n\n')
print("4.5 元组")
print("4.5.1 定义元组")
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])

#尝试修改元组元素
dimensions=(200,50)
#dimensions[0]=250！！！在python中试图修改元组的操作是被禁止的!!!
a=1,2,3,4,5,6#在元组中元组是由逗号标识的，圆括号只是让元组看起来更加整洁，更清晰
print(a[0])
print(a[1])
print(a[2])



print('\n\n\n')
print("4.5.2 遍历元组中的所有值")
dimensions=(200,50)
for dimension in dimensions:
    print(dimension)



print('\n\n\n')
print("4.5.3 修改元组变量")
dimensions=(200,50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions=(400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)



print('\n\n\n')
print("练习4-13：自助餐：")
zizhucans=("炸鸡","烤鸡翅","披萨","可口可乐","水果")
for zizhucan in zizhucans:
    print(zizhucan)
#zizhucan[0]=250!看到了吧就是不能修改元组的元素，但是可以修改元组的变量
print('\n')
zizhucans_1=("炸鸡","烤鸡翅","披萨","冰激淋","雪碧")
for zizhucan_1 in zizhucans_1:
    print(zizhucan_1)



print('\n\n\n')
print('4.6 设置代码格式')
print('4.6.1 格式设置指南')



print('\n\n\n')
print('第5章 if语句')
print('5.1 一个简单实例')
cars=['audi','bmw','subaru','toyota']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())



print('\n\n\n')
print('5.2 条件测试')
print('5.2.1 检查是否相等')
car='bmw'
if car=='bmw':
    print('对了')
else:
    print('不对')
car='audi'
if car=='bmw':
    print('对了')
else:
    print('不对')



print('\n\n\n')
print('5.2.2 检查是否相等时忽略大小写')
cars=['audi','AUDI']
for car in cars:
    if car=='audi':
        print(car,'true')
    else:
        print(car,'false\n')
#cars.lower()=['audi','AUDI']!!!cars是列表不是字符串，不能够给他用方法！！！
#for car.lower() in cars:!!!for循环的in前面必须是变量名！！！
for car in cars:
    if car.lower() =='audi':
        print(car,"true")
    else:
        print(car,'false')
