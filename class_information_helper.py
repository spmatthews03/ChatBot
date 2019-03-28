from responses import *
def get_difficulty(class_id, reviews):
    return get_response('difficulty', class_id, get_average('difficulty', class_id, reviews))


def get_rating(class_id, reviews):
    return get_response('rating', class_id, get_average('rating', class_id, reviews))


def respond():
    return regular_response()


def get_workload(class_id, reviews):
    return get_response('workload', class_id, get_average('workload', class_id, reviews))


def get_exam_info(class_id, reviews):
    return get_response('tests', class_id, get_average('tests', class_id, reviews))


def get_project_info(class_id, reviews):
    try:
        group_projects = get_average('groupProjects', class_id, reviews)
        projects = get_average('projects', class_id, reviews)
        return get_response('projects', class_id, projects, group_projects)
    except:
        return 'There were no reviews indicating projects'

def get_average(indicator, class_id, reviews):
    total = 0.0
    num_of_reviews = 0
    for review in reviews:
        if class_id in review['course'] and indicator in review.keys() and not isinstance(review[indicator], str):
            total = total + int(review[indicator])
            num_of_reviews = num_of_reviews + 1
    if num_of_reviews != 0:
        return float('%.2f'%(total / num_of_reviews))
    else:
        return None


