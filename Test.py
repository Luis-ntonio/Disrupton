import ffmpeg
import os
from random import randint

def main():
    for root, dirs, files in os.walk("./Videos", topdown=False):
        for name in files:
            folder = name.split(".")[0].split("_")[0]
            try:
                os.mkdir(os.path.join('./Data/train', folder))
                dirs.append(folder)
                number = 0
            except:
                number = 0
                for root_, dirs_, files_ in os.walk(f"./Data/train/{folder}", topdown=False):
                    for name_ in files_:
                        file_num = name_.split(".")[0].split("_")[1]
                        if number < int(file_num):
                            number = int(file_num)
            ffmpeg.input(os.path.join(root,name)).filter('fps', fps='10').output(f"./Data/train/{folder}/{folder}_%d.jpg", start_number=number).overwrite_output().run(quiet=True)

    for root, dirs, files in os.walk("./Data/train", topdown=False):
        for dir in dirs:
            videos = []
            for root_, dirs_, files_ in os.walk(f"./Data/train/{dir}", topdown=False):
                test = int(len(files_)*0.2)
                valid = int(len(files_)*0.1)
                for _ in range(test):
                    idx = randint(0, len(files_) - 1)
                    tmp = files_[idx]
                    while tmp in videos:
                        idx = randint(0, len(files_) - 1)
                        tmp = files_[idx]
                    videos.append(tmp)
                    folder = tmp.split(".")[0].split("_")[0]
                    try:
                        os.mkdir(os.path.join('./Data/test', folder))
                    except:
                        pass
                    os.replace(f"./Data/train/{folder}/{tmp}", f"./Data/test/{folder}/{tmp}")    
                for _ in range(valid):
                    idx = randint(0, len(files_) - 1)
                    tmp = files_[idx]
                    while tmp in videos:
                        idx = randint(0, len(files_) - 1)
                        tmp = files_[idx]
                    videos.append(tmp)
                    folder = tmp.split(".")[0].split("_")[0]
                    try:
                        os.mkdir(os.path.join('./Data/valid', folder))
                    except:
                        pass
                    os.replace(f"./Data/train/{folder}/{tmp}", f"./Data/valid/{folder}/{tmp}")    

if __name__ == "__main__":
    main()