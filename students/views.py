from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Student
from .forms import StudentForm

def student_list(request):
    students = Student.objects.all()
    
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                student = form.save()
                messages.success(request, f'Student {student.name} added successfully!')
                return redirect('student_list')
            except Exception as e:
                messages.error(request, f'Error saving student: {str(e)}')
        else:
            print("Form validation errors:", form.errors)
    else:
        form = StudentForm()

    context = {
        'form': form,
        'students': students,
    }
    return render(request, 'students/student_list1.html', context)

def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            try:
                student = form.save()
                messages.success(request, f'Student {student.name} updated successfully!')
                return redirect('student_list')
            except Exception as e:
                messages.error(request, f'Error updating student: {str(e)}')
    else:
        form = StudentForm(instance=student)

    context = {
        'form': form,
        'student': student,
    }
    return render(request, 'students/student_form.html', context)

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == 'POST':
        try:
            student.delete()
            messages.success(request, f'Student {student.name} deleted successfully!')
        except Exception as e:
            messages.error(request, f'Error deleting student: {str(e)}')
        return redirect('student_list')
        
    context = {
        'student': student,
    }
    return render(request, 'students/student_confirm_delete.html', context)
