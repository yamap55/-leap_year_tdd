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

    def isLeap() -> bool:
        """
        うるう年かどうかを判定する

        Returns
        -------
        bool
            うるう年ならばTrueを返し、それ以外ならばFalseを返す
        """
        pass
