from analyzer import *
from args import get_arguments

def main():
    args = get_arguments()
    fs = scan_path(args.path)

    if args.d or (not args.f and not args.d):
        dirs = sort(args.s, fs.directories, args.r)
        print("### Directory sizes: ###")
        for dir in dirs:
            if dir.size == 0 or dir.size < (args.m * 1024 * 1024):
                continue
            
            print(f"{convert_size(dir.size)} - {dir.name}")

    if args.f or(not args.f and not args.d):
        files = sort(args.s, fs.files, args.r)
        print("\n### File sizes: ###")
        for file in files:
            if file.size == 0 or file.size < (args.m * 1024 * 1024) or (args.ext and file.name.split(".")[-1] not in args.ext):
                continue

            print(f"{convert_size(file.size)} - {file.name}")

if __name__ == "__main__":
    main()
