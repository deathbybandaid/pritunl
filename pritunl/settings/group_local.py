# pylama:ignore=E302,W0401
from pritunl.settings.group_base import SettingsGroupBase

from pritunl.constants import *

class SettingsGroupLocal(SettingsGroupBase):
    type = GROUP_LOCAL
