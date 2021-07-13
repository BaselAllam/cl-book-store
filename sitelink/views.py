from sitelink.models import Link
from sitelink.serializer import LinkSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated




class SiteLinkView(APIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format= None):
        categoreis = Link.objects.all()
        serializer = LinkSerializer(categoreis, many= True, context={"request": request})
        return Response(serializer.data)