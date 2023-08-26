# Disk Analyzer
Disk Analyzer to that analyzes and manages the file system in a directory that is able to:
- Scan largest files and folders
- Scan oldest files and folders
- Scan duplicates
- Search and delete files and folders
- Group files by type, extension and date
- Visual representation of a directory

### Examples

Getting all directories and files in the current directory:
```
> python main.py .        
    ### Directory sizes: ###
    1.07 KB - .git
    4.97 KB - __pycache__

    ### File sizes: ###
    317.0 B - README.md
    612.0 B - utils.py
    773.0 B - args.py
    896.0 B - main.py
    912.0 B - classes.py
    1.24 KB - analyzer.py
    3.16 KB - .gitignore
```

Getting all files in the current directory sorted by name in reverse order
```
> python main.py . -f -s name -r         
    ### File sizes: ###
    612.0 B - utils.py
    896.0 B - main.py
    912.0 B - classes.py
    773.0 B - args.py
    1.24 KB - analyzer.py
    1001.0 B - README.md
    3.16 KB - .gitignore
```

Getting all files in the current directory with the minimum size of 1KB with th .py extension:
```
> python main.py . -f -m 0.001 -ext py 
    ### File sizes: ###
    1.24 KB - analyzer.py
```