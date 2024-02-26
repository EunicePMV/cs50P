# Invoice Generator
#### Video Demo: <URL HERE>
#### Description:
<div style='text-align: justify;'>
The project is about generating electronic invoice using the customer information such as name, address, product details (name, quantity, price), total amount due and important dates like issuance and due.
</div>

<!-- explain files i wrote for hte project contains and does -->
## Content of Each File
1. project.py
    - <div style='text-align: justify;'> The file contains the main function including the other functions that helps to facilitate the goal to generate an electronic invoice. Upon execution, it will generate a "rendered.html" file that rendered customer data, and additionally generates an "invoice.pdf", which converts the html file to pdf format. The two mentioned files remained in the folder, serving as examples for viewing purposes, showcasing outputs generated during development.
    </div>
2. test_project.py
    - <div style='text-align: justify;'> The file contains the three testing functions for the "project.py" - organized_data(), get_date() and get_total(). In test_organized_data(), verifies the function that accepts two list that compose of the customer information and order and convert into dictionary data type. In test_get_date() verifies the accuracy of the function in returning the due date according to the issuance date; the issuance_date parameter is provided solely for testing purposes onlt 

    the function to return correct due date according to the issuance date invoice, the passing of the issued_date is only done to test if it will output correct due date. Lastly, the test_get_total() assessed the function that gets the total amount to be paid in the dictionary data type that composed of the products of the customer, based on the quantity of item ordered.
    </div>


<!-- project.py
    - rendered.html
    - invoice.pdf
test_project.py
/templates/invoice.html -->
