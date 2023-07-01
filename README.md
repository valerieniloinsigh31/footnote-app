README FOOTNOTE

# FootNote App - Portfolio Project Four - Full Stack Toolkit

<img src="static/media/AMIResponsive_footnote.png">

## Live Site: 

## Repositary:  
https://github.com/valerieniloinsigh31/footnote-app

## Contents

-Project Description and Goals
-User Experience Design and Agile Methodology
-Features
-Existing Features
-Future Features
-UX Design
-Technologies and Frameworks used
-Testing 
-Deployment
-Credits and thanks


## Project Description and Goals
## Description
FootNote is an app for creative writers who are often struck by inspiration whilst out and about.
 The app will accommodate those who have quick ideas and want fast feedback. It is designed for users to share inspiration.
The app will be comprised of a network of members who work as creative writers in some form; (e.g. a pool of like-minded creatives with similar interests who can give feedback on one another's quick ideas.)
Each idea post will be anonymous (the name of the author will not be published alongside the idea). This is to ensure that feedback received via footnotes will not be biased. The corresponding footnotes however will be attributed to the author of the footnote so that the feedback provided will not be mere trolling or excessively abusive and any remarks provided can be followed up on. Footnotes have additional transparency (the author's name is posted with the footnote) in case they are overly negative, for moderatorship purposes. The name of the person leaving the footnote is presented beside their footnote within the idea page.
There is an approval tick under each idea post, so users can signify their approval by clicking this and a counter is included on this, which denotes the amount of ticks received for an idea on the summary page. This will offer instantaneous feedback to the user on how much traction their idea has received and potentially influence whether they will pursue it further or not.
Approval ticks are anonymous but offer the user who created the idea a useful insight into the popularity of their idea amongst like-minded creatives. 
Users are not obliged to either tick the approval or to leave a 'FootNote' (a moderated comment on the original idea capped at 280 characters, that must be approved by the site administrator before it becomes visible). They can do neither, either or both if they wish. 
The premise of the app is that it will foster creativity, encourage people to freely share ideas without judgement/negative consequences. The user knows what idea they posted but others cannot see who posted the idea as the name of the author does not appear in the original idea post.
The FootNote app is designed to assist creative minds to nudge one another in the right direction. To avoid intellectual theft, the ideas and footnotes are both capped at certain lengths. 
  On the profile tab, each logged in user has their own information which they can edit as they please (stipulating their favourite author/genre/style and specifying their gender and where they are from. Also, the footnotes feed into their own personal footnote log directly from the main page. They can delete footnotes as they please, retaining those they deem to be useful to developing their ideas further.
In summary, the purpose of the FootNote app is to connect creative people. It has the target audience of creative writers, who want to share their original ideas and to get instant feedback from similarly minded people in a useful footnote format, with a maximum amount of characters so that the contribution provided by other app users is a helpful nod as opposed to providing an idea to plagiarise. 
  The evident emphasis on feedback transparency (with every footnote being attributed to the footnote giver) is in place to ensure that nobody abuses the app or tries to use it as a method of stealing the original thoughts of others/to offer unconstructive negative feedback. Equally the ideas left are anonymous so that the ideas are judged/assessed/reacted to exclusively from a creative perspective. The anonymous nature of the idea itself guarantees unbiased footnotes will be provided.

## Goals
## Functionalities to include:
Based on the Minimum Viable Product documentation on Project 4, I concluded that I would have to have the following functionalities available in my FootNote app:
   Both the user and superuser/administrator of my FootNote application, should have the ability to create, read, update and delete items. (CRUD functionality) Albeit, this is applied in different ways.
Admin/Superuser
-For the <em>administrator/Superuser</em> who regulates the FootNote app, they will regulate what ideas and footnotes appear on the app.
- They can create, read, update and delete their own original ideas via the admin interface.
-The FootNote policy is one idea per user only to be posted at a time. Each user must delete their current idea before posting a new one. This is done to avoid oversaturation and to be inkeeping with the transient nature of inspiration that is propagated by the app. Also there is a maximum length stipulated per original idea posted, to be inkeeping with the initial aim of the application; to post a fast idea that occurs to the logged in site user whilst out and about in order to get immediate feedback (as opposed to exposing intricate/vital parts of their original creative ideas.)
-The admin/Superuser will be able to view FootNotes posted by the users and to approve whether they appear on the app. 
-The admin/Superuser can delete ideas via the admin interface (and as a result, all of the footnotes posted to it will delete with the CASCADE effect)
-The admin/Superuser can change the order of the footnotes and ideas that appear on the app.
- The app from the perspective of the superuser who is also the administrator and, as such, a regulator of the site will be able to log in and regulate the front end view of their profile. They will operate as an administrator and readily be able to control what views and posts appear on their page. 
User
-The registered user can stipulate their preferences (e.g. their favourite genre, their method of writing-(e.g. poetry, novel, screenplay, song etc) and input this information into a profile form on the profile tab) 
-The main purpose of this form going forward for future iterations of the app will be to offer the user the ability to filter ideas based on their specifications (e.g. favourite genre, preferred writing style or favourite author or gender). 
-From the user perspective, the eventual goal is that their statistics on the site will accumulate from the moment they join the application and the useful insights garnered from the same will be implemented when applying additional sort and filter features going forward.
 Once the user registers, they can then perform a variety of tasks:
 -They can read the latest original idea posted/any ideas published to the app that have not yet been deleted
-The user can submit their own original idea for approval (from the Site Admin). This has a maximum length.
 -They can click on the green tick beneath an original idea to signify whether they believe that the original idea should be explored further/deserves more traction. 
 -The user can leave a FootNote on an idea, with a maximum length
-The user can edit their own footnotes (edit button will only appear on their own footnote)
-The user can delete their own footnotes (delete button will only appear on their own footnote)
-The signed in registered user can submit a profile form and update this profile form on the ‘Profile’ page. There is no limit to how often they can update their profile form and no approval from admin is required
-They registered user can delete any footnotes that they wish to from the footnote log on their profile page that feeds into their profile page from the main site
-The user can click a button on the Medley page that will generate a random idea from the current database. This is designed to provide a quick injection of out of context inspiration

##  Future/goal functionalities to have in future iterations of the app:
 -The user will be able to update or delete their idea at any point they want to (Will add edit/delete button to idea which becomes visible of the user matches the original poster)
 -They will be able to click like or unlike on FootNotes posted by other users (Will add tick buttons to footnotes also)
 -Insertion of a sort selector on the landing page so that footnotes can be filtered by gender/writing style/genre etc. (Will add a sort selector box to the ideas)
 -Suggested connections will pop up for the users based on the information they provide in their profile form and the idea posts they have liked (similarly to the suggested followers function in instagram or the suggested friend section in facebook or the suggested connection section in LinkedIn). This will be a filter wherein ideas can be filtered based on the profile preferences stipulated by the person who posted the idea; favourite genre/style etc.)
- For future iterations of the app, more emphasis will be placed on profile interaction between different users. They can apply to become a feedback giver on the profile of one of the suggested connections and, if approved, will be alerted whenever that person posts an idea (giving them additional access to see which ideas the person posted). Once they submit to become a feedback giver, the owner of the profile that they have applied to will assess whether or not to accept them as a feedback giver on their profile. This assessment will be made by the historical statistics of the applicant’s engagement-to-date on the FootNote App becoming readily visible to the profile owner. Metrics that will be exposed with the applicants statistics when they joined the app, will be how many original ideas of their own have they posted, how many votes have they submitted to other people’s FootNote Profiles, how many ticks have they sent and how long have the been on the site. This will help the profile owner to make an informed decision about whether or not to accept them as a feedback giver on their profile. 

## User Experience Design and Agile Methodology

 - The agile methodology helped me to focus on what needed to be done, helped to manage tasks and break them down into doable chunks, helped me to identify logical progression and to be more aware of what level pr progression was expected at different stages
Easy way to focus on tasks that needed to be completed
 - I watched all of the tutorials on Agile methodology as well as the additional explanatory youtube video that the Code Institute released discussing the requirements and noted the following agile methodology features that I should incorporate in my own project planning as they seemed very urseful and/or relevant:

- Creating a number of user stories issues on github and linking this with the project
- MOSCOW priorisiation of user stories. I uses the labels feature on github to denote the prioritisation of different user stories. Thesecan also be colour coded so that they are instantly recognisable. I used green for must have priority user stories, I used yellow labels for should have priority user stories, amber for user stories that were a could have level of priority and red for won't have user stories.
- Kanban Board. The kanban board feature of github was an excellent time management and planning tool. It is divided into three levels of progress: to do, in progress and done. I created a kanban board and linked it to the relevant repositary. Then I could user stories as relevant and slot them into the correct progress section.
- User stories were created using a user story template, as advised in tutorials. I ensured they contained the user story, the epic the user story related to, the acceptance criteria, the tasks involved and a MOSCOW label of prioritisation. I also ensured that it was linked to the relevant project (FootNote) and that it was linked to a Milestone, where applicable.:

Detailed user story from the project, on the kanban board: ![alt text](./static/media/footnote_detailed%20user%20story.png)


-Epics -  overarching themes the user stories can slot into
-Themes - 
-Sprints -  short pockets of time that tasks are priortised for
-Acceptance Criteria
-Tasks -  tasks to be carried out to fulfill the user story
-To do/in progress/done - the sections of the kanban board
-I inserted a number of Milestones for the project, which helped me to establish when things needed to be due and aided me in setting realistic goals:

Screengrab of the different milestones created for this project: 
Milestones 1: ![alt text](./static/media/footnote_milestonesv1.png)
Milestones 2: ![alt text](./static/media/footnote_milestones_v2.png)
Milestones 3: ![alt text](./static/media/footnote_milestonesv3.png)


## Prioritisation:

As I was progressing through the Kanban board of user stories, I bore in mind the MOSCOW prioritisation emphasised in the Agile methodology module:
I was always thinking about what is a must-have, what would be nice to have and what would be a feature added only if we had time.

As advised in the tutorials, I applied MOSCOW prioritisation.
I divided my user stories into the following subsections:
Must Have (Ability to post an idea or footnote, separate writer profile page, log in and out and registration functionality. Abilty to edit and delete own comments)
Should Have (Medley button that is inkeeping with the out of context inspiration the app promotes. The writerprofile links to the relevant writers (Marina Carr, John Grisham, Samuel Beckett))
Could have (Ability to like footnotes. Ability to delete and edit ideas)
Won't Have (Ability to delete footnotes from the footnote log on the writer profile-to be implemented in future iterations)

As advised in the tutorials, I ensured that no more than 60% of the user stories should be classified as 'must haves'.

The colored labelling available on the kanban board, allows for quick and easy to understand presentation of the MOSCOW presentation:

Green: Must Have
Yellow: Should Have
Orange: Could Have
Red: Won't Have

Labels and MOSCOW Prioritisation (extract from the kanban board)

![alt text](./static/media/footnote_labels.png)

<b>Must have:</b>
Can create an original idea
Can create an original footnote
Can edit own footnote
Can delete own footnote 
Can register of the app
Can log in/out
Can visit different pages via navigation bar
Can like an idea posted


<b>Should Have</b>
-Counters to display number of ticks on an idea
-Counter to show how many footnotes left on an idea
-Medley button that is inkeeping with the out of context inspiration the app promotes.
- The writerprofile links to the relevant writers (Marina Carr, John Grisham, Samuel Beckett)
-Links to socials in the footer

<b>Could Have</b>
-Ability to like footnotes. 
-Ability to delete and edit ideas

<b> Won’t Have </b>
-Ability to delete footnotes from the footnote log on the writer profile tab
-Ability to rate footnotes on writer profile tab
-Only footnotes that relate to ideas the logged in user posted pulls into their footnote log

 ## Existing Features
## Landing page
Create an idea button
See three ideas, enter to find out more
Navigate to next/previous page
-Navigate to different tabs
-Dropdown to log in/log out/register
-Summary Page
Shows latest three ideas and how many likes they received

## Idea detail 
Idea detailed within
One idea per page.
Footnotes posted below
Ability to create a footnote
If you have posted a footnote, ability to edit and delete your own footnotes

## Writer profile - footnote log and writer profile
User can fill out your personal profile form. These details will be used in future features to implement filters etc
User can update this form whenever they wish
Footnote log-wherein footnotes feed in (designed by the date they were created). User can delete these as they wish with their delete button…how to ensure only deleted from profile page…can’t use delete…must use hidden?

## Sign Up – form
Fill out a registration form and receive a confirmation email

## Log in/out 
Use your registered details to log in by entering your stored email and password.
Log out of the app

## Medley page - random footnotes generated-button
Click medley to be presented with a random out of context idea/footnote from the app. Designed to inspire

## Pagination
Three idea summaries per page, then pagination comes into force.
This is so the user does not become overwhelmed.
It is an app designed to be used on a small, mobile device so visually, summary cards for three ideas seems most appropriate, to avoid unnecessary scrolling.
Once the idea card is clicked into, there will be one idea per page and up to ten footnotes. (has ten footnotes limit been enforced?) A bootstrap collapsible element has been applied to the foonotes so the ability to writer a footnote pops up immediately without having to scroll down the page

## Navigation bar. 
Summary page with summary cards for different ideas (revealing amount of likes/footnotes on an idea). Login/Logoff function. Register function. Medley tab, this is a decorative tab, to provide quick inspiration-quotes from famous writers and a button which generates random footnotes from the database once clicked

## Max length under 500 characters for both idea and footnotes
 As the focus of the website is on giving helpful nuggets on fast-occurring ideas as opposed to crossing the territory into elaborate collaboration/plagiarism.


## Future Features

## Development of writer profile page
Everyone who joins the FootNote app has the choice of having their own FootNote profile, where they post their ideas and are susceptible to criticism/feedback by the other FootNote app members who they have accepted as feedback givers on their profile. Additionally, they will be capable of applying to be a feedback giver on the profiles or other writers who they match with. They will need to be accepted as a feedback giver before they can see the ideas, vote the idea green/red and give feedback on the profiles of other FootNote members.

## Use of profiles/connecting profiles: 

Similarly to the preferences section of Tinder, upon joining the app, the FootNote member is presented with several questions, encouraging them to stipulate their area of interest, the genres they are interested in and writers they are similar to/inspired by and their form of writing (novel/songwriter/screenwriter/poet). Based on the preferences that they list, they will unlock a pool of other profiles that they can apply to be feedback givers on. The owners of the profiles they apply to be feedback givers to, will be able to see their site statistics; how much interaction they have had on the FootNote application (e.g. what ratio of green/red votes on other people's original ideas they have had, how many FootNotes they have posted as feedback to other people's profiles, how many original ideas have they posted to their own profile, when did they join the site etc.) The owner of the profile, who decides whether or not to accept the applicant as a feedback-giver on their own profile will be able to make an informed decision about whether to accept them or not based on their statistics. (e.g. if a profile owners sees that the member who has applied to be a feedback giver on their page, joined three years ago and has yet to post their own original thought and has voted 100% red on other people's original ideas without providing any Footnotes, the profile owner may not be inclined to accept them to their profile as the impression created is that they are there to steal ideas, to offer exclusively negative feedback and not to contribute anything themselves).

## Private view- a separate offline view for the idea owner. 
Can soft delete the idea at an point and due to CASCADE.DELETE function, all related footnotes will soft delete also. By soft delete, this means becomes private and visible only to the user who posted the original idea and not to the general users. Once hard deleted, the idea and all footnotes would be deleted from the app.

## View-bits of inspiration (things we liked). 
A separate view created by the moderator/administrator, showcases the most popular idea of the day and has a variety of quotes from writers and pictures of famous writers. It will also have a button called 'Inspire me'. This button will generate three random footnotes (of all of the hundreds of footnotes stored on the database for the apps) and post three of them at a time. One in each circular shaped bubble, to create a dream like effect. The footnotes will be deliberately without context and the randomness/incongruity/unrelatedness with one another may be humorous or profound and hopefully inspire the user.

## Filter on FootNotes under idea for different users
 I will insert a filter option on the footnotes left on ideas that users can filter by. It will be linked to the profile of the people who left the footnotes so filter fields will consist of their favourite genre, their favourite author, where they are from, their gender, ther style etc.

## Order footnotes by amount of likes
 I will add a like button to the footnotes and add a filter that will allow the user to order the footnotes by most liekd

## Order idea cards on summary page by most liked 
 I will also set up a system of how the cards appear on the summary/landing page. The most popular(most liked) ideas will appear on the first page and so on.

## Order idea cards on summary page by which idea received the most amount of footnotes

On the summary page, the user will be able to toggler between whether they want the ideas ordered by how many green ticks they received or how many FootNotes they received.

# UX Design

## Initial design – Balsamiq wireframes and lucidcharts ERDs

Having used both Balsamiq and Lucidcharts for design at planning phase for apps in the past, I decided to use Balsamiq for design of the wireframes and Lucidcharts to create the entity relationship diagrams for the models.

## BALSAMIQ WIREFRAMES
 Please see below the various balsamiq wireframes for each of the pages in the FootNote app, from the perspective of a desktop as well as from a mobile viewport. Not all planned pages were included in final app(not Must Haves):

Balsamiq 1(Landing page): ![alt text](./static/media/FN_Bals_Landing_Page.png)
Balsamiq 2(Registration page) ![alt text](./static/media/FN_Bals_Register.png)
Balsamiq 3(Sign In page) ![alt text](./static/media/FN_Bals_SignIn.png)
Balsamiq 4(Summary page) ![alt text](./static/media/FN_Bals_Summary.png)
Balsamiq 5(Idea Detail page) ![alt text](./static/media/FN_Bals_Idea_Detail.png)
Balsamiq 6(Writer Profile page) ![alt text](./static/media/FN_Bals_WriterProfile.png)
Balsamiq 7(Medley page) ![alt text](./static/media/FN_Bals_Medley.png)


## LUCIDCHARTS

- When considering how to start designing the models for FootNote, the Lucidchart Entity Relationship Diagrams and the workflow, I also implemented the aforementioned agile methodology and MOSCOW prioritisation. I considered what was realistic with time being the primary constraint. Additionally, I considered which aspects of the app were considered to be ‘Must Have’ features and accordingly were of absolute importance to adjust the fields in the model to suit this.
- I considered the MOSCOW categorisation of the features when designing the models.
- The blog walkthrough and Kanban board feature assisted me in thinking about what features I would include in project four and how to go about implementing these/dividing these into sections that I could apply in a structured manner and what needed to be prioritised at different points. The Kanban board is an excellent time management tool.
- Inspired by the walkthrough projects (Django ‘to do’ app for CRUD functionality as well as the blog walkthrough), I planned on having the design for the model classes neatly planned and laid out in tabular format in  Lucidchart, which would help me to formulate the structure of the models in my own head when designing the code for the app:
- When designing the models, I delved deeply into the tutorials and suggested readings inserted, referenced on the LMS to try to ensure that I had a good level of Django/the Django structure prior to writing/designing the models:

## My understanding of Django:
<b>Model-View-Template Structure</b>
- Model
 The models are based on object relational mapping. They contain essential fields of the data. Each model maps to a single table. Django contains implicit functionality, hiding the plumbing (it is not explicit, all of the details are not transparent on the surface)
- View
The views contains logic, it is the controller of the app. The view defines the business logic that links the html templates with the defined models.
- Template
The HTML templates are the user interface. The templates impact the presentation layer- how the information is displayed to the user. The HTML files should be filled with designer-friendly syntax for rendering information to be presented to user. 

The business logic (contained in the views) should be separated from the presentation logic(contained in the HTML files.)

 Separation of concerns is a core concept/feature of Django. Django was initially used for newspaper functionality (as discussed in a CI Webinar), which contributed (I imagine) to the emphasis on separation of concerns; separating different features of projects into different apps, separating the test files from what the files they are testing (e.g. adding a test_views.py file) and having a separate test file for each type of testing (e.g. test_views.py and then separately, test_models.py and separately test_forms.py). I certainly tried to accommodate this trend/approach. I maintained separate files as necessary, separate test files and also separate apps. For example, I created a separate app for the Medley page despite it only being one model, to be inkeeping with the Django separation of concerns approach.

## What is expected of the developer with regard to Django?:
With Django, the designers are assumed to be comfortable with HTML and Javascript code. The syntax is embedded within the HTML files, which is subsequently used to inject data into the webpage. 
In summary, with Django, the focus is on being implicit and hiding the plumbing (which goes against the usual Python approach of better to see something). The Django approach is to offer enough functionality (branching and looping) to allow us to make 'gooey' decisions.
 Django certainly supports the DRY (Don’t Repeat Yourself) approach to ‘lazy’ (😉) developers. Code need not be rewritten as the foundation html, the ‘base.html’ file can be extended into other files with {% extends base.html %} with additional slices of specific, page specific code splice in (e.g. {% extra title%}) Django allows the user to route between different templates to avoid duplicating/repeating code.
Base.html is the premise and other html files used, %% block quotes slotted into base.html file. Base.html file extended.

With Django, I focussed on convention over configuration, wherein I only specified the unconventional aspect and tried to draw the conventional aspects in directly from the Django framework (e.g. django_countries).

If the developer wishes to stray from convention, explicit code needs to be added.

- Views:
As per the blog walkthrough, I used class-based views but I did also include a number of views which are solely definition based (e.g. function based views)

The class based views allowed me to use code that is reusable and that inherits from one another.
'Generic views' (built in Django feature) used, batteries included philosophy of Django.

Connecting cloudinary, used cloudinary for image storage and for quick urls. Due to some syncing issues between Heroku and Cloudinary, also installed whitenoise to circumvent having any syncing problems.

I summary the Django framework was extremely useful and time-saving, the code is already written, for the developer to plug specific code into it. The django framework provided the basic structure and I customized within reason.

<b>Class Models</b>

The two models in the footnote app have been derived from the blog walkthrough project but customised accordingly and tailored code to suit my project; 'Idea' model and the 'FootNote' model.

I added an additional feature to the footnote model that a counter was attached to each idea and this was displayed under the idea, to show how many footnotes were received on a comment. Also placed exactly beside the likes so a nice visual comparison given for how many footnotes there were compared to how many likes there were. I also connected a form to the Idea model to enable users to leave original ideas. I deliberately removed the author field from the Idea model to ensure unbiased reaction to the ideas due to the anonymous nature.
 I created two new apps since the original submission; the writer_profile app and the medley app.
 Thw writer_profile app contains a Writerprofile model and WriterProfileForm.
The new medley app contains a view that uses the random method to pull random footnotes from the FootNote Model.

## Lucidcharts

Luidcharts and it's easy-to-use shapes (circles, arrows), color scheme (to discern features/relationships from one another) and tabular format (enabling me to use separate tabs for different views/drill downs into models etc) greatly assisted me in designing how I wanted the app to look.

The ability to use various shapes that had colour coding-operated as a visual legend of sorts. The arrows also helped me to design on a chain of command.

I mapped various parts as 'One to Many Relationships' or 'Many to One' and colour coded them. Please see the Entity Relationship Diagram for FootNote designed on lucidcharts below:

FootNote ERD on Lucidcharts: ![alt text](./static/media/lucid_charts_one.png)

 I found lucidcharts useful in general for planning  and prioritization. It helped to draw things out as I was watching tutorials or going through the walkthroughs, as it might the logic easier to understand and assisted with understanding chain of action. Please see various planning tabs from my Lucidcharts below:

Lucidchart extracts:
Lucidcharts 1: ![alt text](./static/media/lc_1.png)
Lucidcharts 2: ![alt text](./static/media/lc_2.png)
Lucidcharts 3: ![alt text](./static/media/lc_3.png)
Lucidcharts 4: ![alt text](./static/media/lc_4.png)
Lucidcharts 5: ![alt text](./static/media/lc_5.png)
Lucidcharts 6: ![alt text](./static/media/lc_6.png)


## Directories, frameworks and technologies used:
Cloudinary
Django
Boostrap
Summernote
Whitenoise

## Things to consider when compiling project
-Order
-Frameworks to be installed (Django, Summernote, considered using Flask and reviewed a number of Bootstrap templates that I could have used)

-MVP-My focus was on keeping in line with the Minimum Viable Product (CRUD, Object orientated programming and object orientated programming (classes))

-Refactoring/inheritance (order of code, inheritance from parent code and using minimum amount of code/avoid repetition)
Excellent feature of Django-blocks of code that could easily be slotted into the base.html file.


# Testing 
-Manual testing:
Do the buttons work
Class tests written
Separate test files and separation of concerns
Build test and make them fail
Manual testing...testing for responsiveness...testing programmes


-Design based coding...app aimed at mobile phones. Used developer tools to view the app from different mobile phones and ensured it was responsive. (bootstrap container/container-fluids and columns used, flexbox used, overscroll:hidden, vh and vw) Developer tools used to assess different viewports-mobile first design

## Bootstrap:
<ul>
Bootstrap made the process fast end easier
Implemented in the design of the following:
<ul>
<li>The cards</li>
<li>The buttons (idea button, footnote button, medley button)</li>
<li>The carousel on the Medley page</li>
<li>The collapsible on the Writer profile page</li>
<li>Responsiveness (container and container fluid classes, columns stipulated the viewport size lg md sm)</li>
<li>Used bootstrap for alert messages (alert when footnote submitted, edited or deleted)</li>
</ul>

# UX DESIGN

I ensured that the design was focussed on the idea behind the app, the transient nature of creativity and quick add-on inspiration whilst on foot. Accordingly, the Foot and Note parts of the name are split by capitalisation and colour in some instances. To emphasize the 'by foot' or transient element, I used the color scheme of the title to separate the Foot from the Note-Foot in purple, Note in black. Also to fit in with the leaving a footnote to an original idea theme, the a ot of superscript 'x' is used throughout. Use of superscript-in keeping with them theme, I used superscript in the titles. Visually appealing and on theme. <sup>FOOTNOTE</sup>

  To denote the creativity, the following play on words is incorporated alongside the Create an idea button:

  'Tread softly because you tread on my dreams' from 'Aedh Wishes for the Cloths of Heaven' by WB Yeats, altered subtly to 'Thread softly because you thread on my dreams', with the distinguishing 'h' emphasised with color. This is in reference how people are putting their creative ideas out there to be footnoted but those providing feedback should also be sensitive with the ideas of others.


To ensure that the app would be fully responsive, I applied mobile-first design, using Google developer tools. I ensured everything was responsive and visible on the smaller viewports.

The app is designed for those who are on the move, out and about and are struck by quick inspiration and want instant feedback so naturally, is designed to be used by users when they would be on their mobile phones. Accordingly, the app has been designed to be responsive to a number of different types of phone, as seen in the responsive testing section.

Having done some research online, the font that I have chosen to incorporate on the majority of the app (aside from the Medley tab), 'Dancing Script' is inkeeping with the theme of creative writing, so I felt it was most appropriate as it looks like handwriting.


To further establish the aforemtioned fast-moving and transient nature of what the app is intended for (quickly occurring spouts of creativity), I used bright colors (purple, red, blue, green), quick messages/modals and the carousel with changing images on the Medley page as well as the medley button that produces random footnotes from the app when clicked.

The writer profile is also an important aspect of the design, it is intended for writers who seek feedback so, accordingly having their own page where they can have their own information stored (which they can readily udpate) and that the footnotes feed in from the main site and they can mark the ones they consider more inspirational/useful from their own perspective (currently this is done with a check button in a 'favourite column' where they can denote the footnotes that are their favourite so that they can refer to them at a quick glance). Future designs will also include a star rating for each.

## Logo on Looka

Having used Look for a logo in a separate project, I considered it to be a good investment and purchased a logo from Looka for this app. I stipulated the theme and colour preferences and was presented with the following (which I have incorporated as a favicon):

Logo: ![alt text](./static/media/favicon.ico)

## Colors
I considered various color combinations when settling on a design.
I explored a variety of options on colormind.io/

The colours that are most used throughout the website: Peachpuff (for the cards and containers) and purple (for the font)
Traditional green and red used for submit, edit, delete buttons so that these would stand out. Blue is used for the medley button as it is intentionally quirky.


- Shape:
 Maintained the summary of cards from blog walkthrough, appreciated the visual impact as the cards look like post-it notes and aligned with the theme of footnote…deliberately note exactly aligned in terms of size, to represent diversity
Use of opaque footprint as background: Above masthead on summary page and in place of masthead on individual idea pages-inkeeping with the transient, on foot theme.

- Font used:
I explored a variety of options on Google Fonts before choosing Dancing Script. I chose Dancing Script because the font looks like handwriting. It is very neat, calligraphy-esque style handwriting and accordingly was inkeeping with the theme of creative writing.

I incoporated different fonts used on the medley page to convery the mix and match theme of that page.

- Additional design feature: Use of Superscript. To represent the ‘footnote’ theme. The comments are there to build/extrapolate on the original ideas not to negate from them or to be off topic

- I incorporated font awesome in my design, footsteps beside ‘thread softly because you thread on my dreams”, the icones beside each field on the suerprofile form in the writer profile tab.
Semantic styling of font, added to word play ‘Foot’ and ‘Note’ aspects of name in different colours

- I always considered how responsiveness when designing the app. I focused on smaller devices(e.g. phones/ipads/tablets/laptops) while on the move-emphasis on responsiveness. This is because the app is aimed for busy people who are on the go who are struck with inspiration and want quick feedback for their ideas.

- Use of footnote superscript in the title (and dragging into the footnotes). 
To support the idea that users are contributing small tidbits of inspiration/nudges in the right direction, adding on to the idea like a footnote as opposed to offering major insights.

- I ensured to incorporate Modal messages in my design, having been impressed by them in the walkthrough. I automatically generated messages that were prompted when various actions are taken. (E.g. a modal message appears when a footnote is submitted or when the user logs out)


-  Alert messages-similar to modals but don't need to be dismissed.

- Counter on likes and counter on number of footnotes-can like without leaving a foonote, both reflected in the summar card on summary page

## Future features of design
- FootNote Log to be developed a lot further. Eventually this will be a place foe the user to privately store footnotes that inpisred them. They will readily be able to delete footnotes from their profile and also they will be able to leave a star rating on footnotes.

# Technologies used
-Summernote
-Django
-Crispy forms
-Cloudinary
-Python
-HTML
-CSS
-Whitenoise

When deciding what to do for the project, I also considered Flask (particularly the CI Torin project).

## Testing

<p>Using the tutorials on testing from the To-Do app walkthrough, I ensured to follow those steps to test the files.</p>


Django has a testing framework-with automated tests.
Django is inbuilt with test.py file. Django imports testcase which is a class-extension of Unittest (methods to assert things about code)
Testing is based on assertions. 
-Write classes within files to test various things within targeted files
Once class is written, run the test command:
-python3 manage.py test command run 
After command run, output will be printed to the terminal providing a summary of the following details of the test:

We see whether a test failed, coded as one of the following, '.','F' 'E'
. = passed test
F= failed test
E= Error detected

We see what test failed and why
We are provided with a Summary detailing: How many tests were run, how long it took and how many failures there were.

## Testing of the FootNote App
For the FootNote App, I tried to write specific tests to see whether the specific tests fail.

Firstly, I split the 'test.py' file out into three separate files for more specified testing, clear code (organised and easy to manage, keeping tests independent of one another). I completed a select number of tests only due to limited time: 


(1)Test forms - split into test_forms.py file

<p>What was tested for forms</p>
Imported 'FootNoteForm' from forms.py file and django.test from TestCase
Wrote a class and included a test for form ensuring that FootNote form was not submitted blank.


(2)Test models - split into test_models.py file
<p>What was tested for models</p>
Test footnote will autmotically be false until approved by admin.


(3)Test views - split into test_views.py file
<p>What was tested for views</p>
-Get summary page
Tell it summary page-idea detail. Test uses HTTP response.
</p>

Once this was done, I performed a coverage test to see what % of the app had been tested. 

Command to install:
pip3 install coverage
Command to run coverage test examine all of the tests written to see what % of app was tested-a report generated as a result:
coverage run --source=todo manage.py test

To view the report, I input the command:
coverage report
Can use an interactive HTML report, using command:
coverage html
and then to view this report, use following command:
python3 -m http.server

Thsi gives us the reason that various parts are not 100% covered so that we are know what is left to be tested.


## Manual Testing Write-Up
I carried out various tests to ensure that the functionality of the app was as intended:
-Pagination-I checked could I move from page to page and were there three ideas per page, as intended
Supposed to move to a new page when three idea summaries are on site, wrote six ideas to test this and sure enough three moved to a separate page.
-Max ten footnotes per page...check if this is in place
-I checked the functionality of the footnote button. Sure enough, when footnote textarea is filled and the submit button is clicked, a message appears confirming that the ‘Footnote was been submitted”.

-Checked that as intended alert messages were prompted when user elects to log in and log out


## Responsiveness testing:

As influenced by the Peer Code Review page on slack, I ran the app through AMIresponsive and have included the image at the start of this README.

I ensured to use Bootstrap, which ensured more centred design. (col, rows, containers)
I employed the following within my CSS design to ensure that the app was responsive to smaller devices: 
Justify-content center
Flex
Overflow:hidden
Margin


vh and vw used- which sizes things relative to the viewport height(vh) and viewport width(vw)

Please see below, a variety of responsiveness testing photos on different viewports,
viewed online via Developer Tools:

Sample photos on different viewports:

Iphone 12 pro: ![alt text](./static/media/footnote_iphone12.png)

MacBook Pro: ![alt text](./static/media/footnote_macbookpro.png)

Ipad Air: ![alt text](./static/media/footnote_ipadair.png);
![alt text](./static/media/footnote_ipadair2.png)

Nest Hub:  ![alt text](./static/media/footnote_nesthub.png)

On small devices, on the landing page, the summary cards stack on top of one another in a responsive fashion instead of becoming stretched or crushed and the visibility is not affected by the size of the viewport.

The user has the ability to scroll down.

## Compatibility testing

I tested the FootNote app on various browsers to check compatibility.
See below various browsers listed and detail on compatibility with app:
<table>
                <caption><b>Testing for compatibility</b></caption>
                <tr>
                    <th><b>Google</b</th>
                    <th><b>Safari</b></th>
                    <th><b>Firefox</b></th>
                    <th><b>Internet explorer</b></th>
                </tr>
                <tr>
                    <td>Site is compatible</td>
                </tr>
                <tr>
                    <td>Yes</td>
                    <td>Yes</td>
                    <td>Yes</td>
                    <td>Yes</td>
                </tr>
                <tr>
                    <td>Links/URLs work as intended:</td>
                </tr>
                <tr>
                    <td>Yes</td>
                    <td>Yes</td>
                    <td>Yes</td>
                    <td>Yes</td>
                </tr>
                <tr>
                    <td>Images load:</td>
                </tr>
                <tr>
                    <td>Yes</td>
                    <td>Yes</td>
                    <td>Yes</td>
                    <td>Yes</td>
                </tr>
                <tr>
            </table> 

 Include screengrabs using developer tools   

 Google: ![alt text](./static/media/footnote_google.png)
 Safari: ![alt text](./static/media/footnote_safari.png)
 Firefox: ![alt text](./static/media/)
 Internet Explorer: ![alt text](./static/media/)        

## Bugs resolved and unresolved

One of the useful inbuilt features of Github with regard to python code is that the PEP 8 errors are detailed under problems.

PEP8 errors: ![alt text](./static/media/)

 Go into each file and check these. Usually issues with line being too long, whitespace left after code lines, not enough spaces before a line of code etc.

- I encountered an issue when I opened the reposiatry from Github as opposed to from the pinned workspace. I had to recreate the env.py file and reinstall dependencies by freezing the requirements.txt file when this happened.

- Used 'Hello Django' blog code as boilerplate code, had to get rid of author as author id not recognised.

- Django, large useful error messages
Browser open as I coded, refreshed and received feedback into different types of errors and reasons for them

- Email was a field in the footnote model but it disrupted the process of users loggin a footnote. All hte logger in user does to leave a footnote is insert text in the content box and submit on the idea page. But I noted when approving footnotes on the admin interface that footnotes could not be approved as they were missing an email address. As an immediate fix, I deleted the email field from the FootNote model, mademigrations and migrated.

## Lighthouse testing outcomes

- I completed Lighthouse testing of the application via google developer tools:
I did this via Google developer tools and was satisifed with the result of 97% performance.

Lighthouse test:  ![alt text](./static/media/footnote_lighthouse.png)

## Code validation

Different validators used for each language type (HTML, CSS, Javascript, Python) Please see below a screengrab of the results for each:

## HTML
<p>[W3 Markup Validation] https://validator.w3.org
 Only minor errors. 3 HTML files, code manually tested for each. Copied and pasted
 into validator

 Please see the results for the HTML validation testing for the various HTML templates below:

 Landing Page:
 Idea Detail:
 Sign In/Out:
 Medley:
 Writer Profile:
 

<p>Javascript testing</p>

jshint.com: ![alt text](./static/media/jshint_footnote.png)

No errors

<p>CSS: [W3 Jigsaw] https://jigsaw.w3.org/css-validator

No errors found received when CSS code runthrough validator (via copy and paste)

medley css: [alt tex](./static/media/footnote_css.png)

</p>

<p>Python:</p>
Django is a python framework, comes with inbuilt python testing
Test.py file and PEP8


To ensure python testing was installed and working, used following commands:
"pip install pep8"

Sure enough, received the message that PEP8 was already installed
Also tried to ensure pylint requirement satisfied also,
"python -m pip install pylint"


 I completed additional python testing on the Code Institute python testing tool: (https://pep8ci.herokuapp.com/)

footnote app:
forms: ![alt text](./static/media/footnoteforms_pytest.png)
models: ![alt text](./static/media/footnotemodels_pytest.png)
urls: ![alt text](./static/media/footnoteurls_pytest.png)
views: ![alt text](./static/media/footnoteviews_pytest.png)

writer_profile app:
forms: ![alt text](./static/media/writerprofileform_pytest.png)
models: ![alt text](./static/media/writerprofilemodels_pytest.png)
urls: ![alt text](./static/media/writerprofileurl_pytest.png)
views: ![alt text](./static/media/writerprofileviews_pytest.png)

medley app:
views: ![alt text](./static/media/medleyviews_pytest.png)
urls: ![alt text](./static/media/medleyurls_pytest.png)


WAVE Accessibility testing:
 I performed accessibility testing at wavewabaim.org. I learned about this additional testing piece when researching on Slack. I noted other students were completing this and thought that it would be useful for my project also.


## Features testing

Having considered the must-have users stories, I ensured to test the following functionalities on the website:

-I ensured to test the ability to 'Create an Idea'. I ensured that the initial call to action button was functional in that it opened the relevant form. I ensured that the placeholders in the form were correct and information. I ensured the submit button worked and that a modal appeared alerting me that I had submitted an idea. When this was complete, I logged into the admin interface and confirmed that the idea had been posted there for approval.
-I checked that the photo upload field worked properly when creating and idea
-I ensured that the counters on the ideas accurately reflected the number of likes an idea received (I tested whether this changed when I clicked it, decreasing and increasing in number accordingling). I also checked how many FootNotes were left on an idea. I manually counted them and checked the number on the counter to ensure accuracy.
-Summary cards open up more detail idea post when clicked
-I checked that the pagination worked as intended (three ideas per summary page)
-I checked the the max footnote function was wokring
-I checked that the account regisation worked. I registered an account and ensured I could log in after that with those details
-I checked that I could log in with my registered account, log out and then back in again.
-I checked that the messages worked and disappeared by themselves after the time i ahd specified in the code (6 seconds-6000)
-FootNotes give detail on who posted them and when they were posted
-I checked that the links to socials, Facebook, Tiktok, Instagram and Twitter, as well as personal website, that were listed in the footer all successfully oepend on a separate page
-I checked that the NAV bar effectively allowed me to navigate to the pages that it indicated. I also checked the the FootNote in the corner led to the landing page as I ahd intended.
-I checked that the dropdown gave me options
-I checked that i could post a footnote to an idea (Enter the idea page, enter text in the footnote content box and submit footnote). I ensured I received a message confirming submission and checked the admin interface afterwards also. 
-I checked did all of my footnoes show that I had the capaability of editing them and deleting them (the edit and delete buttons should automatically appear under footnotes that the logged in user has left)
-I checked did the edit button function as intended (autopopulate the content box with my previous footnote, enable editing and have the text on the button change from submit to update.) I ensured the footnote matched the updated text once submitted.
-I checked did the delete button work as intended. Once delete is clicked, defensive programming was provoked, asking me to confirm whether I would like to permanently delete my footnote. Once confirmed, the footnote was deleted and no longer appeared under the idea.
-I checked on the writer profile tab could I freely update my personal details. The field updated accordingly once update was clicked and the answers remained that way even when navigating away form the page and back again
-I checked did the collapsible work as intended in the footnote log on the writer profile page. As intended, it revealed and hid the footnotes that pulled in from the main site as intended
-I checked did the checkbox inserted beside the footnotes in the footnote log work. These are currently just for aesthetic reasons. It is to be helpful to the writer to tick particular footnotes they are interested in so they can asily transfer them to a laptop etc without losing their place as there are a lot of footnotes. The check box does not remain ticked once the page is refreshed
-I checked did the carousel feature on the Medley page work as intended. As intended, I could flick from one slide to the next using the controls.
-I checked did the medley button work, as intended when the medley button is clicked it pulls in and displays a random footnote from the ideas posted to the app.  It denotes solely the content the the person who left the footnote. It is designed to provide quick moments of out of context inspiration.


# Deployment
<b>Deployment, forking, cloning </b>


<b>Deployment:</b>

I completed early deployment as per the walkthroughs to avoid last minute panic.
Before writing the code, I set up an instance on ElephantSQL and then created the app on Heroku. I used the API from ELlephant SQL to build Heroku APP. Connected Heroku with Github CLI for automatic deployment.

This was done in order to avoid last minute delays.

The importance of disabling the DEBUG feature was emphasised in tutorials as well as the importance of removing the DISABLE_STATICFILES so this was at the forefront of my mind for final deployment.


## Challenges with deployment>
Surely enough, I had some difficulties, migration wouldn't work on my first attempt so I had to redo the entire application (repositary-Elephant SQL-Heroku app-migrate…DEBUG off, remove disable collectstatic etc.)

In the end, I believe migration would not work due to mixing up the use of app name versus project name in some of the code so I ensured to be very careful with this going forward.


I ran into this issue again on the friday prior to finishing the project and as tutor assistence had signed off for the night, I redid entire app and project on Github/ElephantSQL and Heroku. All was well until I tried to deploy on Heroku and the build log revealed the buildpack wouldn't recognise any languages (e.g. python). I tried to tweak...but again believe issue may be app was created as 'footnote_final' on Gitpod but is named as 'footnotefinal' on Heorku as they won't allow underscores.

I checked in with my tutor the next day and after all of the rework, it was revealed the env.py file and installations needed to be redone due to me having opened the code using gitpod as opposed to the pinned workspaces platform. A lesson learned the hard way!

  A couple of shortcuts for this was I used the reveal config vars in Heroku to inform me what to input in my env.py file and I recursivrly installed the needed packages form the requirements.txt file using the following command:

  pip3 install -r requirements.txt

Had a few different versions of the app on Heroku and had connected the database to the wrong postgres url so no info appeared, updated DATABASE URL in env.py file to amend

### Github Deployment

The website was deployed using GitHub. To do this I did the following;

1. When on the websites GitHub repository, I clicked on the 'settings' tab.
2. Then on the settings page, on the left hand side of the page, I clicked on the 'pages' tab.
3. Under the Source section,  I selected 'main' as the branch.
4. This procured a published link.

### Creating a Fork or Copying

To clone/fork/copy the repository you click on the fork tab which is situated next to unwatch tab in the top right corner of the page

### Copying the repositary on Github

To create a clone of your project:

1. Click the green 'Code' dropdown button beside the green 'Gitpod' button in the repositary page on github
2. Select the clipboard/copy icon
3. In the IED open GitBash
4. Change the working directory to the location you prefer
5. Add Git Clone with the copy of the repositrory name
6. Clone has been created

### Heroku

- I logged into my account on Heroku.com.
- I clicked new on the dashboard and selected, 'Create New App' from the drop-down menu.
- I entered an app name, chose my region and proceeded to create the app.
- I navigated to the settings tab and the 'Reveal Config Vars' section. When there, I added the key of 'Port' and the value of '8000'. 
- On the same page, I selected, 'Add buildpack' and selected 'python' first and once that was added, I selected 'nodejs' in that order. The order these are added was important.

## On Heroku
Go to settings-Reveal Config Vars

Remove DISABLE_COLLECTSTATIC config variable

Deploy tab, scroll to end, deploy branch

As the app was deploying, I scrolled to the activity tab and monitored the build log to ensure all was working okay.

# Deployment of the app on Heroku

- I navigated to  the 'Deploy' tab and selected 'Github-Connect to Github' so that for each subsequent commit on Github would be automatically deployed to Herkoku.
- When linking, I retrieved my repositary using the search function available, then connected.
- Following deployment, I could access the deployed live project.


## Additional steps for dpeloyment on Github
- There were a number of tasks to be completed prior to deployment as the project was moved from development to production phase.
- I disablef debug. This gets rid of the traceback which may have compromised the site.
-Install 'X-Frame Options=Same Origin'. This is a CORS(Cross Origin Resource Sharing) security feature.
- Tells system resources are permitted to be loaded
- I removed the DISABLE_COLLECTSTATIC field from Heroku

# Credit and Thanks

## References

The images on the medley page were all pruned from pexels.com
Other images were pruned from pixabay:
https://pixabay.com/photos/pocket-watch-time-sand-clock-3156771/
A number of free open sources used for photos that appear as featured images on idea cards on the summary page.
 They are uploaded to admin interface when original idea is posted. If no image provided then there is code that defaults to a different image via url in code. Whitenoise also installed to overcome any syncing issues between Cloudinary and Heroku.
Footprint image in background from the following source: https://codepen.io/bogers/pen/MWJjwJa?editors=1111
All Code Institute tutorials-particularly the blog walkthrough and ‘to-do’ walkthrough.
Also an additional webinar was provided for PP4 which further detailed requirements and provided an updated blog walkthrough repository with additional features. When implementing the additional CRUD functionality for resubmission, I found the following tutorial and code that the Code Institute made available with regard to the Blog walkthrough very useful: https://www.youtube.com/watch?v=YH--VobIA8c
Agile methodology webinar provided by Code Institute:


## Credits

-Slack community
I derived a huge amount of inspiration from Slack. Particularly the PP4 page, the peer code review page and the MSLETB page. Feedback/encouragement was provided via comments/review of various projects on peer code review page/searching for keywords with regard to my query and looking over old threads.
Drew inspiration from the following projects on the Peer Code Review page, in particular:
Blade 5 Repositary Roman: Romanc
Coffee Now repositary via peer code review: Kieran 123
Fitness Booking
-Django documentation and W3 school
-Tutor Support
Ensured to avail of the ninety minutes of weekly tutor support available to me when I had various queries/coding issues. I was always pointed in the right direction.
-Mentor
Mitko Backvarov
Had my three meetings for submissions and greatly assisted me with two additional meetings for resubmission, targeting the areas highlighted in the assessor feedback (CRUD functionality, agile methodology and testing)
Having considered the updated features included with this tutorial, I included the additional option of the logged in user being able to edit and delete the footnote that they leave (in faded format) prior to being approved by the admin.


-Code open for cloud design on Medley page: [Title](https://codepen.io/fershocastro/pen/dVBgxQ)
-Code tutorial on adding star rating: 
-Codemy video on styling form: [Title](https://www.youtube.com/watch?v%253D6-XXvUENY_8)