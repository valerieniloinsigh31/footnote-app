# FootNote App - Portfolio Project Four - Full Stack Toolkit

<img src="static/media/" -put in image from AmIResponsive

## Live Site: 

## Repositary: 

## Contents

-Project Description and Goals
-User Experience Design and Agile Methology
-Features
Existing Features:
-Landing page
-Summary
-Idea detail
-Writer profile
-Sign In
-Log in/out
-Medley page
Future Features:
-Technologies used
-Testing 
-Deployment
-Credits and thanks


## Project Description and Goals
An app for creative writers who are often struck by inspiration whilst out and about.
The app will be comrpised of a network of members who work as creative writers in some form; e.g. a pool of like-minded creatives with similar interests who can give feedback on one another's quick ideas. They can also store footnotes privately on a page only visible to them. The footnotes will flow automatically in from various ideas posted and the logged in user and delete or keep any footnotes they wish from their personal 'FootNote' log on their profile page. This will not impact others as it is only visible to them and, accordingly, will not negatively imapct the user experience for anybody else.

The is an approval tick beside the idea so users can signify their approval by clicking this.

Approval ticks are anonymous but offer the user who created the idea a useful insight into the popularity of their idea amongst like minded creatives.

Users are not obliged to either tick the approval or to leave a FootNote. They can do neither, either or both if they wish. FootNotes have additional transparency in case they are overly negative, for moderatership purposes. The name of the person leaving the footnote is presented beside their footnote within the idea page.

The premise of the app is that it will encourage free ideas without judgement.

It is designed to assist creative minds to nudge one another in the right direction.

 To avoid intellectual theft, the ideas and footnotes are both capped at certain lengths. 

<b>Functionalities to include:</b>

Based on the Minimum Viable Product documentation on Project 4, I concluded that I would have to have the following functionalities available in my FootNote app:

<b>CRUD mentality</b>
Both the user and superuser/administrator of my FootNote application, should have the ability to Create, Read, Update and Delete items.

Albeit, this is applied in different ways.

ADMIN
-For the <em>administrator/Superuser</em> who regulates the FootNote profile, they will regulate what appears on their profile. They can create, read, update and delete their own original ideas (one idea at a time is the FootNote policy-to avoid oversaturation.) Also there is a maximum length of 100 words per original idea posted,to be inkeeping with the initial aim of the applicaiton, to post a fast idea that occurs to the profile owner whilst out and about in order to get immediate feedback (as opposed to exposing intiacte/vital parts of their original creative ideas.)
-The admin/Superuser will be able to view FootNotes posted by the users and to approve whether they appear on the app. 
-The admin/Superuser can delete ideas (and as a result, all of the footnotes posted to it will delete with the CASCADE effect)
-The admin/Superuser can approve selected FootNotes to their offline profile. They will be able to edit/update these FootNotes once they have been moved offline and are no longer visible on their public FootNote profile.
-The admin/Superuser can change the order of the FootNotes and ideas.

USER
-From the user perspective, their statistics on the site will accumulate from the moment they joined the application. The will stipulate their preferences (e.g. their favourite genre, their method of writing-e.g. poetry, novel, screenplay, song etc) and based on their specifications, suggested connections will pop up for them (similarly to the suggested followers function in instagram or the suggested friend section in facebook or the suggested connection section in LinkedIn). The can apply to become a feedback given on the profile of one of the suggested connections. Once they submit to become a feedback giver, the owner/admin/Superuser of the profile that they have applied to will assess whether or not to accept them as a feedback giver on their profile. This assessment will be made by the historical statistics of the applicants engagement-to-date on the FootNote App becoming readily visible to the profile owner. Metrics that will be exposed with the applicants statistics are when they joined the app, how many original ideas of their own have they posted, how many votes have they submitted to other peoples FootNote Profiles, what ratio green/red votes did they submit for other ideas, how many FootNotes did they leave what % of green votes did they leave FootNotes for (the user can only leave a footnote if they vote green). This will help the profile owner to make an informed decision about whether or not to accept them as a feedback giver on their profile. 

 Once user registers, they can then perform a variety of CRUD functionalities:
 -They can read the latest original idea posted/any number of ideas they want to
 -They can click on the green tick beneath an original idea to signify whetehr they believe should not pursue the original idea further/deserves more traction. 
 -The user can leave a FootNote on an idea, with a maximum length (to support the FootNote aim of providing concise helpful nods in the right direction as opposed to giving away intellectual property). 
 FUTURE FEATURE:-They can update or delete their FootNote at any point they want to (this will also be reflected in the statistics on their own profile). They can do this up until the point that they profile owner deletes the original idea (the FootNotes will disappear along with the original idea due to the CASCADE effect applied)
 FUTURE FEATURE:-They will be able to click like or unlike on FootNotes posted by other users

