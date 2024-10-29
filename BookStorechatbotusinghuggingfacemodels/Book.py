import re
class Bookhandle:
    def book_query(query,books_data):
        
        date_pattern = r'\b\d{4}-\d{2}-\d{2}\b'
        year_pattern = r'\b\d{4}\b'
        date_match = re.search(date_pattern, query)
        year_match = re.search(year_pattern, query)

        if date_match:
            query_date = date_match.group()
            result = [book for book in books_data if book['published_date'] == query_date]
            if result:
                return f"Books published on {query_date}:\n" + "\n".join(
                    f"- '{book['book_title']}' by {book['author']}" for book in result
                )
            else:
                return f"No books found for the given date: {query_date}."

        elif year_match:
            query_year = year_match.group()
            result = [book for book in books_data if book['published_date'].startswith(query_year)]
            if result:
                return f"Books published in {query_year}:\n" + "\n".join(
                    f"- '{book['book_title']}' by {book['author']}" for book in result
                )
            else:
                return f"No books found for the year: {query_year}."


        normalized_query = query.lower()

        for book in books_data:
            if book['book_title'].lower() in normalized_query:
                return f"{book['book_title']} is written by {book['author']}."
        
        for book in books_data:
            if book['author'].lower() in normalized_query:
                return f"The book '{book['book_title']}' is written by {book['author']}."

        return f"No results found for your query: '{query}'."