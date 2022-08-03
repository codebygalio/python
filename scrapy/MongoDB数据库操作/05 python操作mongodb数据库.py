import pymongo  # 导入数据库模块


# 1. 指定连接数据库
client = pymongo.MongoClient(host='106.52.167.142',
                    port=27017)

# 2. 指定用哪一个数据库
collections = client.test

# 3. 指定操作的文档
stu = collections.students

"""插入数据"""
# student = {
#     'id': '20170101',
#     'name': 'Jordan',
#     'age': 20,
#     'gender': 'male'
# }
#
# result = stu.insert(student)
# # 如果数据插入成功会把数据的id值返回
# print(result)

# student1 = {
#     'id': '20170101',
#     'name': 'Jordan',
#     'age': 20,
#     'gender': 'male'
# }
#
# student2 = {
#     'id': '20170202',
#     'name': 'Mike',
#     'age': 21,
#     'gender': 'male'
# }
#
# result = stu.insert([student1, student2])
# print(result)


"""查询数据"""
# result = stu.find_one()
# print(result)

# result = stu.find()
# print(result)
# for i in result:
#     print(i)

# result = stu.find_one({'age':{'$gt': 20}})
# print(result)

"""更新数据"""
# condition = {'name': 'Jordan'}
# student = stu.find_one(condition)
# student['age'] = 25
# result = stu.update(condition, student)
# print(result)

"""删除数据"""
stu.remove({'name': 'Jordan'})
