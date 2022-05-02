from rest_framework import serializers
from .models import Book, Section


class ChildSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


'''This Serializer is the serializer for returning validated data of
sections as well as subsections and also validating that neither a
section have two parent nor without parent.'''


class SectionSerializer(serializers.ModelSerializer):
    child_sections = ChildSectionSerializer(many=True, read_only=True)

    class Meta:
        model = Section
        fields = '__all__'

    def validate(self, attrs):
        if attrs.get("book") and attrs.get("parent_section"):
            raise serializers.ValidationError(
                "Parent Section Can only have a Book as Parent")
        elif not attrs.get("book") and not attrs.get("parent_section"):
            raise serializers.ValidationError(
                "Section should have a Parent")
        return super().validate(attrs)


'''This Serializer contains all fields as their is no confidentiol
field included in the model'''


class BookSerializer(serializers.ModelSerializer):
    sections = ChildSectionSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
