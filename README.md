<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="assets/logo.svg" alt="Logo" width="120" height="120">
  </a>

  <h3 align="center">SPOT AI</h3>

  <p align="center">
    The ultimate AI powered Home Security and Surveillance System
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#installation">Installation</a></li>
  </ol>
</details>

## About The Project

![Thumbnail](assets/thumbnail.png)

SPOT AI is a security system powered by AI that works with current camera systems to offer sophisticated video analytics, detect threats, and provide intelligent monitoring features. The system utilizes computer vision and deep learning methods to analyze video streams, allowing for functionalities like identifying objects, tracking motion, detecting anomalies, and recognizing fires.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

SPOT AI is built with the following technologies:

-   [![Flask][Flask.com]][Flask.com]
-   [![Python][Python.com]][Python.com]
-   [![Firebase][Firebase.com]][Firebase.com]
-   [![Chart.js][Chart.js]][Chart.js]
-   [![Yolov8][Yolov8]][Yolov8]
-   [![Huggingface][Huggingface]][Huggingface]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

To start using SPOT AI, follow the steps below.

### Prerequisites

You will need the following tools to get started:

-   python

```sh
sudo apt-get install python3 # for linux
brew install python3 # for mac
choco install python3 # for windows
```

-   poetry

```sh
pip install poetry
```

### Installation

1. Clone the repository.

```sh
git clone https://github.com/ChiragAgg5k/spot-ai
cd spot-ai
```

2. Install the dependencies.

```sh
poetry install
```

3. Create a firebase project and get the credentials. You can follow the instructions [here](https://firebase.google.com/docs/web/setup)

4. Create a Mailtrap account and get the credentials for email notifications. You can follow the instructions [here](https://mailtrap.io/)
5. Create a .env file in the root directory and add the required credentials. Follow the [.env.example](.env.example) file for reference.

6. Run the application.

```sh
poetry run python src/app.py
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[Flask.com]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[Python.com]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Firebase.com]: https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black
[Chart.js]: https://img.shields.io/badge/Chart.js-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white
[Yolov8]: https://img.shields.io/badge/YOLOv8-000000?style=for-the-badge&logo=python&logoColor=white
[Huggingface]: https://img.shields.io/badge/Hugging%20Face-000000?style=for-the-badge&logo=huggingface&logoColor=yellow

## Features

-   **Object Detection**
    Accurately detect and identify objects in the video stream.
    <img src="assets/object_detection.png" alt="Object Detection" width="300" height="200">

-   **Camera Logs**
    View the logs of the camera and the objects detected.
    <img src="assets/logs.png" alt="Camera Logs" width="300" height="250">

-   **Chatbot**
    Get notifications and alerts on your phone using the chatbot.
    <img src="assets/chatbot.png" alt="Chatbot" width="300" height="300">

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

## License

Distributed under the MIT License. See [LICENSE](LICENSE.txt) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
