import os
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

#file_path = os.path.join(sys.path[0], 'referat.txt')
file_path = 'referat.txt'
with open(file_path, 'r', encoding='utf-8') as f:
    stripped_linet = [len(line.strip().split(' ')) for line in f]

print(sum(stripped_linet))
