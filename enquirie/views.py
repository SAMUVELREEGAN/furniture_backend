from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from django.core.mail import EmailMessage
from .models import enquiriesModel
from .serializers import enquiriesSerializer

class enquieryCreate(CreateAPIView):
    queryset = enquiriesModel.objects.all()
    serializer_class = enquiriesSerializer

    def perform_create(self, serializer):
        enquiry = serializer.save()

        product = enquiry.Product_id
        product_name = product.pro_name
        product_price = float(product.price)
        quantity = enquiry.quantity
        total_price = product_price * quantity

        subject = "🔔 New Product Enquiry Received"
        message = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>New Product Enquiry</title>
  <style>
    body {{
      margin: 0;
      padding: 0;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background-color: #f4f4f4;
    }}
    .email-container {{
      max-width: 600px;
      margin: 30px auto;
      background-color: #ffffff;
      border-radius: 8px;
      overflow: hidden;
      box-shadow: 0 0 12px rgba(0, 0, 0, 0.05);
    }}
    .email-header {{
      background-color: #0d2b56;
      color: #ffffff;
      padding: 30px 20px;
      text-align: center;
    }}
    .email-header h1 {{
      margin: 0;
      font-size: 1.8rem;
    }}
    .email-header h2 {{
      margin: 10px 0 0;
      font-size: 1.2rem;
      font-weight: 500;
    }}
    .email-body {{
      padding: 30px 25px;
      color: #333333;
      font-size: 1rem;
    }}
    .email-body p {{
      margin: 10px 0;
      line-height: 1.6;
    }}
    .highlight {{
      color: #4a148c;
      font-weight: bold;
    }}
    .verified {{
      color: #388e3c;
      font-weight: bold;
    }}
    .email-footer {{
      padding: 20px 25px;
      border-top: 1px solid #cccccc;
      font-size: 0.95rem;
      color: #777777;
      text-align: left;
    }}
  </style>
</head>
<body>
  <div class="email-container">
    <div class="email-header">
      <h1>New Product Enquiry Received</h1>
    </div>
    <div class="email-body">
      <p>Dear <strong>Admin</strong>,</p>
      <p>New Product Enquiry Received From <strong>{enquiry.name}</strong>,</p>
      <p><strong>🛒 Product_Name:<span class="highlight">{product_name}</span></p>
      <p><strong>💰 Price:</strong> ₹{product_price:.2f}</p>
      <p><strong>📦 Quantity:</strong> {quantity}</p>
      <p><strong>🧮 Total Price:</strong> ₹{total_price:.2f}</p>
      <p><strong>📞 Phone:</strong> {enquiry.phone_number}</p>
      <p><strong>✉️ Email:</strong> {enquiry.email}</p>
    </div>
    <div class="email-footer">
       Check and  Confirmation Enquiry.
    </div>
  </div>
</body>
</html>
"""



        email_message = EmailMessage(
            subject=subject,
            body=message,
            from_email="VR Store <samuelreegan372@gmail.com>",
            to=["samuelreegan372@gmail.com"],
            reply_to=[enquiry.email],
        )
        email_message.content_subtype = "html"

        try:
            email_message.send(fail_silently=False)
        except Exception as e:
            print("Email sending failed:", e)
