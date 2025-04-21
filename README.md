# Algorithms and Data Structures - Kruskal


## Characteristics
- Time complexity: O(V log V)
  - Because sorting the edges by weight is the dominant operation
- Space complexity: O(V + E)



## Demos

```mermaid
graph LR
  0((0)) -- 4 --- 1((1))
  0 -- 4 --- 4((4))
  1 -- 1 --- 2((2))
  1 -- 6 --- 6((6))
  1 -- 8 --- 3((3))
  2 -- 5 --- 4
  3 -- 7 --- 5((5))
  3 -- 3 --- 7((7))
  7 -- 5 --- 6
```

[Implementation](./src/kruskal.py)



## References
- [Other Algorithms & Data Structures](https://github.com/NelsonBN/algorithms-data-structures)
