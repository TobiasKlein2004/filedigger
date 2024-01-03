import os
import shutil

# Print Welcome Message
print('|---------------------------------------------------------|')
print('| File digger 1.1 (windows only)                          |')
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
if os.path.exists(OUT_PATH):
    shutil.rmtree(OUT_PATH)

os.mkdir(OUT_PATH)

while True:
    preserveNames = input(' - Preserve Filenames? (Y/N)')
    if preserveNames.lower() == 'y' or preserveNames.lower() == 'n':
        break
    else:
        print(f' - -> "{preserveNames}" is not an accepted input.')

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

def newName(filename, index):
    name, extension = os.path.splitext(filename)
    name = name.split('\\')[-1]
    if preserveNames.lower() == 'y':
        return f'{name}_{index}{extension}'
    else:
        return f'{index}{extension}'

for i, file in enumerate(FILES):
    newpath = OUT_PATH + '\\' + str(newName(file, i))
    print(' - Saving: ' + newpath)
    # copy2 to preserve meta data
    shutil.copy2(file, newpath)

print(' - Finished!')
print(' - Output: ' + OUT_PATH)

