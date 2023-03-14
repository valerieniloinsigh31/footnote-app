<b>FootNote App</b>

An app for creative writers who are often struck by inspiration whilst out and about.
A profile based application, like a crossover between Tinder, Facebook and MySpace but aimed at creative writers. Each creative writer has the ability to build their own profile, which they will operate as the administator and superuser of as well as interacting as a general user/feedback giver on the FootNote profile pages of other FootNote app users. The app will be comrpised of a netwokr of members who work as creative writers in some form. They will stipulate their preferences upon joining and accordingly, they will be presented with a pool of like-minded creatives with similar interests who they can apply to give feedback on their FootNot Profile as well as assess whether they will accept other FootNote members as feedback givers on their profile (once the other FootNote member has submitted an application to join them on their profile as a feedback giver)


<b>Functionalities to include:</b>

Based on the MVP documentation provided with this module/project, I concluded that I would have to have the following functionalities available in my FootNote app:
CRUD mentality
Both the user and superuser/administrator of my FootNote application, should have the ability to Create, Read, Update and Delete items.

Albeit, this is applied in different ways.

-For the administrator/Superuser who owns the FootNote profile, they will regulate what appears on their profile. They can create, read, update and delete their own original ideas (one idea at a time is the FootNote policy-to avoid oversaturation.) Also there is a maximum length of 100 words per original idea posted,to be inkeeping with the initial aim of the applicaiton, to post a fast idea that occurs to the profile owner whilst out and about in order to get immediate feedback (as opposed to exposing intiacte/vital parts of their original creative ideas.)
-The admin/Superuser can view the results of the poll (green votes/red votes) in response to their original idea. They won't be able to view who voted green/red on their idea.
-The admin/Superuser will be able to view FootNotes posted by the feedback givers/users who voted green on their idea. 
-The admin/Superuser cannot delete individual FootNotes, but they can store individual FootNotes. The CASCADE/delete effect will apply to their original idea. If they delete the idea, all of the FootNotes associated with that idea will delete also. 
-The admin/SuperUser cannot edit FootNotes or edit their original idea after the voting poll has opened.
-The admin/Superuser can delete their original idea (and as a result, all of the footnotes posted to it will delete with the CASCADE effect)
-The admin/Superuser can store selected FootNotes to their offline profile. They will be able to edit/update these FootNotes once they have been moved offline and are no longer visible on their public FootNote profile.
-The admin/Superuser can change the order of the FootNotes when storing (to reflect their order of preference potentially)


-From the user perspective, their statistics on the site will be accumulate from the moment they joined the application. The will stipulate their preferences (e.g. their favourite genre, their method of writing-e.g. poetry, novel, screenplay, song etc) and based on their specifications, suggested connections will pop up for them (similarly to the suggested followers function in instagram or the suggested friend section in facebook or the suggested connection section in LinkedIn). The can apply to become a feedback given on the profile of one of the suggested connections. Once they submit to become a feedback giver, the owner/admin/Superuser of the profile that they have applied to will assess whether or not to accept them as a feedback giver on their profile. This assessment will be made by the historical statistics of the applicants engagement-to-date on the FootNote App becoming readily visible to the profile owner. Metrics that will be exposed with the applicants statistics are when they joined the app, how many original ideas of their own have they posted, how many votes have they submitted to other peoples FootNote Profiles, what ratio green/red votes did they submit for other ideas, how many FootNotes did they leave what % of green votes did they leave FootNotes for (the user can only leave a footnote if they vote green). This will help the profile owner to make an informed decision about whether or not to accept them as a feedback giver on their profile. 

 Once accepted as a feedback giver on the profile, the user then can perform a variety of CRUD functionalities:
 -They can read the latest original idea posted by the profile owner
 -They can vote in a poll on original ideas posted by the profile owner (a green vote means that they believe that the profile owner should pursue the original idea that they have posted further, a red vote means that they believe the profile owner should not pursue the original idea that have have posted further). 
 -If the user votes green in order of pursuing the original idea posted, they will be given the option to leave a FootNote, with a maximum length of forty words (to support the FootNote aim of providing concise helpful nods in the right direction as opposed to giving away intellectual property). 
 -They can update or delete their FootNote at any point they want to (this will also be reflected in the statistics on their own profile). They can do this up until the point that they profile owner deletes the original idea (the FootNotes will disappear along with the original idea due to the CASCADE effect applied)
 -They will be able to click like or unlike on FootNotes posted by other users

Fomr what perspective can members use the app?: I intend to apply this from both a user perspective and a supersuer perspective.

