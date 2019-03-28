

def get_response(indicator, class_id, value, *args):

    switcher = {
        'difficulty': difficulty_response(class_id, value),
        'rating': rating_response(class_id, value),
        'workload': workload_response(class_id, value),
        'tests': exam_response(class_id, value),
        'projects': project_response(class_id, value, *args)
    }



    return switcher.get(indicator)



def difficulty_response(class_id, val):
    return True


def rating_response(class_id, val):
    if val < 2:
        return "This class isn't a favorite. People only give if a {0} out of 5.".format(val)
    elif 2 <= val < 4:
        return "{first} has an ok rating. It's rated {second} out of 5.".format(first=class_id, second=val)
    else:
        return "{second}/5!!!! High rating! I'd recommend taking it!".format(first=class_id, second=val)

def workload_response(class_id, val):
    if val < 15:
        return "{first} isn't too demanding. The workload is {second}.".format(first=class_id,second=val)
    elif 15 <= val < 20:
        return "A workload of {first} isn't too bad, Not too many hours each week for {second}.".format(first=val,second=class_id)
    else:
        return "{first}... I repeat {first}... That's your workload if you take {second}".format(first=val, second=class_id)


def exam_response(class_id, val):
    if val.is_integer():
        return 'Reviews are unanimous! There are {first} tests in {second}'.format(first=val, second=class_id)
    else:
        return "People couldn't make up their mind! {first} has approximately {second} tests.".format(first=class_id,second=val)

def project_response(class_id, val, *args):
    if args[0] is None:
        return "There are {0} projects".format(val)
    else:
        return "There are {first} projects, and also {second} group projects".format(first=val, second=args)


def regular_response():
    return 'yes, like I said'