From what perspective can members use the app?: I intend to apply this from both a user perspective and a supersuer perspective.

The app from the perspective of the superuser who is also the administrator and, as such, a regulator of the site will be able to log in and regulate the front end view of their profile. They will operate as an administator and readily be able to control what views and posts appear on their page. 

<b>What is it?:</b>
 The FootNote app is an app connecting creative people. It connects creative people whose art form is original writing of some sort, who want to share their original ideas and to get instant feedback from similarly minded people in useful footnote format, with a maximum amount of characters so that the contribution provided by other app users is a helpful nod as opposed to providing an idea to plagiarise. 
 
  The emphasis on transparency (Every footnote will be attributed to the footnote giver),  is in place to ensure that nobody abuses the app or tries to use it as a method of stealing the original thoughts of others/to offer unconstructive negative feedback. Equally the ideas left are anonymous so that the ideas are judged/assessed/reacted to exclusively from a creative perspective...the anonmymous nature of the idea itself guarantees unbiased footnotes will be provided.

 EXISTING FEATURES 

FUTURE FEATURE
 Similarly to the preferences section of Tinder, upon joining the app, the FootNote member is presented with several questions, encouraging them to stipulate their area of interest, the genres they are interested in and writers they are similar to/inspired by and their form of writing (novel/songwriter/screenwriter/poet). Based on the preferences that they list, they will unlock a pool of other profiles that they can apply to be feedback givers on. The owners of the profiles they apply to be feedback givers to, will be able to see their site statistics (how much interaction they have had on the FootNote application (e.g. what ratio of green/red votes on other people's original ideas they have had, how many FootNotes they have posted as feedback to other people's profiles, how many original ideas have they posted to their own profile, when did they join the site etc.) The owner of the profile, who decides whether or not to accept the applicant as a feedback-giver on their own profile will be able to make an informed decision about whether to accept them or not based on their statistics. (e.g. if a profile owners sees that the member who has applied to be a feedback giver on their page, joined three years ago and has yet to post their own original thought and has voted 100% red on other people's original ideas without providing any Footnotes, the profile owner may not be inclined to accept them to their profile as the impression created is that they are there to steal ideas, to offer exclusively negative feedback and not to contribute anything themselves).

Everyone who joins the FootNote app has the choice of having their own FootNote profile, where they post their ideas and are susceptible to criticism/feedback by the other FootNote app members who they have accepted as feedback givers on their profile. Additionally, they will be capable of applying to be a feedback given on the profiles or other writers who they match with. They will need to be accepted as a feedback giver before they can see the ideas, vote the idea green/red and give feedback on the profiles of other FootNote members.

<b>DESIGN:</b>

Having used both Balsamiq and Lucidcharts for design at planning phase for apps in the past, I decided to sue Balsamiq for design of the wireframes and Lucidcharts to create the entity relationship diagrams for the models.

<b>BALSAMIQ WIREFRAMES</b>

 Please see below the various balsamiq wireframes for each of the pages in the FootNote app, from the perspective of a desktop as well as from a mobile viewport. Not all planned pages were included in final app(not Must Haves):

Balsamiq 1(Landing page): ![alt text](./static/images/FN_Bals_Landing_Page.png)
Balsamiq 2(Registration page) ![alt text](./static/images/FN_Bals_Register.png)
Balsamiq 3(Sign In page) ![alt text](./static/images/FN_Bals_SignIn.png)
Balsamiq 4(Summary page) ![alt text](./static/images/FN_Bals_Summary.png)
Balsamiq 5(Idea Detail page) ![alt text](./static/images/FN_Bals_Idea_Detail.png)
Balsamiq 6(Writer Profile page) ![alt text](./static/images/FN_Bals_WriterProfile.png)
Balsamiq 7(Medley page) ![alt text](./static/images/FN_Bals_Medley.png)


<b>LUCIDCHARTS</b>

Agile methodology-apply the MOSCOWprioritisation...

As I was thinking about what features to add, I categoreised them as must have, nice to have etc.

The blog walkthrough and Kanban board feature assisted me in thinking about what features I would include in project four and how to go about implementing these/dividing these into sections that I could apply and what t to prioritise...

Inspired by the walkthrough projects (Djanjo to do app and blog), I planned on having the design for the model classes neatly planend and laid out in tabular format in a Lucidchart format, which would help me to formulae the idea in my own head when designing the code for the app:

<b>Model-View-Template</b>

<b>Model</b>
 ORM-Object relational mapping...contains essential fields of the data. Each model maps to a single table. Django contains implicit functionality, hiding the plumbing.

<b>View</b>
ontains logic, it is the controller of the app. Define the business logic that link templates and models.

<b>Template</b>
User interface. Presentation layer- how info is displayed to the user. Designer-friendly syntax for rendering information to be presented to user. Business logic separated from presentation logic. Only concerned with presentation of data and visual elements. Can't call python code directly within templates. Visually represent data model. Syntax decoupled from HTML. Designers assumed comfortable with HTML and Javascript code. Syntax embedded within HTML, used to inject data into webpage. Most common language=Django language.

Django...focus on implicit, hiding the plumbing (against usual Python approach of better to see something)

Offer enough functionality (branching and looping) to allow us to make gooey decisions.

Convention over configuration
Developer need only specify unconventional aspects
If stray from convention, explicit code needs to be added
Implicit functionality

Boilerplate code from walkthrough
Adding customisation
Adding some non conventional, specific code

As per the blog walkthrough, I used class-based views.
Allow us to use code that is reusable and that inherits from one another.
'Generic views' (built in Django feature) used, batteries included philosophy od Django.

-Medley view building...

1. Create view code

Employ generic view.

-Views.py file: 

a. Import generic library from django.views 
b. Import model that we will base views on (e.g. 'Medley' model as defined in models.py file)
c. Create a class. 


2. Create view template

Template-html templates. Structures what you see in the view. Foor loops, shape of images. Attribute classes that are designed by CSS.

3. Connect urls file

Add the wiring, ensure to import the correct items at the top of the page and the correct url and brackets are used


<b>Principles of Agile development, prioritisation</b>

-MOSCOW prioritisation
-Kanban board (user stories, themes, epics, milestones and sprints)

Connectint cloudinary, using it for image storage and quick urls

Package=plugs into code already written (use as much/little as possible)
Django framework=code is already written, you plug your code into it...Provides basic structure, customize within reason

Routing between different templates to avoid duplicating/repeating code...extends %%
Base.html is the premise and other html files used, %% block quotes slotted into base.html file. Base.html file extended.

<b>Class Models</b>
Class-based models defined within models.py file and additional definitions included within those models.(specifications)

Two models derived closely from the blog walkthrough project but customised accordingly and tailored code to suit my project which were the 'idea' model and the 'footnote' model.

I added an additional functionality to the footnote model that a counter was attached to each idea and this was displayed under the idea, to show how many footnotes were received on a comment. Also placed exactly beside the likes so a nice visual comparison given for how many footnotes there were compared to how many likes there were.

Future features: Additional model for the person who owns the idea can soft-delete their idea and all corresponding footnotes at any time so that that the view becomes private and visible to only them...this will be a good way to ensure that the summary page doesn't become oversaturated.

Summary page, there will be a filter option inserted to order ideas either by how many green ticks they received or how many FootNotes they recieved.

The cascade delete effect is in place so once an idea is deleted, all accompanying footnotes will be deleted as well.

-Additional model for 'connect with my profile'...people who leave ideas will be able to set up a profile, containing only their ideas.
-Additional model 'Make this my favourite idea'...function of the FootNote website, users can choose one idea per per day as their favourite.

-Authentication-an additional future feature to be added is that only those who like the original idea will be able to leave a footnote-this will be to for website moderation purposes-the focus of the website is to focus on providing small nuggets of inspiration, a nod in the right direction as opposed to negative or frivolous vitriolic comments.

Max length 280 characters for both idea and footnotes as the focus of the website is on giving helpful nuggets on fast-occuring ideas as opposed to crossing the territory into elaborate collaboration/plagiarism.


-Pagination
Six idea summaries per page, then pagination comes into force.
This is so the user does not become overwhelmed.
It is an app designed to be used on a small, mobile device so visually, summary cards for six ideas seems most appropriate, to avoid unnecessary scrolling.
Once the idea card is clicked into, there will be one idea per page and up to ten footnotes. 


Idea Model:
FootNote Model:

Counter-select the green check mark, a counter is activated and this is visible also on the summary page so that users can quickly reference an idea that has received a lot of positive feedback and they might want to explore further.

Future feature: Users can vote approve/disprove of on idea
If they vote like only then will they be given the authentication to post a footnote


<p>Lucidcharts</p>

Luidcharts and it's easy-to-use shapes (circles, arrows), color scheme (to discern features/relationships from one another) and tabular format (enabling me to use spearate tabs for different views/drill downs into models etc) greatly assisted me in designing how I wanted the app to look.

The ability to use various shapes color coded-operated as a visual legend of sorts. The arrows also helped me to design on a chani of command.

I mapped various parts as 'One to Many Relationships' or 'Many to One' and colour coded them.

Order of events and priorisation easier to understand, assisted eith understanding chain of action

Lucidchart extracts:

Lucidcharts 1: ![alt text](./static/images/lc_1.png)
Lucidcharts 2: ![alt text](./static/images/lc_2.png)
Lucidcharts 3: ![alt text](./static/images/lc_3.png)
Lucidcharts 4: ![alt text](./static/images/lc_4.png)
Lucidcharts 5: ![alt text](./static/images/lc_5.png)
Lucidcharts 6: ![alt text](./static/images/lc_6.png)

<b>Kanban board and user stories</b>

Agile methodology
Helped me to form logic
Logical progression
Easy way to focus on tasks that needed to be conpleted
Features I wanted to add

As I was progressing through the Kanban board of user stories, I bore in mind the prioritisation emphasised in the Agile methodology moduke:
I was always thinking about what is a must-have, what would be nice to have and what would be a feature added only if we had time.

<b>Views:</b>

Views-what views are there for this app:
-Summary view-shows a segment of a page containing the idea (summary of all ideas posted (6 ideas per page) and a counter function shows the amount of approvals with a tick and number). Shows amount of approvals associated with idea and the main image.(either the image uploaded with the original post or a default image)
-Idea and footnote view - 1 idea per page with up to ten footnotes. Allows focus to be on that idea. On this page, all users can see idea and footnotes left as well as number of approvals on ideas and number of smiley faces or unhappy faces on footnotes. They can also see when idea/footnotes were created/edited and by whom.
-Sign in/sign out/register tabs: Functional tabs that allows the user/potential user to sign in/sign out or register for the app
-Admin interface-The administrator logs in and can moderate the site. Can issue approvals etc.


Future features:
-Private view- a separate offline view for the idea owner. Can soft delete the idea at an point and due to CASCADE.DELETE function, all related footnotes will soft delete also. By soft delete, this means becomes private and visible only to the user who posted the original idea and not to the general users. Once hard deleted, the idea and all footnotes would be deleted from the app.
-View-bits of inspiration (things we liked). A separate view created by the moderator/adminstrator, showcases the most popular idea of the day and has a variety of quotes from writers and pictures of famous writers. It will also have a button called 'Inspire me'. This button will generate three random footnotes (of all of the hundreds of footnotes stored on the database for the apps) and post three of them at a time. One in each circular shaped bubble, to create a dream like effect. The footnotes will be deliberately without context and the randomness/incongruity/unrelatedness with one another may be humorous or profound and hopefully inspire the user.

User interaction
One to many relationship?
Or many to many relationship?

Functions to break down...

One to many-the profile owner operates as the superuser or administrator of their own profile. Only they can post/edit their own original idea on their own FootNote profile. Accordingly, this is a one to many relationship.

The users or feedback givers who are viewing the original ideas of the profile owner, who are voting like/dislike on the profile owners original ideas, who are posting FootNotes in response to the ideas (which have a maximum character/word restriction but can be deleted or edited by the user until the footnote is stored/removed by the profile owner) and who can like or dislike the footnotes of other users is a many to many relationship as they can interact on the profile but also they can receive interactions by others (such as somebody liking/disliking their footnote)


<b>Directories and frameworks used:</b>
Cloudinary
Django
Boostrap
Summernote

<b>Things to consider when compiling project</b>
-Order
-Frameworks to be installed (Django, Summernote, considered using Flask and reviewed a number of Bootstrap templates that I could have used)

-MVP-My focus was on keeping in line with the Minimum Viable Product (CRUD, Object orientated programming and object orientated programming (classes))

-Refactoring/inheritance (order of code, inheritance from parent code and using minimum amount of code/avoid repititon)
Excellent feature of Django-blocks of code that could easily be slotted into the base.html file.

-Test based coding (what tests were used)
MAKE SURE TO PUT IN TESTS...Write 1/2 original tests
Manual testing...testing for responsiveness...testing programmes


-Design based coding...app aimed at mobile phones. Used developer tools to view the app from different mobile phones and ensured it was reponsive. (bootstrap flexbox, overscroll:hidden, vh and vw)

Bootstrap:
Yes-how did bootstrap assist...
the cards
the buttons
respsonsiveness
considered using different templates-for exmaple the code within the 'creative' template on the bootstrap site

Used bootstrap for alert messages
Used bootstrap formatting for cards

Object orientated design...class based models as opposed to function based models used
funtion based models used on writer profile in places


<b>Deployment:</b>

Early deployment as per the walkthroughs to avoid last minute panic.
Before writing the code, set up an instance on ElephantSQL and then created the app on Heroku. Used the API from ELlephant SQL to build Heroku APP. Connected Heroku with Github CLI for automatic deployment.

Help to avoid last minute disasters.

Importance of disable the DEBUG feature emphasised in tutorials as well as the importance of removing the DISABLE_STATICFILES.


<Challenges with deployment>
Surely enough, I had some difficulties, migration wouldn't work on my first attempt so I had to redo the entire applicaiton (repositary-Elephant SQL-Heroku app-migrate)

In the end, I believe migration would not work due to mixing up the use of app name versus project name in some of the code so I ensured to be very careful with this going forward.


I an into this issue again on the friday prior to finishing the project and as tutor assistence had signed off for the night, I redid entire app and project on Github/ElephantSQL and Heroku. All was well until I tried to deploy on Heroku and the build log revealed the buildpack wouldn't recognise any languages (e.g. python). I tried to tweak...but again believe issue may be app was created as 'footnote_final' on Gitpod but is named as 'footnotefinal' on Heorku as they won't allow underscores.

I checked in with my tutor the next day and after all of the rework, it was revealed the env.py file and installations needed to be redone due to me having opened the code using gitpod as opposed to the pinned workspaces platform. A lesson learned the hard way!

  A couple of tricks for this was i used the reveal config vars in Heroku to inform me what to input in my env.py file and I recursivrly installed the needed packages form the requirements.txt file using the following command:

  pip3 install -r requirements.txt

<b>UX DESIGN</b>

Focus on idea...
Mobile-first design, app is designed for those who are on the move, out and about and are struck by quick inspiration and want instant feedback so naturally, is designed to be used by users when they would be on their mobile phones. Accordingly, the app has been designed to be responsive to a number of different types of phone.

Sharp
Having done some research online, the font that I have chosen, 'Dancing Script' is inkeeping with the theme of creative writing, so chose as it looks like handwriting.

Use of superscript-in keeping with them theme, I used superscript in the titles. Visually appealing and on theme. <sup>FOOTNOTE</sup>

In my design, I wanted to convey the fast-moving and transient nature of what the app is intended for (quickly occurring spouts of creativity) so I used bright colors, quick messages/modals and various animations including...

Also to emphasize the 'by foot' or transient element, I used the color scheme of the title to spearate the Foot from the Note-Foot in purple, Note in black.

Colors used: Peachpuff and purple
Shape: Maintained the summary of cards from blog walkthrough, appreciated the visual
Use of opaque footpprint: Above masthead on summary page and in place of masthead on individual idea pages-inkeeping with the transient, on foot theme.
Font used: Dancing Script

Additional design feature: Use of Superscript

Footsteps...

Design-focused on smaller devices...phones/ipads/tablets/laptops while on the move-empahsis on responsiveness

Important to have one idea per page once you click into idea cards via the summary page...to avoid oversaturtion.

Use of footnote superscript in the title (and dragging into the footnotes). 
To support the idea that users are contributing small tidbits of inspiration/nudges in the right direction, adding on to the idea like a footnote as opposed to offering major insights.


<b>FEATURES</b>

-Admin interface (moderation of site-deleting ideas and footnotes)

-Post idea-all users can see

-Logged in users can check the green tick to indicate they approve of the idea, a counter feature displays the amount of approvals on the summary card for each idea on the summary page


-If vote pursue idea, can leave a footnote...Footnotes are max length 280 characters-FootNote is posted, visible for other users to see. FootNotes appear under the idea on the idea page.

The purpose of the footnote is for users to give one sentence of constructive criticism on the idea. Each user can post as many footnotes as they want. The FootNote reveals who created the FootNote and when they created it.

-Superuser posts an idea. Max length 280 words, a quick idea that occurs to them while out and about. Once posted and polls have opened, they cannot edit the idea any more as this would create a false reflection on what had been voted for if others users had already voted. Superuser can only delete idea and when deleted all associated footnotes will delete with that idea.

-Users can like or dislike other footnotes as they please. They cannot comment on other footnotes. Footnotes have a max length and users can only post one footnote per idea to avoid oversaturation.

-Navigation bar. Summary page with summary cards for different ideas (revealing amount of likes/footnotes on an idea). Login/Logoff function. Register function. Medley tab, this is a decorative tab, to provide quick inspiration-quotes from famous writers and three circles in the shape of an idea bubble which generate random footnotes from the database.
-Tooltips

-Modal messages...how used

-Alert messages

-Counter on likes and counter on number of footnotes-can like without leaving a foonote, both reflected in the summar card on summary page

<b>Future features</b>
-Filter on FootNotes under idea for different users
-Order footnotes by amount of likes
-Order idea cards on summary page by most liked
-The main image that appears on the idea will be also uploaded by the app user, it will be connected to their mobile.

<b>TECHNOLOGIES USED</b>
-Summernote
-Django
-Crispy forms
-Cloudinary
-Python
-HTML
-CSS
-Different websites for images

When performing resarch, considered Flask also (particularly the CI Torin project)

<h1>TESTING</h1>

<p>Using the tutorials on testing from the To-Do app walkthrough, I ensured to follow those steps to test the files.</p>


Django has a testing framework-with automated tests.
Django is inbuilt with test.py file. Django imports testcase class-extension of Unittest (methods to assert things about code)
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

For the FootNote App, I tried to write specific tests to see whether the specific tests fail.

Firstly, split the 'test.py' file out into three separate files for more specified testing, clear code (organised and easy to manage, keeping tests independent of one another). I completed a select number of tests only due to limited time: 


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


<b>Manual Testing Write-Up</b>

Pagination-check could I move from page to page

Supposed to move to a new page when three idea summaries are on site, wrote six ideas to test this and sure enough three moved to a separate page.

Max ten footnotes per page...check this.

Click submit button, footnote submitted, message appears

Alert messages for login and logout

<b>Responsiveness testing:</b>

Bootstrap code used which ensures more centred design.
I employed the following within my CSS design to ensure that the app was responsive to smaller devices: 
Justify-content center
Flex
Overflow:hidden
Margin

vh and vw used- sizes things relative to the viewport height(vh) and viewport width(vw)

Please see below, a variety of responsiveness testing photos on different viewports,
viewed online via Developer Tools:
Sample photos:

Iphone 12 pro: ![alt text](./static/images/iphone12_test.png)

MacBook Pro: ![alt text](./static/images/macbook_pro_test)

Ipad Air: ![alt text](./static/images/ipad_air_test.png)

Nest Hub:  ![alt text](./static/images/nest_hub_test)


Cards stack on top of one another in a responsive fashion instead of becoming stretched or crushed and the visibility is not affected by the size of the viewport

User has the ability to scroll down.


<b>Compatibility testing</b>

Tested on various browsers

See below various browsers listed and detail on compatability with app:
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
                    <td>Links/URLs:</td>
                </tr>
                <tr>
                    <td>Yes</td>
                    <td>Yes</td>
                    <td>Yes</td>
                    <td>Yes</td>
                </tr>
                <tr>
                    <td>Images work:</td>
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
<b>Bugs resolved and unresolved</b>

Inbuilt PEP 8, errors detailed in Github as coding

Opening from Github as opposed to pinned workspace...had to recreate env.py file a number of times.
Had to reinstall various dependencies...allauth, summernote etc.

-Used 'Hello Django' blog code as boilerplate code, had to get rid of author as author id not recognised.

Django, large useful error messages
Browser open as I coded, refreshed and received feedback into different types of errors and reasons for them


<b>Lighthouse testing outcomes</b>

Accessibilty low, could be improved

Lighthouse test:  ![alt text](./static/images/lighthouse_test)

<h1><b>Code validation</b></h1>

<b>HTML</b>
<p>[W3 Markup Validation] https://validator.w3.org
 Only minor errors. 3 HTML files, code manually tested for each. Copied and pasted
 into validator

![alt text](./static/images/html_validation.png) 

<p>Javascript</p>
<p>No javascript used for app</p>

<p>CSS: [W3 Jigsaw] https://jigsaw.w3.org/css-validator
No errors found received when CSS code runthrough validator (via copy and paste)

![alt text](./static/images/css_validation.png)
</p>

<p>Python:</p>
Django is a python framework, comes with inbuilt python testing
Test.py file and PEP8
CI Pytest extracts:

To ensure python testing was installed and working, used following commands:
"pip install pep8"

Sure enough, received the message that PEP8 was already installed
Also tried to ensure pylint requirement satisfied also,
"python -m pip install pylint"

<b>User stories testing</b>
As per the walkthrough, in support of Agile methodology, I set up a Kanban board to track what items I installed for the app.

Three categories:
To do, in progress, complete

Kanban board-completed as I completed coding. As I was progressing through the coding of the application, this helped me to logically prioritise and gave me immediate visual feedback as to what remained left to be done.

Kanban board:
![alt text](./static/images/kanban_board.png)


<b>Prioritisation:</b>

Focused on three categories of prioritisation:

<b>Need to have:</b>
CRUD functionality-administrator interface mainly
Can create also via footnotes as a user
Can create account with registration

-Admin interface
-Account registration
-Different views via navigation bar
-Users ability to submit footnotes for approval


<b>Maybe have</b>
-Counters to display number of ticks on an idea
-Counter to show how many footnotes left on an idea

<b>Nice to have</b>
-have mentioned future features
-Ability to like footnotes left

<b>Features testing</b>

-Post FootNote
-Counters reflect number of likes an idea received and how many FootNotes were left on an idea
-Summary cards open up more detail idea post when clicked
-Pagination works effectively
-Account regisation works
-Log in, log off works
-Messages work and disappear by themselves after specified time (6 seconds-6000)
-FootNotes give detail on who posted them and when they were posted
-Facebook/Tiktok/Instgram at bottom
-NAV bar effectively allows user to navigate from summary page to idea page

<b>Deployment, forking, cloning </b>
PASTED IN FROM COFFEE_NOW:
## Deployment

### Github Deployment

The website was delpoyed using GitHub. To do this I did the following;

1. When on the websites GitHub repository, click on the settings tab
2. Now on the settings page, on the left hand side of the page, click on the pages tab
3. Under the Source section, click on the drop down menu titled Branch and select main
4. The page is now published with a link available to use.

(<https://github.com/Kieran132/Coffee_Now>)

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

- When you have reached the dashboard for Heroku.com, click New and then select 'Create New App' from the drop-down menu.
- On the next page, onput you app anme, select your appropriate region and proceed to create app
- Navigate to the settings tab and scroll to  the 'Reveal Config Vars' section. When there, add the key of 'Port' and the value of '8000'. 
- Below this click Add buildpack and choose python and nodejs in that order. The importance of retaining this order is due to...

#### Deployment of the app

- Navigate to  the 'Deploy' tab and select Github-Connect to Github-this will enable automatic deployment.
- Retrieve your respoitary by name, using the search function available.
- Connect to your chosen repo.
- If you elect to choose automatic deployment (as opposed to the manual deployment which is a once off deployment where in the process will need to be reperformed manually on each deployment) the app will automatically redeploy when you commit on Github.
- Following deployment, you should now be able to access your deployed live project.


<b>Steps</b>
<b>On Github:</b>
Disable debug...get rid of traceback which my compromise your site
Install X-Frame Options=Same Origin...CORS cross origina resource sharing security feature
Tells system resources are permitted to be loaded

<b>On Heroku</b>
Go to settings-Reveal Config Vars

Remove DISABLE_COLLECTSTATIC config variable

Deploy tab, scroll to end, deploy branch

View build log to ensure all working okay

As per future features listed - still room for a lot of development

Django...not everything needs to be in one app
All app logic doesn't need to be in views.py file

<b>References</b>

https://pixabay.com/photos/pocket-watch-time-sand-clock-3156771/
A number of free open sources used for photos that appear as featured images on idea cards on the summary page. They are uploaded to admin interface when original idea is posted. If no image provided then there is code that defaults to a different image via url in code.
All Code Institute tutorials-particularly the blog walkthrough
Stack comments and contributions, as well as various sample repositaries provided on slack.

Footprint: https://codepen.io/bogers/pen/MWJjwJa?editors=1111

Credits

Stack community
Particulary the peer code review page
Drew inspiration from the following projects:
Roman:
Coffee now: Kieran 123
Fitness Booking

Django documentation and W3 school

Tutor Support
Ensured to availa of the ninety minutes of weekly tutor support available to me when I had various queries/coding issues.
Mentor-Mitko
Had my three meetings for submissions and greatly assisted me with two additional meetings for resubmission, targetting the areas highlighted in the assessor feedback (CRUD functionality, agile methodology and testing)

When implementing the additional CRUD functionality for resubmission, I found the following tutorial and code that the Code Institute made available with regard to the Blog walkthrough very useful: https://www.youtube.com/watch?v=YH--VobIA8c
Hvaing considered the updated features included with this tutorial, I included the additional option of the logged in user being able to edit and delete the footnote that they leave (in faded format) prior to being approved by the admin.

Also noted issues with Cloudinary were mentioned wherein the heroku deployed app became out of sync with Cludinary and accordingly whitenoise installation was presented as an option.

In idea_detail.html template:
Edit and delete buttons on footnote
Javascript
Little bit - in static folder of relevant app

comments.js file in static folder

footnotes.js...

variable defintiions
getting elements by class name (walking through the DOM)
getting element by id
getting element by tagname

variables...getting a collection of HTML objects back
because we might have multiple footnotes (comments) placed that we want edit and delete buttons to appear on
so must be done for each button
for each button, an EventListener is added -saw this in Jest content with Simon Says type game

how does the js interact with the HTML template
via ia footnote.id (comment id) is in js and also stored as an attribute in the button in the HTML template
In JS= comment_id/ footnote_id
In HTML= comment_id = {{ comment.id }}/ footnote_id={{ footnote.id }}

so we know which comment we will be acting on when we edit/delete

change the href of delete/confirm button

standard Bootstrap modal also included as delete modal - defensive programming (user must doubly confirm they want to delete comment/footnote)

a standard GET request through the view

at bottom a collection of edit buttons
when we click on edit button

we get comment id
getting text of comment innerText
putting into tesxt area and changing submit button, instead of submit, update

using javascript to improve the FrontEnd experience

Separateion of concerns-commentart on django-used to be a newspaper
dirrect app
different files for test
javascript as a tool to improve the front end-kept separate

Views.py: (functions)

views for delete

def footnote_delete(request, clug, comment_id, *args, **kwargs)

filter for comment with comment_id
when doing a 
'.first()' at end, to avoid it being returned as queryset object as opposed to an individual record
brings it out as a record, not a queryset object
 'You can only delete your own comments...consider adding this to the idea delete also' 





and then for loop
purpose of for loop


automated testing:

Lighthouse-sufficient
if you want to take it furhter, buidl some Django unit tests, have been included to take a look at

most simple test

About

Tests happen in a test view class

files must begin with tests
can be called anything but must inherit from TestCase ()

from django.test import TestCase (automatic)

class TestView(TestCase):
  response = self.client.get(reverse('about')) //get about page
  self.assertEqual(response.status_code, 200) //do I get status code of 200
  self.assetTemplateUsed(response, 'about.html') //was template about.html

testing to see if a page is accessible to us...if it returns status code 200-server confirming request is okay

testing forms and login-more complex

similar to hello Django test

testing forms

class TestFootNoteForm(TestCase):
      def test_body_is_required(self): //
        form = FootNoteForm({'body':''})
        self.assertFalse(form.is_valid()) //
        self.assertIn('body' in form.errors.keys()) //
        self.assertEqual(form.errors['body'][0], 'This field is required') //  

      def test_field_is_explicit_in_form_metaclass(self):
        form = FootNoteForm({'body':''})  
        self.assertEqual(form.Meta.fields, ('body,))

when write tests
in project level app, create new file called 'settings_test.py'
same as main settings file (duplicate to begin) except in Database section, sues SQLite3 instead of Postgres

reason is it is better to run tests against a non production database
and postgres requires all kinds of environment variables

copy of settings.py, database set back to SQLite

to run tests, command is:

python3 manage.py test -- settings=FOOTNOTE_APP.settings_test

screengrab results and include in README

explain results

include testing legend

tests in different apps

tests files need to start with 'test' or 'tests'

helps you when trying to understand what is going on

import form
run tests

for views testing, longer and more involved testing as User model imported, Idea model imported, 

running a set up

can do set up method

runs before other tests - creates a superuser in databse
creates an idea (post) in db
saves that idea(post)

because self.user self.idea used in set up, can also use eslewhere

first test = standard get idea list

all methods must start with word 'tests' or won't be run as tests-'tests' reserved by django

can do tear down method

get idea list
get idea detail (of idea created as part of setUp function)
test like seeing if likes equals one after liking

test footnote
log in as user created in setUp
post an idea to ideadetail with slug as argument

red light green light method-always test it faisl rather than test if it passes
because it might pass first without you knwoing it will fail

test fcuntionality...not jsut decorative tests





could test Idea form also       
    