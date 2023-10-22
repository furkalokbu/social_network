from dj_rql.filter_cls import RQLFilterClass
from apps.posts.models import Post


class PostsFilters(RQLFilterClass):
    MODEL = Post
    SELECT = True
    FILTERS = (
        {
            'filter': 'updated_at',
            'ordering': True,
        },
        {
            'filter': 'author',
            'sources': {'author__username'},
            'ordering': True,
        }
    )
