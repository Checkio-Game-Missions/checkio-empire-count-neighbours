You are given a state for a rectangular board game grid with chips in a binary matrix,
where 1 is a cell with an enemy and 0 is an empty cell. 
You are also given the coordinates for a cell in
the form of row and column numbers (starting from 0). 
You should determine how many enemies are close to this cell.
Every cell interacts with its eight neighbours; those cells that are horizontally, vertically, or diagonally adjacent.

```
|-----|-----|-----|-----|-----|
|     |. . .|. . .|. . .|     |
|  X  |.   .|. X .|.   .|     |
|     |. . .|. . .|. . .|     |
|-----|-----|-----|-----|-----|
|     |. . .|* * *|. . .|     |
|     |. X .|*   *|.   .|     |
|     |. . .|* * *|. . .|     |
|-----|-----|-----|-----|-----|
|     |. . .|. . .|. . .|     |
|     |.   .|. X .|.   .|  X  |
|     |. . .|. . .|. . .|     |
|-----|-----|-----|-----|-----|
|     |     |     |     |     |
|  X  |     |     |     |     |
|     |     |     |     |     |
|-----|-----|-----|-----|-----|
|     |     |     |     |     |
|     |     |  X  |     |     |
|     |     |     |     |     |
|-----|-----|-----|-----|-----|


|-----|-----|-----|-----|-----|
|* * *|. . .|     |     |     |
|* X *|.   .|  X  |     |     |
|* * *|. . .|     |     |     |
|-----|-----|-----|-----|-----|
|. . .|. . .|     |     |     |
|.   .|. X .|     |     |     |
|. . .|. . .|     |     |     |
|-----|-----|-----|-----|-----|
|     |     |     |     |     |
|     |     |  X  |     |  X  |
|     |     |     |     |     |
|-----|-----|-----|-----|-----|
|     |     |     |     |     |
|  X  |     |     |     |     |
|     |     |     |     |     |
|-----|-----|-----|-----|-----|
|     |     |     |     |     |
|     |     |  X  |     |     |
|     |     |     |     |     |
|-----|-----|-----|-----|-----|
```

For the given examples (see the schema) there is the same grid:

```
((1, 0, 1, 0, 0),
 (0, 1, 0, 0, 0),
 (0, 0, 1, 0, 1),
 (1, 0, 0, 0, 0),
 (0, 0, 1, 0, 0),)
```

For the first example, the coordinates of the cell are (1,&nbsp;2) and
as we can see from the schema this cell has 3 neighbour enemies.
For the second example the coordinates are (0,&nbsp;0) and this cell contains
an enemy, but we are only counting the neighbours so the answer is 1.
