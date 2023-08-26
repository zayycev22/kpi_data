import re
import pandas as pd
from datetime import datetime
from tqdm import tqdm
from sklearn.metrics import mean_absolute_error
import numpy as np


class TgRegexp:
    ANCHOR_WORDS = ["vr", "вовлеченность подписчиков", "средний охват", "average reach"]
    PATTERN = r'(\d+\.\d+)\s*%'
    PATTERN2 = r'([\d.]+(?:%)?)'

    def __init__(self, text: str):
        self.text = text.lower().split()

    @staticmethod
    def is_valid_date(date_string, format='%d.%m.%Y'):
        try:
            datetime.strptime(date_string, format)
            return True
        except ValueError:
            return False

    def _cut_text(self) -> str:
        validate_text = " ".join(self.text)
        for word in self.ANCHOR_WORDS:
            if word in self.text:
                idx = self.text.index(word)
                validate_text = " ".join(self.text[idx:])
        return validate_text

    @staticmethod
    def compare(res1: list, res2: list) -> tuple[list, dict]:
        answer = []
        tagged_dict = {}
        if len(res1) == 0:
            answer2 = []
            for res in res2:
                if res[-1] == "%":
                    res = res[:-1]
                    answer2.append(res)
            return answer2, tagged_dict
        for res in res2:
            if res[-1] == "%":
                res = res[:-1]
                tagged_dict[res] = True
            if res in res1:
                if res not in tagged_dict:
                    tagged_dict[res] = False
                answer.append(res)
        return answer, tagged_dict

    @staticmethod
    def get_answer(answer, tags) -> list:
        for tag in tags:
            if tag in answer and not tags[tag]:
                answer.remove(tag)
        return answer

    def parse_text(self) -> str:
        text = self._cut_text()
        res1 = re.findall(self.PATTERN, text)
        res2 = re.findall(self.PATTERN2, text)
        if len(res1) >= 3:
            return res1[-1]
        compared, tags = self.compare(res1, res2)
        answer = self.get_answer(compared, tags)
        idx = len(answer) // 2 - 1
        print(answer)
        if len(answer) > 0:
            return answer[idx]
        res2_idx = len(res2) // 2 - 1
        return res2[res2_idx]

    def parse_text2(self) -> str:
        text = self._cut_text()
        res = re.findall(self.PATTERN2, text)
        return " ".join(res)


if __name__ == '__main__':
    df = pd.read_csv("image_dataset.csv")
    tg_df = df[df['platform'] == 1]
    answers = []
    texts = tg_df['text'].tolist()
    for text in tqdm(texts):
        rg = TgRegexp(text)
        answers.append(rg.parse_text())
    answers = np.array(answers)
    for i in range(len(answers)):
        if answers[i] == '..':
            print(i, "index")
    print(mean_absolute_error(tg_df['y'].tolist(), answers.astype(float)))
    # print()
