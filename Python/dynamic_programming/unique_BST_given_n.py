"""
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
Example 1:
Input: n = 3
Output: 5
Example 2:
Input: n = 1
Output: 1
"""

class Solution:
    def numTrees(self, n: int) -> int:
        #            left subtree         right subtree
        #numTree[3] = numTree[0]=1      *     numTree[2]=2       +
        #             numTree[1]=1      *     numTree[1]=1       +
        #             numTree[2]=2      *     numTree[0]=1       = 5
        numtree = [1] * (n+1)
        for nodes in range(2, n+1): #starting from 2 nodes
            total = 0
            for root in range(1, nodes+1): #making every node as root node
                left = root - 1 # number of nodes remaining in left substree taking a node as root
                right = nodes - root # number of nodes remaining in right substree taking a node as root
                total += numtree[left] * numtree[right]
            numtree[nodes] = total 
        return numtree[n]
    
if __name__ == "__main__":
    obj = Solution()
    
    print(obj.UniqueBST(3)) #5
    
    print(obj.UniqueBST(10)) # 16796
    
    print(obj.UniqueBST(1000)) #2046105521468021692642519982997827217179245642339057975844538099572176010191891863964968026156453752449015750569428595097318163634370154637380666882886375203359653243390929717431080443509007504772912973142253209352126946839844796747697638537600100637918819326569730982083021538057087711176285777909275869648636874856805956580057673173655666887003493944650164153396910927037406301799052584663611016897272893305532116292143271037140718751625839812072682464343153792956281748582435751481498598087586998603921577523657477775758899987954012641033870640665444651660246024318184109046864244732001962029120


# Time Complexity: O(n^2)
# Space Complexity: O(n)