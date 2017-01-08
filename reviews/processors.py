from .models import Movie
def search_movie(request):
    search_movie = (item for item in Movie.objects.all() if item.review_set.count() >= 225)
    #print len(movie_list)
    return {'search_movie': search_movie}