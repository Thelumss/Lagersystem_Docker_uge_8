import pytest
from unittest.mock import patch
from flask import Flask
from flask_restx import Api, Resource, Namespace


api = Namespace("product", description="Product operations")

@api.route("/price/<price>")
class ProductGetByPrice(Resource):
    @api.doc('Get product based on price')
    def get(self, price):
        newPrice = float(price)
        products = db_manager.product.GetByPrice(price)
        print(products)
        return {"products": products}, 200


class MockDBManager:
    class product:
        @staticmethod
        def GetByPrice(price):
            return [{"id": 1, "name": "Test Product", "price": float(price)}]

db_manager = MockDBManager()

app = Flask(__name__)
api_blueprint = Api(app)
api_blueprint.add_namespace(api, path="/api/product")

client = app.test_client()


@patch.object(db_manager.product, "GetByPrice", return_value=[{"id": 1, "name": "Mock Product", "price": 9.99}])
def test_get_product_by_price(mock_get_by_price):
    response = client.get("/api/product/price/9.99")
    assert response.status_code == 200

    data = response.get_json()
    assert "products" in data
    assert data["products"][0]["name"] == "Mock Product"

    mock_get_by_price.assert_called_once_with("9.99")
