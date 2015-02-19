You are given a state for a rectangular board game grid with chips in a binary matrix,
where 1 is a cell with a chip and 0 is an empty cell. 
You are also given the coordinates for a cell in
the form of row and column numbers (starting from 0). 
You should determine how many chips are close to this cell.
Every cell interacts with its eight neighbours; those cells that are horizontally, vertically, or diagonally adjacent.

![Map](example.svg)

For the given examples (see the schema) there is the same grid:

```
((1, 0, 0, 1, 0),
 (0, 1, 0, 0, 0),
 (0, 0, 1, 0, 1),
 (1, 0, 0, 0, 0),
 (0, 0, 1, 0, 0),)
```

For the first example coordinates of the cell is (1,&nbsp;2) and
as we can see from the schema this
cell has 3 neighbour chips.
For the second example coordinates is (0,&nbsp;0) and this cell contains
a chip, but we count only neighbours and the answer is 1.
