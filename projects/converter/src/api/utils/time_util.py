from time import time
from typing import Union

def get_time(seconds_precision: bool =True) -> Union[int, float]:
    return time() if not seconds_precision else int(time())
