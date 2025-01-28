


> 
> 

# Nature blog
![Nature on my doorstep](https://github.com/user-attachments/assets/3b5f2d10-8103-4d8a-9c39-f8ce6608fd0f)



> [View live project here](https://nature-blog-5d97cb035a15.herokuapp.com/)

For Admin access with relevant sign-in information: [Nature blog Admin](https://nature-blog-5d97cb035a15.herokuapp.com/admin/)
> 
> This is my nature blog which allows me to create blog posts about the wildlife in my garden.
> Users can read and comment on each post that they can share their thoughts and ideas and feel part of a wider community helping nature to thrive.
---
> 
<img width="937" alt="Screenshot 2024-10-04 at 10 42 39" src="https://github.com/user-attachments/assets/87d34c2d-0bd4-432c-8575-04ed47dc3f52">


>
---

## CONTENTS

 - [User experience (UX)](#user-experience)
     - database planning
     - purpose and intended audience		 
     - user stories
 - [Creation process](#creation-process)
		 
     - [Wireframes](#wireframes)
 - [Design](#design)
		 
     - Colour scheme
		 
     - Typography
		 
     - Imagery
 - [Website features](#website-features)
 - [Tablet/mobile view](#tablet/mobile-view)
 - [Future features](#future-features)
 - [Technologies used](#technologies-used)
 - [Deployment](#deployment)
 - [Testing](#testing)
 - [Credits](#credits)
 ---
 ## USER EXPERIENCE
 ---
**Database Planning**

I used [LucidChart](https://lucid.app/documents#/home?folder_id=recent) to create my ERD for my database. It is a simple model with only four models: User, Post, Comment and Category.
The User model was imported from Django Allauth

![erd](https://github.com/user-attachments/assets/81a2689c-789b-4e01-8810-a91b1193002a)

**Purpose and Intended Audience**

My intention was to design a website which allowed me to showcase the amazing wildlife I found in my garden and the work I have done to increase the species diversity. At the same time I wanted people to visit and feel involved by being able to comment and give their own experiences and tips for me and everyone in the community.
By adding the category model to the project I wanted to make it easier for users to identify the posts which interested them most and which they could engage with.


**User stories**
		 
| User story | MoSCoW prioritisation |
| --- | --- |
| As a **User** I can **use a navigation links** so that **access other areas of the site easily** | Must have |
| As a **user** I can **click the home page icon** so that **I can quickly and easily return to the home page** | Must have |
| As a **user** I can **click on the about page link** so that **find out more information about the site** | Must have |
| As a **user** I can **navigate the social links** so that **connect with the site via social media** | Must have |
| As a **user** I can **open a blog post** so that **I can get the full information on a post I am interested in** | Must have |
 | As a **user/admin** I can **view comments on individual posts** so that **I can follow the conversation** | Must have |
 | As a **user/admin** I can **comment on posts** so that **I can take part in the conversation and be a part of the community** | Must have |
 | As a **user** I can **edit or delete my comments on a post** so that **I can be involved in the conversation and community** | Must have |
 | As a **user** I can **use my email and a password to register an account** so that **I can interact with the community and leave comments on posts** | Must have |
 | As a **site admin** I can **moderate user comments** so that **nothing inappropriate or offensive is added to the site** | Must have |
 | As a **user** I can **filter the blog posts based on their category** so that **see posts that match my interests** | Must have |
 | As a **site admin** I can **create new blog posts** so that **my audience has up to date and new content to enjoy** | Must have |
 | As a **site admin** I can **edit or delete blog posts** so that **users have the correct content and mistakes can be rectified** | Must have |
 | As a **site admin** I can **create and assign post categories** so that **users are able to filter the blog posts for a more tailored experience** | Must have |
 | As a **user** I can **search for blog posts using keywords** so that **get the specific information I need more quickly** | Should have |
 | As a **user** I can **see the most recent posts in a sidebar** so that **I have access to the most recent information quickly** | Won't have |
 | As a **user** I can **share posts on social media platforms** so that **I can interact with other users and a wider community** | Won't have |
 | As a **user** I can **view a separate page showing activities available to book** so that **I can interact with nature and learn more** | Won't have |
 | As a **user** I can **navigate to a separate gallery page** so that **I can enjoy more content in an enjoyable way** | Won't have |
 
I used [GitHub Projects](https://github.com/users/helproudman/projects/4/views/2) to create my project board and populated it with my user stories and added labels according to MoSCoW prioritisation.
All of the 'must have' user stories were completed with any other issues being carried over to the next phase of the project development.
Each user story had acceptance criteria added. The key user stories and acceptance criteria are listed below with evidence of how I completed each issue:

![User story 14 - Create new blog posts](https://github.com/user-attachments/assets/396cb671-4df6-4a6a-8aa1-99bcfd71b78e)
Acceptance criteria:
Site admin can log in
Once logged in can create a post
The fulfillment of these criteria can be demonstrated by the presence of blog posts on the site


![user-story-9 - Modify or delete comment on a post](https://github.com/user-attachments/assets/c0210822-2ebb-4527-af29-5f0c9c5038c4)
Acceptance criteria:
As a logged in user their comments are available to edit/delete - this was set up to display CRUD functionality and tested extensively during development. 
	 

![user-story-8 - Comment on a post](https://github.com/user-attachments/assets/b5add256-1625-4ae7-983e-d257a3e22554)
Acceptance criteria:
The user can log in and create comments
If there is more than one comment then there is a conversation thread
This user story also contributed towards the CRUD functionality and was tested throughout every phase of the project development
 
 
		 
---

## CREATION PROCESS

  ### Wireframes
  I only created wire frames for the pages I intended to create myself. All login and registration forms were created by allauth and as such I haven't provided wire frames.
<details open>
<summary>Blog page wireframes for mobile and desktop</summary>
<img width="1080" alt="Blog page mobile and large screen" src="https://github.com/user-attachments/assets/7bf359f9-8291-4d1d-a806-482b8ea5c93e">

  
</details>

<details>
<summary>Blog detail wireframes for mobile and desktop</summary>

  <img width="1080" alt="blog post detail" src="https://github.com/user-attachments/assets/9f94cd74-4afe-4984-8455-f962e58bd48b">

</details>



---

## DESIGN
  - **Typography**
    
    [Google Fonts](https://fonts.google.com/) was used to choose the font used. I had the idea that I wanted two fonts to 
   differentiate the general site text from the personal blog text so the following font was imported:
    
    The Gloria Hallelujah font was chosen for the blog introduction and the blog entries themselves as it resembles 
    handwritten text and I felt it would lend a more personal touch to the blog. I wanted it to feel as though the user was 
    reading my diary entries directly.
    
  - **Colour scheme**
    
  ![colour-scheme](https://github.com/user-attachments/assets/00aa9746-14ed-425e-979c-1dee50ba4843)

        
    As the blog is about nature and wildlife I wanted the colour scheme to reflect the colours I have in my garden. I wanted 
    strong, primary colours for impact as they would be against a white background, but didn't want a large palette as I 
    included lots of images of wildlife that I didn't want to detract from. 
    The palette was chosen using [Coolers](https://coolors.co/)
    
  - **Imagery**
    
    The majority of the images used in each blog post are my own images taken of my garden and I was really proud to be able 
    to use them. I had a lot of fun creating posts and uploading images. Seeing the finished article on the screen gave 
    me enormous pleasure despite the fact that the load time for my site was compromised.
    Two of the images were royalty-free stock images from [Pexels](https://www.pexels.com/) Acknowledgements for the 
    individual photographers are in the [credits](#credits) section.
 


 ---

## WEBSITE FEATURES


  **MAIN VIEW**
  <details open>
  <summary>landing page</summary
  ![home-page](https://github.com/user-attachments/assets/72eefb0f-81d3-41d5-b856-bfa8198ccf6b)


  </details>
  I decided to have users arrive directly on the blog post page rather than requiring them to log in or register before being able to see anything. 
  I felt it would draw people in more and encourage them to then register and get involved.
  There are clear messages to tell the user whether they are logged in or not

<br>
    
  **BLOG POST DETAIL VIEW**
  <details>
  <summary>The detailed view of each </summary>
					     
  ![post-detail](https://github.com/user-attachments/assets/03b2cda8-1505-4bd3-9fe2-8fcd2cf7ca2d)

  
  </details>
  Each blog post is shown with the image and the detail of the post in a font I chose to make it appear as though it was an entry in a diary. 

  <br>

  **COMMENT FEATURE**
  <details>
  <summary>Comment box</summary>
  ![comment](https://github.com/user-attachments/assets/cdf67ea2-1fad-410c-91e2-659a28432bde)

	  
  </details>
  Each blog post gives the user the option to add comments. They can also edit/delete commemts they have previously made. The 
 comments then appear colour coded so that the user can tell which have been approved by admin.


  **SOCIAL LINKS FEATURE**


 ![footer](https://github.com/user-attachments/assets/57a79318-bd2f-423e-b015-3f59dea69dce)



  The footer gives links to social sites and GitHub. The colour was chosen to match the header and fit in with the overall 
  colour scheme.




 ---

## FUTURE FEATURES
The following would be options to consider including in future versions of the website:
  - an about page for information about the developer
    
  - an option for users to create their own blog posts
    
  - a way for users to take part in some citizen science where they can document species they have seen in their gardens

  - a booking site where users can book nature activities

  - a gallery page of users pictures



## TECHNOLOGIES USED

  ### Languages used
  - HTML5

  - CSS

  - JavaScript

  - Python
   - asgiref==3.8.1
   - cloudinary==1.41.0
   - dj-database-url==0.5.0
   - gunicorn==20.1.0
   - oauthlib==3.2.2
   - psycopg==3.2.1
   - PyJWT==2.9.0
   - python3-openid==3.2.0
   - requests-oauthlib==2.0.0
   - sqlparse==0.5.1
   - urllib3==1.26.19
   - whitenoise==5.3.0
     

  - Django
    - summernote==0.8.20.0
    - allauth==0.57.2
    - crispy-forms==2.3

  ### Frameworks, libraries and programs used

   
  1. [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
        - Bootstrap was used to ensure the site was responsive and for styling
  2. [Balsamiq](https://balsamiq.com/wireframes/)   
        - Balsamiq was used to produce the wireframes in the design phase.
  3. [Git](https://git-scm.com/)
        - Git was used for version control
  4. [Github](https://github.com/)
        - GitHub was used to store the code and allow collaboration on the project.
  5. [Contrast Finder](https://app.contrast-finder.org/?lang=en)
        - Contrast Finder was used to check the contrast between text colour and background image
  6. [Tiny.PNG](https://tinypng.com/)
        - Tiny.PNG was used to compress images
  7. [StackEdit](https://stackedit.io/)
        - StackEdit was used to assist with the markdown in the README.md
  8. [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools)
        - Used to troubleshoot and test design ideas and styling.   
  9.  [Google Lighthouse](https://developer.chrome.com/docs/lighthouse/overview)  
        - used to test performance of the website
  10. [Favicon](https://favicon.io/)
        - used to generate the favicon  
  11. [W3 Schools](https://www.w3schools.com/)
        - used to look up syntax for HTML and CSS
  12. [Stack Overflow](https://stackoverflow.com/)                  
        - used for queries around coding
  13. [Perplexity](https://www.perplexity.ai/)    
        - used to provide sources to generate text for the website   
  14. [Wikipedia](https://www.wikipedia.org/)      
        - used to generate text
  15. [Wave web accessibility evaluation tool](https://wave.webaim.org/)
        - used to supply the weather API
  16. [Font Awesome](https://fontawesome.com/)    
        - used for the favicon
  17. [Pexels](https://www.pexels.com/)
        - used for copyright free images
  18. [W3C HTML validator](https://validator.w3.org/)
        - used to validate the HTML
  19. [W3 Jigsaw](https://jigsaw.w3.org/css-validator/)
        - used to validate the CSS
  20. [JSHint](https://jshint.com/)
        - used to validate the JavaScrip
  21. [Python Enhancement Proposals](https://peps.python.org/pep-0008/)
        - for advice on PEP8 compliance
  22. [Free Code Camp](https://freecodecamp.org)   
        - for help with JavaScript concepts and syntax 
  23. [Code Academy](https://codeacademy.com)   
        - for help with JavaScript concepts and syntax  
  24. [Code explained repository on GitHub](https://github.com/CodeExplainedRepo/Weather-App-JavaScript)
        - for help setting up a weather app using an API
  25. [Claude AI](https://claude.ai/)
         - for help with code queries
  26. [Adobe Color](https://color.adobe.com/create/color-wheel)
        
  28. [Django framework](https://www.djangoproject.com/)
  29. [Django Project - Build a simple blog tutorial](https://www.youtube.com/watch?v=S9-Bt1JgRjQ&list=PLOLrQ9Pn6cawWd-5UZM6CIm0uqFXeBcTd&index=5)
  30. [CI Python Linter](https://pep8ci.herokuapp.com/) - for validating Python code
  31. [Heroku](https://dashboard.heroku.com/apps)



 ---

## DEPLOYMENT
The site was deployed to Heroku. The steps to deploy are as follows:
 - Install the gunicorn python package and create a file called 'Procfile' in the repo's root directory
 - In the Procfile write 'web: gunicorn lunar_lists.wsgi'
 - In settings.py add ".herokuapp.com" to the ALLOWED_HOSTS list
 - In settings.py add 'https://*.herokuapp.com' to CSRF_TRUSTED_ORIGINS list, git add, commit and push to github

Navigate to the Heroku dashboard
 - Create a new Heroku app
 - Give it a name and select the region 'Europe'
Navigate to settings tab and scroll down to Config Vars
 - Click 'Reveal Config Vars'
 - Add the following keys:
         key = DATABASE_URL | value = (my secret database url)
         key = SECRET_KEY | value = (my secret key)
Navigate to Deploy tab
 - Connect to GitHub and select the repo 'lunar-lists'
 - Scroll down to 'Manual deploy' and select the 'main' branch
 - Click 'Deploy Branch'
   


 ---

## TESTING

 ### Unit Tests

The following Unit Tests were performed:

| Test Category            | Test Description                                                                 |
|--------------------------|----------------------------------------------------------------------------------|
| **Test Setup**           | Initializes test data, including creating a regular user, an admin user, and a sample topic. |
| **Test Topic Detail Page** | Verifies that the topic detail page renders correctly with the topic details when accessed by an admin user. |
|                          | Ensures that the create topic page renders correctly and uses the appropriate template. |
|                          | Confirms that the edit topic page renders correctly and uses the appropriate template. |
|                          | Checks that the delete topic page renders correctly and uses the appropriate template. |
| **Test Forms**           | Ensures that the comment form is valid when provided with valid data.             |
|                          | Verifies that the comment form is invalid when provided with empty data.          |
|                          | Confirms that the topic form is valid when provided with valid data.              |
|                          | Ensures that the topic form is invalid when provided with empty data.             |
| **Test Models**          | Verifies that the string representation of the topic model returns the topic title. |
|                          | Ensures that the string representation of the comment model returns the first 20 characters of the comment body. |
| **Test Comment Functionality** | Verifies that a comment can be added to a topic.                              |
|                          | Ensures that a comment can be edited.                                             |
|                          | Confirms that a comment can be deleted.                                           |


  ### HTML validation

I have used the W3C Markup validator to validate all of my HTML code - [W3C Markup Validator](https://validator.w3.org/)

A different approach was required for validating the HTML for this project as all of the pages are developed using DTL and most require user authentication. The HTML validator will throw errors if I were to use the URL so I followed the below approach for every page:
  - navigate to the deployed Heroku link
  - right click to find the 'view page source' link
  - copy and paste the HTML code from here into the validator via the direct input

[home page html validation](readme.docs/landing_page_validation.png)

All HTML was checked and had no errors or warnings to show as indicated above. 
The home (landing) page some initial syntax errors which were identified and corrected and then commited the code and the validation was clear.

   ### CSS validation

[CSS validation](readme.docs/css_validation.png)

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate the CSS file. External CSS for Bootstrap, provided by [CDN](https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.2.3/css/bootstrap.min.css) was not tested.

   ### Javascript validation

  [JavaScript Validator](https://jshint.com) - the JavaScript validation did not throw up and issues. The fact that the use of let and const to define variables and template literals is only available with ES6 was highlighted.

   ### Python validation
[CI Python Linter](https://pep8ci.herokuapp.com/#) was used to validate the python files I created or edited myself.
Initial errors were thrown up involving line length of comments and spacing but these were corrected.    

  

## Lighthouse scores via Chrome dev tools 
![lighthouse](https://github.com/user-attachments/assets/ad97e67e-3d28-4c94-a847-d2c011aeac67)

The performance score is low due to the amount of images used but all the images have been compressed.

  

### Accessibility     

The site was tested via WAVE the web accessibility evaluation tool and showed some alerts for contrast between the text and the background colour.
The first was for the message warning a user they are not logged in, which had white text against a bright red. The colour of the background was muted and checked via [Contrast Finder](https://app.contrast-finder.org/?lang=en) which showed excellent contrast. 
There was also a contrast issue between the white text and the orange background in the navbar and footer but I felt this was not enough of an issue to change the appearance and style of the whole site.


<br>


### Issues/Bugs
  
  - On the blog post detail page the image is only showing the top part
  - The images on the main page are very large and not a uniform shape....I decided I like being able to see the full image rather than limiting how much to see and I like
    the fact that everything isn't uniform but that might just be me!
 - there are too many to list in all honesty, so apologies, but I didn't have the ability or confidence to be able to sort everything out in this version of the project...hopefully I 
   will have more luck with a resubmission...I will be less stressed  and have time to learn Django more


### Agile Process
I made an attemtpt to follow an agile process. I had a project board in github which I updated with my user stories. Each user story was labelled according to MoSCoW prioritisation and had acceptance criteria. If I'm honest I didn't then keep the board up to date as I should have as I was so focused on the minutiae of the project and the stress of not thinking I would be able to actually produce anything that the board was the last priority. I have updated it since drawing a line under my development for now and many of the user stories have been moved into the finished section. There are several still in the backlog which have been added to my future features.
I have learned a lot for the future about planning and a large part of that is using the project board more and following an agile process more closely to keep myself on track.



## CREDITS

**Content**
  - [Kera Cudmore/readme-examples on GitHub](https://github.com/kera-cudmore/readme-examples)
   was used to help write the README.md
  - [Code Institute Sample README](https://github.com/Code-Institute-Solutions/SampleREADME)
  was used as a reference when writing the README.
  - [Django project - build a simple blog](https://www.youtube.com/watch?v=S9-Bt1JgRjQ&list=PLOLrQ9Pn6cawWd-5UZM6CIm0uqFXeBcTd&index=5) was used to give a tutorial for setting up a blog app in Django and adding a category model
  - [Code Institute](https://learn.codeinstitute.net/) was used for extra reference for HTML, CSS, Python and Django
  - [W3 Schools](https://www.w3schools.com/) was used for reference on syntax
  - [Stack Overflow](https://stackoverflow.com/) was used for syntax and coding queries
  
**Media**
  - All images not my own were taken from [Pexels](https://www.pexels.com/). Credit to the individual artists: Graeme Travers for Damselfly and Mark A Jenkins for Blue Tit 
  - [Amiresponsive](https://ui.dev/amiresponsive) for the responsivity mockup on the README.

  - [Ignore X frame headers](https://chromewebstore.google.com/detail/ignore-x-frame-headers/gleekbfjekiniecknbkamfmkohkpodhe)
    was used to download a Chrome extension to allow the resposivity image to be taken


**Acknowledgements**
  - Amy Richardson (Facilitator with Code Institute) - For providing support and resources and tirelessly encouraging
  - Mark Briscoe (SME with Code Institute) - For providing technical knowledge and support with coding and GitHub/GitPod and being constantly 
    encouraging and positive
  - John Rearden (Coding coach with Code Institute) - for amazing coding expertise and calm advice
  - Ruairidh MacArthur (Coding coach with Code Institute) - for amazing coding expertise and calm advice
  - my amazing cohort for the support and laughs and encouragement - particularly Alex Curnow for making me stay every time I was determined to quit