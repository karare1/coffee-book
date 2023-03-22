![Logo](static/img/coffee-time.png)
# be home barista 

<!-- ![Logo](assets/favicon/favicon-32x32.png) -->
Whether you prefer your coffee black or with a little more milk and sugar, there are so many ways to prepare it that you can’t help but fall in love with this flavourable beverage all over again.
Be home barista is a web application developed for coffee lovers as well as for all occasional coffee drinkes that would like to share their coffee experience and delicious recipes online.  
It also provides a great opportunity for coffee drinkers to share their delightful local recipes with others from all around the world.
This application makes it easy for users to create and save their coffee-recipes online, as well as search for recipes and save them in their profile (coffee book).
Be home barista was designed with a UI/UX in mind and provides the functionalities a coffee-recipe sharing website should have. Users benefit from having convenient access to the data provided by all other app members.


## User Experience (UX)

### User Stories 

New User / non-signed up
- As a user, I would like to understand the purpose of the website and what the website offers.
- As a user, I would like to use the website and see the content clearly on any device.
- As a user, I would like to be able to easily navigate through the website.
- As a user, I would like to search for recipes in the website.
- As a user, I would like to explore all recipes shared on the website.
- As a user, I would like to see a full recipe version without having to sign up.
- As a user, I would like to have the option to sign up and create my own coffee book.
- As a user, I would like to navigate intuitively and spot the Sign-Up button and all other important links right away.
- As s user, I would like to find contact details in case I need to aproach the website creator.

Returning User
- As a user, I would like to easily spot a Log In button. 
- As a user, I would like to easily navigate to profile and other pages available to me.
- As a user, I would like to be able to create and share my recipes with other users.
- As a user, I would like to edit recipes I have created.
- As a user, I would like to delete recipes I have created.
- As a user, I would like to save recipes to my profile.
- As a user, I would like to have an option to remove a recipe from my coffee book.

Admin
- As an admin, I would like to edit existing recipes created by any user.
- As an admin, I would like to delete existing recipes created by any user.
- As an admin, I would like to remove any inappropriate or other offensive content shared in a user recipe.
- As an admin, I would like to have an option to create, edit or delete a category.


### Implementation 

- Used a layout with a coffee background image and coffee theme colours as well as an initial message to give users an 
  early sense of what the website is about.
- Made the website responsive, visible and easy to read on desktops, laptops, tablets and smartphones.
- The website 
- Implement a search bar for a user to find a recipe based on name, ingredients and recipe intro.
- For signed-up users a profile page has been created with two tabs - for the recipes they created themselves and recipes 
  they added to their favourites.
- If a user created/added a recipe two extra buttons appear in a full recipe pafe for them to edit or delete their
  recipes if they wish.
- Signed-up users are also provided with an extra Add/remove favourites button in full recipes for those recipes that
  have been created by other users in order to give a signed-up users an option to add these recipies into their coffee book. 
- User can find an email address on footer in case they want to contact admin.
- The same layout and navigation bar/footer are used throughout the whole website for effective manipulation.
- Sign Up and Log In buttons are easy to spot and Sign Up process is very simple.
- Addition and editing recipies are very siple as well, when editing a recipe all fields are populated with your original
  input so it is easy to make changes. 
- Even for users that do not intend to sign up, this website could be helpful and informative.


### Existing Features

- __Home Page__

- The home page is the screen the end user is presented with on page load. <br>
  All webpages have the same gray-colour background with white navigation bar and pale brown footer. Two colors have been used for fonts: brown and pale blue. All project is using warm brownish (coffee) design to match the purpose of the website.

  Base.html template has been used as a parent template, that includes the basic html structure with all important links for frameworks and libraries needed for the website to function properly. 
  The parent template also includes navbar and footer that are the same on all webpages. This support the intuitiveness of the entire website and enhances the user experience and makes the website easy to use.
  
  Home Page includes a theme picture that fits the overall layout of the website. This coffee image has been used to attract potential users and give them a hint on what the website is about. The aim is also make the website useful and intersting for the users that are already signed up to come back and share their new delicious recipes. 
  The home page also has a message attached to the background image that says why a potential user should sign up and what advantage they get. 
  The main purposure of this website is to share coffee recipies but italso gives sign-up users the opportunity to create their own online coffee book - and save the recepis they like. 
  Overall the Home page has been created to give a pleasant first impression and prompt a new visitors to click on sign up button and contribute with thier coffee recipes.

- __Recipe Page__

- In the Recipe page a user will find all recipes shared by other users or themselves. They also have the opportunity
  to search for a recipe if they are looking for a particular recipe or ingredients. 
  The website mostly consists of recipe cards with an image and a brief recipe description (recipe intro).
  If any of the shared recipes catches a users's attention, they can click on discover recipes button at the bottom of the recipe card and open the full recipe.
  Full recipe page includes all details and instructions necessary for a coffee drink preparation, such as
  recipe name, recipe brief descriprion, preparation time and serving information as well as difficulty, and two most important sections - ingredients and method.
  It also shows creator username, category and an recipe image. 
  Overall the full-recipe is divided into 4 sections for bettter readability and user experience. In ingredients section, every single ingredient is underlined and every step in method section in numbered.
  Preparation time, difficulty and serves also have Icon prefixes for a better UX snd layout.


 __Sign Up / Log In Page__
