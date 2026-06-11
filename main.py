import os
import sys
import glob
import argparse
import importlib
from transformregistry import transforms

'''
Transform manager. Actually loads and runs all transforms.
'''

if __name__ == '__main__':
    print(f'loading transforms')
    
    scriptdir = os.path.dirname(__file__)
    transform_dir = os.path.join(scriptdir, 'transforms')
    
    sys.path.append(transform_dir)
    for file in glob.glob('*.py', root_dir=transform_dir):
        importlib.import_module(os.path.splitext(os.path.basename(file))[0])
    
    parser = argparse.ArgumentParser()
    
    for transform_ in transforms:
        parser.add_argument(transform_.disableFlag, action='store_true', help=f'Disables the "{transform_.name}" transform.')
        
    parser.add_argument('INFILE', help='G-code file to transform.')
    parser.add_argument('--outfile', '-o', help='G-code file to write output to. Defaults to input file.', default=None, required=False)
        
    args = parser.parse_args()
    
    lines = []
    print(f'reading {args.INFILE}')
    with open(args.INFILE, 'r') as f:
        lines = f.readlines()
        
    print(f'read {len(lines)} lines')
    
    for transform_ in transforms:
        if not getattr(args, transform_.disableFlag.removeprefix('-'), False):
            lines = transform_.func(lines)
            
    output_file = args.outfile or args.INFILE
    print(f'writing {len(lines)} lines to {output_file}')
    with open(output_file, 'w') as f:
        f.write(''.join(lines))