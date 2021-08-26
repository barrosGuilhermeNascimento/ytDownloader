import subprocess
import os

class youtubeDownloader:
    def __init__(self) -> None:
        pass

    def downloadByUrl(self, url: str, dirPath: str):
        self.execute(url, dirPath)
        print("downloaded")
        return


    def execute(self, options: str, dirPath: str):
        try:
            print(os.getcwd())
            dir_path = dirPath
            print(dir_path)
            executeString = dir_path + "/youtube-dl.exe " + options
            print(executeString)
            os.system(executeString)
            # proc = subprocess.Popen(executeString, stdin = subprocess.PIPE, stdout = subprocess.PIPE)
            # print(proc)
            return
        except Exception as err:
            print(err)
            return
