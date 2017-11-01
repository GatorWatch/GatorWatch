from bs4 import BeautifulSoup
import requests
import re

# Show listing object to hold show information
class ShowListing:
    name = ""
    episode_name = ""
    episode = ""
    description = ""
    channel = ""
    time = ""

    def __init__(self, name, episode_name, episode, description, channel, time):
        self.name = name
        self.episode_name = episode_name
        self.episode = episode
        self.description = description
        self.channel = channel
        self.time = time

# Return an array of shows
def scrapeTV(search):
    # Search TV Guide with the given search term
    try:
        r = requests.get("http://www.tvguide.com/search/listings/?keyword=" + search)
    except:
        print("No internet connection")
        return 1

    print("Status:", r.status_code)
    if r.status_code != 200:
        print("Site not available")
        return r.status_code

    # Parse through HTML
    soup = BeautifulSoup(r.text, "html.parser")

    # Isolate the text: find the portion with the main content
    results = soup.find("div", {"class": "content-main"})

    # Get section that contains the search results
    entry_parent = results.find("div", {"class": "search-results-listings"})

    # Get section that contains information about the search results
    children = entry_parent.findAll("div", {"class": "airing section-xs"})


    shows = []  # Hold show_listing objects

    # Iterate through the children to find show information and push information to shows
    for listing in children:

        # Find the show name and episode name
        try:
            name = listing.find("span", {"class": "airing-details-program-title"})
            childs = name.findChildren()
            name = childs[0].text

            # If the name does not contain the search term, ignore the show
            # There may be results without the search term in its title, rather in its description instead
            if not re.search(search, name, re.IGNORECASE):
                continue

            # Try-except necessary here in case the user inputted a movie as a search term
            try:
                episode_name = childs[1].text
            except:
                episode_name = "N/A"
        except:
            name = "N/A"
            episode_name = "N/A"

        # Find episode number
        try:
            episode = listing.find("span", {"class": "airing-details-program-number"}).text
        except:
            episode = "N/A"

        # Extract description of the episode
        try:
            description = listing.find("p", {"class": "airing-details-program-description"}).text
        except:
            description = "N/A"

        # Find channel of episode
        try:
            channel = listing.find("span", {"class": "airing-details-channels"}).text
        except:
            channel = "N/A"

        # Find the show time (day and time)
        try:
            temp = listing.find("span", {"class": "airing-date-date"}).text
            time = temp

            temp = listing.find("span", {"class": "airing-date-time"}).text
            time += " " + temp
        except:
            time = "N/A"

        # Create ShowListing object with the information
        show = ShowListing(name, episode_name, episode, description, channel, time)
        shows.append(show)

    return shows
