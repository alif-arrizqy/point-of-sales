import uuid
import requests
from rest_framework.response import Response
from .serializers import TransactionSerializer

class ResponseHelper():
    def __init__(self, status, message, data=None):
        self.status = status
        self.message = message
        self.data = data

    def helper_response(self):
        return Response({
            'status_code': self.status,
            'message': self.message,
            'data': self.data
        })

    def helper_response_without_data(self):
        return Response({
            'status_code': self.status,
            'message': self.message,
        })


class ValidationItemHelper():
    def __init__(self, data):
        self.data = data

    def item_validation(self):
        '''
        method helper to validate item
        '''
        transaction = self.data['transaction']
        for item in transaction:
            data = {
                "name": item['item'],
            }
            try:
                req = requests.get(
                    'http://localhost:8002/item/find-name/', data=data)
                resp = req.json()
                if resp.get('status_code') == 404:
                    return False
                else:
                    return True
            except:
                None

    def item_info(self):
        '''
        method helper to get item info
        '''
        transaction = self.data['transaction']
        # append to list
        item_info = []
        for item in transaction:
            data = {
                "name": item['item'],
            }
            try:
                req = requests.get(
                    'http://localhost:8002/item/find-name/', data=data)
                resp = req.json()
                item_info.append(resp.get('data')[0])
            except:
                None
        return item_info


class ValidationBuyerHelper():
    def __init__(self, data):
        self.data = data

    def buyer_validation(self):
        '''
        method helper to validate buyer
        '''
        transaction = self.data['transaction']
        for name in transaction:
            data = {
                "name": name['buyer'],
            }
            try:
                req = requests.get(
                    'http://localhost:8001/user/find-name/', data=data)
                resp = req.json()
                if resp.get('status_code') == 404:
                    return False
                else:
                    return True
            except:
                None

    def buyer_info(self):
        '''
        method helper to get buyer info
        '''
        transaction = self.data['transaction']
        buyer_info = []
        for name in transaction:
            data = {
                "name": name['buyer'],
            }
            try:
                req = requests.get(
                    'http://localhost:8001/user/find-name/', data=data)
                resp = req.json()
                buyer_info.append(resp.get('data')[0])
            except:
                None
        return buyer_info


class BodyTransactionHelper():
    def __init__(self, data):
        self.data = data

    def serialize_data(self):
        '''
        method helper to parse data to serializers
        '''

        trans = self.data['transaction']

        # validation
        item = ValidationItemHelper(data=self.data)
        item_info = item.item_info()

        buyer = ValidationBuyerHelper(data=self.data)
        buyer_info = buyer.buyer_info()

        for transaction in trans:
            buyer_name = transaction["buyer"]
            item_name = transaction["item"]

            # Check if buyer name is valid
            if not any(buyer["name"] == buyer_name for buyer in buyer_info):
                print(f"Invalid buyer name: {buyer_name}")
                continue
            
            # Check if item name is valid
            if not any(item["name"] == item_name for item in item_info):
                print(f"Invalid item name: {item_name}")
                continue
            
            # valid_transactions.append(transaction)
            serializer = TransactionSerializer(data=transaction)
            if serializer.is_valid():
                serializer.save()
        
        return True


    def parser_data(self):
        '''
        method helper to parse data from request body
        '''
        trans = self.data['transaction']

        # calculate the total transaction
        total_transaction = len(trans)

        # calculate the total quantity per item
        item_quantities = {}

        for transaction in trans:
            item_name = transaction["item"]
            qty = transaction["quantity"]

            if item_name in item_quantities:
                item_quantities[item_name] += qty
            else:
                item_quantities[item_name] = qty

        # Find the best selling item
        best_selling_item = max(item_quantities, key=item_quantities.get)

        # Find the best selling category
        data = {
            "name": best_selling_item,
        }
        req = requests.get('http://localhost:8002/item/find-name/', data=data)
        resp = req.json()
        best_selling_category = resp.get('data')[0]['type']

        # collect data
        item = ValidationItemHelper(data=self.data)
        item_info = item.item_info()

        buyer = ValidationBuyerHelper(data=self.data)
        buyer_info = buyer.buyer_info()

        # rpc
        revenue_per_item = self.calculate_transaction_revenue_item(trans, item_info, buyer_info)

        rpc = []
        for item_name, revenue in revenue_per_item.items():
            rpc.append({
                "category": item_name,
                "revenue": revenue
            })

        # calculate the total revenue
        total_revenue = 0
        for revenue in revenue_per_item.values():
            total_revenue += revenue

        # best spenders
        total_spending_per_buyer = self.calculate_total_spending(trans, item_info, buyer_info)

        # Sort buyers by total spending in descending order
        sorted_buyers = sorted(total_spending_per_buyer.items(), key=lambda x: x[1], reverse=True)

        spenders = []
        for buyer_name, total_spending in sorted_buyers:
            buyer_type = next(buyer["type"] for buyer in buyer_info if buyer["name"] == buyer_name)
            spenders.append({
                "name": buyer_name,
                "type": buyer_type,
                "total_spending": total_spending
            })

        data = {
            "totalTransaction": total_transaction,
            "bestSeller": best_selling_item,
            "bestSellingCategory": best_selling_category,
            "rpc": rpc,
            "revenue": total_revenue,
            "bestSpenders": spenders
        }

        return data

    def calculate_transaction_revenue_item(self, trans, item_info, buyer_info):
        '''
        method helper to calculate transaction revenue per item
        '''

        total_revenue_per_item = {}

        for transaction in trans:
            buyer_name = transaction["buyer"]
            item_name = transaction["item"]
            qty = transaction["quantity"]

            # Find buyer's type
            buyer_type = None
            for buyer in buyer_info:
                if buyer["name"] == buyer_name:
                    buyer_type = buyer["type"]
                    break

            if buyer_type is None:
                continue  # Skip if buyer type is not found

            # Find item's price based on buyer's type
            item_price = None
            for item in item_info:
                if item["name"] == item_name:
                    type_item = item["type"]
                    item_price = item[buyer_type + "_price"]
                    break

            if item_price is None:
                continue  # Skip if item price is not found

            # Calculate transaction revenue
            transaction_revenue = item_price * qty

            # Update total revenue for the item
            if type_item in total_revenue_per_item:
                total_revenue_per_item[type_item] += transaction_revenue
            else:
                total_revenue_per_item[type_item] = transaction_revenue

        return total_revenue_per_item

    def calculate_total_spending(self, trans, item_info, buyer_info):
        '''
        method helper to calculate total spending per buyer
        '''
        
        total_spending_per_buyer = {}

        for transaction in trans:
            buyer_name = transaction["buyer"]
            item_name = transaction["item"]
            qty = transaction["quantity"]

            # Find buyer's type
            buyer_type = None
            for buyer in buyer_info:
                if buyer["name"] == buyer_name:
                    buyer_type = buyer["type"]
                    break

            if buyer_type is None:
                continue  # Skip if buyer type is not found

            # Find item's price based on buyer's type
            item_price = None
            for item in item_info:
                if item["name"] == item_name:
                    item_price = item[buyer_type + "_price"]
                    break

            if item_price is None:
                continue  # Skip if item price is not found

            # Calculate transaction spending
            transaction_spending = item_price * qty

            # Update total spending for the buyer
            if buyer_name in total_spending_per_buyer:
                total_spending_per_buyer[buyer_name] += transaction_spending
            else:
                total_spending_per_buyer[buyer_name] = transaction_spending

        return total_spending_per_buyer
