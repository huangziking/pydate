user={"xuezhiqian":{"yanyuan":2.0,"dongfengpo":3.5,"longjuanfeng":1.5,"wenwendexingfu":2.5},
      "zhoujielun":{"yanyuan":2.5,"dongfengpo":3.0,"shuangjiegun":2.0,"woniu":4.5,"longjuanfeng":2.5,"hongmeigui":1.5},
      "chengyixun":{"hongmeigui":1.5,"wenwendexingfu":2.5,"langfei":5.0,"mengxiangtiank":35,"shuangjiegun":3.0}
      }
def manhattan(rating1,rating2):
    #计算曼哈顿距离rating1,rating2参数格式为{'yanyuan':3.0,'dongfengpo':2.5}
    distance=0
    for key in rating1:
        if key in rating2:
            distance+=abs(rating1[key]-rating2[key])
    return distance