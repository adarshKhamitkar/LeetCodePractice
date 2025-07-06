"""
Suppose you are at a party with n people labeled from 0 to n - 1 and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know the celebrity, but the celebrity does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. You are only allowed to ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given an integer n and a helper function bool knows(a, b) that tells you whether a knows b. Implement a function int findCelebrity(n). There will be exactly one celebrity if they are at the party.

Return the celebrity's label if there is a celebrity at the party. If there is no celebrity, return -1.

Note that the n x n 2D array graph given as input is not directly available to you, and instead only accessible through the helper function knows. graph[i][j] == 1 represents person i knows person j, wherease graph[i][j] == 0 represents person j does not know person i.

Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.

Input: graph = [[1,0,1],[1,1,0],[0,1,1]]
Output: -1
Explanation: There is no celebrity.
 

Constraints:

n == graph.length == graph[i].length
2 <= n <= 100
graph[i][j] is 0 or 1.
graph[i][i] == 1
 

Follow up: If the maximum number of allowed calls to the API knows is 3 * n, could you find a solution without exceeding the maximum number of calls?
"""

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

def knows(a: int, b: int) -> bool:
    # This is a placeholder for the actual implementation of the knows function.
    # In a real scenario, this function would access the party's knowledge graph.
    pass

class Solution:
    #Logical deduction
    def findCelebrity(self, n:int) -> int:
        def is_celebrity(node):
            for j in range(n):
                if node == j: continue
                if knows(node,j) or not knows(j,node): return False
            return True

        celebrity_candidate = 0
        for i in range(n):
            if celebrity_candidate == i: continue
            if knows(celebrity_candidate,i):
                celebrity_candidate = i

        return celebrity_candidate if is_celebrity(celebrity_candidate) else -1
             


    #Brute Force
    # def findCelebrity(self, n: int) -> int:
    #     def is_celebrity(node):
    #         for j in range(n):
    #             if node == j: continue
    #             if knows(node,j) or not knows(j,node):
    #                 return False
    #         return True
    #     for i in range(n):
    #         if is_celebrity(i):
    #             return i
    #     return -1

    #Time Complexity: O(n) for the first loop to find the celebrity candidate and O(n) for the second loop to verify if the candidate is a celebrity, resulting in O(n) overall.
    #Space Complexity: O(1) since we are using a constant amount of space for the candidate and the verification function does not use any additional space that scales with n.
