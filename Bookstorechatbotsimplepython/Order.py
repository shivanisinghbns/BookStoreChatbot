import re
class Order_handle:
    def Order_query(query):
        order_id_pattern = r'\b[A-Za-z]\d{3}\b'
        order_ids = re.findall(order_id_pattern,query)
        if order_ids:
            if len(order_ids)>1:
                response="Hello you are seeking information about the order ids-->"+','.join(order_ids)
            else:
                response=f"Hello you are seeking information about the order ids-->{order_ids[0]}"
        else:
            response="Can you please tell me your order number."
        return response

