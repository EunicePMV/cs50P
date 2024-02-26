# Invoice Generator

#### Video Demo: <URL HERE>

#### Description:
<div style='text-align: justify;'>
    Generating accurate and timely invoices is crucial for companies, as one incorrect information can potentially lead to significant problems. Errors may cause confusion or suspicion from customers that may lead to loss of their loyalty. Hence, it will be a great help to automate the invoice generation process that is more efficient and flawless. In the project, customer details should be entered and the application would fill the invoice and calculate the total amount needed to be paid.
</div>
<br/>
<div style='text-align: justify;'>
    The invoice generator first prompts the user to enter the customer information such as name, address, and product details (name, quantity, price). Afterward, generate invoice in PDF format, presenting customer's information and purchased items in a table format, additionally, like other invoices that includes the total amount due and important dates like issuance and deadline, that were set to be paid after three months.
</div>
<br/>
<div style='text-align: justify;'>
    In the development process of the project, both Jinja2 and WeasyPrint were utilized. Jinja2 was used to structure the invoice template to render customer data dynamically within the HTML file. It populated the template with the data entered by the user, and afterward, saved the HTML file that includes the customer information. The WeasyPrint was used to convert HTML file into PDF format that way it can be saved and forwarded to the designated customer.
</div>
<br/>
<div style='text-align: justify;'>
    In summary, the project aimed to streamline the manual generation of invoices that will benefit businesses mostly small enterprices to facilitate the process of customer's invoice that will be more accurate and efficient, potentially leading to increase in sales and fostering greater customer loyalty. In essence, the automation enhance customer satisfaction and operational efficiency constributes to the growth that lead for more success in their business ventures.
</div>

## Content of Each File
1. project.py
- <div style='text-align: justify;'>
    The file contains the main function including the other functions that helps to facilitate the goal to generate an electronic invoice. Upon execution, it will generate a "rendered.html" file that rendered customer data, and additionally generates an "invoice.pdf", which converts the html file to pdf format. The two mentioned files remained in the folder, serving as examples for viewing purposes, showcasing outputs generated during development.
</div>

2. test_project.py
- <div style='text-align: justify;'>
    The file contains the three testing functions for the "project.py" - organized_data(), get_date() and get_total(). In test_organized_data(), it verifies the function that accepts two list that compose of the customer information and order which combined and convert lists into one dictionary data type. In test_get_date(), it verifies the accuracy of the function in returning the due date according to the issuance date; the issuance_date parameter is provided solely for testing purposes only to validate the correct due date output. Lastly, the test_get_total() verifies the function that gets the total amount to be paid in the dictionary data type that composed of the products of the customer, considering the quantity of items ordered.
</div>

3. templates/invoice.html
- <div style='text-align: justify;'>
    The file contains the invoice template, where data is structured using Jinja2 syntax to be able to render data dynamically. When "project.py" is executed, it prompts user for customer details, which are then populated into the template.
</div>
