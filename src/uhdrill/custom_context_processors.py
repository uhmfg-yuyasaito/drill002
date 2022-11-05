# テンプレートで使用する変数などの場合は、各viewに全部記載するとなると冗長になるため
# どのテンプレートでもアクセス・参照できるようにする(viewに記載をしなくても値をTemplateに渡せる)

from django.conf import settings
from base.models import Item


def base(request):
    items = Item.objects.filter(is_published=True)
    return {
        # htmlのタイトル
        'TITLE': settings.TITLE,
        # 関連商品、オススメ商品の表示用
        'ADDTIONAL_ITEMS': items,
        # 人気商品の表示用(一番売れたものが上に来るように)
        'POPULAR_ITEMS': items.order_by('-sold_count')
    }