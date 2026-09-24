class JobpostForm(forms.ModelForm):
    class Meta:
        model = Jobslist
        #fields = ['postname']
        fields = ['postname', 'posts', 'jobtype', 'salary', 'address', 'description', 'tehsil']


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        #fields = ['academic_session', 'subject', 'class_name']
        fields = ['subject', 'classname']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        #fields = ['academic_session', 'subject', 'class_name']
        fields = ['father_name', 'mother_name', 'mobile', 'admission_no', 'admission_date']


class SchoolDetailsForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['school_name']

class SubjectMarksForm(forms.ModelForm):
    class Meta:
        model = SubjectMark
        fields = ['classname', 'subject', 'first', 'second', 'third']
