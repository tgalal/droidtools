from droidtools import ext4fs

MODE_NORMAL = 0
MODE_SPARSED = 1
MODE_GZIP = 2

def make_ext4fs(filename, directory, length, mountPoint = None, mode = MODE_NORMAL):
    return ext4fs.make_ext4fs(filename, directory, mountPoint or "", str(int(length)), mode)


if __name__ == "__main__":
    make_ext4fs(
        "/home/tarek/.inception/out/suitepad/samsung-matissewifi/inselhof/cache.img",
        "/home/tarek/.inception/work/suitepad/samsung-matissewifi/inselhof/cache",
        314572800,
        "cache",
        MODE_SPARSED
        )

