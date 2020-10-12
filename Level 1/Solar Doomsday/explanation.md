# Explanation

> Write a function solution(area) that takes as its input a single unit of measure representing the total area of solar panels you have (between 1 and 1000000 inclusive) and returns a list of the areas of the largest squares you could make out of those panels, starting with the largest squares first. So, following the example above, solution(12) would return [9, 1, 1, 1].

They give us an Integer, the area, and we must return a list that contains all the areas of squares that we can create.

## How to find the squares
Using the example given: `solution(12)`

The biggest square we could create is a `sqrt(12)` by `sqrt(12)` square.

IMAGE

However, `sqrt(12) = 3.464`. This is not an Integer! We must round this up.

So we do `int(sqrt(12))` and we get `9`.

Now that we got our first square, we can store it: `result = [9]`.

Now we must subtract this area from the total one because we now want to the same for the rest of the area.

Now we have `area = 3`: `sqrt(3) = 1.732`.

So we get a `1` by `1` square.

We add `1` to the result: `result = [9, 1]`.

And we keep going until `area = 0`.

At the end we have `result = [9, 1, 1, 1]`.
