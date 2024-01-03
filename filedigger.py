import os
import shutil

# Print Welcome Message
print('|---------------------------------------------------------|')
print('| File digger 1.0 (windows only)                          |')
print('| - - - - - - - - - - - - - - - - - - - - - - - - - - - - |')
print('| Function: Saves all the files beneath a                 |')
print('|           directory into an output folder.              |')
print('| Usage   : Enter the path to your directory              |')
print('|           like this: "Path > C:\\Users\\usr\\your_dir"     |')
print('| - - - - - - - - - - - - - - - - - - - - - - - - - - - - |')
print('| © Tobias Klein 2024                                     |')
print('|---------------------------------------------------------|')
print('')


PATH = ''
OUT_PATH = ''
FILES = []

while not os.path.exists(PATH):
    PATH = input('Path >  ')

OUT_PATH = PATH + '_OUT'

print(' - Output Path:', OUT_PATH)
print(' - Start extraction')

def explore(path):
    for f in os.listdir(path):
        filepath = path + '\\' + f
        if os.path.isdir(filepath):
            explore(filepath)
        else:
            FILES.append(filepath)
    return

explore(PATH)

# Copy files over

def getEnd(filename):
    name, extension = os.path.splitext(filename)
    return extension

os.mkdir(OUT_PATH)

for i, file in enumerate(FILES):
    newpath = OUT_PATH + '\\' + str(i+1) + str(getEnd(file))
    print(' - Saving: ' + newpath)
    # copy2 to preserve meta data
    shutil.copy2(file, newpath)

print(' - Finished!')
print(' - Output: ' + OUT_PATH)