- Signing Up to the website is very simple and straightforward. The aim was to keep it as simple as possible for users
  not to get discouraged by tedious process of filling in a lot of fields.
  Sign Up form include Icon Prefixes for a better user experience and layout.
  All three fields: username, email and password need to be input in order to sign up.
  There are some restrictions when creating a username and password; username needs to have a minimum of 5 and maximum of 12 characters - all alphanumeric without spaces. Password needs to be at least 8 characters long and maximum of 20 - all alphanumeric and without spaces. 
  If a user input correct details into a sign up form and the inputed username does not already exists, they will be provided with a flash message informing them they have been succesfully signed up. Otherwise they will get a message asking them to fill in the form again. 
  All three fields have validation applied so if username, password or email do not meet criteria for signing up, red underline will appear. Green underline will indicate that all fielda have been filled correctly and the form is ready for submission. 
  Werkzeug "generate_password_hash" and "check_password_hash" method has been used for converting a user's password. 

  Log In Page includes two input fiels that need to be filled in by a registered user in order to Log-In.
  Again, both have validation applied and will indicate if the criteria for log-in have been met. If correct username and password have been used and they match the details on mongodb the user will be provided with a flash message that they have been logged in, otherwise the will prompt the user to input the correct log-in details. 

 __Profile Page__

 Profile Page is only assessible for registered users; here they can create their own coffee book. 
 It consists of a personalized greeting with a welcome message, 'Add new recipe' button to prompt a registered user to add a new recipe and share it with the coffee community and the most important part: tabs for created recipes and favourite recipes. In created recipes tab are stored all recipies that the user has added and shared on the website. In favourite recipes tab are stored all recipies created by other users and added by the logged-in user when click on 'Add to favourites' button in a full recipe page. All created recipes can be edit or deleted and all favourite recipies can be removed from favouries and add to favouries again, if a user wish to. If no recipes created or added to favourites messages will be displayed to prompt a user to create or save recipes. 
 A user can therefore create their personalized coffee book that contains both their own recipes as well as recipes they discover and like while searching or browsing on recipes page. 
 
__Adding and Editing Recipes Page__

Add recipe form will appear on screen once clicked on 'Add new recipe' button in the profile page.
Again, the adding form is simple and straightforward. It includes input fields for: recipe name, recipe image url, category, difficulty, time of prepartion, serves and the most important, ingredients and method. 
Ingredients and method input field have a button to add extra fields to input ingredients and step of preparation separately in new lines (or paragraphs). All fields are required to fill in apart from recipe image url; if the re recipe image url is not provided, a general image will be displayed instead.
All fields have validation applied or pre-populated format make it easier of a user to fill in the form and provide a correct details. 

Edit recipe form appear on screen if a user click the button on full recipe page. All original input will appear in input fields for better and more effective editting. If a user does not want to proceed and change the recipe, they can click on cancel button to go back to full recipe. If a user want to delete the created recipe they will click on 'delete' button and a confirmation pop-up block will be displayed to verify if they would like to proceed with an action.


__Coffee Category Page__
Coffee Category is displayed only if logged-in as an admin and provides an admin with an option to create, edit or delete a category. An admin also have an access to edit and delete all recipes on website in case any inapprocpiate or offensive content has been shared. Coffee category page includes a category cards with an image and 'edit' as well as 'delete' buttons. It has a 'Add coffee category' button that will redirect an admin to 'Add coffee category' form. 
'Add coffee category' form has two input fields for a category name and category image url, but the latter one is optional. When clicking on 'Edit' button, editting form will appear on the screen with the original input for simple and effective editing. If an admin does not want to edit the category, they have an option to click on 'Cancel' button and return to 'Coffee Category' page.


## Testing 

Manual Testing of implemented features: <br><br>


 - HOME PAGE Testing

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| LOGO link  | Click on the logo | It will redirect a user from any page back to the Home page | Works as expected |
| NAV BAR - HOME | Click on the Home | It will redirect a user from any page back to the Home page | Works as expected |
| NAV BAR - RECIPES| Click on the Recipes| It will redirect a user from any page to the Recipe page and is available even for non-registered users| Works as expected |
 | NAV BAR - SIGN UP| Click on the Sign Up| It will redirect a user to a Sign Up form and it is available for all users| Works as expected |
 | NAV BAR - LOG IN| Click on the Log In| It will redirect a user to a Lof In form and it is available for all users| Works as expected |
 | NAV BAR - PROFILE|Click on Profile |Profile is available only for registed users, once registered, clicking on it will redirect a registered user to the Profile page from any other page | Works as expected |
 | NAV BAR - LOG OUT|Click on Log out |Log out is available only for logged-in users, once logged in, clicking on it will log out the user from their account and redirect them to Log In page| Works as expected |
 | NAV BAR - COFFEE CATEGORIES|Click on Coffee Categories |It is available only to admin, and will redirect an admin from any other page to Coffee Categories| Works as expected |
 | FOOTER - HOME link|Click on Home link|It will redirect a user from any page back to the Home page and if on Home page it will take a user back to the top of the page| Works as expected |
 | FOOTER - RECIPES link|Click on Recipes link|It will redirect a user from any page to the Recipes page and if on Recipe page it will take a user back to the top of the page| Works as expected |
 | FOOTER -  SIGN UP link|Click on Sign Up link|It will redirect a user from any page to the Sign Up page and if on Sign Up page it will take a user back to the top of the page| Works as expected |
 | FOOTER -  LOG IN link|Click on Log In link|It will redirect a user from any page to the Log In page and if on Log In page it will take a user back to the top of the page| Works as expected |
