from dataclasses import dataclass
from time import sleep

@dataclass
class urls:
    url_list = [
        'https://www.wikipedia.org/',
        'https://www.reddit.com/',
        'https://www.target.com/',
    ]

class nums:
    num_executions: int = 3
    num_nodes: int = 1

class time_altered:
    time_buffer = sleep