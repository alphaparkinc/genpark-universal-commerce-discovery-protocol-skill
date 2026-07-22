from client import UniversalCommerceDiscoveryProtocolClient

def main():
    client = UniversalCommerceDiscoveryProtocolClient()
    res = client.sync_and_search(merchant_id="merch_8819", query="desk", min_stock=1)
    print(f"Protocol: {res['protocol_version']}")
    print("Found Compliant Products:")
    for item in res["structured_catalog"]:
        print(f"  [{item['ucp_sku']}] {item['title']} - ${item['price_usd']} (Stock: {item['stock_count']})")

if __name__ == "__main__":
    main()
