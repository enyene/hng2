
def operation(operation_type,x,y):
    if operation_type in ['addition', 'add', 'plus', 'sum', 'total']:
        result = x + y
        return result
    elif operation_type in ['subtraction', 'subtract', 'minus', 'deduct', 'sub']:
        result = x - y
        return result
    elif operation_type in [ 'multiplication' , 'multiply' ,'times' ,'mul' ,'product']:
        result = x * y
        return result
