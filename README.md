<h1>NEEWO: Fashion and Beauty News Portal</h1>


![Mockup](readme-images/Mockup.png)


<h3>Overview</h3>

[NEEWO](https://neewo-a26db386d628.herokuapp.com/), your go-to source for the latest fashion and beauty news. Get the scoop on runway trends, celebrity styles, makeup tips, and skincare advice. Discover in-depth articles, exclusive interviews, and expert insights in the world of fashion and cosmetics.
<br>
<h3>Project Description</h3>
NEEWO is a Django-based web application designed to provide users with up-to-date fashion and beauty news. The platform offers various features for both administrators and regular users to enhance their experience.


<br>
<h2>USER EXPERIENCE</h2>

<h3>Admin Features</h3>

 1.  Post News: Admins can create and publish new articles about fashion and beauty trends.<br>
 
 ![admin_page](readme-images/admin_page.png)
 
 2.  Edit News: Admins can edit existing news articles.<br>
 
 ![edit](readme-images/edit_post_page.png)
 
 3.  Delete News: Admins can delete news articles that are no longer relevant or appropriate.<br>
 
 ![delete](readme-images/delete_post_page.png)
 
 4.  View Likes: Admins can view the number of likes on each news article.<br>
 5.  Comment Management: Admins can view, approve, or delete comments made by users.<br>
 6.  News List Management: Admins can view a list of all news articles.<br>
 7.  Account Registration: Admins can manage user registrations and accounts.<br>
 8.  News Categories: Admins can create and manage different categories for news articles.<br>
 9.  Site Pagination: Admins can configure pagination settings for the site.<br>
 10. View Comments: Admins can see all comments on articles.<br>
 11. Number of Likes: Admins can view the total number of likes for each article.<br>

<h3>User Features</h3>

 1. View News List: Users can browse through a list of all published news articles.<br>
 2. Comment: Users can comment on news articles.<br>

 ![comment](readme-images/comment_user_loggedin.png)
 
 3. Like: Users can like news articles.<br>
<br>
<h2>FEATURES</h2>

<h3>Navigation</h3>
The navigation feature of the NEEWO fashion and beauty news website is designed to provide a seamless and intuitive user experience.<br><br>


![nav](readme-images/nav-bar.png)

<h4>Navbar Admin</h4>

![nav](readme-images/nav-bar_admin.png)

<h4>Responsive Navbar Guest </h4>

![nav](readme-images/responsive_nav-bar.png)

<h4>Responsive Navbar User </h4>

![nav](readme-images/responsive_nav-bar_user.png)

<h3>Homepage</h3>
The homepage of NEEWO showcases a dynamic news list, displaying the latest articles along with their associated images. Each news item includes a link to the detailed article page and indicates the category of the post. This structured layout ensures that users can quickly access the most recent and relevant fashion and beauty news.<br><br>

![homepage](readme-images/homepage.png)


<h3>Article Detail Page</h3>
Each news article page includes:<br>

 * Title and Author: The title of the article and the author's name.<br>
 * Publication Date: When the article was published.<br>
 * Content: The main body of the article with images, videos, and text.<br>
 * Comments Section:
     * If the user is logged in, they can leave a comment in the designated comment section.<br>
     * If the user is not logged in, they will only see the list of existing comments but won't have the option to comment.<br>


![detail](readme-images/news_detail_page.png)

<h3>Sign Up and Login Pages</h3>

 * Sign Up Page: New users can create an account by providing necessary details such as username, email, and password.<br>
 * Login Page: Existing users can log in to access more features by entering their username and password.<br>
 * Welcome Message: Once logged in, users are greeted with a personalized welcome message like "Welcome, Admin" or "Welcome, User."<br>

![signup](readme-images/signup_page.png)

![login](readme-images/signin_page.png)

<h3>Footer</h3>

The footer of the website includes social media links, allowing users to connect with NEEWO on various platforms:<br>
 * GitHub<br>
 * LinkedIn<br>
 * Instagram<br>
 
![login](readme-images/footer.png)

<h3>Admin Dashboard</h3>
The admin dashboard provides easy access to all administrative features:<br>

 * Post New Article: A form for creating and publishing new articles.<br>
 * Edit Article: A form for editing existing articles.<br>
 * Delete Article: An option to delete articles.<br>
 * Manage Comments: A section for approving, editing, or deleting user comments.<br>
 * View News List: A list of all articles with options to edit or delete them.<br>
 * User Management: Tools for managing user accounts and registrations.<br>
 * Category Management: Options for creating and managing article categories.<br>
 * Settings: Configure site settings such as pagination and view statistics on likes and comments.<br>
<br>

<h2>WIREFRAMES</h2>
I've designed wireframes to layout the structure of your fashion and beauty news website, focusing on a clean, user-friendly, and responsive design. 

<h3>Homepage</h3>

![homepage](readme-images/wireframe_homepage.png)

<h3>News Detail Page</h3>

![detiail](readme-images/wireframe_newsdetail.png)

<h3>Sign In Page</h3>

![login](readme-images/wireframe_signin.png)

<h3>Sign Up Page</h3>

![singup](readme-images/wireframe_signup.png)


<h2>DESIGN & COLORS</h2>
The design of NEEWO is sleek and modern, using the following color scheme:

 * #000000 (Black): Used for text and other primary elements.<br>
 * #a74ebf (Purple): Used for highlights, buttons, and other important accents.<br>
 * #ffffff (White): Used for backgrounds and text.<br>

<h3>Image Styling</h3>
All images on the site are displayed with a grayscale filter to create a chic and timeless aesthetic. <br>The CSS for this is:

![filter](readme-images/css_filter.png)

![filter](readme-images/image_with_filter.png) ![filter](readme-images/image_withput_filter.png)

<br><br>
<h2>TESTING</h2>
<h3>CI Python Linter</h3>

<h4>settings.py</h4>

![filter](readme-images/settings_py.png)

<h4>views.py</h4>

![filter](readme-images/views_py.png)

<h4>views.py</h4>

![filter](readme-images/views_py.png)

<h4>models.py</h4>

![filter](readme-images/models_py.png)

<h4>forms.py</h4>

![filter](readme-images/forms_py.png)

<h4>forms.py</h4>

![filter](readme-images/forms_py.png)

<h4>admin.py</h4>

![filter](readme-images/admin_py.png)

<h4>urls.py</h4>

![filter](readme-images/urls_py.png)

<h4>app/urls.py</h4>

![filter](readme-images/app_urls_py.png)

<h3>HTML Validation</h3>

![filter](readme-images/html_checker.png)

<h3>CSS Validation</h3>

![filter](readme-images/css_validation.png)

<h2>DEPLOYMENT</h2>

The project is deployed on Heroku. Ensure that all necessary environment variables and configurations are set up in the Heroku dashboard, including the database settings and static file handling.<br>
<h2>FUTURE FEATURES</h2>

 1. Newsletter: A feature to allow users to subscribe to a newsletter for regular updates.<br>
 2. Filter and Search for Categories: Advanced filtering and search options to find articles based on categories.<br>
 3. Contact Form: A contact form for users to reach out to the site administrators.<br>
 4. Subscribe Button: A button for users to subscribe to specific news categories or authors.<br>
 5. Share Button: Social media share buttons to share articles directly from the site.<br>
 6. Save for Later: A feature for users to save articles to read later.<br>
 7. Follow Other Users: Allowing users to follow other users to see their liked and commented articles.<br>
<br>
<h2>CONCLUSION</h2>

NEEWO provides a comprehensive platform for users to stay updated with the latest in fashion and beauty. With robust features for both administrators and regular users, the site ensures a seamless and engaging experience for everyone. The clean design, intuitive navigation, and efficient user management make it a reliable source for fashion and beauty news.
