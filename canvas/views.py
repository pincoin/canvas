from django.views import generic


class ProductListView(generic.ListView):
    pass


class ProductCustomizeView(generic.TemplateView):
    template_name = 'canvas/product_customize.html'
