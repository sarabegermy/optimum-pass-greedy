'''
Consider the entire 2D plane as a football ground. You are given the N coordinates of the N football players each of team Barcelona. Any player having the ball, can pass it to any other player on the field.

Lets define Optimal Pass as the length of pass, that can change the position of ball by maximum distance.

Since we don't have complete information of the location of ball at the current moment, you have the freedom to assume that it can be with any of the player on the field.

Find the Optimal Pass, that can be achieved at this orientation of players. Since we want to avoid precision error, you have to find (Optimal Pass)2.

You can assume that passing a ball from one player to another takes minimal time.

NOTE: 'Optimal Pass' will be from one player to another only. Also, you are asked the Optimal Pass at this instant. Multiple passes are not allowed.

Input Format

The first line of input will contain N. The number of players. Then N lines follow. The ith line will contain pair of integers "X Y", denoting the coordinates of ith player.

Output Format

Output in one line, the value of (Optimal Pass)2.

CONSTRAINTS

1 ≤ N ≤ 105
1 ≤ X,Y ≤ 105
All N coordinates will be distinct.

Sample Input

3
5 1
3 5
2 1

Sample Output

20

Explanation

We can assume that the player at position (5,1) has the ball. He can pass it to player at (3,5) and get (Optimal Pass)2 = 20. This is the best possible answer i.e. any other assumption will not improve our current answer.
'''
def opt(x, y):
    '''
    min_x = min(x)
    indeces_min_x = [i for i, item in enumerate(x) if item == min_x]

    min_y = min(y)
    indeces_min_y = [i for i, item in enumerate(y) if item == min_y]

    max_x = max(x)
    indeces_max_x = [i for i, item in enumerate(x) if item == max_x]

    max_y = max(y)
    indeces_max_y = [i for i, item in enumerate(y) if item == max_y]
    '''
    sum = [x+y for x, y in zip(x, y)]
    difference = [x-y for x, y in zip(x,y)] #[abs(x-y) for x, y in zip(x,y)]
    #get corners:
    index = sum.index(min(sum))
    point_top_left=(x[index], y[index])

    index = sum.index(max(sum))
    point_down_right=(x[index], y[index])

    #max_diff = sorted(difference, reverse=True)[0]
    #print(max_diff)
    #second_max_diff = sorted(difference, reverse=True)[1]
    #print(second_max_diff)
    #indeces_max_differences = [i for i, item in enumerate(y) if item == max_diff]
    index = difference.index(max(difference))
    point_top_right=(x[index], y[index])

    #index = difference.index(second_max_diff)####max
    index = difference.index(min(difference))  ####negative or max abs
    point_down_left=(x[index], y[index])

    distance_diagonal_1 = pow((point_top_left[0]-point_down_right[0]),2) + pow((point_top_left[1]-point_down_right[1]), 2)
    distance_diagonal_2 = pow((point_top_right[0]-point_down_left[0]),2) + pow((point_top_right[1]-point_down_left[1]), 2)
    return max(distance_diagonal_1, distance_diagonal_2)







players=(int(input()))
x=[]
y=[]
for i in range(players):
    player=input().split()
    playerx=int(player[0])
    playery=int(player[1])
    x.append(playerx)
    y.append(playery)
print(opt(x,y))