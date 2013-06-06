problem_no = 14
description = '''The following iterative sequence is defined for the set of positive integers:

n --> n/2 (n is even)
n --> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 --> 40 --> 20 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.'''


def solve():
    # A dictionary mapping starting numbers to their following number.
    # Structure: (start: next), which represents start --> next
    # E.g. (13: 40) is 13 --> 40, (2: 1) is 2 --> 1
    links = {2: 1}
    # Construct all links for n from 3 to 1e6
    for n in range(3, int(1e2)+1):
        # print 'next in for loop:', n
        path_complete = False
        if n not in links.keys():
            # print n, 'has no link yet...'
            while not path_complete:
                if n % 2 == 0:
                    next = n/2
                else:
                    next = 3*n + 1
                links[n] = next  # n --> next
                # print n, '-->', next
                if next in links.keys():
                    # print 'path complete'
                    path_complete = True
                else:
                    n = next
    # print len(links)
    # print links
    return 'not yet...'

if __name__ == '__main__':
    print solve()
