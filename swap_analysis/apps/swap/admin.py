from django.contrib import admin

from swap_analysis.apps.swap.models import (
    Battery, Swap, Driver, Station, Attendant, Motor)

models = [Battery,
          Swap, Driver, Station, Attendant, Battery, Motor]

admin.register(models)
