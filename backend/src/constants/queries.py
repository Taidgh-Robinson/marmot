# Both of these queries were LLM generated

def generate_crop_query(movie_title: str, movie_quote: str):
    return f"""
        Your job is to act as an expert film archivist. Extract the single most iconic, standalone, and recognizable quote or punchline from the provided movie line. 

        Rules:
        1. Extract ONLY the famous portion. Strip away all narrative filler, conversational back-and-forth, and setup lines UNLESS the entire passage is a single famous monologue.
        2. Do NOT inject dates, names, or phrases that are not inherently part of the core quote just because they appeared in other examples.
        3. Return ONLY the exact text of the cropped quote. No extra explanation, formatting, or quotation marks.
        4. The output must be a complete, self-contained thought or clause. Do not return broken sentence fragments or trailing phrases. 
        ---
        Examples:
        Movie Title: Star Wars: Episode V - The Empire Strikes Back
        Movie Line: Luke, I am so sorry about everything that happened, but you must know that... No, I am your father.
        Cropped: No, I am your father.

        Movie Title: The Godfather
        Movie Line: This Hollywood big shot's gonna give you what you want. Too late. They start shooting in a week. I'm gonna make him an offer he can't refuse. Now just go outside, enjoy yourself... and forget about all this nonsense.
        Cropped: I'm gonna make him an offer he can't refuse.

        ---
        Movie Title: {movie_title}
        Movie Line: {movie_quote}
        """

def generate_score_query(movie_title: str, movie_quote: str):
    return f"""
        You are an expert film archivist and movie quote curator.

        Score the following quote for inclusion in a movie quote application.

        Evaluate ONLY the exact provided quote.

        Scoring dimensions:
        - iconicity: 0-40
        - standalone: 0-20
        - quotability: 0-20
        - movie_specificity: 0-10
        - conciseness: 0-10

        Definitions:

        iconicity:
        How strongly recognized and associated with the movie the quote is.
        Famous, frequently referenced, parodied, or culturally memorable lines score highest.

        standalone:
        Whether the quote makes sense as a complete thought without surrounding dialogue.

        quotability:
        Whether the wording is memorable, distinctive, funny, dramatic, clever, or enjoyable to repeat.

        movie_specificity:
        Whether the quote feels connected to this specific movie, character, or franchise rather than being generic dialogue.

        conciseness:
        Whether the quote contains only meaningful material and works well when displayed independently.

        Important rules:
        - Do not score the fame of the movie itself.
        - Do not substitute another quote from the movie.
        - Do not rewrite or crop the quote.
        - Generic dialogue should receive a low iconicity and movie_specificity score.
        - A short quote can receive a very high score if it is extremely recognizable.
        - The total MUST equal the sum of the five categories.

        Return ONLY valid JSON using exactly this structure:

        {{
            "iconicity": 0,
            "standalone": 0,
            "quotability": 0,
            "movie_specificity": 0,
            "conciseness": 0,
            "total": 0
        }}

        Movie Title: {movie_title}
        Quote: {movie_quote}
        """
