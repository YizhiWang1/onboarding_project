# About The Project

This project automatically extracts the following auction information from LiveAuctioneers:

- **Date**
- **Auction Title**
- **Timed**
- **Items**
- **Bids**
- **Bidders**
- **Sold**

It scrapes data from **page 1 to page 5**, and **stops at the end of March 13, 2025** based on a cutoff time.

---

## How to Run

### 1. Install dependencies

```bash
pip install selenium webdriver-manager
```

### 2. Add credentials to basic_config,json:
        {
            "username": "your_email@example.com",
            "password": "your_password"
        }

### 3. run main.py



## Output will be saved to:
    post_auctions.json:

        {
            "date": "2025-03-14 1:00PM",
            "auction title": "Shine Bright - Lab Grown Diamonds",
            "timed": "*",
            "items": "1250",
            "bids": "3 (3)",
            "bidders": "5 (0)",
            "sold": "$0 (0%)"
        }
    
