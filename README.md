# optimum-pass-greedy
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
