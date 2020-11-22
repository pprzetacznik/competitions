import os
import sys
from subprocess import Popen, PIPE
import time


def test_program(program_name, test_file):
    print("* Testing: %s.in" % test_file)
    test_file_in = open("./%s/%s.in" % (program_name, test_file))
    with open("./%s/%s.out" % (program_name, test_file)) as test_file_out:
        test_file_out_data = test_file_out.read()

    time1 = time.time()

    p = Popen("./%s.out" % program_name, stdin=test_file_in, stdout=PIPE)
    stdout, stderr = p.communicate()

    stdout = stdout.decode()
    if stdout.rstrip() == test_file_out_data.rstrip():
        print("  * OK [%0.3fs]" % (time.time() - time1))
    else:
        print("  * Failure")
        print("    ######## Expected ########")
        print(test_file_out_data.rstrip())
        print("    ######## Received ########")
        print(stdout.rstrip())
        print("    ##########################")


def main(program_name):
    path = "./" + program_name
    files = os.listdir(path)
    selected_files = filter(lambda x: x.endswith(".in"), files)
    selected_files_in = [os.path.splitext(x)[0] for x in selected_files]
    for test_file in selected_files_in:
        test_program(program_name, test_file)


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        program_name = sys.argv[1]
        main(program_name)
    else:
        print("Usage: %s [program_name]" % sys.argv[0])
