from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from resumes.models import Resume
from resumes.permisions import IsOwner
from resumes.serializers import ResumeSerializer


class ResumeListView(ListAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer


class ResumeDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    http_method_names = ['get', 'patch']
    permission_classes = [IsOwner]
