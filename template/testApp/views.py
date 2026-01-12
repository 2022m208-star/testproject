from django.shortcuts import render

def index(request):
    if request.method == "POST":
        pass  # 何もしなくてOK（CSRF確認用）
    context = {
        'title': 'こんにちわ、Django',
        'message': "<script>alert('ハッキング成功！');</script>",
        'food_list': ['リンゴ', 'ラーメン', 'カレー'],
    }
   return render(request, 'testApp/index.html', context)
# Create your views here.
