import re


if __name__ == "__main__":

    number_of_matched_requests = 0
    pattern = r"21\S+\s-\s-\s\S+\s\S+\s\S+\s+\S+(?:php)(?:[A-za-z0-9 \S]+)"
    read_lines = 0

    with open("log") as file:
        for line in file:
            read_lines += 1
            if re.match(pattern, line):
                number_of_matched_requests += 1
                print(re.findall(pattern, line))

    print("\nNumber of all read lines: %d" % read_lines)
    print("\nNumber of all requests starting with 21 and containing php: %d" % number_of_matched_requests)
