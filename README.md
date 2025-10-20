# DVA Booking Automation Script

This Python script automates the process of checking or managing bookings on the **Northern Ireland DVA Booking Portal** using **Selenium**. It automatically logs into the DVA booking page using your credentials and navigates to the change booking section.

---

## Features

- Automates login to the [DVA booking portal](https://dva-bookings.nidirect.gov.uk/MyBookings/FindDriver)  
- Fills in your booking details automatically  
- Clicks through to the **Change Booking** section  
- Keeps the browser session open for easy manual interaction  
- Handles connection or element errors gracefully with retry logic  

---

## Requirements

Make sure you have the following installed:

- **Python 3.8+**
- **Google Chrome**
- **ChromeDriver** (matching your Chrome version)
- **Selenium**

You can install Selenium using pip:

pip install selenium

## Setup

Clone or download this repository.

Open the script and enter your details:

```bash
booking_reference = 'xxxxxxxxxx'
driver_no = 'xxxxxxxx'
date_of_birth = 'xxxxxxxx'
```

Ensure chromedriver is in your system’s PATH or in the same directory as the script.

Run the script:

    python main.py

## How It Works

  Opens the DVA Find Driver Booking page.
  Inputs the booking reference, driver number, and date of birth.
  Clicks Find Booking and then Change Booking.
  Keeps the browser open for 6 minutes (360 seconds) for further actions.
  Closes the browser automatically after that time.

If any issue occurs (e.g. page timeout, element not found), the script retries after 5 seconds.

## Example Output

Exception occurred: no such element: Unable to locate element...
In the queue. Retrying...

## Security Notes

  Do not commit or share your personal details (booking reference, driver number, DOB) in public repositories.
  Consider using environment variables or a .env file to store sensitive information securely.

