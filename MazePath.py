def count_paths(maze):
    rows = len(maze)
    cols = len(maze[0])
    dp = [[0]*cols for _ in range(rows)]

    if maze[0][0] == 1:
        return 0

    dp[0][0] = 1

    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 1:
                dp[i][j] = 0
            else:
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]

    return dp[rows-1][cols-1]

maze = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

print("Number of escape paths:", count_paths(maze))