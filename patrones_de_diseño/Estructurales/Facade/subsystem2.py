class Payment:
    def process_payment(self, user_id, amount):
        print(f'Usuario: {user_id} pago: ${amount}')
        return True