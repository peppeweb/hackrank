# Counting the ways

Python solution for the challenge on [Hacker rank](https://www.hackerrank.com/challenges/count-ways-1).

There are three versione implemented, one iterative solution and two based on dynamic programming.
 - iterative_v : as you can expect.
 - dynamic_programming_recursion_based: It does recursion call and save in a table calculated value. Issue is that even with the table, the calls are too much.
 - dynamic_programming_chunking: It is a version of the iterative_v based on dynamic programming.
By default, the Docker will expose port 80, so change this within the Dockerfile if necessary. When ready, simply use the Dockerfile to build the image.