| FOOTER -  TikTok link|Click on TikTok link|It will open a new window with TikTok website| Works as expected |
| FOOTER -  FACEBOOK link|Click on FACEBOOK link|It will open a new window with Facebook website| Works as expected |
| FOOTER -  INSTAGRAM link|Click on Instagram link|It will open a new window with Instagram website| Works as expected |
| FOOTER -  TWITTER link|Click on Twitter link|It will open a new window with Twitter website| Works as expected |
| SIGN UP button|Click on Sign Up button|It will redirect a user to a Sign Up page | Works as expected |
 <br><br>


- SIGN UP Page Testing

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| USERNAME  | Input a username | Username needs to have min. 5 and max.20 characters, no spaces and must be unique, if the same username alredy exists, a flash message will prompt the user to create another username. It is a required field, validation and pattern applied | Works as expected |
| EMAIL ADDRESS | Input an email address | It is required, validation and email pattern applied | Works as expected |
| PASSWORD | Input a password | Password needs to have min. 8 and max.20 characters, no spaces. It is a required field, validation and pattern applied | Works as expected |
| SUBMIT button| Click on Submit button| If all input fields are filled in correctly, a flash message will appear to confirm the registration and a user will be redirected to their profile page, otherwise they will be prompted to complete a form again.| Works as expected |
| LOG IN link | Click on the link| If a user is already registered, they will click on Log in link to get to the Log in page  | Works as expected |
 <br><br>


- LOG IN  Page Testing

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| USERNAME / PASSWORD | Input username / password | A user needs to input their username and password that meet all requirements  | Works as expected |
| LOG IN button| Click on Log In button| If both username and password are correct, a flash message will confirm that they are logged and will be redirected to their profile page. Otherwise, a flash message will prompt a user to input the correct details | Works as expected |
| SIGN UP link | Click on the link| If a user is not registered yet, they will click on the Sign Up link to get to the Sign Up page   | Works as expected |
 <br><br>


- RECIPE PAGE Testing

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| SEARCH bar  | Input text into the Search bar | Validation applied; minlength 3 characters, if no input or less then 3 characters - red undelined | Works as expected |
| CANCEL (Search) button | Click on Cancel button| It will remove all input from the Search bar and revert the bar into the initial position | Works as expected |
| FIND (Search) button  | Input text into Search bar and click on Find button | Input a key word from recipe name, intro or ingredients and it will find the affected recipes | Works as expected |
| DISCOVER RECIPE button | Click on Discover Recipe button | It will open a full recipe | Works as expected |
<br><br>

- FULL RECIPE PAGE Testing

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| A user not logged in | Automatic feature | No buttons displayed (Edit, Delete, Favourites) if a user is not logged in | Works as expected |
| User logged in | Automatic feature| It will display edit and delete buttons for recipes recipes created by the user and add/remove favourites button for other recipes  | Works as expected |
| Logged in as a user | Automatic feature  | Both edit and delete  buttons for all recipes + add/remove favourites for recipes not created by admin | Works as expected |
| EDIT (recipe) button | Click on Edit button | It will populate the edit recipe form with the original input | Works as expected |
| DELETE (recipe) button | Click on Delete button | It will display a message for a user to confirm they wish to delete a recipe  | Works as expected |
|CANCEL (confirmation) button | Click on Cancel button | It will redirect a user back to a full recipe  | Works as expected |
|DELETE (confirmation) button | Click on Delete button | It will delete a recipe (flash message) and redirect a user back to full recipe | Works as expected |
| ADD TO FAVOURITES button | Click on Add to favourites button | It will sent a copy of the recipe into a user's profile, button will change to 'Remove from favourites' | Works as expected |
| REMOVE FROM FAVOURITES button | Click on Remove from favourites button | It will remove a recipe from user's profile and button will change back to 'Add to favourites' | Works as expected |
<br><br>

- ADD RECIPE PAGE Testing

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| ADD NEW RECIPE button  | Click on Add new recipe | It is in profile page and available only for registered users and redirect a user to 'Add a new recipe' form | Works as expected |
| RECIPE NAME  | Input text into recipe name field | Validation applied; min.5 and max.40 characters, if no input or less then 5 characters - red undelined; it will not let a user to input more then 40 characters | Works as expected |
| RECIPE IMAGE URL  | Input url into the Recipe Image Url | It is optional to add Image URL, if not provided, alternative image will display | Works as expected |
| RECIPE INTRODUCTION | Input text into the Recipe Introduction | This field is required, validation applied; min. 5 max.125 characters| Works as expected |
| CATEGORY | Dropdown selection | This field is required, validation applied| Works as expected |
| DIFFICULTY | Dropdown selection | This field is required, validation applied| Works as expected |
| PREPARATION TIME | Input text into Preparation Time | It is required, validation applied, max.15 characters | Works as expected |
| SERVES | Pick a number from options | It is required, validation applied, min.1 max.30 | Works as expected |
| INGREDIENTS | Input text into Ingredients | It is required to input at least one line, validation applied, min.5 max.200 characters; max.20 inputs allowed | Works as expected |
| METHOD | Input text into Method | It is required to input at least one line, validation applied, min.5 max.750 charcters; max.20 inputs allowed | Works as expected |
| ADD RECIPE button  | Click on Add recipe | It will display a flash message that recipe has been successfully added, it will be automatically shared with others in recipes page and also will appear in user's 'created recipes' tab | Works as expected |
<br><br>


