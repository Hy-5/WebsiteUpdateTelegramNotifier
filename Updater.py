import subprocess
necessaryImports = []




def main():
    for i in necessaryImports:
        try:
            __import__(i)
        except ImportError:
            print(f"{i} missing. Installing {i} now")
    return


if __name__=='__main__':
    main(sys.argv[1:])