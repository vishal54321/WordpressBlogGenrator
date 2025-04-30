import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from wordpress_auto_post import WordPressAutoPost
import threading

class WordPressPostGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("WordPress Auto Post Generator")
        self.root.geometry("800x600")
        self.root.minsize(600, 400)
        
        # Configure grid weights
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        main_frame.grid_rowconfigure(4, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        
        # Title section
        title_frame = ttk.LabelFrame(main_frame, text="Post Title", padding="10")
        title_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        title_frame.grid_columnconfigure(0, weight=1)
        
        self.title_entry = ttk.Entry(title_frame, width=50)
        self.title_entry.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=5)
        
        # Buttons frame
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=5)
        
        self.generate_button = ttk.Button(buttons_frame, text="Generate Post", command=self.generate_post)
        self.generate_button.pack(side=tk.LEFT, padx=5)
        
        self.preview_button = ttk.Button(buttons_frame, text="Preview Content", command=self.preview_content)
        self.preview_button.pack(side=tk.LEFT, padx=5)
        
        # Status section
        status_frame = ttk.Frame(main_frame)
        status_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=5)
        
        self.status_label = ttk.Label(status_frame, text="")
        self.status_label.pack(side=tk.LEFT)
        
        self.progress = ttk.Progressbar(status_frame, length=200, mode='indeterminate')
        self.progress.pack(side=tk.RIGHT, padx=5)
        
        # Content section
        content_frame = ttk.LabelFrame(main_frame, text="Generated Content", padding="10")
        content_frame.grid(row=3, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_columnconfigure(0, weight=1)
        
        self.result_text = scrolledtext.ScrolledText(content_frame, wrap=tk.WORD)
        self.result_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
    def generate_post(self):
        title = self.title_entry.get().strip()
        if not title:
            self.status_label.config(text="Error: Title cannot be empty")
            return
            
        # Disable buttons and start progress bar
        self.generate_button.config(state='disabled')
        self.preview_button.config(state='disabled')
        self.progress.start()
        self.status_label.config(text="Generating post...")
        self.result_text.delete(1.0, tk.END)
        
        # Start generation in a separate thread
        thread = threading.Thread(target=self._generate_post_thread, args=(title,))
        thread.daemon = True
        thread.start()
        
    def preview_content(self):
        title = self.title_entry.get().strip()
        if not title:
            self.status_label.config(text="Error: Title cannot be empty")
            return
            
        # Disable buttons and start progress bar
        self.generate_button.config(state='disabled')
        self.preview_button.config(state='disabled')
        self.progress.start()
        self.status_label.config(text="Generating preview...")
        self.result_text.delete(1.0, tk.END)
        
        # Start preview in a separate thread
        thread = threading.Thread(target=self._preview_content_thread, args=(title,))
        thread.daemon = True
        thread.start()
        
    def _generate_post_thread(self, title):
        try:
            auto_post = WordPressAutoPost()
            result = auto_post.generate_post(title)
            self.root.after(0, self._update_ui, result)
        except Exception as e:
            self.root.after(0, self._update_ui, {'success': False, 'error': str(e)})
            
    def _preview_content_thread(self, title):
        try:
            auto_post = WordPressAutoPost()
            content = auto_post.generate_content(title)
            self.root.after(0, self._update_preview, content)
        except Exception as e:
            self.root.after(0, self._update_ui, {'success': False, 'error': str(e)})
            
    def _update_ui(self, result):
        # Stop progress bar and re-enable buttons
        self.progress.stop()
        self.generate_button.config(state='normal')
        self.preview_button.config(state='normal')
        
        if result['success']:
            self.status_label.config(text="Success!")
            self.result_text.insert(tk.END, f"Post created with ID: {result['post_id']}\n")
            self.result_text.insert(tk.END, f"Message: {result['message']}")
        else:
            self.status_label.config(text="Error")
            self.result_text.insert(tk.END, f"Failed to create post: {result['error']}")
            
    def _update_preview(self, content):
        # Stop progress bar and re-enable buttons
        self.progress.stop()
        self.generate_button.config(state='normal')
        self.preview_button.config(state='normal')
        
        self.status_label.config(text="Preview Generated")
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, content)

def main():
    root = tk.Tk()
    app = WordPressPostGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 