class UniversalCommerceDiscoveryProtocolClient:
    def sync_and_search(self, merchant_id: str, query: str, min_stock: int = 1) -> dict:
        mock_inventory = [
            {"ucp_sku": "SKU-1001", "title": "Ergonomic Desk Chair", "price_usd": 299.99, "stock_count": 15, "availability": "IN_STOCK"},
            {"ucp_sku": "SKU-1002", "title": "Standing Desk Converter", "price_usd": 189.50, "stock_count": 0, "availability": "OUT_OF_STOCK"},
            {"ucp_sku": "SKU-1003", "title": "Monitor Arm Dual Mount", "price_usd": 89.99, "stock_count": 8, "availability": "IN_STOCK"}
        ]
        matched = [
            item for item in mock_inventory
            if query.lower() in item["title"].lower() and item["stock_count"] >= min_stock
        ]
        return {
            "structured_catalog": matched,
            "protocol_version": "UCP-v2.1"
        }
