from rest_framework import serializers
from api.models import Chapter, Subchapter, Group, GroupItem




class GroupItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupItem
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    group_items = GroupItemSerializer(many=True, read_only=True, source='groupitem_set')

    class Meta:
        model = Group
        fields = '__all__'


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'


class SubchapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subchapter
        fields = '__all__'