- EDIT RECIPE PAGE Testing

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| CANCEL button  | Click on cancel button | Once in 'Edit recipe form', if a user does not want to submit any changes, clicking on Cancel button they will be redirected to their profile page  | Works as expected |
| EDIT YOUR RECIPE button  | Click on 'Edit your recipe' button | Clicking on the button, changes will be stored and an updated recipe version will be displayed in recipes page as well as in user's profile. | Works as expected |
<br><br>
All original content has been checked - if retrieved properly - works as expected
<br>
All input fields validation and requirements - works as expected 
<br><br>

- PROFILE PAGE Testing

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| GREETING | automatic feature | Once logged in a user will see a flash message and a personalized greeting | Works as expected |
| TABS (CREATED/FAVOURITE RECIPES)  | click on the tabs | Clicking on 'created recipes' tab, all recipes created by the user will be displayed; clicking on 'favourite recipes' tab all saved favourite recipes will be displayed. If no recipies created or saved, message will appear to prompt the user to create or saved recipes | Works as expected |
| ADD NEW RECIPE button  | Click on Add new recipe | It will redirect a user to 'Add a new recipe' form | Works as expected |
<br><br>

- COFFEE CATEGORY / ADD COFFEE CATEGORY / EDIT COFFEE CATEGORY PAGE Testing

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| ADD NEW COFFEE CATEGORY button | click on the button | Only admin has access to Coffee Category page. Clicking on the button will redirect an admin to 'Add coffee category' form | Works as expected |
| EDIT (CATEGORY) button  | click on the button |  It will populate 'edit coffee category' form with the original input| Works as expected |
| DELETE (CATEGORY) BUTTON  | Click on the button | It will display a message for an admin to confirm they wish to delete a recipe  | Works as expected |
|DELETE (confirmation) button | Click on the button | It will delete a category (flash message) and redirect an admin back to coffee category page| Works as expected |
| CATEGORY NAME  | Input text into category name field | Validation applied; min.4 and max.30 characters, if no input or less then 4 characters - red undelined; it will not let an admin to input more then 30 characters | Works as expected |
| CATEGORY IMAGE URL  | Input url into the Category Image Url | It is optional to add Image URL | Works as expected |
| ADD COFFEE CATEGORY button  | Click on the button | It will display flash message (confirmation)  and redirect an admin to 'coffee category' page. New category will be added on Coffee Category page | Works as expected |
| EDIT COFFEE CATEGORY button  | Click on the button | It will display flash message (confirmation) about update and redirect an admin to 'coffee category' page. The updated category will be displayed on Coffee Category Page | Works as expected |
<br><br>
All original content has been checked - if retrieved properly - works as expected
<br>
All input fields validation and requirements - works as expected 














### Wireframes 
- [Home Desktop](static/wireframes/Home_Desktop.png)
- [Home Tablet](static/wireframes/Home_Laptop.png)
- [Home Mobile](static/wireframes/Home_Mobile.png)
- [Recipes Desktop](static/wireframes/Recipes_Desktop.png)
- [Recipes Laptop](static/wireframes/Recipes_Laptop.png)
- [Recipes Mobile](static/wireframes/Recipes_Mobile.png)
- [Sign Up Desktop](static/wireframes/Sign_Up_Desktop.png)
- [Sign Up Laptop](static/wireframes/Sign_Up_Laptop.png)
- [Sign Up Mobile](static/wireframes/Sign_Up_Mobile.png)
- [Log In Desktop](static/wireframes/Log_In_Desktop.png)
- [Log In Laptop](static/wireframes/Log_In_Laptop.png)
- [Log In Mobile](static/wireframes/Log_In_Mobile.png)
- [Profile Desktop](static/wireframes/Profile_Desktop.png)
- [Profile Laptop](static/wireframes/Profile_Laptop.png)
- [Profile Mobile](static/wireframes/Profile_Mobile.png)
- [Add Recipe Desktop](static/wireframes/Add_Recipe_Desktop.png)
- [Add Recipe Laptop](static/wireframes/Add_Recipe_Laptop.png)
- [Add Recipe Mobile](static/wireframes/Add_Recipe_Mobile.png)
- [Edit Recipe Desktop](static/wireframes/Edit_Recipe_Desktop.png)
- [Edit Recipe Laptop](static/wireframes/Edit_Recipe_Laptop.png)
- [Edit Recipe Mobile](static/wireframes/Edit_Recipe_Mobile.png)
- [Full Recipe Desktop](static/wireframes/Full_Recipe_Desktop.png)
- [Full Recipe Laptop](static/wireframes/Full_Recipe_Laptop.png)
- [Full Recipe Mobile](static/wireframes/Full_Recipe_Mobile.png)
- [Categories Desktop](static/wireframes/Categories_Desktop.png)
- [Categories Laptop](static/wireframes/Categories_Laptop.png)
- [Categories Mobile](static/wireframes/Categories_Mobile.png)
- [Add Category Desktop](static/wireframes/Add_Category_Desktop.png)
- [Add Category Laptop](static/wireframes/Add_Category_Laptop.png)
- [Add Category Mobile](static/wireframes/Add_Category_Mobile.png)
- [Edit Category Desktop](static/wireframes/Edit_Category_Desktop.png)
- [Edit Category Laptop](static/wireframes/Edit_Category_Laptop.png)
- [Edit Category Mobile](static/wireframes/Edit_Category_Mobile.png)



## Deployment
  For this project, I have used Gitpod as the IDE and the repository has been stored on GitHub. 
  The web application has been deployed on Heroku.
- There are two ways how to deploy an app on Heroku: <br> 
  a) Using Heroku command-line interface (CLI) /Heroku toolbelt
  b) Setting up automatic deployments from GitHub
  For this project,  the second option - Automatic Deployment - from my GitHub repository has been used:

