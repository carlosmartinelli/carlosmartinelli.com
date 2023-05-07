# from django.views.generic import TemplateView
# from home.models import HomePage


# class HomePageView(TemplateView):
#     template_name = 'home_page.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['page'] = HomePage.objects.first()
#         return context