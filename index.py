a = 10
b = 20
c = 30 
d = 40
import rediscluster

try:

#     创建节点　　
    start_nodes = [

    {'host':'192.168.90.171','port':'7000'},
    {'host':'192.168.90.171','port':'7001'},
    {'host':'192.168.90.171','port':'7002'},
    {'host':'192.168.90.171','port':'7003'}

    ]
#     1.链接集群
    client = rediscluster.StrictRedisCluster(startup_nodes=start_nodes,decode_responses=True)
#     ２．写入数据
    result = client.set('name','itheima')

    print(result)

# 　　　３．读取数据
    content = client.get('name')

    print(content)

except Exception as e:
    print(e)
