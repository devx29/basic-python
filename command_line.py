#command line arguments

def hi(fname, lname):
    msg = f"Hello {fname} {lname}!"
    print(msg)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Provide name")

    parser.add_argument(
        "-n", "--my_name", metavar="my_name",
        required=True, help="Your name!"
    )

    parser.add_argument(
        "-l", "--l_name", metavar="l_name",
        required=True, help="Your l name!"
    )

    args = parser.parse_args()

    hi(args.my_name, args.l_name)