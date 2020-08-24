from rest_framework import serializers
from records.models import Task, Choice, Income, Expenditure, Category


class ChoiceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)    
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Choice
        fields = '__all__' 
        read_only_fields = ('task',)


class TaskSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)
    # content = serializers.PrimaryKeyRelatedField(
    #     many=True, read_only=False, queryset=TaskRecord.objects.all())    
    choices = ChoiceSerializer(many=True)
    class Meta:
        model = Task
        exclude = ["updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%Y-%m-%d")

    def create(self, validated_data):
        choices = validated_data.pop('choices')
        task = Task.objects.create(**validated_data)
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        for choice in choices:
            Choice.objects.create(**choice, task=task, author=user)
        return task

    def update(self, instance, validated_data):
        choices = validated_data.pop('choices')
        instance.title = validated_data.get("title", instance.title)
        instance.save()
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user        
        keep_choices = []
        for choice in choices:
            if "id" in choice.keys():
                if Choice.objects.filter(id=choice["id"]).exists():
                    c = Choice.objects.get(id=choice["id"])
                    c.text = choice.get('text', c.text)
                    c.save()
                    keep_choices.append(c.id)
                else:
                    continue
            else:
                c = Choice.objects.create(**choice, task=instance, author=user)
                keep_choices.append(c.id)

        for choice in instance.choices:
            if choice.id not in keep_choices:
                choice.delete()

        return instance


class IncomeSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Income
        exclude = ["updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%Y-%m-%d")


class CategorySerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Category
        exclude = ["updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%Y-%m-%d")

class ExpenditureSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)
    # category = serializers.SerializerMethodField()
    # category = serializers.StringRelatedField(read_only=False)
    # category = CategorySerializer()

    class Meta:
        model = Expenditure
        exclude = ["updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%Y-%m-%d")

    # def get_category(self, instance):
    #     return {
    #         "id": instance.category.id,
    #         "title": instance.category.title  
    #     }
     

