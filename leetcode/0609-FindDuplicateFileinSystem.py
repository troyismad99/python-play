'''
609. Find Duplicate File in System

Given a list paths of directory info, including the directory path, and all the files 
with contents in this directory, return all the duplicate files in the file system 
in terms of their paths. You may return the answer in any order.

A group of duplicate files consists of at least two files that have the same content.

A single directory info string in the input list has the following format:

    "root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"

It means there are n files (f1.txt, f2.txt ... fn.txt) with content (f1_content, f2_content ... fn_content) 
respectively in the directory "root/d1/d2/.../dm". 

Note that n >= 1 and m >= 0. If m = 0, it means the directory is just the root directory.

The output is a list of groups of duplicate file paths. 
For each group, it contains all the file paths of the files that have the same content. 
A file path is a string that has the following format:

    "directory_path/file_name.txt"

Example 1:
    Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
    Output: [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]

Example 2:
    Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]
    Output: [["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]

Constraints:
    1 <= paths.length <= 2 * 10^4
    1 <= paths[i].length <= 3000
    1 <= sum(paths[i].length) <= 5 * 10^5
    paths[i] consist of English letters, digits, '/', '.', '(', ')', and ' '.
    You may assume no files or directories share the same name in the same directory.
    You may assume each given directory info represents a unique directory. A single blank space separates the directory path and file info.
'''
# Runtime: 88 ms        Your runtime beats 61.55 % of python3 submissions.
# Memory Usage: 24.2 MB Your memory usage beats 27.12 % of python3 submissions.

from typing import DefaultDict

class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:

        # Populate a hashmap with our results
        # the hashmap key will be the file contents
        # the value will be a list of the paths with those file contents.
        # duplicates will simply have more than one path in the list

        # hashmap with default type of list
        result = DefaultDict(list)

        # A Python dictionary throws a KeyError if you try to 
        # get an item with a key that is not currently in the dictionary. 
        # The defaultdict will create any item that you try to access that doesn't exist.
        # in this case it will create a new empty list.
    
        for path in paths:
            data = path.split()
            root = data[0] # path is in the first element
            for file in data[1:]:
                filename, _, filecontents = file.partition('(')
                result[filecontents[:-1]].append(root + '/' + filename)

        # return all with more than one entry
        return [x for x in result.values() if len(x) > 1]
        
s = Solution()
print(s.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]))
print(s.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]))


