from django.views.generic.edit import CreateView
from .models import Classrooms


class MakeClassroomView(CreateView):
    model = Classrooms
    fields = ['classname', 'members']
    template_name = 'make_classroom.html'

    def form_valid(self, form):
        form.instance.teacher_id = self.request.user.id
        return super(MakeClassroomView, self).form_valid(form)
