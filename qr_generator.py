import qrcode

data = input("🔗 Enter text or URL to generate QR code: ")
qr = qrcode.make(data)
qr.save("qrcode.png")
print("✅ QR code saved as 'qrcode.png'.")
