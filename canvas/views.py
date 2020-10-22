from django.views import generic


class ProductListView(generic.ListView):
    pass


class ProductCustomizeView(generic.TemplateView):
    template_name = 'canvas/product_customize.html'

    def get_context_data(self, **kwargs):
        context = super(ProductCustomizeView, self).get_context_data(**kwargs)
        context['IframeApi'] = 'https://h2.customerscanvas.com/Users/f7edbcda-2531-4854-b660-d84ca949dff3/SimplePolygraphy/Resources/Generated/IframeApi.js'
        return context
