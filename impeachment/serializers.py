from rest_framework import serializers
from impeachment.models import Impeachment

class ImpeachmentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Impeachment
        fields = "__all__"