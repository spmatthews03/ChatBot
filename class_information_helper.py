

def get_difficulty(class_id, reviews):
    total = 0.0
    num_of_reviews = 0
    for review in reviews:
        if class_id in review['course']:
            total = total+int(review['difficulty'])
            num_of_reviews = num_of_reviews + 1
    return float('%.2f'%(total / num_of_reviews))


def get_rating(class_id, reviews):
    total = 0.0
    num_of_reviews = 0
    for review in reviews:
        if class_id in review['course']:
            total = total+int(review['rating'])
            num_of_reviews = num_of_reviews + 1
    rating = float('%.2f'%(total / num_of_reviews))
    if rating < 2:
        return "This class isn't a favorite. People only give if a {0} out of 5.".format(rating)
    elif 2 <= rating < 4:
        return "{first} has an ok rating. It's rated {second} out of 5.".format(first=class_id, second=rating)
    else:
        return "{first}/5!!!! High rating! I'd recommend taking it!".format(first=class_id, second=rating)


def get_response():
    return "Yes, like I said."


def get_workload(class_id, reviews):
    total = 0.0
    num_of_reviews = 0
    for review in reviews:
        if class_id in review['course']:
            total = total+int(review['workload'])
            num_of_reviews = num_of_reviews + 1
    workload = float('%.2f'%(total / num_of_reviews))
    if workload < 15:
        return "{first} isn't too demanding. The workload is {second}.".format(first=class_id,second=workload)
    elif 15 <= workload < 20:
        return "A workload of {first} isn't too bad, Not too many hours each week for {second}.".format(first=workload,second=class_id)
    else:
        return "{first}... I repeat {first}... That's your workload if you take {second}".format(first=workload, second=class_id)
