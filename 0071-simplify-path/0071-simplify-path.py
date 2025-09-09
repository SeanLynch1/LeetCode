class Solution:
    def simplifyPath(self, path: str) -> str:
        
        simplified_path = ['']

        for text in path.split('/'):
            if text == '..':
                if len(simplified_path) > 1:
                    simplified_path.pop()
            elif text != '' and text != '.':
                simplified_path.append(text)

        if len(simplified_path) <= 1:
            return '/'
        else:
            return '/'.join(simplified_path)


            