#### Execution:

```
pip3 install --upgrade google-cloud-documentai
python3 document_ai.py
```

#### Output:
```
Full document text: 'Sliced Invoices\nInvoice\nInvoice Number\nInvoice Date\nDue Date\nIN-76889987977778\nFebruary 8, 2022\nFebruary 22, 2022\nFrom:\nDEMOSliced Invoices\nSuite 5A-1204\n123 Somewhere Street\nYour City AZ 12345\nadmin@slicedinvoices.com\nTotal Due\n$180.00\nTo:\ndasf\nsafasf\nopolsonk@gmail.com\nQty\nDescription\nRate\nDiscount\nSub Total\n12\ntest\n$5.00\n0.00%\n7\n$5.00\n0.00%\njggfjfgfj\nfgjsfdjgfsjfgj\n$60.00\n$35.00\n$85.00\n85\n$1.00\n0.00%\nSub Total\n$180.00\n$0.00\nTax\nTotal Due\n$180.00\nPayment can be made via check:\n123 Somewhere St\nSomewhereville, CA 90210\nANZ Bank\nACC # 1234 1234\nBSB # 4321 432\nSWIFT: 12333211\nPayment is due within 30 days from date of invoice. Late payment is subject to fees of 5% per month.\ninfo@slicedinvoices.com\nslicedinvoices.com\n555 1234 123\nPage 1/1\n'

There are 1 page(s) in this document.


**** Page 1 ****
Found 3 table(s):
Table with 2 columns and 3 rows:
Collumns: 'Invoice Number' | 'IN-76889987977778'
First row data: 'Invoice Date' | 'February 8, 2022'

Table with 5 columns and 3 rows:
Collumns: 'Qty' | 'Description' | 'Rate' | 'Discount' | 'Sub Total'
First row data: '12' | 'test' | '$5.00' | '0.00%' | '$60.00'

Table with 2 columns and 2 rows:
Collumns: 'Sub Total' | '$180.00'
First row data: 'Tax' | '$0.00'

Found 13 form fields:
    * 'Invoice Number': 'IN-76889987977778'
    * 'Due Date': 'February 22, 2022'
    * 'Invoice Date': 'February 8, 2022'
    * 'SWIFT:': '12333211'
    * 'Tax': '$0.00'
    * 'Total Due': '$180.00'
    * 'From:': 'DEMOSliced Invoices\nSuite 5A-1204\n123 Somewhere Street\nYour City AZ 12345\nadmin@slicedinvoices.com'
    * 'Sub Total': '$180.00'
    * 'Total Due': '$180.00'
    * 'To:': 'dasf\nsafasf\nopolsonk@gmail.com'
    * 'BSB #': '4321 432'
    * 'ACC #': '1234 1234'
    * 'Payment can be made via check:': '123 Somewhere St\nSomewhereville, CA 90210'

```
