from flask_restx import Namespace, Resource, fields, Model
from flask_jwt_extended import jwt_required
from apis.auth import authorizations
from flask import Flask, jsonify, request


def create_api_orders(db_manager):
    api: Namespace = Namespace("orders", description="Order namespace", authorizations=authorizations)

    orders_model = api.model('OrderModel', {'orderID': fields.Integer, 'produktID': fields.Integer, 'invoicenummer': fields.Integer, 'customerID': fields.Integer, 'status': fields.String, 'mangde': fields.Integer, 'lagerID': fields.Integer})

    remove_orders_model = api.model('RemoveOrderModel', {'orderID': fields.Integer})

    orders_list = [
        {'id': 0, 'name': "Viktor", 'warelist': ['banana', 'planes', 'car'], 'total': 500},
        {'id': 1, 'name': "Michael", 'warelist': ['sofa', 'bed', 'car'], 'total': 1500},
        {'id': 2, 'name': "Vera", 'warelist': ['glasses', 'flatbed', 'truck'], 'total': 500}
    ]

    @api.route("/<int:id>")
    class OrderGet(Resource):
        @api.doc('Get an order based on ID')
        def get(self, id):
            result = db_manager.orders.GetByID(id)
            if result == []:
                return jsonify({'message': 'Order does not exist'}, 404)
            else:
                return result
    
    @api.route("/ByCustomerID<int:id>")
    class OrderGet(Resource):
        @api.doc('Get an order based on CustomerID')
        def get(self, id):
            result = db_manager.orders.OrderCustomerView(id)
            if result == []:
                return jsonify({'message': 'Order does not exist'}, 404)
            else:
                return result

    @api.route("/")
    class Order(Resource):
        
        @api.doc('Get all orders')
        def get(self):
            result = db_manager.orders.GetAll()
            return result

        @jwt_required()
        @api.doc('Receive a new order', security='jsonWebToken')
        @api.expect(orders_model)
        def post(self):
            orderID = api.payload['orderID']
            produktID = api.payload['produktID']
            invoicenummer = api.payload['invoicenummer']
            customerID = api.payload['customerID']
            status = api.payload['status']
            mangde = api.payload['mangde']
            lagerID = api.payload['lagerID']
            if ((orderID == 0) or (produktID == 0) or (customerID == 0) or (lagerID == 0)):
                return jsonify({'message': 'Invalid order'}, 400)
            else:
                result = db_manager.orders.Insert(produktID, invoicenummer, customerID, status, mangde, lagerID)
            #orders_list.append({'id': {orderID}, 'produktID': {produktID}, 'warelist': {warelist}, 'total': {total}})
            return result
        
        @jwt_required()
        @api.doc("Update order", security='jsonWebToken')
        @api.expect(orders_model)
        def put(self):
            orderID = api.payload['orderID']
            produktID = api.payload['produktID']
            invoicenummer = api.payload['invoicenummer']
            customerID = api.payload['customerID']
            status = api.payload['status']
            mangde = api.payload['mangde']
            lagerID = api.payload['lagerID']
            result = db_manager.orders.GetByID(orderID)
            if result == []:
                return jsonify({"message": "Order does not exist"}, 400)
            else:    
                db_manager.orders.UpdateOrder(orderID, produktID, invoicenummer, customerID, status, mangde, lagerID)
            result = db_manager.orders.GetByID(orderID)
            return result
        
        @jwt_required()
        @api.doc("Delete order", security='jsonWebToken')
        @api.expect(remove_orders_model)
        def delete(self):
            orderID = api.payload['orderID']
            result = db_manager.orders.GetByID(orderID)
            if result == []:
                return jsonify({'message': 'Order does not exist'})
            else:
                result = db_manager.orders.UpdateStatus(orderID, "Inactive")
            return jsonify({'Removed order': result})
        
    return api