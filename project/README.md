# Invoice Generator

#### Video Demo: <URL HERE>

#### Description:
<div style='text-align: justify;'>
Generation of invoice for companies is crucial that should be delivered on time and accurately, one incorrect information may lead to further conflicts that may cause massive problem to the business. Errors may cause confusion and suspicions to the customer that may lead to lost of loyal customers. 

The project is about generating electronic invoice using the customer information such as name, address, product details (name, quantity, price), total amount due and important dates like issuance and due.
</div>
<!--
problem in  generating invoice -> manual
proposed solution
tackle: jinja2 and weasyprint?
 -->
<!-- dagdag sa proj descp -->

## Content of Each File
**1. project.py**
    <div style='text-align: justify;'>
    The file contains the main function including the other functions that helps to facilitate the goal to generate an electronic invoice. Upon execution, it will generate a "rendered.html" file that rendered customer data, and additionally generates an "invoice.pdf", which converts the html file to pdf format. The two mentioned files remained in the folder, serving as examples for viewing purposes, showcasing outputs generated during development.
    </div>

**2. test_project.py**
    <div style='text-align: justify;'> The file contains the three testing functions for the "project.py" - organized_data(), get_date() and get_total(). In test_organized_data(), it verifies the function that accepts two list that compose of the customer information and order which combined and convert lists into one dictionary data type. In test_get_date(), it verifies the accuracy of the function in returning the due date according to the issuance date; the issuance_date parameter is provided solely for testing purposes only to validate the correct due date output. Lastly, the test_get_total() verifies the function that gets the total amount to be paid in the dictionary data type that composed of the products of the customer, considering the quantity of items ordered.
    </div>

**3. templates/invoice.html**
    <div style='text-align: justify;'> The file contains the invoice template, where data is structured using Jinja2 syntax to be able to render data dynamically. When "project.py" is executed, it prompts user for customer details, which are then populated into the template
    </div>
