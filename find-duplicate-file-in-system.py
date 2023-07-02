from typing import List

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        from collections import defaultdict
        
        content_dict = defaultdict(list)
        
        for path in paths:
            elements = path.split(' ')
            directory = elements[0]
            
            for i in range(1, len(elements)):
                file_info = elements[i].split('(')
                file_name = file_info[0]
                file_content = file_info[1][:-1]
                
                file_path = directory + '/' + file_name
                content_dict[file_content].append(file_path)
        
        duplicate_files = []
        for content, file_paths in content_dict.items():
            if len(file_paths) > 1:
                duplicate_files.append(file_paths)
        
        return duplicate_files
