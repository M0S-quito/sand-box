import base64
import pandas as pd
import os

class Decoder:
    def __init__(self, encoding="utf-8"):
        self.encoding = encoding
        
    def decode(self, paths):
        decoded_list = []
        for path in paths:
            try:
                with open(path, "rb") as file:
                    base64_string = base64.b64encode(file.read()).decode(self.encoding)
                    decoded_list.append(base64_string)
            except FileNotFoundError:
                print(f"파일을 찾을 수 없습니다: {path}")
            except Exception as e:
                print(f"에러 발생: {e}")
        return decoded_list

# 이거 만드는 중....
class File_Manager:
    def __init__(self,paths):
        self.PATHS=paths
        self.save_files=[]

    def get_file_path(self, folder_path):
        return [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]