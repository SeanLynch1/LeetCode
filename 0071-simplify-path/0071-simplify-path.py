class Solution:
    def simplifyPath(self, path: str) -> str:
        
        simplified_path = ['']

        path = path.split('/')

        print(path)
        for i in range(len(path)):
            text = path[i]

            if text == '..':
                if len(simplified_path) > 1:
                    simplified_path.pop()
            elif text != '' and text != '.':
                simplified_path.append(text)
            print(simplified_path)

        print(simplified_path)
        if len(simplified_path) <= 1:
            return '/'
        else:
            return '/'.join(simplified_path)


            