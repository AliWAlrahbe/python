import argparse
from pathlib import Path

#preparing args path and keywords
def parse_arg():
    parser = argparse.ArgumentParser(
        description="Parse a logfile and search for given keywords."
    )
    parser.add_argument(
        "logfile",
        type=Path,
        help="Path to the log file",
    )
    parser.add_argument(
        "keywords",
        nargs="+",
        help="Keywords to search for in the log file",
    )
    return parser.parse_args()

def main():
    args = parse_arg()
    if not args.logfile.exists() or not args.logfile.is_file():
        print(f"[ERROR] File does not exist: {args.logfile}")
        return 1

    match_count = {}
    for item in args.keywords:
        match_count[item.lower()] = 0

    reporttext="report.txt"
    with open(args.logfile, "r") as in_file, open(reporttext, "w") as out_file:
        #read line by line to save ram
        for lineNumber, line in enumerate(in_file, start=1):
            cols = line.split()
            if len(cols) < 2:
                continue

            for cell in cols:
                key = cell.lower().strip(".,:;!?()[]{}\"'")
                if key in match_count:
                    match_count[key] += 1
                    report_line = (
                        f"line # {lineNumber} {cols[0]} -- {cols[1]} match: {key}\n"
                    )
                    #write directly to the file not store the results in ram
                    out_file.write(report_line)
        #print the dict that has the total of keywords found            
        out_file.write(str(match_count) + "\n")
               
    print("The report is ready in: ", reporttext)

if __name__ == "__main__":
    main()
