This is a nursery webiste built out of Django , HTML , CSS and Bootstrap.

Functionalities:

Sign Up and Login(Authorization and Authentication):

  1. User can sign up with their username , email address and password.
  2. On signup , redirects to Login Page and they can login.
  3. Login takes the user to the page where they can view all the plants.  


User:

1. Can see all the plants along with its image , price and category
2. Add to Cart functionality with more than 1 items. User can add / delete items from the cart. On adding or removing items, the cart shows its count on its side.
3. User can view the cart for the current orders with the total price
4. Checkout functionality - redirects to a new page "Your Orders" where the user can view all his/her orders after entering their address and phone number
5. User can see the status of their order items in "Your Orders" page. It is either pending(yellow colour) or delivered(green). User can also see the date of the order for that      particular item.
6. User can view their orders, with the most recent order at the top
7. User can also see his/her contact information while navigating in the plants page.

Admin:

1. Admin login via <website-name>/admin OR directly login using interface login page with username="Administrator" password="########"
2. Admin can then see his dashboard where he/she can see the count of TOTAL ORDERS , PENDING ORDERS , DELIVERED ORDERS, RECENT ORDERS FROM EACH CUSTOMER , CUSTOMERS
3. Admin can go to invidual customer's name and can view their orders.
4. Admin can go to recent orders and update the order details. E.g. if the admin updates an order as Delivered, it will reflect in the user's 'Your Orders' where he/she can view the updated status.
5. Admin can also delete a particular order. The change will be reflected in the user's Orders Page as well.
6. Admin can click on "View" for each customer and see the information of customer, their orders , their order state and the date on which thier order was placed

Concepts Used:

1. Django | Python
2. Git
3. Github
4. Sessions
5. Web Hosting via cloud
6. Database Designing and their Relations
7. Filters
8. HTML,CSS,Bootstrap
9. Administration 


@Author - Tanusree Basak