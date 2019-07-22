import pymongo

client = pymongo.MongoClient(host="localhost", port=27017)
# client = pymongo.MongoClient(mongodb://localhost:27017/)
db = client.test1
# db = client[test1]
collection = db.temp1
# collection = db[temp1]


# 插入数据
# student3 = {"name": "fanjiahui", "age": 22, "gender": "woman"}
# student1 = {"name": "fanjiale", "age": 22, "gender": "man"}
# student2 = {"name": "feiliang", "age": 23, "gender": "man"}
# # result = collection.insert([student1, student2])
# ret1 = collection.insert_one(student3)
# ret2 = collection.insert_many([student1, student2])
# # print(result)
# print(ret1, ret2)
# print(ret1.inserted_id, ret2.inserted_ids)

# 查询数据
# result = collection.find_one({"name": "fanjiale"})
# result2 = collection.find({"name": "fanjiale"})
# print(type(result), result)
# print("*"*100)
# print(type(result2), result2)
# a = [i for i in result2]
# print(len(a))
# result3 = collection.find({"age": {"$gt": 22}})
# print(len([i for i in result3]))
#
# result4 = collection.find({"age": {"$in": [10, 23]}})
# print(len([i for i in result4]))
#
# result5 = collection.find({"name": {"$regex": "^f.*"}})
# print(len([i for i in result5]))

# 计数
# num = collection.find({"name": {"$regex": "^fei.*"}}).count()
# print(num)

# 排序
# result = collection.find().sort("name", pymongo.ASCENDING) # 降序为pymongo.DESCENDING
# # print(type(result))
# print([i for i in result])

# 偏移
# result = collection.find().sort("name", pymongo.ASCENDING).skip(10).limit(10) # skip向后偏移的个数，limit是限制返回10个结果
# print(len([i for i in result]))

# 更新
# result = collection.update({"name": "feiliang"}, {"age": 32, "gender": "man"}) # 第一种方法
# # print(type(result))
# print(result)
# result1 = collection.update({"name": "fanjiale"}, {"$set": {"age": 23}}) # 第二种方法
# print(result1)
# 官方提倡用法
# ret1 = collection.update_one({"name": "fanjiajia"}, {"$set": {"name": "fanjiale"}})
# ret2 = collection.update_many({"name": "fanfanfan"}, {"$set": {"name": "fanjiajia"}})
# print(ret1.matched_count, ret2.matched_count)

# 删除用法
# result1 = collection.remove({"name": "fanjiale"})
# result2 = collection.delete_one({"name": "fanjiajia"})
# result3 = collection.delete_many({"name": "fanjiajia"})
# print(result1, result2.deleted_count, result3.deleted_count)
