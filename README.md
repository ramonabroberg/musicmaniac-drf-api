# musicManiac API

MusicManiac is a website made for musicians that easily wants to get in touch with other musicians. On this website you can view posts that users upload and if you create an account you can even make posts yourself! Do you play an instrument and are searching for a band or do you and your bandmates looking for the missing piece in your band? At musicManiac you can easily search for specific posts so you can find what you're looking for in a matter of seconds!

### [You can see the website live here](https://musicmaniac-drf-api-961711dd9bd4.herokuapp.com/)

# User Stories

- As an admin I can create, edit, and delete users, profiles, posts, insterests and comments so that I have control over the website.

# Models

- User: id, username..
- Profile: owner, image, name, description, created_at.
- Post: owner, title, instrument, genre, city, website, description, updated_at, creaeted_at.
- Interested: owner, post, created_at.
- Comment: owner, post, content, created_at, updated_at.

## Left to implement:

- Message
    - Sender, receiver, content, sent_at.

# Testing

### General

- The user has to enter correct username and password to be able to log in.
- The user get information about what it has to change to be able to log in if it's not correct.
- Both username and password are mandatory.
- The user can log out without problem.
- As a logged out user you can:
    - View posts.
    - View profiles.
    - See how many likes and comments a post has.
    - Read comments.
- As a logged in user you can also:
    - Upload posts.
    - Edit posts.
    - Delete posts.
    - Like posts.
    - Comment on posts.
- It's possible to create, edit and delete as admin.
- It's not possible for users to like their own posts.
- Users can search on posts by title, username, intrument, genre and description.

# Deployment

The site was deployed using the following steps:

1. Change "DEBUG = True" to "DEBUG = 'DEV' in os.environ" in the settings.py file.
2. Push to GitHub.
3. Create database at ElephantSQL.com.
4. Log in on Heroku and click on the app.
5. Click on the "Settings" tab and then on "Reveal Config Vars".
6. Add the database url.
7. Update the settings.py file on the project.
8. Push again.
9. Add secret key and cloudinary url to Config Vars.
10. Now click on the tab "Deploy" and then on the button "Deploy Branch" at the bottom of the page.
11. When it's deployed, you can click on "Open App" and see it live.

# Credits

- I have had Code Institute's walkthrough project as inspiration and as a base.
- I have used:
    - Django
    - Djangorestframework
    - Cloudinary
    - Pillow

- This website is powered by Django, a high-level Python web framework.
- Images on this website are hosted and managed by Cloudinary.
- Rest Framework
- Axios
- GitHub
- Heroku
