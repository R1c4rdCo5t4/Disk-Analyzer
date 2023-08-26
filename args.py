import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description="Disk Analyzer")
    parser.add_argument("path", type=str, help="Path to the directory to analyze")
    parser.add_argument("-m", type=float, default=0, help="Minimum file size to consider (in MB)")
    parser.add_argument("-s", type=str, default="size", help="Sort by size, name or date")
    parser.add_argument("-r", action="store_true", default=False, help="Sort in reverse order")
    parser.add_argument("-f", action="store_true", help="Display only files")
    parser.add_argument("-d", action="store_true", help="Display only folders")
    parser.add_argument("-ext", nargs="+", type=str, help="Filter files by specific extensions")
    return parser.parse_args()

