# a, b = map(int, input().split())
#
# print(a//b, a%b, float(a/b))


# なんかよくわからないけど小数点以下6位までだしてくれるっぽい
A, B = map(int,input().split())
print("%d %d %f" % (A/B, A%B, A/B))


print("%f" % (A/B))