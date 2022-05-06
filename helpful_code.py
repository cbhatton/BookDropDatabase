import subprocess


def reset_test_database():
    print("\n\nReloading database....")

    process = subprocess.Popen(["powershell", "..\\RebuildDatabase-local.ps1",
                                "-Server", '"(local)\\SQLEXPRESS"',
                                "-Database", '"cc520"',
                                '-Dir', '..\\src'],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               universal_newlines=True, shell=True)

    for result in process.communicate():
        print(result)

    process.communicate()

    print("done.\n\n")


if __name__ == "__main__":
    reset_test_database()