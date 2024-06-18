#!/usr/bin/env python3

# Add all the urls:
UrlList = [
       'https://web.telegram.org/k/#@herewalletbot',        # UrlList[0]
       'https://web.telegram.org/k/#@catizenbot',           # UrlList[1]
       'https://web.telegram.org/k/#@nearharvestmoonbot',   # UrlList[2]
       'https://web.telegram.org/k/#@gamee',                # UrlList[3]
      ]

# Add new users and specify url by creating new entries in the list below:
ProfileList = [
               # Telegram User 1
               ('User1', UrlList[0]), # Website 1
               ('User1', UrlList[1]), # Website 2
               ('User1', UrlList[2]), # Website 3
               ('User1', UrlList[3]), # Website 4
               # Telegram User 2
               ('User2', UrlList[0]),
               ('User2', UrlList[2]),
               # Telegram User 3
               ('User3', UrlList[0]),
               ('User3', UrlList[2]),
               # Telegram User 4
               ('User4', UrlList[0]),
               ('User4', UrlList[2]),
              ]

# Window position Configuration
Size = [315,450] # Windows size (width, height)
Position = [0,34] # First window position (x-left, y-top)
MarginLeft = 1 # Margin between windows left side
MarginTop = 70 # Margin between windows top side
