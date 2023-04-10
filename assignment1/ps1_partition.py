# From codereview.stackexchange.com                    
def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(2**len(set_)//2):
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b

def get_partitions(set_):
    for partition in partitions(set_):
        yield [list(elt) for elt in partition] #여러개의 데이터를 미리 만들어 두는 것이 아니라 필요할때 마다 즉석해서 하나씩 만들어 낼 수 있는 객체를 의미합니다.(yield)
