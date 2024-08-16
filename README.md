Introduction
This code is a simple console-based application for a virtual cafe, named "Mini Cafe." Here's a breakdown of what the code does:

1.Menu Creation:
   - The `menu` dictionary is defined to store the items available in the cafe along with their prices. The keys are the names of the items (e.g., `"Cold Coffee"`), and the values are their corresponding prices (e.g., `80`).

2.Welcome Message:
   - The program prints a welcoming message to the user, introducing them to the cafe.
   - It then displays the entire menu with item names and prices.

3. Order Processing:
   - An `order_total` variable is initialized to zero. This will store the cumulative total of the user's order.
   - The program prompts the user to enter the name of the item they would like to order.
   - It checks if the entered item is available in the `menu`:
     - If available, the item's price is added to the `order_total`.
     - If not available, the program informs the user that the item is not on the menu.

4. Adding More Items:
   - The program asks the user if they would like to order additional items.
   - It allows the user to order up to three items:
     - For each item, the program checks if it exists in the `menu` and adds the price to the `order_total` if it does.
     - If an item is not available, the user is informed accordingly.

5. Final Total:
   - After the user has completed their order, the program calculates and displays the total amount that needs to be paid.

6. Farewell Message:
   - Finally, the program prints a thank-you message, encouraging the user to visit the cafe again.

Summary:
This code demonstrates how to use basic programming concepts such as dictionaries, conditional statements, and user input handling to create a simple yet functional application. The user interacts with the program to place an order, and the program processes the order by checking availability and calculating the total cost.
