from typing import List, Dict
from .rssfeed import RssFeed




# For next time, actually send the parsed output to the front. Execute RSS Feed in the translation layer and send the output [via GET request]
def get_podcast_episodes(rss_url:str) -> Dict:
    rs = RssFeed()
    
    return rs.parse(rss_url)


