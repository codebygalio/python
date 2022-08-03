"""
db.fanren.updateOne(
   { name: "雷云子" },
   {
     $set: { "detail.sex": "保密", status: "保密" }
   }
)

update  更新数据, 首先应该根据条件找到数据

updateOne  更新查找到的第一条数据

updateMany 更新查找到的所有数据
"""