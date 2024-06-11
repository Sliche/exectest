import mwclient
import wikipedia
import requests
import datetime
from fx_ef import context

category_name = context.params.get('category')
max_records = context.params.get('maxrecords')


def get_last_modified(page):
    try:

        # Define the API endpoint
        endpoint = "https://en.wikipedia.org/w/api.php"

        # Define parameters for the API request
        params = {
            "action": "query",
            "prop": "revisions",
            "titles": page.title,
            "rvlimit": 1,
            "rvprop": "timestamp",
            "format": "json"
        }

        # Make the API request
        response = requests.get(endpoint, params=params)
        data = response.json()

        # Extract the timestamp of the last revision
        page_data = next(iter(data['query']['pages'].values()))
        revisions = page_data.get('revisions', [])
        if revisions:
            timestamp = revisions[0]['timestamp']
            last_modified = datetime.datetime.strptime(timestamp, '%Y%m%d%H%M%S')
            return last_modified
        else:
            print(f"No revision information found for page '{page.title}'.")
            return None
    except wikipedia.exceptions.PageError:
        print(f'Page "{page.title}" does not exist on Wikipedia.')
        return None
    except wikipedia.exceptions.DisambiguationError as e:
        print(f'Page "{page.title}" is ambiguous. Choose one of the following options:')
        print(e.options)
        return None


def get_category_pages(category_name):
    try:
        site = mwclient.Site('en.wikipedia.org')
        category = site.Categories[category_name]
        pages = category.members()
        return [page.name for page in pages]
    except mwclient.errors.InvalidCategoryName:
        print(f'Category "{category_name}" does not exist on Wikipedia.')
        return []
    except mwclient.errors.MWApiError as e:
        print(f'Error retrieving pages for category "{category_name}": {e}')
        return []


pages = get_category_pages(category_name)
for page in pages:
    if page.startswith("Category:"):
        print(page)
    else:
        page_object = wikipedia.page(page, auto_suggest=False)
        last_revision = get_last_modified(page_object)

        data = {"metadata": {}, "url": page_object.url, "timestamp": str(last_revision), "collection": "wikipedia"}
        context.events.send(
            event_type="aiflow.rag.extractor.start",
            event_source="aiflow.rag.wikipediascraper",
            data=data
        )
