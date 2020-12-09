import os


def main():
    print("ENVIRONMENT VARIABLES: \n")

    for i,j in os.environ.items():
        print(f'{i} = {j}')


if __name__ == "__main__":
    main()
