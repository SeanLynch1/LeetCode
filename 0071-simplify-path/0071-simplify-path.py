class Solution:
    def simplifyPath(self, path: str) -> str:
        
        simplified_path = ['']

        path = path.split('/')

        for i in range(len(path)):
            text = path[i]
            if simplified_path and simplified_path[-1] == "..":
                    simplified_path.pop()

            if text == '..':
                if len(simplified_path) > 1:
                    simplified_path.pop()

                if i < len(path) - 1:
                    simplified_path.append(text)

            elif text != '' and text != '.':
                simplified_path.append(text)
            
        if len(simplified_path) <= 1:
            return '/'
        else:
            return '/'.join(simplified_path)


            