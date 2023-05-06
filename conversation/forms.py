from django import forms

from .models import ConversationMessage

class ConversationMessagesForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = (
            'content',
        )
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rouded-xl border'
            })
        }
