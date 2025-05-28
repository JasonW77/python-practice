import feedparser

def fetch_python_news():
    feed_url = "https://realpython.com/atom.xml"  # Using Real Python's RSS feed
    feed = feedparser.parse(feed_url)

    if not feed.entries:
        print("❌ No news items found. Check the RSS URL or your internet connection.")
        return

    print("\n📰 Latest Python Articles from Real Python:\n")
    for i, entry in enumerate(feed.entries[:5], 1):
        title = entry.get("title", "No Title")
        link = entry.get("link", "No Link")
        published = entry.get("published", "No Date")
        print(f"{i}. {title}\n   🗓️ {published}\n   🔗 {link}\n")

if __name__ == "__main__":
    fetch_python_news()
