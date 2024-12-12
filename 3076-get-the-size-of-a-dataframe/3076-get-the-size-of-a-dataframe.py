import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List:
    return [*players.shape]