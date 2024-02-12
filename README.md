# Project Name README

## Introduction

Welcome to the RecipeHub project repository! This README provides guidelines on how to format code and the necessary steps to follow before pushing changes to the remote repository.

## Code Formatting

To maintain consistency and readability across the codebase, we follow a code formatting standard. We use **Eslint**, **Prettier**, **djlint** and **black** for code formatting.

## Steps for Code Formatting

1. **Install Necessary Tools**: Ensure you have **node** installed on your local development environment. Run the following commands to install the tools

   ###### *1. to install eslint and prettier*
    ```bash
    npm install
    ```
   ###### *2. to install black and djlint*
    ```bash
    pip install -r requirements.txt
    ```

2. **Format Code**: Use the following command to format your code before committing changes:
    ###### *1. to format python code*

    ```bash
    black .
    ```
   ###### *2. to format html*
    ```bash
    djlint ./template --check
    ```

    ```bash
    djlint ./template --reformat
    ```
    ###### *3. to format css and js*
    ```bash
    npm run format:all
    ```

## Before Pushing Changes

Before pushing your changes to the remote repository, follow these steps:

1. **Format Code**: Ensure that your code is formatted by running the formatting command mentioned above.

2. **Review Changes 📃**: Review your changes locally to ensure that they align with project standards and requirements.

3. **Run Tests 🧪**: If applicable, run any tests associated with your changes to ensure that they pass successfully.

4. **Commit Changes**: Once you're satisfied with your changes, commit them with a descriptive commit message.

5. **Push Changes 🚀**: Finally, push your committed changes to the remote repository.

## Additional Notes

- It's essential to format your code before committing to maintain consistency and make code reviews easier.
- If you encounter any issues or have questions about the code formatting process, feel free to reach out to maintainer.
