from .models import Product


def search_products(query):

    query = query.lower().strip()

    results = []

    products = Product.objects.all()

    for product in products:

        category = product.category.lower()
        tags = [tag.lower() for tag in product.tags]
        name = product.product_name.lower()
        description = product.product_description.lower()

        score = 0
        reason = ""

        # -----------------------------
        # Tier 1: Category Match
        # -----------------------------
        if query in category:

            score = 0.90

            if "5g" in tags:
                score += 0.03

            if "performance" in tags:
                score += 0.03

            if "camera" in tags:
                score += 0.02

            if "battery" in tags:
                score += 0.01

            reason = "Category match"

        # -----------------------------
        # Tier 2: Tag Match
        # -----------------------------
        elif any(query in tag for tag in tags):

            exact_match = any(query == tag for tag in tags)

            if exact_match:
                score = 0.80
                reason = f"Exact tag match ({query})"
            else:
                score = 0.70
                reason = f"Partial tag match ({query})"

        # -----------------------------
        # Tier 3: Name/Description Match
        # -----------------------------
        elif query in name:

            score = 0.50
            reason = "Product name match"

        elif query in description:

            score = 0.35
            reason = "Description match"

        # -----------------------------
        # Add Result
        # -----------------------------
        if score > 0:

            results.append({
                "product": product,
                "score": round(min(score, 1.0), 2),
                "reason": reason
            })

    # Sort by score descending
    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results