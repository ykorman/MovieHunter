from release_date import get_release_date
from playlist_read import get_playlist

import re

def title_sanitize(title):
    match = re.match(r"^[A-Za-z0-9 ]*", title)
    if match:
        title = match.group(0)
    title = title.replace(" trailer","")
    title = title.replace(" Trailer", "")
    return title

def main():
    playlist_id = "PLprHQa_hvwWq-zygEzKtNVGmMAeoNc3b8"

    titles = get_playlist(playlist_id)

    for title in titles:
        title = title_sanitize(title)
        release_date = get_release_date(title)
        if release_date != None:
            print(f"release date for \"{title}\" is \"{release_date}\"")
        else:
            print(f"release date for \"{title}\" not found 😢")

if __name__ == "__main__":
    main()