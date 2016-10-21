A = [[1, 2, 3],
     [4, 5, 6]]     # a 2 x 3 matrix

B = [[1, 2],
     [3, 4,],
     [5, 6]]        # a 3 x 2 matrix

def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

def get_row(A, i):
    return A[i]

def get_col(A, j):
    return [A_i[j]
            for A_i in A]

def make_matrix(num_rows, num_cols, entry_fn):
    """returns a num_rows x num_cols matrix
    whose (i, j)th entry is entry_fun(i, j)"""
    return [[entry_fn(i, j)
                for j in range(num_cols)]
            for i in range(num_rows)]

def is_diagonal(i, j):
    """1's on the diagonal, 0's everywhere else"""
    return 1 if i==j else 0

identity_matrix = make_matrix(5, 5, is_diagonal)

#          user 0  1  2  3  4  5  6  7  8  9   user
friendships = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0], # 0
               [1, 0, 1, 1, 0, 0, 0, 0, 0, 0], # 1
               [1, 1, 0, 1, 0, 0, 0, 0, 0, 0], # 2
               [0, 1, 1, 0, 1, 0, 0, 0, 0, 0], # 3
               [0, 0, 0, 1, 0, 1, 0, 0, 0, 0], # 4
               [0, 0, 0, 0, 1, 0, 1, 1, 0, 0], # 5
               [0, 0, 0, 0, 0, 1, 0, 0, 1, 0], # 6
               [0, 0, 0, 0, 0, 1, 0, 0, 1, 0], # 7
               [0, 0, 0, 0, 0, 0, 1, 1, 0, 1], # 8
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]] # 9

friendsships_orig = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                     (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

friends02 = friendships[0][2] == 1
friends08 = friendships[0][8] == 1

print "Are user 0 and user 2 friends? %s" % friends02
print "Are user 0 and user 8 friends? %s" % friends08

friends_of_five = [i
                   for i, is_friend in enumerate(friendships[5])
                   if is_friend]

print "Who are user 5's friends? %s" % friends_of_five
