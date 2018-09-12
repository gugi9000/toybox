from django import forms
from .models import Cliente
import datetime


class NewProspectForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.Textarea(
        attrs={
            'id': 'autosize-demo',
            'class': 'form-control',
            'style': 'overflow: hidden; overflow-wrap: break-word; resize: none; height: 81.3333px;',
            'rows': 3,
        }
    ))
    rz_pf = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'type': 'text',
            'placeholder': 'Nombre del prospecto: Joe Doe',
        }
    ))

    obligaciones = forms.MultipleChoiceField(
        choices=(
            ('ISR', "ISR"),
            ('IVA', "IVA"),
            ('ISPT', "ISPT"),
            ('ISR_RET', "ISR RET"),
            ('IVA_RET', "IVA RET"),
            ('IEPS', "IEPS"),
            ('MULTIIEPS', "Multiieps"),
            ('DPIVA', "DPIVA"),
            ('DOSSN', "2% Sobre Nomina"),
            ('IMINF', "IMSS e INFONAVIT"),
            ('RTP', "3% (Honorario Medico) o R.T.P."),
            ('DOSRET', "2% RET"),
            ('CE', "Contabilidad Electrónica"),
        ),
        widget=forms.CheckboxSelectMultiple(),
    )

    class Meta:
        model = Cliente
        fields = ('descripcion', 'rz_pf', 'obligaciones', )

from .forms import NewProspectForm


def new_prospect_view(request):

    form = NewProspectForm()

    if request.method == 'POST':
        form = NewProspectForm(request.POST)


        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tccontrol:dashboard-admin-prospectos'))

        else:
            print('Invalid form.')

    return render(request, 'tccontrol/prospectos/page_nuevo_prospecto.html', {'prospect_form': form})


