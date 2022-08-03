"""
db  查看当前使用的数据库

show dbs  查看所有数据库

use + 数据库名字  切换数据库

db.stu.insert({ name: "小明", age: 10, sex: '男'})
    db  表示当前的数据库
    stu 表示文档的名字
    insert 插入的关键字, 括号内部中需要传递字典格式

db.stu.insert()   可以插入多条数据, 需要中[]包裹数据

"""