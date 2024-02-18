from rpsls import rpsls

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Provide name")

    parser.add_argument(
        "-n", "--my_name", metavar="my_name",
        required=True, help="Your name!"
    )

    args = parser.parse_args()

    rpsls(args.my_name)