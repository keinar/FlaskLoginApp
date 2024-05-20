# Flask Login App

This repository contains the source code for the Flask application. Below you will find the instructions for setting up the application and additional resources.

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
- [Deployment Instructions](#deployment-instructions)
- [Contributing](#contributing)
- [License](#license)


## Overview

This project is a Flask-based web application that includes user authentication, image fetching from AWS S3, and other features.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You'll need Docker and Docker Compose installed on your system to run the application. You can download them from the following links:

- Docker: [Get Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

### Installing

First, clone the repository to your local machine:

```bash
git clone https://github.com/keinar/FlaskLoginApp.git
cd FlaskLoginApp
```

Next, build the Docker image:

```bash
docker-compose build
```

Once the build is complete, you can run the application:

```bash
docker-compose up
```

The application will be available at `http://localhost:5001`.

### Environment Variables

Before running the application, you need to set the following environment variables:

- `SECRET_KEY`: A secret key for your application. This is used to keep the client-side sessions secure. Make sure this is set to a random string.

For example, you can set the `SECRET_KEY` on your system like this:

```bash
export SECRET_KEY='your-random-string-here'
```

Alternatively, you can add these to a `.env` file at the root of the project which Docker Compose will automatically pick up:

```env
SECRET_KEY=your-random-string-here
```

### Database Initialization

The database initialization is automated through the `entrypoint.sh` script. When you run the application with `docker-compose up`, the script will initialize the database with the necessary tables for the application.

## Usage

Once the application is running, you can register a new user and log in using the UI provided at the home page.

## Deployment Instructions
For detailed instructions on how to deploy this application on an EC2 instance, including setting up Docker, Docker Compose, and configuring S3, refer to the [AWS_Deployment.md](Deployment-Instructions).

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
