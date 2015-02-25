For maximum damagem, a machinegunner should choose a point where enemies are concetrated.

We'll develop a life-like training program to practice this, based on cellular automata. In cellular automata, [the Moore neighborhood](http://en.wikipedia.org/wiki/Moore_neighborhood) comprises
the eight cells surrounding a central cell on a two-dimensional square lattice.
The neighborhood is named after Edward F. Moore, the pioneer of cellular automata theory.

You are given a state for a rectangular board game grid with chips in a binary matrix,
where 1 is a cell with an enemy and 0 is an empty cell. 
You are also given the coordinates for a cell in
the form of row and column numbers (starting from 0). 
You should determine how many enemies are close to this cell.
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

For the first example, the coordinates of the cell are (1,&nbsp;2) and
as we can see from the schema this cell has 3 neighbour enemies.
For the second example the coordinates are (0,&nbsp;0) and this cell contains
an enemy, but we are only counting the neighbours so the answer is 1.

**Input:** Three arguments. A grid as a tuple of tuples with integers (1/0), a row number and column number for a cell as integers. 

**Output:** How many neighbouring cells have enemies as an integer.

**Example:**

```python
count_neighbours(((1, 0, 0, 1, 0),
                  (0, 1, 0, 0, 0),
                  (0, 0, 1, 0, 1),
                  (1, 0, 0, 0, 0),
                  (0, 0, 1, 0, 0),), 1, 2) == 3
count_neighbours(((1, 0, 0, 1, 0),
                  (0, 1, 0, 0, 0),
                  (0, 0, 1, 0, 1),
                  (1, 0, 0, 0, 0),
                  (0, 0, 1, 0, 0),), 0, 0) == 1
```
**How it is used:**

This idea can be useful for developing board game algorithms.
In addition, the same principles it can be useful for navigational software, or geographical surveying software or even basic cellular reproduction.
**Precondition:**
```python
3 <= len(grid) <= 10
all(len(grid[0]) == len(row) for row in grid)
```