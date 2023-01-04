import spacy
nlp = spacy.load('en_core_web_md')

hulk_description_raw = "Will he save the world or destroy it? When the Hulk \
                        becomes too dangerous for the Earth, the Illuminati \
                        trick Hulk into a shuttle and launch him into space to \
                        a planet where the Hulk can live in peace. Unfortunately, \
                        Hulk land on the planet Sakaar where he is sold into \
                        slavery and trained as a gladiator."


hulk_description_nlp = nlp(hulk_description_raw)

def movie_rec(hulk_description_nlp):
    with open("movies.txt", "r") as f:
        # Split each movie into list elements
        movie_list = f.read().splitlines()

        # Establish empty movie string variable to return, & max_similarity
        # variable to establish max value
        movie = ""
        max_similarity = 0

        # For each movie in list, establish similarity value. Then establish
        # max similarity, then returns that movie
        for each_movie in movie_list:
            similarity = nlp(each_movie).similarity(hulk_description_nlp)
            if similarity > max_similarity:
                max_similarity = similarity
                movie = each_movie
        return movie
            
print(f"\n\033[91m\033[1mWhat to watch next...\033[0m")
print(movie_rec(hulk_description_nlp) + "\n")