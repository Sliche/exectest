import wikipedia

def scrape_wikipedia(query, sentences=2):
    try:
        # Use the summary function to get the summary of the Wikipedia page
        summary = wikipedia.summary(query, sentences=sentences)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        # If there are multiple results for the query, print the options
        print("DisambiguationError: There are multiple possible pages. Please be more specific:")
        print(e.options)
        return None
    except wikipedia.exceptions.PageError as e:
        # If the query doesn't match any Wikipedia page
        print("PageError: The page does not exist.")
        return None

# Example usage
query = "Web scraping"
summary = scrape_wikipedia(query)
if summary:
    print("Summary of", query, ":", summary)
