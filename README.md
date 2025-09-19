# Static Site Generator

Converts Markdown to a static HTML site

---

## 🚀 Features

- Make your website with markdown
- Host it for free with GitHub Pages
- Easy setup and extensibility

---

## 📦 Installation & Setup


1. **Clone the repository:**
    ```bash
    git clone https://github.com/andynesse/static_site_generator.git
    cd static_site_generator
    ```

2. **Create your own content:**
    Create markdown files in the `/content` directory or edit the example files.

    Also add your images and edit the styling in the `/static` directory.

3. **Build the HTML site from the shell:**
    ```bash
    ./build.sh
    ```

4. **Host the site on GitHub:**
    - Navigate to your repository and click the **"Settings"** tab. 
    - Then scroll down to the **"Pages"** section from the left section.
    - Under **"Build and deployment"** set the branch to **"main"** and folder to **"/docs"** and click save
    - Visit the site by clicking the **"Visit site"** button on the top of the settings page or by entering `https://<github_username>.github.io/static_site_generator/` in the browser.

> ⚠️ 
> The github repository has to be public to host the site directly with GitHub pages.
---