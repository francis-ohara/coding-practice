# 01-tailwind-practice
This is my very first Tailwind CSS project and serves as an introduction to [Tailwind CSS](https://tailwindcss.com/).

## Prerequisites
- **Node.js**: Ensure you have Node.js installed. You can verify this by running:
  ```sh
  node -v
  ```

## Installation
1. Install the dependencies:
   ```sh
   npm install
   ```

## Usage
To start the Tailwind CSS CLI in watch mode, run the following command:

```sh
npx @tailwindcss/cli -i ./src/input.css -o ./src/output.css --watch
```

This command will watch for changes in your `src/input.css` and `index.html` files and automatically rebuild the `src/output.css` file.

## Project Structure
- **index.html**: The main HTML file serving the application.
- **src/input.css**: The source CSS file where you add Tailwind directives and custom styles.
- **src/output.css**: The generated CSS file containing the compiled styles.
- **package.json**: Contains project metadata and dependencies.
