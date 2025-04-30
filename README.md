# WordPress Auto Post Generator

A WordPress plugin that automatically generates posts with content and images using Cursor's capabilities.

## Features

- Generate WordPress posts with a single click
- Automatically create content based on the post title
- Generate and attach featured images
- Create draft posts that you can review and publish
- Simple and intuitive user interface

## Installation

### As a WordPress Plugin

1. Download the plugin files
2. Upload the `wordpress-auto-post-generator` folder to the `/wp-content/plugins/` directory
3. Activate the plugin through the 'Plugins' menu in WordPress
4. Access the plugin from the new "Auto Post Generator" menu item in the WordPress admin

### Manual Installation

If you prefer to use the standalone scripts:

1. Place `wordpress_auto_post.php` in a directory accessible to WordPress
2. Place `wordpress_auto_post_web.php` in a directory accessible to WordPress
3. Access the web interface through your browser

## Usage

### Using the WordPress Plugin

1. Log in to your WordPress admin panel
2. Navigate to "Auto Post Generator" in the admin menu
3. Enter a title for your post
4. Click "Generate Post"
5. Once the post is created, you can edit it to make any necessary changes
6. Publish the post when you're ready

### Using the Command Line

You can also generate posts from the command line:

```bash
php wordpress_auto_post.php "Your Post Title"
```

### Using the Web Interface

If you're using the standalone web interface:

1. Access the web interface through your browser
2. Enter a title for your post
3. Click "Generate Post"
4. Once the post is created, you can edit it to make any necessary changes
5. Publish the post when you're ready

## Requirements

- WordPress 5.0 or higher
- PHP 7.0 or higher
- GD library for image generation

## How It Works

1. You provide a title for your post
2. The system uses Cursor's capabilities to generate content based on the title
3. The system generates an image related to the title
4. The image is uploaded to the WordPress media library
5. A new draft post is created with the generated content and featured image
6. You can edit the post to make any necessary changes before publishing

## Customization

You can customize the plugin by modifying the following files:

- `includes/class-wordpress-auto-post.php`: Contains the main functionality
- `admin/admin-page.php`: Contains the admin page template
- `wordpress-auto-post-generator.php`: Contains the plugin initialization code

## Troubleshooting

If you encounter any issues:

1. Make sure you have the required permissions to create posts
2. Check that the GD library is installed and enabled
3. Ensure that your WordPress installation has write permissions to the uploads directory
4. Check the WordPress error log for any error messages

## License

This plugin is licensed under the GPL v2 or later.

## Credits

This plugin was created using Cursor's capabilities for content and image generation.

# WordPress API Credentials
WORDPRESS_URL=https://iamdeveloper.in/testwordpress
WORDPRESS_USERNAME=web-admin
WORDPRESS_APP_PASSWORD=code@2022!


# Note: For WORDPRESS_APP_PASSWORD, use an Application Password, not your regular WordPress password
# To create an Application Password:
# 1. Log in to your WordPress admin panel
# 2. Go to Users > Your Profile
# 3. Scroll down to the 'Application Passwords' section
# 4. Enter a name for the application (e.g., 'Cursor Auto Post')
# 5. Click 'Add New Application Password'
# 6. Copy the generated password and use it here 