#import pytest
#from unittest.mock import patch
#from flask_restx import Namespace, Resource, fields, Model
#from flask_jwt_extended import create_access_token
#
#from app import create_app
#from apis import api
#
#
#@pytest.fixture
#def client():
#    app = create_app()
#    app.config['TESTING'] = True
#    with app.app_context():
#        with app.test_client() as client:        
#            yield client
#
#@pytest.fixture
#def headers():
#    token = create_access_token("testuser")
#    return {"Authorization": f"Bearer {token}"}
#
#
#
#@pytest.fixture
#def mock_warehouses_data():
#    return [{"id": 0, "name":"Odense"}]
#
#@pytest.fixture
#def mock_inventory_data():
#    return [ {"id": 0, "product_id":0, "warehouse_id": 0, "quantity": 5}]
#
#
#@pytest.mark.parametrize("endpoint, expected_status", [
#    ("/warehouse/", 200),
#    ("/warehouse/0", 200) ,   
#    ("/warehouse/999", 404),
#    ("/warehouse/abc", 404)
#])
#def test_get_warehouse_inputs(client, endpoint, expected_status):
#    response = client.get(endpoint)
#    assert response.status_code == expected_status
#
#
#@pytest.mark.parametrize("endpoint, expected_status", [
#    ("/warehouse/0/inventory", 200),
#    ("/warehouse/0/inventory/0", 200) ,   
#    ("/warehouse/0/inventory/999", 404),
#    ("/warehouse/0/inventory/abc", 404),
#    ("/warehouse/999/inventory/0", 404),
#    ("/warehouse/999/inventory/999", 404),
#    ("/warehouse/999/inventory/abc", 404),
#    ("/warehouse/abc/inventory/0", 404),
#    ("/warehouse/abc/inventory/999", 404),
#    ("/warehouse/abc/inventory/abc", 404)
#])
#def test_get_inventory_inputs(client, endpoint, expected_status, mock_warehouses_data):
#    with patch("apis.warehouse.warehouses", mock_warehouses_data):
#        response = client.get(endpoint)
#        assert response.status_code == expected_status
#
#
#@pytest.mark.parametrize("payload, expected_status", [
#    ({"id": 1, "name": "Main Warehouse"}, 201),
#    ({"id": "abc", "name": "Invalid ID"}, 400),
#    ({"id": 1, "name": ""}, 400),
#    ({}, 400),
#    ({"id": 2}, 400),  
#])
#def test_post_warehouse_auth(client, payload, headers, expected_status, mock_warehouses_data):   
#    with patch("apis.warehouse.warehouses", mock_warehouses_data):
#        response = client.post("/warehouse/", json=payload, headers=headers)
#        assert response.status_code == expected_status
#
#@pytest.mark.parametrize("payload, expected_status", [
#    ({"id": 1, "name": "Main Warehouse"}, 401),
#    ({"id": "abc", "name": "Invalid ID"}, 401),
#    ({"id": 1, "name": ""}, 401),
#    ({}, 401),
#    ({"id": 2}, 401),  
#])
#def test_post_warehouse_no_auth(client, payload, expected_status, mock_warehouses_data):  
#    with patch("apis.warehouse.warehouses", mock_warehouses_data):  
#        response = client.post("/warehouse/", json=payload)
#        assert response.status_code == expected_status
#
#
#@pytest.mark.parametrize("payload, expected_status", [
#    ({"id": 1, "name": "Main Warehouse"}, 201),
#    ({"id": "abc", "name": "Invalid ID"}, 400),
#    ({"id": 1, "name": ""}, 400),
#    ({}, 400),
#    ({"id": 2}, 400),  
#])
#def test_put_warehouse_auth(client, payload, headers, expected_status, mock_warehouses_data):
#    with patch("apis.warehouse.warehouses", mock_warehouses_data):  
#        response = client.post("/warehouse/", json=payload, headers=headers)
#        assert response.status_code == expected_status
#
#
#@pytest.mark.parametrize("payload, expected_status", [
#    ({"id": 1, "name": "Main Warehouse"}, 401),
#    ({"id": "abc", "name": "Invalid ID"}, 401),
#    ({"id": 1, "name": ""}, 401),
#    ({}, 401),
#    ({"id": 2}, 401),  
#])
#def test_put_warehouse_no_auth(client, payload, expected_status, mock_warehouses_data):
#    with patch("apis.warehouse.warehouses", mock_warehouses_data):  
#        response = client.post("/warehouse/", json=payload)
#        assert response.status_code == expected_status
#
#
#@pytest.mark.parametrize("endpoint, expected_status", [
#    ("/warehouse/0", 200),
#    ("/warehouse/999", 404),
#    ("/warehouse/abc", 404),
#])
#def test_delete_warehouse_auth(client, endpoint, headers, expected_status, mock_warehouses_data):
#    with patch("apis.warehouse.warehouses", mock_warehouses_data):  
#        response = client.delete(endpoint, headers=headers)
#        assert response.status_code == expected_status
#
#@pytest.mark.parametrize("endpoint, expected_status", [
#    ("/warehouse/0", 401),
#    ("/warehouse/999", 401),
#    ("/warehouse/abc", 404)
#])
#def test_delete_warehouse_no_auth(client,endpoint, expected_status, mock_warehouses_data):
#    with patch("apis.warehouse.warehouses", mock_warehouses_data): 
#        response = client.delete(endpoint)
#        assert response.status_code == expected_status
#
#@pytest.mark.parametrize("endpoint, payload, expected_status", [
#    ("/warehouse/0/inventory", {"id": 0, "product_id":0, "warehouse_id": 0, "quantity": 5}, 201),
#    ("/warehouse/999/inventory", {"id": 0, "product_id":0, "warehouse_id": 0, "quantity": 5}, 404),
#    ("/warehouse/0/inventory", {"id": "abc", "product_id":"abc", "warehouse_id": "abc", "quantity": "abc"}, 400),
#    ("/warehouse/abc/inventory", {"id": 0, "product_id":0, "warehouse_id": 0, "quantity": 5}, 404),
#    ("/warehouse/0/inventory", {}, 400)
#])
#def test_post_warehouse_inventory_auth(client, endpoint, 
#        payload, headers, expected_status, 
#        mock_warehouses_data, mock_inventory_data):
#    with patch("apis.warehouse.warehouses", mock_warehouses_data): 
#        with patch("apis.warehouse.warehouse_items", mock_inventory_data): 
#            response = client.post(endpoint, json=payload, headers=headers)
#            assert response.status_code == expected_status
#
#@pytest.mark.parametrize("endpoint, payload, expected_status", [
#    ("/warehouse/0/inventory", {"id": 0, "product_id":0, "warehouse_id": 0, "quantity": 5}, 401),
#    ("/warehouse/999/inventory", {"id": 0, "product_id":0, "warehouse_id": 0, "quantity": 5}, 401),
#    ("/warehouse/0/inventory", {"id": "abc", "product_id":"abc", "warehouse_id": "abc", "quantity": "abc"}, 401),
#    ("/warehouse/abc/inventory", {"id": 0, "product_id":0, "warehouse_id": 0, "quantity": 5}, 404),
#    ("/warehouse/0/inventory", {}, 401)
#])
#def test_post_warehouse_inventory_no_auth(client, endpoint, 
#        payload, expected_status, 
#        mock_warehouses_data, mock_inventory_data):
#    with patch("apis.warehouse.warehouses", mock_warehouses_data): 
#        with patch("apis.warehouse.warehouse_items", mock_inventory_data): 
#            response = client.post(endpoint, json=payload)
#            assert response.status_code == expected_status
#
#@pytest.mark.parametrize("endpoint, payload, expected_status", [
#    ("/warehouse/0/inventory/0", {"id": 0, "product_id":0, "warehouse_id": 0, "quantity": 5}, 200),
#    ("/warehouse/0/inventory", {"id": 0, "product_id":0, "warehouse_id": 0, "quantity": 5}, 405),
#    ("/warehouse/999/inventory/999", {"id": 0, "product_id":0, "warehouse_id": 0, "quantity": 5}, 404),
#    ("/warehouse/0/inventory/abc", {"id": "abc", "product_id":"abc", "warehouse_id": "abc", "quantity": "abc"}, 404),    
#    ("/warehouse/0/inventory/", {}, 404)
#])
#def test_put_warehouse_inventory_auth(client, endpoint, 
#        payload, headers, expected_status, 
#        mock_warehouses_data, mock_inventory_data):
#    with patch("apis.warehouse.warehouses", mock_warehouses_data): 
#        with patch("apis.warehouse.warehouse_items", mock_inventory_data): 
#            response = client.put(endpoint, json=payload, headers=headers)
#            assert response.status_code == expected_status
#
#
#@pytest.mark.parametrize("endpoint, payload, expected_status", [
#    ("/warehouse/0/inventory/0", {"id": 0, "product_id":0, "warehouse_id": 0, "quantity": 5}, 401),
#    ("/warehouse/0/inventory", {"id": 0, "product_id":0, "warehouse_id": 0, "quantity": 5}, 405),
#    ("/warehouse/999/inventory/999", {"id": 0, "product_id":0, "warehouse_id": 0, "quantity": 5}, 401),
#    ("/warehouse/0/inventory/abc", {"id": "abc", "product_id":"abc", "warehouse_id": "abc", "quantity": "abc"}, 404),    
#    ("/warehouse/0/inventory/", {}, 404)
#])
#def test_put_warehouse_inventory_no_auth(client, endpoint, 
#        payload, expected_status, 
#        mock_warehouses_data, mock_inventory_data):
#    with patch("apis.warehouse.warehouses", mock_warehouses_data): 
#        with patch("apis.warehouse.warehouse_items", mock_inventory_data): 
#            response = client.put(endpoint, json=payload)
#            assert response.status_code == expected_status
#
#@pytest.mark.parametrize("endpoint, expected_status", [
#    ("/warehouse/0/inventory/0", 200),
#    ("/warehouse/0/inventory/999", 404),
#    ("/warehouse/0/inventory/abc", 404),
#    ("/warehouse/999/inventory/0", 404),
#    ("/warehouse/abc/inventory/0", 404)
#])
#def test_delete_warehouse_inventory_auth(client, endpoint, 
#        expected_status, headers,
#        mock_warehouses_data, mock_inventory_data):
#    with patch("apis.warehouse.warehouses", mock_warehouses_data): 
#        with patch("apis.warehouse.warehouse_items", mock_inventory_data): 
#            response = client.delete(endpoint, headers=headers)
#            assert response.status_code == expected_status
#
#@pytest.mark.parametrize("endpoint, expected_status", [
#    ("/warehouse/0/inventory/0", 401),
#    ("/warehouse/0/inventory/999", 401),
#    ("/warehouse/0/inventory/abc", 404),
#    ("/warehouse/999/inventory/0", 401),
#    ("/warehouse/abc/inventory/0", 404)
#])
#def test_delete_warehouse_inventory_no_auth(client, endpoint, 
#        expected_status,
#        mock_warehouses_data, mock_inventory_data):
#    with patch("apis.warehouse.warehouses", mock_warehouses_data): 
#        with patch("apis.warehouse.warehouse_items", mock_inventory_data): 
#            response = client.delete(endpoint)
#            assert response.status_code == expected_status