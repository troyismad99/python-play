import pathlib

def main():

    template = "./leetcode/template/leet_template.py"
    contents = pathlib.Path(template).read_text()
    newfile = "./leetcode/xxxx-xxxx.py"

    with open(newfile, "a") as nf:
        nf.write(contents)


if __name__ == "__main__":
    main()
