from flask import Flask, request, jsonify  
import electrum  
  
app = Flask(__name__)  
  
# Set up the Electrum client  
ecl = electrum.ElectrumClient('electrumx-core.1209k.com', 50002, ssl=True)  
  
# Function to generate a new address  
def generate_address():  
   address = ecl.get_new_address()  
   return address  
  
# Function to verify the Bitcoin payment  
def verify_payment(address, amount):  
   payment = ecl.get_payment(address, amount)  
   if payment:  
      return True  
   else:  
      return False  
  
# Function to send the donor's information to you  
def send_donor_info(name, email, address, city, state, zip, donation_amount, gift_choice):  
   # Send the information to your email or server using a service like SendGrid or Mailgun  
   # For this example, we'll just log the information to the console  
   print(f"Donor Information:  
  Name: {name}  
  Email: {email}  
  Address: {address}  
  City: {city}  
  State: {state}  
  Zip: {zip}  
  Donation Amount: {donation_amount} BTC  
  Gift Choice: {gift_choice}")  
  
@app.route('/donate', methods=['POST'])  
def donate():  
   data = request.get_json()  
   name = data['name']  
   email = data['email']  
   address = data['address']  
   city = data['city']  
   state = data['state']  
   zip = data['zip']  
   donation_amount = data['donation_amount']  
   gift_choice = data['gift_choice']  
  
   # Generate a new address for the payment  
   payment_address = generate_address()  
  
   # Verify the payment  
   payment_verified = verify_payment(payment_address, donation_amount)  
  
   if payment_verified:  
      # Send the donor's information to you  
      send_donor_info(name, email, address, city, state, zip, donation_amount, gift_choice)  
  
      # Return a success message  
      return jsonify({'message': 'Payment successful! Thank you for your donation!'})  
   else:  
      # Return an error message  
      return jsonify({'message': 'Payment failed. Please try again.'})  
  
if __name__ == '__main__':  
   app.run(debug=True)