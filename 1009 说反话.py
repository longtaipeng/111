# 字符串由若干单词和若干空格组成，其中单词是由英文字母（大小写有区分）组成的字符串，
# 单词之间用 1 个空格分开，输入保证句子末尾没有多余的空格。
a = input().split(' ')
print(' '.join(a[::-1]))
