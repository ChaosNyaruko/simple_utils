n = 4
def fork(a, b):
    res = set()
    for x in a:
        for y in b:
            res.add((x[0] + y[0], '(' + x[1] + '+' + y[1] + ')'))
            res.add((x[0] - y[0],'(' + x[1] +  '-' + y[1] + ')'))
            res.add((y[0] - x[0],'(' + y[1] + '-' + x[1] + ')'))
            res.add((x[0] * y[0],'(' + x[1] + '*' + y[1] + ')'))
            if y[0]:
                res.add((x[0] / y[0],'(' + x[1] + '/' + y[1] + ')'))
            if x[0]:
                res.add((y[0] / x[0],'(' + y[1] + '/' + x[1] + ')'))
    return res

def helper(memo, i):
    if i == 0 or i == 2 ** n:
        return None
    if memo[i] != None:
        return memo[i]

    res = set()
    for x in range(1, i): # 只有小于i的x才“有可能”是i的非空真子集
        if x & i == x: # 此时x才为非空真子集
            res |= fork(helper(memo,x), helper(memo,i - x))

    memo[i] = res
    return res


if __name__ == '__main__':
    inputs = [[5,5,5,1], [3,3,7,7],[3,3,8,8],[1,4,5,6],[3,8,8,10],[4,4,10,10],[9,9,6,2]]
    for input in inputs:
        assert n == len(input)
        memo = [None for _ in range(2 ** n + 1)]
        for i in range(n):
            memo[2 ** i] = {(input[i], str(input[i]))}
        res = helper(memo, 15)
        t = False
        for r in res:
            if abs(r[0] - 24) < 1e-5:
                print(input, True, r)
                t = True
                break
        if not t:
            print(input, False)
            print(res)

        # print("memo", memo)
