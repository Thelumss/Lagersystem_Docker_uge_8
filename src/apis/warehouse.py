from flask import jsonify
from flask_restx import Namespace, Resource, fields, Model
from flask_jwt_extended import jwt_required
from apis.auth import authorizations

from core.utils import parse_int, parse_dict_key


def create_api_warehouse(db_manager):
    api: Namespace = Namespace("warehouse", description="Warehouse namespace", authorizations=authorizations)


    warehouse_model = api.model("WarehouseModel",{
        "id": fields.Integer,
        "name": fields.String
    })

    warehouse_item_model = api.model("WarehouseItemModel",{
        "id": fields.Integer,
        "product_id": fields.Integer,
        "warehouse_id": fields.Integer,
        "quantity": fields.Integer
    })

    @api.route('/')
    class WarehouseList(Resource):

        @api.doc( description='Get list of warehouses')
        @api.marshal_list_with(warehouse_model, code=200)
        def get(self,):
            warehouses = db_manager.warehouse.GetALL()        
            return warehouses, 200

        @jwt_required()
        @api.doc(
            description="Create new warehouse",
            security="jsonWebToken"
            )
        @api.expect(warehouse_model)
        @api.marshal_with(warehouse_model, code=200)
        def post(self):
            id = parse_dict_key(api.payload, 'id')
            name = parse_dict_key(api.payload, 'name')
            
            if id is None or not name:
                return {"error": "invalid body"}, 400

            id = parse_int(id)
            if id is None:
                return {"error": "invalid id"}, 400
            if not api.payload['name']:
                return {"error": "empty name is not allowed"}, 400
            wh = db_manager.warehouse.Insert(name)
            if not wh:
                return {"error": "database error inserting model"}, 400
            return wh, 201
        
    @api.route("/homeView")
    class WarehouseListget(Resource):
        @api.doc('Get an order based on CustomerID')
        def get(self,):
            newtest = db_manager.warehouse_inventory.showSmartAll()
            if newtest == []:
                return jsonify({'message': 'Order does not exist'}, 404)
            else:
                return newtest
        
    @api.route('/<int:id>')
    class WarehouseDetail(Resource):
        
        @api.doc(
            description='Get warehouse by ID')
        @api.marshal_with(warehouse_model, code=200)
        def get(self, id):
            wh = db_manager.warehouse.GetByID(id)
            if not wh:
                return {"error": "warehouse not found"}, 404
            return wh, 200

        @jwt_required()
        @api.doc(
            description='Update warehouse of ID',
            security="jsonWebToken")
        @api.expect(warehouse_model)
        @api.marshal_with(warehouse_model, code=200)
        def put(self, id):            
            # find warehouse
            wh = db_manager.warehouse.GetByID(id)
            if not wh:
                return {"error": "warehouse does not exist"}, 400
            # update warehouse
            wh = db_manager.warehouse.Update(id, api.payload['name'])
            return wh, 200

            
        @jwt_required()
        @api.doc( 
            description='Delete warehouse of ID',
            security="jsonWebToken")
        def delete(self, id):
            wh = db_manager.warehouse.Delete(id)
            if not wh:
                return {"error": "warehouse not found"}, 404

            return {"message": "warehouse deleted"}, 200


    @api.route('/<int:id>/inventory')
    class InventoryDetail(Resource):
        
        @api.doc( 
            description='Get inventory of warehouse with ID')
        @api.marshal_list_with(warehouse_item_model)
        def get(self,id):
            wh_entries = db_manager.warehouse_inventory.GetByWarehouseID(id)            
            if not wh_entries:
                return {"error": "warehouse not found"}, 404

            return wh_entries, 200
            
        
        @jwt_required()
        @api.doc( 
            description='Create inventory item of warehouse with ID',
            security="jsonWebToken")
        @api.expect(warehouse_item_model)
        @api.marshal_with(warehouse_item_model)
        def post(self,id):
            # check for key errors
            product_id = parse_dict_key(api.payload, 'product_id')
            warehouse_id = parse_dict_key(api.payload, 'warehouse_id')
            quantity = parse_dict_key(api.payload, 'quantity')
            # check for value errors
            id_= parse_int(id)
            product_id = parse_int(product_id)
            warehouse_id = parse_int(warehouse_id)
            quantity = parse_int(quantity)
            if id_ is None or\
                product_id is None or\
                warehouse_id  is None or\
                quantity is None:
                return {"error": "bad request"}, 400
            wh = db_manager.warehouse.GetByID(id)
            if not wh:
                return {"error": "warehouse not found"}, 404
            
            item = db_manager.warehouse_inventory.Insert(
                warehouse_id,
                product_id, 
                quantity)            
            return item, 201

    @api.route('/<int:id>/inventory/<int:item_id>')
    class InventoryList(Resource):
        
        @api.doc( 
            description='Get inventory item with item_id from warehouse with ID')
        @api.marshal_with(warehouse_item_model)
        def get(self,id,item_id):
            wh_entries = db_manager.warehouse_inventory.GetByWarehouseID(id)  
            if not wh_entries:
                return {"error": "warehouse not found"}, 404
            item = next((i for i in wh_entries if i['id'] == item_id), None)
            if not item:
                return {"error": "item not found"}, 404
            return item, 200

        @jwt_required()
        @api.doc( 
            description='Update inventory item with item_id from warehouse with ID',
            security="jsonWebToken")
        @api.expect(warehouse_item_model)
        @api.marshal_with(warehouse_item_model)
        def put(self,id,item_id):            
            wh = db_manager.warehouse.GetByID(id)
            if not wh:
                return {"error": "warehouse not found"}, 404
            item = db_manager.warehouse_inventory.GetByID(item_id)
            if not item:
                return {"error": "item not found"}, 404
            # check for key errors
            product_id = parse_dict_key(api.payload, 'product_id')
            warehouse_id = parse_dict_key(api.payload, 'warehouse_id')
            quantity = parse_dict_key(api.payload, 'quantity')
            item = db_manager.warehosue_inventory.Update(
                item_id,
                warehouse_id,
                product_id,
                quantity
                )        
            return item, 200

        @jwt_required()
        @api.doc( 
            description='Delete inventory item with item_id from warehouse with ID',
            security="jsonWebToken")
        def delete(self,id,item_id):            
            wh = db_manager.warehouse.GetByID(id)
            if not wh:
                return {"error": "warehouse not found"}, 404
            item = db_manager.warehouse_inventory.GetByID(item_id)
            if not item:
                return {"error": "item not found"}, 404

            result = db_manager.warehouse_inventory.Delete(item_id)
            if not result:
                return {"error": "inventory not deleted"}, 400
            return {"message": "inventory deleted"}, 200


    return api