from django.views.generic import CreateView, UpdateView, TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from base.models import Profile, UserActivateTokens
from base.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
 
 
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = '/login/'
    template_name = 'pages/signup.html'
    
    #フォームが有効の場合の処理
    def form_valid(self, form):
        messages.success(self.request, '入力したメールアドレスにメールを送信しました。')
        return super().form_valid(form)


# token認証とユーザーアクティベーション
class AccountActivateView(TemplateView):
    template_name = 'pages/activate.html'
 
    def get_context_data(self, activate_token,**kwargs):
        context = super().get_context_data(**kwargs)
        activated_user = UserActivateTokens.objects.activate_user_by_token(
        activate_token)
        if hasattr(activated_user, 'is_active'):
            if activated_user.is_active:
                context["message"] ='ユーザーのアクティベーションが完了しました'
            if not activated_user.is_active:
                context["message"] = 'アクティベーションが失敗しています。管理者に問い合わせてください'
        if not hasattr(activated_user, 'is_active'):
            context["message"] = 'エラーが発生しました'
        return context
 
class Login(LoginView):
    template_name = 'pages/login.html'
 
    #フォームが有効の場合の処理
    def form_valid(self, form):
        messages.success(self.request, 'ログインしました。')
        return super().form_valid(form)
 
    #フォームが無効の場合の処理
    def form_invalid(self, form):
        messages.error(self.request, 'ログイン出来ませんでした。ユーザー名、パスワードを確認してください。')
        return super().form_invalid(form)
 
 
class AccountUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = 'pages/account.html'
    fields = ('username', 'email',)
    success_url = '/account/'
 
    def get_object(self):
        # URL変数ではなく、現在のユーザーから直接pkを取得
        self.kwargs['pk'] = self.request.user.pk
        return super().get_object()
 
 
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'pages/profile.html'
    fields = ('name', 'zipcode', 'prefecture',
              'city', 'address1', 'address2', 'tel')
    success_url = '/profile/'
 
    def get_object(self):
        # URL変数ではなく、現在のユーザーから直接pkを取得
        self.kwargs['pk'] = self.request.user.pk
        return super().get_object()