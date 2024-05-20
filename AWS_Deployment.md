# Flask Application Deployment

This README provides instructions for deploying the Flask application on an EC2 instance, storing images on an S3 bucket, and setting the necessary access rules.

## Prerequisites

- AWS account with necessary permissions
- AWS CLI configured with your credentials
- Docker and Docker Compose installed on your local machine

## Step 1: Setting Up EC2 Instance

1. Open an EC2 instance based on Amazon Linux 2 - with Inbound Security Group Rule of custom TCP on port 5001.
2. Connect to your EC2 instance via SSH.

### Install Docker, Docker Compose, and Git

Run the following commands on your EC2 instance:

```sh
# Update the package index
sudo yum update -y

# Install Docker
sudo amazon-linux-extras install docker -y

# Start and enable Docker service
sudo service docker start
sudo systemctl enable docker

# Add your user to the docker group
sudo usermod -a -G docker ec2-user
docker --version
```
After exiting, reconnect to your EC2 instance for the group changes to take effect.

```sh
# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Verify installation
docker-compose --version

# Install Git
sudo yum install git -y
```

## Clone the Repository and Run the Application

```sh
# Clone your repository
git clone https://github.com/keinar/FlaskLoginApp.git

# Navigate to the project directory
cd FlaskLoginApp

# Build and run the application using Docker Compose
docker-compose up --build

```

## Step 2: Setting Up S3 Bucket
1. Open the AWS Management Console and navigate to S3.
2. Create a new bucket (e.g., test-keinar).
## Upload the Image
1. Click on your newly created bucket.
2. upload your image file (e.g., me.png).
## Configure Bucket Policy
To make the image publicly accessible, you need to set the appropriate bucket policy. Go to the Permissions tab of your bucket and add the following bucket policy:

```sh
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::test-keinar/*"
    }
  ]
}

```

This policy allows public read access to all objects in your bucket.

## Step 3: Running the Application
After setting up the environment variables, navigate to the project directory and run the application:

```sh
docker-compose up --build
```

Your Flask application should now be running, and you can access it through the EC2 instance's public IP address.

## Step 5: Accessing the Image
The /image route in your Flask application fetches the image from the S3 bucket. Ensure the image exists in the bucket and is named correctly as specified in your application.
