'''
复习
*字符串是什么？
字符串就是一系列的字符，在python中用引号括起来的都是字符串，其中的引号可以是单引号或双引号
eg:
'hello world'
"hello world" 
*方法：是pyhon可对数据执行的操作
*使用方法title()修改字符串的大小写(以首字母大写的方式显示单词或者说字符串)
eg:
name="ada lovelace"
print(name.title())
当然我们可以使用upper()的方法将所有字符串全部改写为全部大写的形式
eg:
name="ada lovelace"
print(name.upper())
或者使用lower()的方法将所有字符串全部改写为全部小小写的形式
eg:
name="ADA LOVELACE"
print(name.lower())
*在字符串中使用变量
当我们想在字符串中插入变量的值时，我们可以使用f字符串来实现，f是format（格式化）的缩写，在前引号前加上字母f,再将要插入的变量用花括号括起来就可以了
eg:
first_name="ada"
last_name="lovelace"
full_name=f"{first_name} {last_name}"
print(full_name)
'''
#2026年4月18日
#学习使用制表符或者换行符来添加空白
print("python")#不添加制表符或者换行符时的输出
print("\tpython")#要在字符串中添加制表符时，可以使用字符组合\t的输出