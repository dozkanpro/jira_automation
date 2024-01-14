# Jira Issue Creation Automation 
Due to my job, I have to create problems in Jira every day. This is a very time consuming and boring job. I decided to write automation to shorten this work. During the tests, I take my notes into Excel, and this automation creates an issue in Jira based on data from an Excel file.

This Python script is designed to save time and effort for users who frequently need to generate Jira issues with predefined details.

## Features
- **Excel Integration**: Reads data from an Excel file to create Jira issues.
- **Customizable Fields**: Allows customization of Jira issue fields such as summary, description, project key, and issue type.
- **Error Handling**: Provides feedback on the success or failure of issue creation.

## Technology Used
- **Python**: The script is written in Python, making it easy to run and modify.
- **Requests Library**: Utilizes the `requests` library for making HTTP requests to the Jira API.
- **Openpyxl Library**: Uses the `openpyxl` library for interacting with Excel files.

## Getting Started
  - **Fork the repository:** You should **fork the repository** and then **clone it** so you can manage your own repo and use this only as a template.
    ```
    $ git clone https://github.com/your-username/jira-automation-tool.git
    ```
  - **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```
- **Set Environment Variables:** Ensure you have your own 'api_username' and 'api_password' for  Jira API credentials.
- **Place your Excel file** with the Jira issue details in the project directory.

## Usage
- Run the script using the following command:
    
   ``` python main.py ```
- The script will read the Excel file, create Jira issues, and provide feedback on the success or failure of each issue creation.

- Check the console for the generated Jira issue keys and links.

## Screenshots
 - Home Page:    
   <div align="center"><img src="e_commerce_homepage.png" alt="UI Screenshot"/></div>

 - Product Detail:    
   <div align="center"><img src="e_commerce_product_detail.png" alt="UI Screenshot"/></div>

## Contributing
   Contributions are welcome! Please fork the repository and create a pull request with your changes.
