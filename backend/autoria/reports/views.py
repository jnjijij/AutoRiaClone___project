from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View


from .models import Auto
from .models import AutoImage
from .models import Report


class ReportListView(View):
    @login_required(login_url=reverse_lazy('accounts:login'))
    def get(self, request):
        auto_id = request.user.auto.pk
        reports = Report.objects.filter(auto=auto_id, status='pending')
        return render(request, 'reports/report_list.html', {'reports': reports})

class ReportDetailView(View):
    @login_required(login_url=reverse_lazy('accounts:login'))
    def get(self, request, *args, **kwargs):
        report = get_object_or_404(Report, pk=kwargs['report_id'])
        return render(request, 'reports/report_detail.html', {'report': report})

class ReportDismissView(View):
    @login_required(login_url=reverse_lazy('accounts:login'))
    def post(self, request, *args, **kwargs):
        report = get_object_or_404(Report, pk=kwargs['report_id'])
        report.status = 'dismissed'
        report.save()
        auto = Auto.objects.get(pk=report.auto.pk)
        return redirect('reports:report_list', auto_id=auto.pk)

class ReportDeleteAllView(View):
    @login_required(login_url=reverse_lazy('accounts:login'))
    def post(self, request, *args, **kwargs):
        auto = Auto.objects.get(pk=kwargs['auto_id'])
        report_list = Report.objects.filter(auto=auto.pk, status='pending')
        for report in report_list:
            report.delete()
        return redirect('reports:report_list', auto_id=auto.pk)
class ReportCreateView(View):
    def post(self, request, *args, **kwargs):
        data = request.json()
        report = Report.objects.create(
            name=data['name'],
            description=data['description'],
        )
        data = {
            'id': report.id,
            'name': report.name,
            'description': report.description,
            'created_at': report.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        }
        return JsonResponse(data)

class ReportDetailView(View):
    def get(self, request, report_id, *args, **kwargs):
        report = Report.objects.get(id=report_id)
        data = {
            'id': report.id,
            'name': report.name,
            'description':report.description,
            'created_at': report.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        }
        return JsonResponse(data)

class ReportUpdateView(View):
    def put(self, request, report_id):
        report = Report.objects.get(id=report_id)
        data = request.json()
        report.name = data['name']
        report.description = data['description']
        report.save()
        data = {
            'id': report.id,
            'name': report.name,
            'description': report.description,
            'created_at': report.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        }
        return JsonResponse(data)

class ReportDeleteView(View):
    def delete(self, report_id):
        report = Report.objects.get(id=report_id)
        report.delete()
        return JsonResponse({'message': 'Report deleted successfully.'})

def auto_image_update(request, auto_pk, image_pk):
    auto_image = AutoImage.objects.get(pk=image_pk)
    if request.method == 'POST':
        form = Auto(request.POST, request.FILES, instance=auto_image)
        if form.is_valid():
            form.save()
            return redirect('auto_images')
    else:
        form = Auto(instance=auto_image)
    return render(request, 'auto_image_update.html', {'form': form})

def auto_image_delete(request, auto_pk, image_pk):
    auto_image = AutoImage.objects.get(pk=image_pk)
    if request.method == 'POST':
        auto_image.delete()
        return redirect('auto_images')
    else:
        return render(request, 'auto_image_delete.html', {'auto_image': auto_image})

def report(request):
    autos = Auto.objects.all()
    return render(request, 'reports/report.html', {'autos': autos})


class ReportCreateView:
    @classmethod
    def as_view(cls):
        pass


class ReportResolveView:
    @classmethod
    def as_view(cls):
        pass