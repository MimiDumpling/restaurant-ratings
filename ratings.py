def rating_items(file):

    """Restaurant rating lister."""

    restaurant_scores = open(file)

    scores = {}
    


    for line in restaurant_scores:
        line = line.strip()
        tokens = line.split(':')
        restaurant = tokens[0]
        rating = tokens[1] 
        scores[restaurant] = rating
    
    print sorted(scores)

    
rating_items("scores.txt")