from dataclasses import dataclass

@dataclass
class urls:
    main_url: str = 'https://www.wikipedia.org/'
    url_dict = {
        1:'https://www.wikipedia.org/',
        2:'https://www.reddit.com/',
        3:'https://www.peardeck.com/',
    }

class nums:
    retries: int = 1
    max_retries: int = 5
    num_iterations: int = 1
    num_nodes: int = 1
    num_list = [1,2,3,4,5]