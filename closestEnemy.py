"""
Using the Python language, have the function ClosestEnemyII(strArr) read the
matrix of numbers stored in strArr which will be a 2D matrix that contains only
the integers 1, 0, or 2. Then from the position in the matrix where a 1 is,
return the number of spaces either left, right, down, or up you must move to
reach an enemy which is represented by a 2. You are able to wrap around one side
of the matrix to the other as well.
"""


def closest_enemy(arr):
    # position of the 1 and the enemies
    position = []
    enemies = []
    # loop through every number
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            # get the position of the 1
            if arr[j][i] == "1":
                position.append([i, j])
            # get the positions of the enemies
            elif arr[j][i] == "2":
                enemies.append([i, j])
    current_enemy = 1000
    # if there are any enemies
    if len(enemies) > 0:
        # get the difference between the 1 coordinates and the enemy coordinates
        for enemy in enemies:
            x_distance = abs(enemy[0] - position[0][0])
            y_distance = abs(position[0][1] - enemy[1])
            total_distance = x_distance + y_distance
            # if the total_distance of the enemy is < than the current_enemy make him the new current_enemy
            if total_distance < current_enemy:
                current_enemy = total_distance
        return current_enemy
    # if there aren't any enemies return 0
    return 0


print(closest_enemy(["0000", "2010", "0000", "2002"]))
