from wordpress_auto_post import WordPressAutoPost
import sys


def main():
    # Get title from command line argument or prompt
    if len(sys.argv) > 1:
        title = sys.argv[1]
    else:
        title = input("Enter the title for your WordPress post: ")

    # Check if title is empty
    if not title.strip():
        print("Error: Title cannot be empty")
        sys.exit(1)

    try:
        # Create WordPressAutoPost instance
        auto_post = WordPressAutoPost()
        
        # Generate post
        print(f"Generating post with title: {title}")
        result = auto_post.generate_post(title)
        
        # Print result
        if result['success']:
            print("\nSuccess!")
            print(f"Post created with ID: {result['post_id']}")
            print(f"Message: {result['message']}")
        else:
            print("\nError:")
            print(f"Failed to create post: {result['error']}")
            sys.exit(1)
            
    except Exception as e:
        print(f"\nError: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 