import os
import shutil
import argparse

# lenovo screen lock version

src = "C:\ProgramData\Lenovo\devicecenter\LockScreen\cache"

dst = os.path.expanduser("~\Pictures\Saved Pictures\lock")


def get_filelist(dir, extract):
    filelist = []
    filenames = os.listdir(dir)
    for filename in filenames:
        ext = os.path.splitext(filename)[-1]
        if ext == extract:
            filelist.append(filename)
    return filelist


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dst', help='dst path', type=str, default=dst)
    parser.add_argument('-s', '--src', help='src path', type=str, default=src)
    args = parser.parse_args()

    dst = args.dst
    src = args.src

    if not os.path.exists(src):
        exit("src path not found")

    if not os.path.exists(dst):
        os.mkdir(dst)

    # ignore zip
    srcFilenames = set(get_filelist(src, '.jpg'))
    dstFilenames = set(os.listdir(dst))
    # remove duplicate filename
    lackFilenames = srcFilenames - dstFilenames

    # copy file
    for filename in lackFilenames:
        srcFile = os.path.join(src, filename)
        dstFile = os.path.join(dst, filename)
        shutil.copyfile(srcFile, dstFile)
