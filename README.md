# Hotel Reservation Prediction
A machine learning MLOps project for predicting hotel reservation outcomes, built with Python and Jupyter Notebook. Includes automated training, UI, and CI/CD pipeline.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Example Workflow](#example-workflow)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
This project aims to predict hotel reservation outcomes, such as whether a reservation will be honored or canceled, using machine learning techniques. The workflow includes data preprocessing, feature engineering, training and evaluating models, model logging, versioning, and deployment with Docker and Jenkins for CI/CD.

## Features
- **Prediction Model**: Predicts hotel booking outcomes.
- **Automated MLOps Pipeline**: Training, evaluation, logging, and versioning.
- **User Interface**: Includes a user-friendly interface for predictions.
- **Docker Integration**: Containerized for easy setup/deployment.
- **Jenkins CI/CD**: Configured for continuous integration and deployment.
- **Notebooks**: All experimentation, data cleaning, and EDA in Jupyter Notebooks.

## Tech Stack
- Python
- Jupyter Notebook
- MLflow
- Jenkins
- Docker
- Other supporting libraries (requirements.txt)
- Custom utility scripts

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yashpadhye17/Hotel_Reservation_Prediction.git
cd Hotel_Reservation_Prediction
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run with Docker (Optional):
```bash
docker build -t hotel_reservation_prediction .
docker run -p 5000:5000 hotel_reservation_prediction
```

## Usage
- **Jupyter Notebooks**: Explore data and run experiments from the `/notebook` directory.
- **Run prediction**: Use `application.py` to launch the UI.
- **Train and log models**: Use scripts in `/pipeline` and `/src` directories for model training and versioning.
- **Monitor logs & artifacts**: Inspect the `/artifacts` and `/logs` directories.

## Project Structure
```text
Hotel_Reservation_Prediction/
│
├── artifacts/
├── config/
├── custom_jenkins/
├── logs/
├── mlruns/
├── notebook/            # Notebooks for EDA and model development
├── pipeline/            # Pipeline scripts
├── src/                 # Source code
├── static/templates/    # Web UI assets
├── utils/               # Utility scripts
│
├── requirements.txt     # Dependencies
├── Dockerfile           # Containerization file
├── Jenkinsfile          # CI/CD setup
├── application.py       # Main UI application
└── README.md
```

## Example Workflow
1. Run the data preprocessing notebook in `/notebook`.
2. Train model using `/src` pipeline scripts.
3. Deploy and access the prediction UI.
4. Monitor predictions and retrain as new data arrives.

## Deployment
- **Docker**: Containerize app for reproducibility.
- **Jenkins**: Use included Jenkinsfile for automated CI/CD.
- **Local**: Directly run using Python after dependency installation.

## Contributing
Pull requests welcome! Please submit issues for feature requests and bugs.

## License
MIT License (or specify your license here).
