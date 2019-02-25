import os, urllib.parse

def updateIndex():
    dirList = os.listdir('./')
    targetFile = open('Index.md', "w", encoding="utf-8")
    for dir in dirList:
        if os.path.isdir(dir) and not dir.startswith('.'):
            children = os.listdir(dir)
            print('- ' + dir + '\n')
            targetFile.write('- ' + dir + '\n')
            for item in children:
                if item.endswith('md'):
                    strs = item.rsplit(".", 1) # 截取最后一个'.'
                    if len(strs) == 2:
                        url = urllib.parse.quote(item)
                        strItem = '  - [{}](./{}/{})'.format(strs[0], dir, url)
                        print(strItem)
                        targetFile.write(strItem + '\n')


updateIndex()