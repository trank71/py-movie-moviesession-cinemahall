from django.db.models import QuerySet

from db.models import Movie


@property
def get_movie(
        genres_ids: list[int] = None
        , actors_ids: list[int] = None
) -> QuerySet:
    if genres_ids and actors_ids:
        return Movie.objects.filter(
            genre__id__in=genres_ids,
            actor__id__in=actors_ids)
    if genres_ids:
        return Movie.objects.filter(
            genre_id__in=genres_ids
        )
    if actors_ids:
        return Movie.objects.filter(
            actor_id__in=actors_ids
        )
    return Movie.objects.all()


@property
def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


@property
def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
    return movie
