README for EC2 Instance Management with AWS Lambda
Project Overview
This project provides an AWS Lambda function to automate the stopping of EC2 instances in a development environment to save costs. The Lambda function is designed to:

Stop all running EC2 instances in a specified environment after work hours.
Use tags to ensure only development instances are stopped.
Provide an API interface via API Gateway to stop instances based on tag filters passed as query parameters.
Features
Basic Functionality: Stops all running EC2 instances.
Environment Filtering: Stops only instances with the Environment: Dev tag to avoid affecting production resources.
API Gateway Integration: Allows users to trigger the Lambda function via an HTTP request with custom tag filters, making it possible to stop specific instances based on query parameters.
Files in This Repository
stop_all_instances.py:

A basic version of the Lambda function that stops all running EC2 instances.
stop_dev_instances.py:

An advanced version of the Lambda function that stops only EC2 instances tagged with Environment: Dev.
stop_instances_with_query_params.py:

A complex version that integrates with API Gateway. It accepts key and value query parameters to stop instances with specific tags (e.g., https://api-url/?key=Environment&value=Dev).
Usage Instructions
Lambda Function Setup

Choose the version of the function you want to deploy (basic, advanced, or complex).
Copy the code from the relevant .py file and create a new AWS Lambda function in the AWS Management Console.
Set the runtime to Python 3.8 or higher.
Permissions

Ensure that the Lambda function's IAM role has the following permissions:
ec2:DescribeInstances
ec2:StopInstances
Schedule the Function (for automatic stopping)

Use Amazon CloudWatch Events to set a scheduled trigger (e.g., daily at 7 PM).
This ensures the function runs automatically after work hours to stop instances and save costs.
Using API Gateway for Dynamic Tag Filtering

For the complex version (stop_instances_with_query_params.py), set up an HTTP API in API Gateway.
Configure it to trigger the Lambda function with key and value query parameters to specify tags.
Example usage: https://your-api-id.execute-api.region.amazonaws.com/prod/?key=Environment&value=Dev

Requirements
AWS Account: This project requires access to AWS Lambda, EC2, CloudWatch Events, and API Gateway.
Python 3.8 or Higher: The Lambda function code is compatible with Python 3.8+.
IAM Permissions: Ensure your Lambda function has permissions to describe and stop EC2 instances.
Links
Medium Article: [Link to your Medium article here]
LinkedIn: [Link to your LinkedIn profile here]
Future Enhancements
Email Notifications: Send an email alert after instances are stopped.
Error Handling: Add more robust error handling for production environments.
Instance Start: Implement functionality to start instances at the beginning of the workday.
License
This project is open-source and available under the MIT License.
