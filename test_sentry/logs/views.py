import logging
from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger(__name__)

from rest_framework.views import APIView


class TestView(APIView):
    """
    A simple view to test logging at different levels.
    This view generates logs at debug, info, and warning levels.
    """

    def get(self, request):
        # Test different log levels
        logger.debug("This is a debug message")
        logger.info("This is an info message")
        logger.warning("This is a warning message")

        return Response({"message": "Logs generated"}, status=status.HTTP_200_OK)
