def main():
    searchList = ["ERROR", "Failed"]  # case-insensitive search terms
    match_count = {}
    for item in searchList:
        match_count[item.lower()] = 0
    report_file = []

    with open("app.log", "r") as in_file:
        for lineNumber, line in enumerate(in_file, start=1):
            cols = line.split()
            if not cols:
                continue

            for cell in cols:
                # Normalize token so matching works with mixed case and trailing punctuation.
                key = cell.lower().strip(".,:;!?()[]{}\"'")
                if key in match_count:
                    match_count[key] += 1
                    report_line = f"line # {lineNumber} time: {cols[0]} date: {cols[1]} match: {key}\n"
                    report_file.append(report_line)

    # First line in report: summary counts. Remaining lines: matched entries.
    with open("report.txt", "w") as out_file:
        out_file.write(str(match_count) + "\n")
        out_file.write("".join(report_file))

if __name__ == "__main__":
    main()
