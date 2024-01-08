"""
    Module name :- score
    Method(s) :- score()
"""


import os


def score():
    dir_path = os.listdir()

    # print(dir_path)

    for folder in dir_path:
        path = os.path.join(folder, "solution.py")

        if "math" in path:
            os.system("python3 " + path)


if __name__ == "__main__":
    score()
