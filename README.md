Citybox Chile Python
==============

All Citybox of Santiago de Chile

**"install citybox"**
```
pip install -e git://github.com/rulz/cityboxpython#egg=cityboxchile
```

**"config in forms.py"**
```
from django import forms
from citybox import get_choices_citybox

CHOICES_CITYBOX = get_choices_citybox()

class CityBoxForm(forms.Form):
	address_citybox = forms.ChoiceField(choices=CHOICES_CITYBOX)

```

