from django.shortcuts import render
from  .models import poost
from django.views.generic import ListView, DetailView, CreateView,DeleteView,UpdateView


class PoostList(ListView):
    model=poost
   # context_object_name = 'all_post'#هون بحدد اسم الاوبجكت اللي رح استخدمه لما استدعي الكلاس هاد 
    ordering=['-created_at']#الليست اللي بترجع برتبها بناء على الاشي اللي بحدده هون حددنا التاريخ 
    queryset=poost.objects.filter(active=True) #بترجع بس المودل اللي بكون أكتيف اله ترو بقدر ارجع اي صفة معينة للداتا باستخدام الفيلتر 
    #template_name ='post/test.html' #بنعملها اذا بدي يروح على تيمبليت معين  بحطله مسار التمبليت اللي بدي يروح عليه او الصفحة لما اشغل هاد المودل
    def  get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['myname']='raghad'
        return context
class PoostCreate():
    pass
class PoostDetail(DetailView):
    model=poost
class PoostUpdate():
    pass
class PoostDelete():
    pass