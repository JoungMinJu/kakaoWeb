from django.shortcuts import render, redirect, get_object_or_404
from .models import Community, Comment, Like
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .filters import CommunityFilter
from django.db.models import Count
from django.core.paginator import Paginator
# Create your views here.

def show(request):
    context = {}
    # http request의 정보를 딕셔너리 데이터로 받는 기능.
    # request.GET이 아니라 request.GET.get을 사용하면 value값이 없는 경우 ''를 발생시킨다.
    sort = request.GET.get('sort','')
    if sort == 'likes':
        filtered_community = CommunityFilter(
            queryset=Community.objects.all().annotate(likes=Count('like_user_set')).order_by('-likes')
        )
    elif sort == 'views':
        filtered_community  = CommunityFilter(
            queryset=Community.objects.order_by('-view_count')
        )
    else:
        filtered_community = CommunityFilter(
            request.GET,
            queryset=Community.objects.order_by('-pub_date')
        )
    context['filtered_community'] = filtered_community

    paginated_filtered_persons = Paginator(filtered_community.qs, 7)
    page_number = request.GET.get('page')
    person_page_obj = paginated_filtered_persons.get_page(page_number)

    context['person_page_obj'] = person_page_obj
    return render(request, 'show.html', context=context)


def detail(request, id):
    community = get_object_or_404(Community, id=id)
    all_comments = community.comments.order_by('-created_at')
    community.view_count +=1
    community.save()
    return render(request, 'detail.html', {'community':community, 'comments':all_comments})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_community = Community()
    new_community.title = request.POST['title']
    new_community.writer = request.user
    new_community.pub_date = timezone.now()
    new_community.body = request.POST['body']
    new_community.image = request.FILES.get('image')
    new_community.category = request.POST['category']
    new_community.save()
    return redirect('community:detail', new_community.id)

def edit(request, id):
    edit_community = Community.objects.get(id = id)
    return render(request, 'edit.html', {'community': edit_community})

def update(request, id):
    update_community = Community.objects.get(id = id)
    update_community.title = request.POST['title']
    update_community.writer = request.user
    update_community.pub_date = timezone.now()
    update_community.body = request.POST['body']
    update_community.image = request.FILES.get('image')
    update_community.category = request.POST['category']
    update_community.save()
    return redirect('community:detail', update_community.id)

def delete(request, id):
    delete_community = Community.objects.get(id = id)
    delete_community.delete()
    return redirect('community:show')

def create_comment(request, community_id):
    if request.method == "POST":
        community = get_object_or_404(Community, pk=community_id)
        current_user = request.user
        comment_content = request.POST.get('content')
        Comment.objects.create(content=comment_content, writer=current_user, community=community)
    return redirect('community:detail', community_id)

def update_comment(request, comment_id):
    comment=get_object_or_404(Comment, pk=comment_id)
    if request.method == "POST":
        community_id = comment.community.id
        comment.content=request.POST.get('content')
        comment.save()
        return redirect('community:detail', community_id)
    return render(request, 'update_comment.html',{"comment":comment})

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    community_id = comment.community.id
    comment.delete()
    return redirect('community:detail', community_id)

@login_required
def community_like(request, community_id):
    community = get_object_or_404(Community, pk=community_id)

    #좋아요 확인
    if request.user in community.like_user_set.all():
        community.like_user_set.remove(request.user)
    else:
        community.like_user_set.add(request.user)

    if request.GET.get('redirect_to')=='detail':
        return redirect('community:detail', community_id)
    else:
        return redirect('community:show')