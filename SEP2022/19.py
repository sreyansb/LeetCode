#attempt1:
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        di_content_file = {}
        for path in paths:
            files = path.split(" ")
            rootPath = files[0]
            for file_with_content in files[1:]:
                
                file,content = file_with_content.split("(")
                content = content[:-1]
                if content not in di_content_file:
                    di_content_file[content] = []
                di_content_file[content].append((rootPath+"/"+file).replace("//","/"))
        ans = []
        for content in di_content_file:
            if len(di_content_file[content])>1:
                ans.append(di_content_file[content])
        return ans
                
            
        
