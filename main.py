from analyzer import *
import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description="Disk Analyzer")
    parser.add_argument("path", type=str, help="Path to the directory to analyze")
    parser.add_argument("--m", type=int, default=0, help="Minimum file size to consider (in MB)")
    parser.add_argument("--r", action="store_true", default=False, help="Sort file/folder sizes in reverse order")
    parser.add_argument("--f", action="store_true", help="Display only file sizes")
    parser.add_argument("--d", action="store_true", help="Display only folder sizes")
    parser.add_argument("--ext", nargs="+", type=str, help="Filter files by specific extensions")
    return parser.parse_args()


def main():

    args = get_arguments()
    fs = get_dir_size(args.path)

    if args.d:
        dir_sizes = sort_dict(fs.directories, args.r)
        print("### Directory sizes: ###")
        for dir_name, dir_size in dir_sizes.items():
            if dir_size == 0 or dir_size < (args.m * 1024 * 1024):
                continue
            
            print(f"{convert_size(dir_size)} - {dir_name}")

    if args.f:
        file_sizes = sort_dict(fs.files, args.r)
        print("\n### File sizes: ###")
        for file_name, file_size in file_sizes.items():
            if file_size == 0 or file_size < (args.m * 1024 * 1024) or (args.ext and file_name.split(".")[-1] not in args.ext):
                continue

            print(f"{convert_size(file_size)} - {file_name}")



if __name__ == "__main__":
    main()