The app from the perspective of the superuser who is also the administrator and, as such, a regulator of the site will be able to log in and regulate the front end view of their profile. They will operate as an administator and readily be able to control what views and posts appear on their page. it is via the administation also that the superuser will be able to decide whether they store FootNotes to their original idea in their private (hidden profile) so that they have they available when pursuing their idea at a later stage.

<b>What is it?:</b>
 The FootNote app is an app connecting creative people. It connects creative people whose art form is original writing of some sort, who want to share their original ideas and to get instant feedback from similarly minded people in useful footnote format, with a maximum amount of characters so that the contribution provided by other app users is a helpful nod as opposed to providing an idea to plagiarise. The emphasis on transparency, with the statistics of members becoming visible to the owners of profiles that they apply to give feedback on is in place to ensure that nobody abuses the app or tries to use it as a method of stealing the original thoughts of others/to offer unconstructive negative feedback.

 Similarly to the preferences section of Tinder, upon joining the app, the FootNote member is presented with several questions, encouraging them to stipulate their area of interest, the genres they are interested in and writers they are similar to/inspired by and their form of writing (novel/songwriter/screenwriter/poet). Based on the preferences that they list, they will unlock a pool of other profiles that they can apply to be feedback givers on. The owners of the profiles they apply to be feedback givers to, will be able to see their site statistics (how much interaction they have had on the FootNote application (e.g. what ratio of green/red votes on other people's original ideas they have had, how many FootNotes they have posted as feedback to other people's profiles, how many original ideas have they posted to their own profile, when did they join the site etc.) The owner of the profile, who decides whether or not to accept the applicant as a feedback-giver on their own profile will be able to make an informed decision about whether to accept them or not based on their statistics. (e.g. if a profile owners sees that the member who has applied to be a feedback giver on their page, joined three years ago and has yet to post their own original thought and has voted 100% red on other people's original ideas without providing any Footnotes, the profile owner may not be inclined to accept them to their profile as the impression created is that they are there to steal ideas, to offer exclusively negative feedback and not to contribute anything themselves).

Everyone who joins the FootNote app has the choice of having their own FootNote profile, where they post their ideas and are susceptible to criticism/feedback by the other FootNote app members who they have accepted as feedback givers on their profile. Additionally, they will be capable of applying to be a feedback given on the profiles or other writers who they match with. They will need to be accepted as a feedback giver before they can see the ideas, vote the idea green/red and give feedback on the profiles of other FootNote members.

<b>DESIGN:</b>

Having used both Balsamiq and Lucidcharts for design at planning phase for apps in the past, I decided that Lucidcharts would be suitable for this project as the shapes and visual aspect to it would be able to convey my stream of thoughts but also to help me to priorise each step/task as I was completing it.

Agile methodology-apply the ROMDAS prioritisation...

The blog walkthrough and Kanban board feature assisted me in thinking about what features I would include in project four and how to go about implementing these/dividing these into sections that I could apply and what t to prioritise...

Inspired by the walkthrough projects (Djanjo to do app and blog), I planned on having the design for the model classes neatly planend and laid out in tabular format in a Lucidchart format, which would help me to formulae the idea in my own head when designing the code for the app:

Model-View-Template

<b>Class Models</b>
Class models defined and additional definitions included within those models.
Profile model (how is this done-form a profile, view other profiles, statistics and levels of engagement)

Two models derived closely from blog project but customised accordingly and tailored code to suit my project

Additional model for superuser to store the footnote - If the superuser takes a liking to particular footnotes, these footnotes can be stored on their offline profile before being deleted from their footnote profile.
The cascade delete effect is in place so once idea is deleted, all accompanying footnotes will be deleted as well.
Additional model for 'connect with my profile'
Additional model for like/dislike the idea
Additional model 'Make this my favourite idea'...function of the FootNote website, users can favourite one idea per per day but once favourited cannot change until 24 hours is up

Authentication-only those who like the original idea would be able to leave a footnote-this was for website moderation purposes-the focus of the website is to focus on providing small nuggets of inspiration, a nod in the right direction.

If the feedback giver votes dislike, discouraging the idea posted then they cannot leave a footnote.

Max length 280 characters for both idea and footnotes as the focus of the website is on giving helpful nuggets on fast-occuring ideas as opposed to crossing the territory into elaborate collaboration/plagiarism.

Only one idea per page, administator encouraged to delete the one idea before posting another.

Idea model
FootNote Model

Users can vote like/dislike on idea
If they vote like only then will they be given the authentication to post a footnote
Store model (offline profile)

Lucidcharts

Luidcharts and it's shapes etc would assist me in designing how I wanted the app to look.

<b>Views:</b>

Views-what views...

User interaction
One to many relationship?
Or many to many relationship?

Functions to break down...

One to many-the profile owner operates as the superuser or administrator of their own profile. Only they can post/edit their own original idea on their own FootNote profile. Accordingly, this is a one to many relationship.

The users or feedback givers who are viewing the original ideas of the profile owner, who are voting like/dislike on the profile owners original ideas, who are posting FootNotes in response to the ideas (which have a maximum character/word restriction but can be deleted or edited by the user until the footnote is stored/removed by the profile owner) and who can like or dislike the footnotes of other users is a many to many relationship as they can interact on the profile but also they can receive interactions by others (such as somebody liking/disliking their footnote)

Views...
The views included are:

Models...
The models included are...


Django format is the model, view, template

Directories and frameworks used-Cloudinary, Materialize, Summernote

Design....CSS (starter template used from blog project but how has this been adapted further)...hover..what frameworks have been connected that are aiding in bringing this app to fruition

Visibility


<b>Things to consider when compiling project</b>
-Order
-Frameworks to be installed (Django, Summernote)
-MVP
-Refactoring/inheritance
-Test based coding (what tests were used)
Manual testing...testing for responsiveness...testing programmes
-Design based coding

Was bootstrap used?
Yes-how did bootstrap assist...
We used bootstrap for alert messages
Format we wrote bootstrap in...
What effect did this have on the project?

Object orientated design...defining classes


Testing-what tests were used
Test for HTML:
Test for Javascript:
Test for Python:


Languages-what languages were used

Deployment:

Early deployment as per the walkthroughs to avoid last minute panic.
Before writing the code, set up an instance on ElephantSQL and then created the app on Heroku. Used the API from ELlephant SQL to build Heroku APP. Connected Heroku with Github CLI for automatic deployment.

  Help to avoid last minute disasters.


<Challenges with deployment>
Surely enough, I had some difficulties, migration wouldn't work on my first attempt so I had to redo the entire applicaiton (repositary-Elephant SQL-Heroku app-migrate)

In the end, I believe migration would not work due to mixing up the use of app name versus project name in some of the code soi ensured to be very careful with this going forward.


<b>UX DESIGN</b>

Focus on idea
Sharp
Scribe...creation
Fast-moving
Transient
Footsteps
Creation in motion
What font was selected
Design-focused on smaller devices...phones/ipads/tablets/laptops while on the move-empahsis on responsiveness


Background...

Animated background
Focus not on reading long pieces of narrative so background does not be to be dull
Vibrant colour
Animation and graphics
Hover effect for likes and dislikes


<b>FEATURES</b>

-Admin interface (moderation of site-deleting idea)
-Post idea-all users can see
-Vote pursue or don't pursue idea/chase or don't chase idea
(will this be in poll format, button format or what?)
-If vote pursue idea, can leave a footnote...Footnotes are max length 280 characters-
to give one sentence construcitve criticism on idea. Each user can post as many footnotes as they want. They cannot delete their footnote, only the superuser/profile owner can do that. They cannot
-Superuser posts an idea. Max length 280 words, a quick idea that occurs to them while out and about. Once posted and polls have opened, they cannot edit the idea any more as this would create a false reflection on what had been voted for if others users had already voted. Superuser can only delete idea and when deleted all associated footnotes will delete with that idea.
-Users can like or dislike other footnotes as they please. They cannot comment on other footnotes. Footnotes have a max length and users can only post one footnote per idea to avoid oversaturation.
-Navigation bar. Login. Register. Idea of the day. Author bio.
-Tooltips
-Modal messages

<b>TECHNOLOGIES USED</b>
-Summernote
-Django
-Javascript
-Python
-HTML
-CSS
-Different websites for graphics

<b>Manual Testing Write-Up</b>

<b>Responsiveness testing:</b>
Flexbox...overscroll...bootstrap

<b>Compatibility testing</b>

...Developer tools, screengrabs of different devices

<b>Bugs resolved and unresolved</b>

...mark as we go

<b>Lighthouse testing outcomes</b>

...screengrab

<b>Code validation</b>
HTML: [W3 Markup Validation] https://validator.w3.org
Javascript: JS Lint...
CSS: [W3 Jigsaw] https://jigsaw.w3.org/css-validator
lighthouse: https://developers.google.com/web/tools/lighthouse
Python: PEP8

<b>User stories testing</b>
Kanban board
Code along with blog


<b>Features testing</b>

<b>Deployment, forking, cloning </b>

<b>References</b>