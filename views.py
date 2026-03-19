def submit(request, course_id):
    if request.method == 'POST':
        course = get_object_or_404(Course, pk=course_id)
        # Logic to get choices and calculate score...
        # ...
        return redirect('onlinecourse:show_exam_result', course_id=course.id, submission_id=submission.id)

def show_exam_result(request, course_id, submission_id):
    context = {}
    # Logic to fetch results and pass to context...
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)
