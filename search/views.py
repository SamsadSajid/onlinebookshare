from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import redirect, render

from feeds.models import Feed
from mylibrary.models import BookList


@login_required
def search(request):
    if 'q' in request.GET:
        querystring = request.GET.get('q').strip()
        if len(querystring) == 0:
            return redirect('/search/')

        try:
            search_type = request.GET.get('type')
            if search_type not in ['feed', 'books', 'users']:
                search_type = 'feed'

        except Exception:
            search_type = 'feed'

        count = {}
        results = {}
        results['feed'] = Feed.objects.filter(post__icontains=querystring,
                                              parent=None)
        results['books'] = BookList.objects.filter(
            Q(book_title__icontains=querystring) | Q(
                author__icontains=querystring) | Q(
                catagory__icontains=querystring))
        results['users'] = User.objects.filter(
            Q(username__icontains=querystring) | Q(
                first_name__icontains=querystring) | Q(
                    last_name__icontains=querystring))
        count['feed'] = results['feed'].count()
        count['books'] = results['books'].count()
        count['users'] = results['users'].count()

        return render(request, 'search/results.html', {
            'hide_search': True,
            'querystring': querystring,
            'active': search_type,
            'count': count,
            'results': results[search_type],
        })
    else:
        return render(request, 'search/search.html', {'hide_search': True})