- Setting up automatic deployments from GitHub: <br>
  1) Create an account on Heroku and once signed up click on the "Create New App" button.
       The app name must be unique - something that nobody else currently has and without spaces (use dash or minus instead of spaces) and all lowercase letters.
       Then select a region closest to you. 
  2) Go to Heroku 'Settings' Tab, click 'Reveal Config Vars' and input the following variables (do not include any quotes): 
        | **KEY** | **VALUE** | 
        |-------------|------------|  
        |IP  | 0.0.0.0 |
        |PORT  | 5000 |
        |SECRET_KEY | your_secret_key|
        |MONGO_URI | mongodb+srv://coffee:<password>@cluster3.jhm4r33.mongodb.net/?retryWrites=true&w=majority
        |MONGO_DBNAME |	<database_name>|
  3) Go to Gitpod workspace and create a 'requirements.txt' file, which will install the dependencies 
        for the project, and tell Heroku that Python language is using.
        To create a requirements.txt file, type the following command in the terminal: <br>
        <strong>pip3 freeze --local > requirements.txt</strong>
        Then Add, commit and push the file into Github:
        + git add -A or git add requirements.txt
        + git commit -m "Add requirements.txt".
        + git push 
  4) Create a Procfile. The Procfile tells Heroku how to run the application.
     To create Procfile, type the following command in the terminal: 
     <strong>echo web: python app.py > Procfile</strong>
     Then Add, commit and push the file into GitHub:
     + git add -A or git add Procfile
     + git commit -m "Add Procfile".
     + git push 
  5) Make sure all your code is pushed to your GitHub repository.
     + git add -A 
     + git commit -m "insert your message here"
     + git push 
  6) Go to the Heroku Deploy Tab and click 'GitHub (Connect to GitHub)' for 'Deployment Method'
  7) Make sure your GitHub profile is displayed, then provide your Github repository name and then click Search.
     Once it finds your repository, click to 'Connect' to this app.
  8) Click 'Enable Automatic Deploys'
  9) Choose a branch to deploy 'main' and then click 'Deploy Branch' on Heroku
  10) You will see a message: "Your app has been succesfully deployed"
      Click 'View' to lauch your new app.

  My deployed app: <br>
    https://coffee-book-project.herokuapp.com/
  

  ## Technologies Used 
