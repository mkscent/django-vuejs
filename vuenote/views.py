from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from vuenote.models import Note
from vuenote.serializers import NoteSerializer


# Note viewset
# Create, edit or display our notes via the API
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'id'
