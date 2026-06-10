from django.shortcuts import render, get_object_or_404, redirect
from .form import StudentForm
from .models import Student
# Create your views here.


def student_create(request):
    form = StudentForm()
    if request.method == 'POST':
        
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'student/student_success.html')
    
    
    return render(request, 'student/student_create.html', {
        'form':form
    })


def Student_list(request):
    stu_list = Student.objects.all()

    return render(request, 'student/stu_list.html', {
        'students':stu_list
    })

def stu_details(request, detail_id):
    stu_data = get_object_or_404(Student, pk = detail_id)
    return render(request, 'student/stu_details.html', {
        'data':stu_data
    })

def stu_edit(request, edit_id):
    stu_data = get_object_or_404(Student, pk = edit_id)
    
    if request.method == "POST":
        stu_data.name = request.POST.get('name')
        stu_data.age = request.POST.get('age')
        stu_data.email = request.POST.get('email')
        stu_data.save()

        return  redirect('Student_list')
    
    return render(request, 'student/stu_edit.html',{
        'stu_data': stu_data
    })


def stu_delete(request, del_id):
    stu_data = get_object_or_404(Student, pk = del_id)
    if request.method == 'POST':
        stu_data.delete()
        return redirect('Student_list')
    return render(request, 'student/stu_delete.html', {
        'stu_data': stu_data
    })
