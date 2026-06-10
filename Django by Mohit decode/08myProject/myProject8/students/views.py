from django.shortcuts import redirect, render
from students.models import Student,Review
from django.shortcuts  import get_object_or_404
# Create your views here.

def stu_Data(request):
    stu_data = Student.objects.all()
    return render(request, 'students/stu_data.html', {
        'stu_data': stu_data
        })

def stu_details(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'students/stu_details.html', {
        'stu_details': student
    })



def stu_feedback(request, feedback_id):
    stu_feedback = get_object_or_404(Student, id=feedback_id)

    if request.method == 'POST':
        feedback = request.POST.get('feedback')
        stu_rating = request.POST.get('rating')
        review_text = request.POST.get('review_text')
        name = request.POST.get('name')
        # stu_feedback.save()

        review = Review.objects.create(
            student=stu_feedback,
            review_text=review_text,
            name=name,
            rating=stu_rating,
             
        )
        return redirect('stu_details', student_id=stu_feedback.id)
        
        
    
    return render(request, 'students/stu_feedback.html')

def stu_reviews(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    return render(request, 'students/stu_review.html', {
       'review': review
    })

def stu_selected(request):
    return render(request, 'students/stu_selected.html')