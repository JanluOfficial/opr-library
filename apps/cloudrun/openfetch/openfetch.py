import platform
from rich import print
import os

print(f'[deep_pink3]OS:[/deep_pink3] {platform.uname().system}')
print(f'[deep_pink3]PC Name:[/deep_pink3] {platform.uname().node}')
print()
print(f'[deep_pink3]Platform:[/deep_pink3] {platform.platform()}')
print(f'[deep_pink3]Architecture:[/deep_pink3] {platform.machine()}')
print(f'[deep_pink3]CPU:[/deep_pink3] {platform.processor()}')
print(f'[deep_pink3]CPU Cores:[/deep_pink3] {os.cpu_count()}')
print()
if os.name == "nt":
    print(f'[deep_pink3]Windows Version:[/deep_pink3] Windows {platform.win32_ver()[0]}')
    print(f'[deep_pink3]Build:[/deep_pink3] {platform.win32_ver()[1]}')
    print(f'[deep_pink3]Windows Edition:[/deep_pink3] {platform.win32_edition()}')
    print(f'[deep_pink3]Service Pack:[/deep_pink3] {platform.win32_ver()[2]}')
