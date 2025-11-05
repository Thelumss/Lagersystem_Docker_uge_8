import pytest
from unittest.mock import patch
from flask import Flask
from flask_restx import Api, Resource, Namespace


api = Namespace("customer", description="Customer operations")

@api.route("/<int:id>")
class CustomerGet(Resource):
    @api.doc('Get the customer based on the ID number')
    def get(self, id):
        customer = db_manager.customers.GetById(id)
        return {"customer": customer}, 200

class MockDBManager:
    class customers:
        @staticmethod
        def GetById(id):
            return {"id": id, "name": f"Customer {id}"}

db_manager = MockDBManager()


app = Flask(__name__)
api_blueprint = Api(app)
api_blueprint.add_namespace(api, path="/api/customer")

client = app.test_client()

@patch.object(db_manager.customers, "GetById", return_value={"id": 1, "name": "Mock Customer"})
def test_get_customer_by_id(mock_get_by_id):
    response = client.get("/api/customer/1")
    assert response.status_code == 200

    data = response.get_json()
    assert "customer" in data
    assert data["customer"]["name"] == "Mock Customer"

    mock_get_by_id.assert_called_once_with(1)
