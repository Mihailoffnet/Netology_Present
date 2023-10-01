from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from demo.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    text = serializers.CharField(min_length=10)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'created_at']

    def validate_text(self, value): # validate_ после подчеркивания идет название поля, которое хотим проверить
        ban = ['одмин', 'коммент']
        for word in ban:
            if word in value:
                raise ValidationError(F'Вы использовали запрещенное слово {word}')
        return value

    # def validate(self, attrs):
    #     if 'hello' in attrs['text'] or attrs['user'].id == 2:
    #         raise ValidationError('Что-то пошло не так')
    #     return attrs

    def validate(self, attrs):
        text = attrs['text'].lower()

        if 'флуд' in text:
            raise ValidationError('разрабу нельзя флудить')
        return attrs

    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)