from rest_framework import serializers
from posts.models import Post, Group, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        fields = ('id', 'text', 'group', 'author', 'pub_date')
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all(), required=False)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'post', 'created')