- [HTML](https://en.wikipedia.org/wiki/HTML)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [Javascript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://www.python.org/)

Also made use of:
- [jQuery 3.6.3](https://jquery.com/)
- [Materialize CSS](https://materializecss.com/) responsive front-end framework
- [Flask](https://flask.palletsprojects.com/en/2.2.x/)
- [Jinja](https://jinja.palletsprojects.com/en/3.1.x/)
- [Werkzeug](https://werkzeug.palletsprojects.com/en/2.2.x/)
Flask uses Werkzeug to handle various utilities for WSGI applications, providing more structure
and patterns for defining powerful apps.
One of the benefits of using Werkzeug with Flask, is that it comes with simple-to-use
Security features.
- [pymongo](https://pypi.org/project/pymongo/)
- [Font Awesome](https://fontawesome.com/)
- [favicon.io](https://favicon.io/favicon-generator/)
- [HTML Validator](https://validator.w3.org/)
- [CSS Validator](https://jigsaw.w3.org/css-validator/)
- [Javascript Validator](https://jshint.com/)
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/open/)
- [Balsamiq](https://en.wikipedia.org/wiki/Balsamiq)




<!-- - ADD RECIPE PAGE Testing

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| RECIPE NAME  | Input text into the Search bar | Validation applied; minlength 3 characters, if no input or less then 3 characters - red undelined | Works as expected |
| CANCEL (Search) button | Click on Cancel button| It will remove all input from the Search bar and revert the bar into the initial position | Works as expected |
| FIND (Search) button  | Input text into Search bar and click on Find button | Input a key word from recipe name, intro or ingredients and it will find the affected recipes | Works as expected |
| DISCOVER RECIPE button | Click on Discover Recipe button | It will open a full recipe | Works as expected |

 -->


<!-- | NAV BAR - RECIPES| Click on the Recipes| It will redirect a user from any page to the Recipe page and is available even for non-registered users| Works as expected |
 | NAV BAR - SIGN UP| Click on the Sign Up| It will redirect a user to a Sign Up form and it is available for all users| Works as expected | -->



<!-- | RECIPE NAME  | Input text into the Search bar | Validation applied; min.5 and max.40 characters, if no input or less then 5 characters - red undelined; it will not let a user to input more then 40 characters | Works as expected |
| RECIPE IMAGE URL  | Input url into the Recipe Image Url | It is optional to add Image URL, if not provided, alternative image will display | Works as expected |
| RECIPE INTRODUCTION | Input text into the Recipe Introduction | This field is required, validation applied; min. 5 max.125 characters| Works as expected |
| CATEGORY | Dropdown selection | This field is required, validation applied| Works as expected |
| DIFFICULTY | Dropdown selection | This field is required, validation applied| Works as expected |
| PREPARATION TIME | Input text into Preparation Time | It is required, validation applied, max.15 characters | Works as expected |
| SERVES | Pick a number from options | It is required, validation applied, min.1 max.30 | Works as expected |
| INGREDIENTS | Input text into Ingredients | It is required to input at least one line, validation applied, min.5 max.200 charcters; max.20 inputs allowed | Works as expected |
| METHOD | Input text into Method | It is required to input at least one line, validation applied, min.5 max.750 charcters; max.20 inputs allowed | Works as expected |
| ADD RECIPE button  | Click on Add recipe | It will display a flash message that recipe has been successfully added, it will be automatically shared with others in recipes page and also will appear in user's 'created recipes' tab | Works as expected | -->

<!-- The COOL Quiz was created for anyone who wants to test their knowledge or learn some new interesting facts about the winter season. The players can take the quiz on their own or it can be used as a family indoor activity for those cold and dark evenings. The quiz has 12 multiple choice questions with a 120-second timer and a Top Score page so the players can save their best score. It hopes to engage all age groups or individuals of various interests, not just 'winter fans'.
![Responsive Design](assets/images/responsive-img.png) -->
<!-- 

## User Experience (UX)

### User Stories 

- As a user, I would like to understand the purpose of the website and what is being tested by the quiz before I start.
- As a user, I would like to have the option to read the instructions, so that I can understand how to play the game.
- As a user, I would like to play the quiz and see the content clearly on any device.
- As a user, I would like to be able to easily navigate through the website to complete the quiz.
- As a user, I would like to see if the answer I have chosen is correct or incorrect before proceeding to the next question.
- As a user, I would like to see my progress during the quiz (question counter, time counter and score counter).
- As a user, I would like to see my final score, have an option to save my best score and play again.


### Implementation 

- Used a layout with a winter background image, winter colours and picked an appropriate quiz title as well as a catchy initial        
  message to give users an early sense of what the quiz is about.
- Created a pop-up window to introduce the game to the users and to familiarize them with the quiz rules.
- Made the quiz responsive, visible and easy to read on desktops, laptops, tablets and smartphones.
- Created a simple intuitive design for easy navigation and used links for a smooth transport between pages.
- Made the quiz interactive as the chosen answers will turn green if correct or red if incorrect.
- Added Question counter, Time counter and Score counter to the game page.
- Added a result page that displays the quiz results as well as gives an option to save the users' scores.


## Features 

Cool Quiz consists of four webpages that all have an intuitive design for easy navigation.

  - ### Home Page
  This page introduces the quiz and shows important links to the game itself and to the Top Score page.
  - ### Game Page
  This is the core page of the quiz; it displays questions and multiple answer options as well as a navigation bar displaying the progress of the game.
  - ### Result Page
  It shows the results of the quiz and enables the player to save their score if they wish to do so.
  - ### Top Score Page
  Displays a list of top 7 scores.


### Existing Features

- __Home Page__

- The home page is the screen the end user is presented with on page load. <br>
  All four webpages have the same winter themed background image and colours, with a silver background for the website content. The 
  aim is to create a wintry atmosphere for players and bring back some memories of exciting winter events and activities.
  
- _Header_
  - The header has the same colour design as all other pages to support the intuitiveness of the entire website. The name of the
    quiz was chosen in order to give the visitors a hint of what the quiz is about. This intuitive layout enhances the user experience and makes the website easy to use.

- _Body_
  - The body includes an encouraging message to challenge the visitors to click on the START button and play the game.
  - The skeleton of the body has three buttons:
  - ABOUT button - clicking on the ABOUT button will display a pop-up box with the game rules. It includes all information the player 
    needs to know before starting the game.
  - START button is placed in the middle and has a different colour to underlay its importance. Clicking on this button will redirect 
    the player to the game page where they can start the quiz.
  - TOP SCORE button will forward the visitors to the list of the 7 best results.
  - Overall, the body layout is simple to understand and easy to navigate for the user.
  
- _Footer_
  - Similarly to the header, the footer remains the same regardless of the webpage. It contains a name of the production company and 
    the year of production. This intuitive layout contributes to the user experience.
    <br><br>
    <p align="center">
      <img src="assets/images/home-page.png">
    </p>
    <br><br>
    <p align="center">
      <img src="assets/images/pop-up-box.png">
    </p>

__Game Page__
- _Header_
  - The header includes the navigation bar which consists of the link to the home page and three other elements to monitor the  
    progress of the quiz. The player can click on the home icon anytime during the game to take them back to the home page and start the game again. Placing the home icon on this page allows users to navigate easily between pages and to return to the home page if they wish without having to use the back button. <br>
    The progress elements are all dynamic and are being updated with each question asked. 
  - Elements to monitor the progress:
    - Question counter shows how many questions have been answered so far as well as the total number of questions.
    - Time counter shows how many seconds are still left to complete the quiz. There is a 120 seconds countdown timer and if a player  
      runs out of time before completing the quiz, they will be redirected back to the home page to have another go.
    - Score counter shows how many points a player has received so far for all correctly answered questions. For each correct answer, 
      a player will get 100 points (1200 points maximum).<br>
    This ability to monitor the progress during the quiz enhances the user experience and also the motivation to achieve the highest score.
 
- _Body_  
  - The body shows the current question with four answer options. Clicking on one of these four options will deactivate the remaining 
    three and reveal if the chosen option is correct or not. The player will then be forwarded to the next question. Once a player clicks on an option, it cannot be changed. This will enhance the fluidity and energy of the game and encourage players to complete the quiz on time. <br>
    The time counter will prompt the user to answer questions correctly but also within a short period of time. This presents a double challenge and it makes the game more interesting and appealing to users. If the user does not answer all 12 questions in the allocated time, the quiz will automatically finish and they will be taken back to the home page. This will encourage users to take the quiz again. <br>
    Furthermore, if a player answers the question incorrectly, the correct answer will not be revealed. This should make the game more attractive as it will encourage the user to try again and improve their score. Once all questions have been answered, a player will automatically be directed to the result page.
- _Footer_ (please see the section about Footer above) 
   <br><br>
   <p align="center">
     <img src="assets/images/game-page.png">
   </p>    

__Result Page__
  - It shows how many points a player has scored in the quiz and gives them an option to save their score. To do so, a player has to 
    insert a username containing only alphabetic characters, without any numbers, special characters or spaces.
  - If the username meets the criteria, clicking on the SAVE button will save the player's score and return the player to the home 
    page. If the user does not want to save their score, they have an option to click on Go Home button which takes them back to the home page or on Play Again button to get to the game page and start playing again.
    <br><br>
    <p align="center">
      <img src="assets/images/result-page.png">
    </p>    

__Top Score Page__
  - This page displays a list of the 7 highest scores. 
    It also has the home icon for better navigation and it takes the user back to the home page.
    <br><br>
    <p align="center">
      <img src="assets/images/score-page.png">
    </p>    

### Features Left to Implement

  - Optaining more questions from the API open database to offer users a greater variety of questions and to make the quiz more 
    attractive
  - I would like to incorporate difficulty levels (easy, medium, hard)
  - Adding audio effects to a quiz question



### Wireframes 
- [Home Desktop](assets/wireframes/Home%20Desktop.png)
- [Home Tablet](assets/wireframes/Home%20Tablet.png)
- [Home Mobile](assets/wireframes/Home%20Phone.png)
- [Game Desktop](assets/wireframes/Game%20Desktop.png)
- [Game Tablet](assets/wireframes/Game%20Tablet.png)
- [Game Mobile](assets/wireframes/Game%20Phone.png)
- [Result Desktop](assets/wireframes/Result%20Desktop.png)
- [Result Tablet](assets/wireframes/Result%20Tablet.png)
- [Result Mobile](assets/wireframes/Result%20Phone.png)
- [Top Score Desktop](assets/wireframes/Top%20Score%20Desktop.png)
- [Top Score Tablet](assets/wireframes/Top%20Score%20Tablet.png)  
- [Top Score Mobile](assets/wireframes/Top%20Score%20Phone.png)



## Testing 

Manual Testing of implemented features: <br><br>


 - HOME PAGE Testing

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| ABOUT button  | Click the button | A pop-up box opens with introduction and game rules | Works as expected |
| START button  | Click the button| Player is directed to the game page and can start playing | Works as expected |
| TOP SCORE button | Click the button| This takes the player to the top-score page to check the leaderboard	| Works as expected |
 
 <br><br>

- GAME PAGE Testing

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| HOME button  | Click the button | Take a player to the home page anytime during the game | Works as expected |
| QUESTION counter  | Automatic feature| Shows what question the player is currently on, onwards counting | Works as expected |
| TIMER  | Automatic feature | Starts counting down automatically when the quiz appears on the screen | Works as expected |
| TIMER  | Automatic feature | For the last ten seconds the time text changes to red | Works as expected |
| TIMER  | Automatic feature | When time is up before answering all questions, the player is returned to the home page | Works as expected |
| SCORE counter | Click on the correct answer | Clicking on the correct answer will increase the score by 100 points| Works as expected |
| SCORE counter|  Click on the incorrect answer|  Clicking on the incorrect answer will not change the score| Works as expected |
| ANSWERS options  | Click on one of the 4 answers-options | Clicking on an option will disable the remaining three options | Works as expected |
| ANSWERS options  | Click on one of 4 answer options | The clicked option will change to green if correct and the score will be updated | Works as expected |
| ANSWERS options  | Click on one of 4 answer options | The clicked option will change to red if incorrect and the score will remain unchanged | Works as expected |
| NEXT question  | Automatic feature | Clicking on an answer option will evaluate the correctness and after 2 seconds a new question will appear| Works as expected |
| LAST question | Automatic feature | Clicking on the last answer option will evaluate the correctness and then forward the player to the result page |  Works as expected |

<br><br>

- RESULT PAGE Testing

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| RESULT  | Automatic feature | The correct score will appear on the result page | Works as expected |
| USERNAME  | Enter name | Only text of min 3 and max 10 letters is excepted, no numbers or spaces | Works as expected |
| SAVE button  | Click the button| Saves the players’ score and takes them back to the home page | Works as expected |
| SAVE button  | Click the button| Input validation – do not save the score if the entered username does not meet the relevant criteria | Works as expected |
| GO HOME button  | Click the button | Takes players back to the home page if they do not want to save the score | Works as expected |
| PLAY AGAIN buton  | Click the button | Takes players to the game page where they can start the quiz again without saving their score | Works as expected |

<br><br>

- TOP SCORE PAGE Testing

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Saved result | click on TOP SCORE button | Correct score displayed against a correctly saved name | Works as expected |
| 7 best scores | click on TOP SCORE button | Score appears on this page only if it is within the 7 best results | Works as expected |
| HOME buton  | Click the button | Takes the player back to the home page | Works as expected |

<br><br>


### Validator Testing 

- HTML
  The W3C Validator has been used to validate the HTML of the website. <br>
  All errors have been corrected. <br>
  [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fkarare1.github.io%2Fquiz-game%2F)

- CSS
  The W3C Jigsaw Validator was used to validate the CSS of the website. <br>
  All errors have been corrected. <br>
  [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fkarare1.github.io%2Fquiz-game%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

- JSHint Services were used to validate Javascript <br>
  All errors syntax errors corrected <br>
  [script.js](assets/js-validation/js-validator-script.png) <br>
  [game.js](assets/js-validation/js-validator-game.png) <br>
  [result.js](assets/js-validation/js-validator-result.png) <br>
  [topscore.js](assets/js-validation/js-validator-topscore.png) <br>


- The WAVE Web Accessibility Evaluation Tool was used to check accessibility of the website: <br>
  [Wave Web report](assets/images/wave-evaluation.png)

- Lighthouse reports: <br><br>
  [Lighthouse report Index](assets/lighthouse/lighthouse-report-index.png) <br>
  [Lighthouse report Game](assets/lighthouse/lighthouse-report-game.png) <br>
  [Lighthouse report Result](assets/lighthouse/lighthouse-report-result.png) <br>
  [Lighthouse report Score](assets/lighthouse/lighthouse-report-score.png) <br>


- Further testing has been done with Chrome DevTools, making sure that responsiveness works correctly on all devices.
  After the deployment, I tested the website link focusing on the game and result page to check if all important features work as expected. No issues were detected. 

- The website was assessed in various browsers: Mozilla Firefox, Google Chrome and Microsoft Edge.
  Live link was tested on Huawei P30, Samsung A50 to test smaller screen sizes, on a small display laptop - HP ProBook 430 and also on a larger display laptop - Dell Latitude 5580. <br>
  Each of the pages functioned well.

### Fixed Bugs
- preventDefault() removed html validation (min 4 and max 10 letters) <br>
  I have applied an extra function in javascript to prevent submitting usernames that do not meet the criteria
- favicon link to webmanifest showed error in console <br>
  Resolved by adding the crossorigin attribute

### Unfixed Bugs
None I am aware of. 

## Deployment

Deployment To GitHub Pages:  <br>

1. Create a repository in GitHub <br><br>
  ![Deploy-1](assets/deploy/deploy-1.png) <br>

2. Create the entry file for a site. GitHub Pages will look for an index.html as the entry file for the site  <br>

3. Git push all contents from Integrated Development Environment (IDE) into GitHub <br>

4. On GitHub page, click on the site's repository on the left sidebar or alternatively click on the avatar icon and 
   then 'Your repositories' <br><br>
   ![Deploy-2](assets/deploy/deploy-2.png) &nbsp; &nbsp; &nbsp; &nbsp; ![Deploy-3](assets/deploy/deploy-3.png) <br>

5. In the repository, under the repository name (e.g. karare1/white-lines), click Settings  <br><br>
  ![Deploy-4](assets/deploy/deploy-4.png) <br>

6. In the "Code and automation" section on the left sidebar, click on Pages  <br><br>
  ![Deploy-5](assets/deploy/deploy-5.PNG) <br>

7. From the source section drop-down menu, select 'Deploy from a Branch'  <br>
   From the branch section drop-down menu, select 'main' and 'root' and then click on Save button  <br><br>
  ![Deploy-6](assets/deploy/deploy-6.PNG)  <br>

8. The link to the site will be automatically created. <br>
   To see the published site, under "GitHub Pages", click the site's URL  <br><br>
  ![Deploy-7](assets/deploy/deploy-7.png) <br>

   The live link can be found here: https://karare1.github.io/quiz-game/ <br>


## Technologies Used 
- [HTML](https://en.wikipedia.org/wiki/HTML)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [Javascript](https://en.wikipedia.org/wiki/JavaScript)

Also made use of:
- [Font Awesome](https://fontawesome.com/)
- [favicon.io](https://favicon.io/favicon-generator/)
- [HTML Validator](https://validator.w3.org/)
- [CSS Validator](https://jigsaw.w3.org/css-validator/)
- [Javascript Validator](https://jshint.com/)
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/open/)
- [Balsamiq](https://en.wikipedia.org/wiki/Balsamiq)


## Credits 
- [www.scrimba.com.com](https://scrimba.com/learn/learnjavascript)  <br>
- [www.nikitahl.com.com](https://nikitahl.com/convert-array-like-collections-to-array/)  <br>
- [www.www.classcentral.com](https://www.classcentral.com/course/youtube-build-a-quiz-app-with-html-css-and-javascript-45707/classroom) <br>
- [www.freecodecamp.org](https://www.freecodecamp.org/news/javascript-projects-for-beginners/)  <br>
- [www.developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)  <br>
- [www.w3schools](https://www.w3schools.com/)  <br>



### Content 


- The text for the Home page was taken from:  <br>
  [www.ultimatequizquestions.com](https://www.ultimatequizquestions.com/winter-trivia-questions/)  <br>
  [www.quiztriviagames.com](https://www.quiztriviagames.com/winter-quiz/)  <br>
  [www.wordsforlife.org.uk](https://wordsforlife.org.uk/activities/take-a-quiz-about-winter-celebrations/)  <br>



### Media

- Background image:  <br>
  [winter.jpg](https://www.pexels.com/photo/aurora-borealis-624015/)  <br>
  Photo by Frans van Heerden downloaded from Pexels
- Icons were taken from [Font Awesome](https://fontawesome.com/)






<!-- intuitive/first-time learning and effective
In order to promote that form of ease-of-use and intuition
it's always better to present your functionality to a user in
the most intuitive way possible that promotes a positive user experience

Sign up 
Log In
let's include some Icon Prefixes for a better user experience
and layout.

Werkzeug
The two main helpers we're going to use for this mini-project, are "generate_password_hash",
and "check_password_hash".
Hashing passwords essentially means that we're converting the user's password into another
string, which is one-way, and practically impossible to reverse.
To include additional security, it will then salt that string with random data, making
it even tougher to crack. -->














 -->
