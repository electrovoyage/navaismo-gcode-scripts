'''
Move Creality Print's info section of the file to the bottom and add OrcaSlicer spoofing.
'''

from transformregistry import transform

@transform('Move info footer + OrcaPrint spoof', disableFlag='-norcafooter')
def footer(file: list[str]) -> list[str]:
    # First, find "; EXECUTABLE_BLOCK_END"
    startindex = None
    endindex = None
    for index, line in enumerate(file):
        if line.strip().upper().startswith('; EXECUTABLE_BLOCK_END'):
            startindex = index + 1
            break
        
    if not startindex:
        print(f'warning: could not locate footer start')
        return file
    
    # then, find "; CONFIG_BLOCK_START"
    for index, line in enumerate(file):
        if line.strip().upper().startswith('; CONFIG_BLOCK_START'):
            endindex = index - 1
            break
        
    if not endindex:
        print(f'warning: could not locate footer end')
        return file
    
    return ["; OrcaSlicer (Orca Slicer) spoof\n"] \
        + file[0:startindex] \
        + file[endindex:] \
        + file[startindex:endindex]