#!/usr/bin/env python
# -*- coding: utf-8 -*-
endstr="end"#重新定义结束符
str=""
for line in iter(input,endstr):#每行接收的东西 用了iter的哨兵模式
    str+= line+"\n"#换行
print(str)