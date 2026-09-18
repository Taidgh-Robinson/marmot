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