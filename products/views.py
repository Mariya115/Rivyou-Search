from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from .search import search_products
from .models import Product
from .serializers import ProductSerializer


class ProductSearchView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        query = request.GET.get("q")

        if not query:
            return Response(
                {"error": "Query parameter 'q' is required"},
                status=400
            )

        limit = int(request.GET.get("limit", 20))

        results = search_products(query)

        data = []

        for item in results[:limit]:

            product = item["product"]

            data.append({
                "id": product.id,
                "product_name": product.product_name,
                "category": product.category,
                "tags": product.tags,
                "relevance_score": round(item["score"], 2),
                "rank_reason": item["reason"]
            })

        return Response({
            "query": query,
            "total_results": len(results),
            "results": data
        })


class ProductDetailView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, product_id):

        product = get_object_or_404(
            Product,
            id=product_id
        )

        serializer = ProductSerializer(product)

        return Response(serializer.data)


class ProductCategoryView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, category):

        products = Product.objects.filter(
            category__iexact=category
        )

        serializer = ProductSerializer(
            products,
            many=True
        )

        return Response(serializer.data)