
def numbers_actions(*args):
    print(f"Sum: {sum(args)}")
    print(f'Avg: {"{:.2f}".format(sum(args)/len(args))}')
    print(f"Max: {max(args)}")
    print(f"Min: {min(args)}")
    print(f"Count: {len(args)}")

numbers_actions(2,1,2,4,22,6)