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
print(repr(favorite_language))
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