![Logo](static/images/full-logo.png)

# The Veggie Patch

As my Milestone Project 3 for the Code Institute Full Stack Web Development course,
I have built an application where people are able to find and share vegetarian recipes with each other.

The application can be found at ....

## UX
The application is meant to be a platform for people who are interested in vegetarian cooking,
to get inspired and find and share recipes with each other.\
Data for the app is kept in a MongoDB document-based database with two collections.\
The app incorporates the four basic CRUD (create, read, update, delete) functions, and it was created using HTML, Flask, Jinja templating and CSS.

### User stories
1. as a user I want to be able to browse all recipes for inspiration
2. as a user looking for a specific type of recipe, I want to be able to filter on meal type
3. as a user looking to use up some ingredients, I want to be able to perform a search based on ingredients
3. as a user I want an easy overview of required ingredients
4. as a user I want to be able to print out a clean, well-structured copy of the recipe
5. as a user I want to be able to share recipes with other users
6. as a user who previously added a recipe, I want to be able to edit or delete it

### Wireframes
Wireframes for this project were created for [small screens](static/wireframes/small-screens.pdf)
and for [medium and up](static/wireframes/medium-large-screens.pdf). The decision to roll wireframes for medium and large screens into one
was taken when it quickly became clear that they would only have minor differences. Apart from the navigation bar being collapsed on medium-sized screens,
they are largely identical.

Differences between the wireframes and the actual layout are discussed in the [Features](#features) section below.

### Database
The data for this project is stored in a MongoDB database with two collections:\
**Categories collection**:
| Field Name  | Data Type |
| ------------|-----------|
| _id         | ObjectId  |
|category_name|String     |
|category_url |String     |

**Recipes collection**:
| Field Name   | Data Type |
|--------------|-----------|
|_id           |ObjectId   |
|name          |String     |
|category_name |String     |
|prep_time     |Integer    |
|cook_time     |Integer    |
|serves        |String     |
|ingredients   |Array      |
|image_url     |String     |
|instructions  |String     |
|id_key        |String     |

The two collections have the category_name field in common.
This is so that it is possible to return recipes belonging to a specific category when that category is chosen in the category view.\
The ingredients are stored in an array in order to be able to display them on separate lines in an unordered list.

## Features

### Existing Features

### Features Left to Implement

## Technologies and Tools Used
- HTML, CSS, JavaScript and Python were used to build the webpage
- The [Flask framework](https://palletsprojects.com/p/flask/) and [Jinja template engine](https://palletsprojects.com/p/jinja/) were used to create and render dynamic HTML pages.
- The [Bootstrap](https://getbootstrap.com/) framework was used to set up a responsive layout
- [MongoDB Atlas](https://www.mongodb.com/) was used to store the data in a non-relational database
- [Gitpod](https://www.gitpod.io/) was used as the IDE for this Project
- [Git](https://git-scm.com/) and [GitHub](https://github.com/) were used for version control and repository hosting
- [Heroku](https://www.heroku.com/) was used as the platform for deployment of the website
- [Autoprefixer](https://autoprefixer.github.io/) was used to add vendor prefixes to CSS code
- [Google Fonts](https://fonts.google.com/) provided the fonts used throughout the website (Just Another Hand and Cambay)
- [Canva](https://www.canva.com/) was used to design the website logo and [Favicon.io](https://favicon.io/) to turn it into a favicon
- [Font Awesome](https://fontawesome.com/) provided all icons used throughout the website
- [Balsamiq](https://balsamiq.com/) was used to create wireframes for the project


## Testing
JavaScript code was run through the [JSHint](https://jshint.com/) analysis tool to check for syntax errors.
In addition, CSS was checked in the [CSS Validator](https://jigsaw.w3.org/css-validator/) and HTML in the [HTML Validator](https://validator.w3.org/).

## Deployments

## Credits
- [This article](https://pythonise.com/series/learning-flask/flask-message-flashing) by Julian Nash was used as a guide for flash messages

### Content and Media
- Landing page background photo is from [Pexels](https://www.pexels.com/)
- Recipes including photos are from the [BBC goodfood](https://www.bbcgoodfood.com/) website

### Acknowledgments

*This website is for educational purposes only. It was created as part of the Code Institute Full Stack Developer course.*
