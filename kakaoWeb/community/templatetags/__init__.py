from django import template
from typing import re
# 유효한 tag library 만들기 위한 모듈 레벨의 인스턴스 객체
register = template.Library()

# template에서 사용할 사용자 정의 필터
@register.filter
def add_link(value):
    # 전달된 value 객체의 content 멤버 변수 가져옴.
    content = value.content
    # 전달된 value 객체의 tag_set 전체를 가져오는 query set을 리턴
    tags = value.tag_set.all()

    # tags를 순회하며 content 내에서 해당 문자열을 링크를 포함한 문자열로 replace
    for tag in tags:
        # re.sub(정규표현식, 대상문자열, 치환문자)

        content = re.sub(r'\#'+tag.name+ r'\b', '<a href="/post/explore/tags/'+tag.name+'">#'+tag.name+'</a>', content)
        return content

