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
print(f"整数+浮点数：{name_1}\n 整数+整数：{name_2.lstirp()}")