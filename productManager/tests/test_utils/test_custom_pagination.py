from django.test import TestCase
from productManager.utils.CustomPagination import CustomPagination


class CustomPaginationTest(TestCase):
    def test_paginate_queryset(self):
        paginator = CustomPagination()
        queryset = [1, 2, 3, 4, 5]

        # Mocks a request object with query_params
        class MockRequest:
            query_params = {}

        result = paginator.paginate_queryset(queryset, MockRequest())
        self.assertIsNotNone(result)
