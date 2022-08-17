from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from . import serializers
from .models import Profile, Post, Comment


# 新規ユーザー作成
class CreateUserView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.UserSerializer


# プロフィール
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

    # 新規に作成する時には、ユーザーを指定する必要
    def perform_create(self, serializer):
        serializer.save(userProfile=self.request.user)


# 自分のプロフィールを返す
class MyProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

    def get_queryset(self):
        return Profile.objects.filter(userProfile=self.request.user)


# 投稿
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    # 新規に作成する時には、ユーザーを指定する必要
    def perform_create(self, serializer):
        serializer.save(userPost=self.request.user)


# コメント
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer

    # 新規に作成する時には、ユーザーを指定する必要
    def perform_create(self, serializer):
        serializer.save(userComment=self.request.user)