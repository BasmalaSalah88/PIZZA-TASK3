
class Payment:
    def process_payment(self, method, amount):
        if method == "PayPal":
            return f"Payment of ${amount} processed via PayPal."
        elif method == "Credit Card":
            return f"Payment of ${amount} processed via Credit Card."
        else:
            return "Invalid payment method."
