### selenium关键字驱动
##### 反射原理
```
python:

```
### POM差异
```
POM:以一个个页面的元素及元素操作为对象进行封装,不必穷尽封装所有selenium框架的api,测试用例设计再进行业务调用;
关键字：二次封装selenium框架的api为关键字,以反射同名字符串的方法实现调用,excel编写测试用例即可;
异同：在没有测试平台时,建议以po为主,可以协同开发,若是规划测试平台,则建议关键字驱动;至于数据驱动是可以任何模式搭配使用.
```

### 测试报告
- 结合unittest测试框架
```
需要思考:一个sheet为一个测试用例的操作步骤,那么html的测试报告改如何展示?
假设50个测试用例,那就是50个sheet,如果不用html展示报告,那么就需要在excel标记执行状态;
如果是excel展示测试报告,那么其中的报错日志错误信息及截图又该如何插入?
```

### 实战
- 执行一个sheet页的测试用例
```
实现:遍历一个sheet页的所有操作步骤关键字调用与类中关键字同名的方法,关键的类:excel操作类
```
- 遍历多个sheet页的测试用例
```
实现:在excel操作类中增加两个方法,一个获取所有sheet\另一个根据sheet_index或者name获取sheet页所有的操作步骤
```
- 依测试用例执行需要执行的测试用例
```
实现:新增excel测试用例中sheet,标记需要执行以及获取可以执行的sheet页名称,然后再以第二个实现方案进行遍历.
```
- selenium关键字驱动应用:建议在平台开发中使用.
```
平台开发技术栈:Django+flask+jinja2+mysql,python实现
设想:将excel的关键信息:关键字\元素\内容,提取在web中组装测试用例

已知使用excel作为web自动化测试用例设计,并且关键字已实现,那么是否可以简单GUI上传excel文件,然后执行脚本即可呢?
```
### tkinter桌面化,即GUI
```

```