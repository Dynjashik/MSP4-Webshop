

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

<span  id="deployment"></span>
## Deployment

### Heroku & AWS
Instructions below describe how to deploy this project using Heroku and Amazon Web Services (AWS).

Prerequisits:

- Clone the repository and have the command line ready.
- There are some dependencies that are specifically required for deploying an app to Heroku. In order to prevent any errors during deployment process install all libraries in requirements.txt file:
```
pip install -r requirements.txt
```

This deployment process is designed to use fixtures in order to load data to the database.
You should update JSON files in _fixtures/_ directory with your own custom data if required.

#### Heroku

##### Create Heroku app
1. Create an account [here](https://www.heroku.com/) and login.
2. Start creating new application by clicking _New -> Create new app_.
3. Give the app a unique name using lowercase letters, numbers and dashes.
4. Choose a region closest to you.

##### Create Heroku Database
5. Switch to _Resources_ tab, use _Add-ons_ search field to find _Heroku Postgress_ addon and select it.
6. Select a plan that fits you and proceed by clicking confirmation button.

##### Load data to Heroku Database
7. Run the following command in your terminal to avoid possible known problem before proceding to the next step:
```
unset PGHOSTADDR
```
8. We should temporarily make a change in _setting.py_ in order to load data from local environment to Heroku database:
In settings.py change a piece of code from:
```python
  if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
    else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```

	to:

```python
  DATABASES = {
    'default': dj_database_url.parse(_<your_db_url>_)
  }
```
_<your_db_url>_ you can find in Config Vars under "Settings" tab at your Heroku dashboard.

9. Run the following command to make sure that everything is set up correctly. You should see a printed list of apps and migration script name:"
```
python3 manage.py showmigrations
```
10. Run the following command to apply migrations and set up a database:
```
python3 manage.py migrate
```
11. Load data to the database from fixtures by running following commands in this specific order (products depend on categories):
```
python3 manage.py loaddata skill_categories
python3 manage.py loaddata env_categories
python3 manage.py loaddata products
```
12. Create superuser (admin) for your app by running the following command and follow instructions in the console:
```
python3 manage.py createsuperuser
```
13. Revert the changes made in step #8 in _settings.py_

##### Add Config Vars to Heroku
14. Go to _Setting_ tab on your Heroku dashboard and click _Reveal Config Vars_ in _Config Vars_ section. Add following variables:
  * DISABLE_COLLECTSTATIC = 1 (disabling collecting static files by Heroku, we will remove it later)
  * SECRET_KEY = _<generated_key>_
  _<generated_key>_ you can get [here](https://miniwebtool.com/django-secret-key-generator/)

##### Last steps

15. Add name of your Heroku app to ALLOWED_HOSTS list in _settings.py_.
16. Login to Heroku via command line:
```
heroku login
```

or without opening a browser

```
heroku login -i
```
17. Initialize Heroku git remote for your app:
```
heroku git:remote -a <name_of_your_app>
```
18. Push the app to Heroku:
```
git push heroku master
```

or

```
git push heroku
```

At this point you are finished setting up Heroku app.

##### (Optional) Set automatic deployment to Heroku on every push to GitHub:
19. On you Heroku Dashboard go to _Deploy_ tab choose _Deployment method GitHub_ and choose your repository to connect.
20. Once connected click _Enable Automatic Deploys_.


#### Amazon Web Services (AWS)

AWS is used to host static and media files.

##### Create S3 Bucket
1. Create account [here](https://aws.amazon.com/).
2. Login to your _AWS Management Console_.
3. In search box type _S3_ and select _S3_ (Scalable Storage in the Cloud).
4. Click _Create Bucket_.
5. Type in a bucket name and select closest region to you.
6. Uncheck _Block all public access_ checkbox and check _I aknowledge.._ popup message.
7. Click _Create bucket_.

##### Configure S3 Bucket
8. Open your newly created bucket dashboard, go to _Properties_ tab and select to edit _Static website hosting_ option.
9. Select option to host a static website, fill in default values like _index.html_/_error.html_ (we will not use them).
10. Click _Save_
11. Navigate to _Permissions_ tab -> _Cross-origin resource sharing (CORS)_ and add following configuration:
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
12. Navigate to _Permissions_ tab -> _Bucket Policy_, 
13. Save _Bucket ARN_ somewhere. You will need it several times in the future during this instructions.
14. Navigate to _Edit_ -> _Policy Generator_:
   * Type of Policy - S3 Bucket Policy
   * Principal - * 
   * Actions - GetObject
   * Amazon Resource Name (ARN) - Bucket ARN from step #13
13. Click _Add Statement_, then _Generate Policy_, copy configuration settings from the popup window
14. Paste those settings to the Bucket Policy editor and add _/*_ in the end of _Resource_ key, click save.
15. Navigate to _Permissions_ tab -> _Access Control List_, check _List_ objects to _Everyone (public access)_, click _Save_.

##### Set user with Identity and Access Management (IAM)

Create Group and attach Policy

16. In your AWS Management Console in search box type _IAM_ and select _IAM_.
17. Create new user group.
18. Click _Policy_ -> _Create Policy_.
19. Change to JSON tab, click _Import managed policy_
20. Search for _S3FullAccess_ policy and import it.
21. Change _*_ for _Resource_ key to _["<your_bucket_arn>", "<your_bucket_arn>*"]_ (<your_bucket_arn> from step #13).
22. Click _Review Policy_, give it a name/description and create policy.
23. Go to your user group created earlier and under _Permissions_ tab attach a policy you just created.

Create User

24. Go to _Users_ -> _Add User_.
25. Give user a name and select _Programmatic Access_, click _Next_.
26. Add a user to the group created above.
27. Click _Create User_.
28. Download and save .csv file with user credentials.
29. Add following Config Vars to your Heroku app and use data from the file downloaded in previous step:
  * AWS_ACCESS_KEY_ID = <access_key_id>
  * AWS_SECRET_ACCESS_KEY = <secret_access_key>

##### Last Steps
30. Add following Config Var to your Heroku app:
  * USE_AWS = True
31. Remove DISABLE_COLLECTSTATIC Config Var from your Heroku app.
32. In _settings.py_ update AWS_STORAGE_BUCKET_NAME parameter with your bucket name.
33. Go to your AWS Bucket dashboard and create media/ folder.
34. Upload all of your images to that folder. Choose _Grant public read access_ under _Permissions_.

#### Stripe & Email

##### Stripe
1. Go to your Stripe account -> _ Developers_ -> _API Keys_.
2. In Heroku create following Config Vars and use API key information from Stripe:
  * STRIPE_PUBLIC_KEY = <public_key_from_stripe>
  * STRIPE_PRIVATE_KEY = <private_key_from_stripe>
4. Create new Webhook in Stripe using _<heroku_app_url>/checkout/wh/_ as an _Endpoint URL_. Select _Payment Intent_ events.
5. Add STRIPE_WH_SECRET Config Var in Heroku with webhook signing secret.

##### Email
This project supports gmail account configuration.
After you have all the settings set in your Gmail you need to add two Config Vars to Heroku:
  * EMAIL_HOST_USER: <your_email_address>
  * EMAIL_HOST_PASS: <password_generated_by_gmail>
