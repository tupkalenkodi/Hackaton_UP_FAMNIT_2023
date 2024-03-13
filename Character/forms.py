from django import forms
from .models import Character


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = [
            'name',
            'art_forms',
            'art_preference',
            'art_inspiration',
            'art_emotions',
            'art_themes',
            'art_creation',
            'art_role',
            'art_feedback',
            'art_goals',
            'creative_process',
            'technical_skill',
            'art_experimentation',
            'target_audience',
            'cultural_influences',
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'field', 'placeholder': 'PewDiePie, The Weeknd, Michelangelo '
                                                                            'Buonarroti'}),
            'art_forms': forms.TextInput(attrs={'class': 'field', 'placeholder': 'Painting, sculpture, photography, '
                                                                                 'music'}),
            'art_preference': forms.TextInput(attrs={'class': 'field', 'placeholder': 'Appreciating Both for '
                                                                                      'Different Reasons, Traditional'
                                                                                      ' Art for Classic Beauty'}),
            'art_inspiration': forms.TextInput(attrs={'class': 'field', 'placeholder': 'Leonardo da Vinci, '
                                                                                       'Impressionism, Pop Art'}),
            'art_emotions': forms.TextInput(attrs={'class': 'field', 'placeholder': 'A sense of action and '
                                                                                    'spontaneity, Comment on consumer '
                                                                                    'culture'}),
            'art_themes': forms.TextInput(attrs={'class': 'field', 'placeholder': 'Nature and Tranquility, Human '
                                                                                  'Emotions and Relationships'}),
            'art_creation': forms.TextInput(attrs={'class': 'field', 'placeholder': 'Independently, Collaborating, '
                                                                                    'Both, Depending on the Project'}),
            'art_role': forms.TextInput(attrs={'class': 'field', 'placeholder': 'Stress Relief and Relaxation, '
                                                                                'Connecting with Others'}),
            'art_feedback': forms.TextInput(attrs={'class': 'field', 'placeholder': 'Open-Minded Approach, Staying '
                                                                                    'Authentic'}),
            'art_goals': forms.TextInput(attrs={'class': 'field', 'placeholder': 'Establishing a Recognizable Style, '
                                                                                 'Impactful Social Commentary'}),
            'creative_process': forms.TextInput(attrs={'class': 'field', 'placeholder': 'Intuitive Exploration, '
                                                                                        'Research and Inspiration'}),
            'technical_skill': forms.TextInput(attrs={'class': 'field', 'placeholder': 'Balanced Blend, Emphasis on '
                                                                                       'Personal Expression'}),
            'art_experimentation': forms.TextInput(attrs={'class': 'field', 'placeholder': 'Enthusiastic and Curious, '
                                                                                           'Essential for Growth'}),
            'target_audience': forms.TextInput(attrs={'class': 'field', 'placeholder': 'All Ages and Backgrounds, '
                                                                                       'Youthful and Trendy'}),
            'cultural_influences': forms.TextInput(attrs={'class': 'field', 'placeholder': 'Futurism and Industrial '
                                                                                           'Revolution, '
                                                                                           'Bauhaus Simplicity'}),

        }
