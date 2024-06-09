import wikipedia
from fx_ef import context


scrape_query = context.params.get('query')
sentances = context.params.get("sentences")


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


summary = scrape_wikipedia(scrape_query)
if summary:
    context.events.send(
        event_type="aiflow.rag.extractor.start",
        event_source="aiflow.rag.wikipediascraper",
        data={
            "summary": str(summary)
        }
    )
