"""
うるう年
"""


class MyYear:
    """
    年を保持するClass
    """

    def __init__(self, year: int):
        """初期化"""
        self.year = year

    def __str__(self) -> str:
        """
        保持しているyearを文字列として返す

        Returns
        -------
        str
            保持しているyearの文字列表現
        """
        return str(self.year)

    def is_leap(self) -> bool:
        """
        うるう年かどうかを判定する

        - 西暦年が4で割り切れる年は(原則として)閏年
        - ただし、西暦年が100で割り切れる年は(原則として)平年。

        Returns
        -------
        bool
            うるう年ならばTrueを返し、それ以外ならばFalseを返す
        """
        if self.year % 100 == 0:
            return False
        return self.year % 4 == 0
