import wikipedia

wikipedia.set_lang("de")

def get_first_paragraph(title):
    try:
        # Fetch the Wikipedia page
        page = wikipedia.page(title)
        
        # Extract the first paragraph
        first_paragraph = page.content.split('\n')[0]
        
        return first_paragraph
    except wikipedia.exceptions.PageError:
        return "Page not found"
    except wikipedia.exceptions.DisambiguationError:
        return "Disambiguation page found"

# Specify the Wikipedia article title
article_title = "Pessach"

# WENN kein Feiertag (holiday = []), DANN random article

# Call the function to get the first paragraph
first_paragraph = get_first_paragraph(article_title)

# Print the result
print(first_paragraph)
