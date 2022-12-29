from django import forms 

class AddPeopleForm(forms.Form):
    name= forms.CharField(max_length=126, label='اسم', required=True)
    family = forms.CharField(max_length=126, label='فامیلی', required=True)

    field = forms.CharField(max_length=256, label='رشته', required=False)
    university = forms.CharField(max_length=126, label='دانشگاه', required=False)
    title= forms.CharField(max_length=256, label='عنوان', required=False)
    doctor_adviser = forms.CharField(max_length=126, label='استاد راهنما', required=False)

    money = forms.IntegerField(label='پول', required=True)
    debt_payment1 = forms.FileField(max_length=126, label='قسط اول', required=False)
    debt_payment2 = forms.FileField(max_length=126, label='قسط دوم', required=False)
    debt_payment3 = forms.FileField(max_length=126, label='قسط سوم', required=False)

    start_date = forms.DateField(label='شروع کار', required=False)

    proposal = forms.FileField(label='پروپوزال', required=False)
    ch123 = forms.FileField(label='فصل 1 تا 3', required=False)
    ch45 = forms.FileField(label='فصل 4 و 5', required=False)

    translation = forms.CharField(max_length=126, label='ترجمه', required=False)
    RAC = forms.CharField(max_length=126, label='کد رهگیری پژوهشیار', required=False)
    representative = forms.CharField(max_length=126, label='معرف', required=False)
    description = forms.CharField(label='توضیحات', widget=forms.Textarea, required=False)

class AddTODOForm(forms.Form):
    CHOICES = [('today', 'امروز'), ('necessary', 'ضروروی'), ('zremind', 'یادآوری')]
    title = forms.CharField(max_length=126, label='عنوان')
    status = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    description = forms.CharField(widget=forms.Textarea, required=False)
    remind_datetime = forms.DateTimeField(required=False)