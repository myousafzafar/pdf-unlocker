import pikepdf

# Set the filename of the locked and unlocked PDFs
locked_pdf = "file.pdf"
output_pdf = "unlocked.pdf"

# Brute-force 4-digit passwords: 0000 to 9999
# To try more digits, increase the range (e.g., range(100000) for 5-digit, and so on...)
for i in range(10000):
    password = f"{i:04d}"  # Format number as 4-digit string (e.g., 0001, 0423). For 5-digit string, use '{i:05d}', and so on...
    try:
        # Attempt to open the PDF with the current password
        with pikepdf.open(locked_pdf, password=password) as pdf:
            print(f"[✓] Password found: {password}")
            pdf.save(output_pdf)
            print(f"[→] Unlocked PDF saved as: {output_pdf}")
            break  # Exit loop when password is found
    except pikepdf.PasswordError:
        continue  # Try the next password if current one fails
