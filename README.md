

## Table of Contents

1.  <a  href="#overview">**Overview**</a>

1.  <a  href="#purpose">**Purpose & Motivation**</a>

2.  <a  href="#ux">**User Experience (UX)**</a>

3.  <a  href="#design">**Design & Development**</a>

4.  <a  href="#userstories">**User Stories**</a>

5.  <a  href="#wireframes">**Wireframes**</a>

6.  <a  href="#technologies">**Technologies**</a>

7.  <a  href="#features">**Features**</a>

8.  <a  href="#testing">**Testing**</a>

9.  <a  href="#deployment">**Deployment**</a>

10. <a  href="#database">**Database**</a>

11. <a  href="#credits">**Credits**</a>

12. <a  href="#acknowledgements">**Acknowledgements**</a>

<span  id="overview"></span>
## Overview
Baby Hero is an e-commerce web store offering a wide range of toys & accessories for babies under 1 year old. It is a full-stack application that is designed to help customers understand the usage of the products and its functional purpose. It is possible for unregistered users to get to know all the products in stock and purchase them with ease. Additionally, customers can register their profiles, save their personal information for faster checkout process and view order history. There is a news feed that broadcasts  latest store updates for all the visitors of the site. Also users have a possibility to contact webshop administration with a help of a special contact form provided on the site.

<span  id="purpose"></span>
## Purpose and Motivation
There is a huge amount of toy shop out there, both online and physical ones. Most of them have a very broad spectrum of products for all kind of usages and ages. It can get very confusing when you look for something specific, especially if you just became a parent or want to buy something as a present. That's why I saw a need to start a store specifically with products for babies under 1 year old, because it is not 100% clear what toys & accessories are fit for such fragile children. In addition I came up with an unusual categories for such shop, that would filter products by baby's skills and environment where products can be used.

The website has clear and simple design that allows users to quickly navigate and search the products. While adding products to a shopping bag the total cost will update dynamically and the user can easily track his upcoming expenses. Afterwards the user can procced to the check-out page where he can make a payment and complete an order. The order confirmation & details will be sent to the user's email.

Website admins (or superusers) has access to extended rights & functionality: manage products, news blog and contact requests. 

<span  id="userstories"></span>

## User Stories

### As a user I would like to:

#### Navigation
- **Easily understand the purpose of the website** so that **I can decide if it is relevant to me**
- **Have simple and self-explanatory navigation tools** so that I can **find products fast**
- **View multiple amount of products at once** so that I can **compare them and quicker choose the one I need**
- **View each product separately** so that I can **share a link to the product with others**
- **Be able to sort products by price** so that I can **easily compare product prices and find the cheapest products quicker**
- **Be able to filter products by type of environment where they are reccommended to be used** so that I can **make right decisions based on my needs**
- **Get responsive feedback from the web store on my actions** so that I am **aware of correctness of my actions**.

#### User account
- **Register and account** so that I can **have my personal account**
- **Login and logout** so that I can **easily access my personal information**
- **Recover my password** so that I can **get access to my personal account in case pasword was forgotten**
- **Recieve an email after registration** so that I can **be sure that my account was registered successfully**
- **Have my personal profile page** so that I can **manage my payment/billing information and view order history**

#### Shopping bag
- **Be able add products to shopping bag** so that I can **make a purchase when I am ready**
- **See an overview of all added products** so that I can **make sure that I did everything correct**
- **Modify quantity and remvoe products in my shopping bag** so that I can **make corrections to my order before making a payment**
- **Add delivery information** so that I can **recieve products to the specified address after making a payment**

#### Payment and checkout
- **Make a payment for products that are in my shopping bag** so that I can **recieve chosen products to the specified address**
- **Recieve a confirmation email with all of the order details** so that I can **have all the required information in case if emergency**


#### News and Contact
- **Contact the store owners** so that I can **leave my feedback/suggestion/complaint regarding my expierence using the site**
- **Be able to read latest updates from store admins** so that I can **be aware of all the latest news**

### As a store owner I would like to:

- **Add/modify/delete products** so that I can **be flexible and manage products that are avaialbe for purchase on the site**
- **Add/modify/delete news articles** so I can **update customers with any important information**
- **Read messages submitted by contact form** so that I can **act on cutomer's feedback appropriately**.


<span  id="features"></span>
## Features

### Existing features

#### General

1. Navigation bar on top of each page that consists of:
  a Site logo
  b Search bar
  c Main mavigation menu
  d Menu entries to Login/Register for anonymous users
  e My Account menu entry with a dropdown sub menu for authorized users
  f Shopping bag menu entry with a total amount displayed
2. Responsive layout that is adapted to desktop and mobile screen sizes.
3. Supported by all of the most popular web browsers.
4. Instant feedback from the site to the user with the help of pop-up messages when important actions take place.

#### User can:
1. View multiple products on single page.
2. View each product on separate page.
3. Search box where products can be found by name or descriprion.
4. Sort products by price, name and categories, both ascending and descending.
5. Filter prodcuts by categories.
6. Add product to the shopping bag with specified quantity.
7. View shopping bag.
8. Update quantity or Remove product(s) from the shopping bag.
9. View checkout page.
10. Submit delivery information and payment details on checkout page.
11. Complete an order and make a payment.
12. View order details on payment completion.
13. Recieve an email with order details on payment completion.
Authentication functionality that makes it possible to login/register for users.
14. View latest news and updates from the store owners.
15. Contact store owners directly from the website.
16. Register or Login to private user account.

#### Authorised User can:
1. View My Profile page
2. Updade personal delivery information that will be used to prefill checkot form
3. View order history
4. Logout from the site

### Site Administrator can: 
1. Execute all the feautures of an authorised user mentioned above.
2. Add new product(s) to the site.
3. Modify or delete existing products on the site.
4. Add new News Articles to the site.
5. Modify or delete existing News Articles on the site.
6. View contact forms submitted by users.
