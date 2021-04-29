import os
import shutil
import argparse

# win10 screen lock version

src = os.path.expanduser(
    "~\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets")

dst = os.path.expanduser("~\Pictures\Saved Pictures\lock")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dst', help='dst path', type=str, default=dst)
    args = parser.parse_args()

    dst = args.dst

    if not os.path.exists(dst):
        os.mkdir(dst)

    # remove duplicate filename
    srcFilenames = set(os.listdir(src))
    dstFilenames = os.listdir(dst)
    dstFilenames = [filename.replace('.jpg', '') for filename in dstFilenames]
    dstFilenames = set(dstFilenames)
    lackFilenames = srcFilenames - dstFilenames

    # copy file
    for filename in lackFilenames:
        srcFile = os.path.join(src, filename)
        dstFile = os.path.join(dst, filename)+'.jpg'
        shutil.copyfile(srcFile, dstFile)
