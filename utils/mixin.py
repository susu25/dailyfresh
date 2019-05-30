from django.contrib.auth.decorators import login_required


class LoginRequiredMixin(object):
    """登录访问限制"""
    @classmethod
    def as_view(cls, **initkwargs):
        # 调用父类的as_view
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)