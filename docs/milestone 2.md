# MileStone 2

## Project Title

Secure and Personal Organizing Technology AI (SPOT AI)

## User Interface Design [prototype].

The goal of the user-centric SPOT AI project is to improve user security and safety by utilizing their current security camera equipment. The project's design is founded on the concepts of User-Centered Design (UCD), which give the end-user's wants, preferences, and behaviors first priority throughout the development process. The following key factors demonstrate how SPOT AI satisfies UCD requirements:

1. **User study and Understanding**: A great deal of study has been done to learn about the security apprehensions, problems, and expectations of the target users regarding such a system. This data is essential for determining SPOT AI's features, operations, and user interface.

2. **Iterative Design method**: A constant method of gathering user feedback and integrating it into the design is used in the development of SPOT AI. This methodology guarantees that the system develops according to real user requirements and preferences, as opposed to conjecture.

3. **Usability Testing**: To detect any usability problems, assess how intuitive the user interface is, and obtain input for enhancements, regular usability testing sessions are carried out with representative users. This guarantees a seamless user experience and makes SPOT AI easy to use.

4. **Multi-platform Accessibility**: SPOT AI accommodates customers' varied needs and preferences by providing a smartphone app for real-time updates and a web app for operating the cameras and a dashboard. This ensures accessibility across several platforms.

5. **Personalization and Customization**: Users can configure detection preferences, create custom alarms, and edit the user interface to suit their tastes by customizing and personalizing SPOT AI to meet their unique needs.

6. **Easy and Seamless Integration**: SPOT AI is made to work with consumers' current security camera configurations in an intuitive and seamless manner, reducing the need for complicated installs or extra hardware. This user-centric strategy improves the entire user experience and lowers adoption obstacles.

7. **continual Improvement**: In order to make sure that SPOT AI stays applicable, efficient, and user-friendly over time, it was designed with the idea of continual improvement. User feedback and developing technologies are incorporated into the system.

8. **Design Consistency**: To provide a seamless experience across different components, a unified design system is followed with consistent patterns for visuals, interactions and terminology.

9. **Accessibility and Inclusivity**: The design process actively considers accessibility needs for users with disabilities or impairments. This includes ensuring the user interfaces are compatible with assistive technologies and following web accessibility guidelines.


<div>
<img 
src="./Landing.png"
height="500"
/>
<img 
src="./MobileDashboard.png"
height="500"
/>
<img 
src="./DesktopDashboard.png"
height="500"
/>
<img 
src="./Chatbot.png"
height="500"
/>
</div>

## Potential User Feedback

## Design Documents

- Use Case Diagram

![Use Case Diagram](./use-case-diagram.png)

- Activity Diagram
    The overall flow and exchanges between the user, the SPOT AI system, and security staff (if applicable) are depicted in the activity diagram. The user must first gain access to the system, either by creating a new account or logging in if they already have one.

    The user chooses and configures the camera settings if they choose to configure CCTV cameras. At that point, the system simultaneously detects flames, anomalies, and objects. In addition, it provides updates, processes data in real time, and updates the admin dashboard and mobile app.

    In addition to performing administrative duties, the user can browse the admin dashboard to see data and communicate with the chatbot to question and control functionalities.

    Concurrently, security staff gets real-time updates in the event that an incident is discovered. After that, they can handle the situation by sending out teams, getting in touch with emergency services, or putting safety procedures in place.

    Using the fork notation, the diagram shows the parallel execution of individual tasks. It also includes supplementary annotations that explain particular actions or functionalities involved in particular steps.

![Activity Diagram](./activity-diagram.png)

- Class Diagram
    Users, cameras, and incidents are managed by the central `SPOTAISystem` class.

    Individual CCTV cameras are represented by the `Camera` class, which stores data about them such as location, settings, and camera ID. Its techniques for identifying items, irregularities, and fires allow the system to perform its essential surveillance functions.

    Users, including administrators and security staff, are represented by the `User` class, which has attributes defined by the `UserType` enumeration, such as credentials.

    The detected events, including the incident type ({IncidentType} enum), location, timestamp, and status ({IncidentStatus} enum), are encapsulated in the `Incident` class.

    The `SecurityPersonnel` class is used to represent employees who are in charge of reacting to situations in a specific way.

    The types ({ObjectType{ and {AnomalyType} enums), locations, and timestamps of detected entities are stored in supporting classes like {Object{, {Anomaly{, and `Fire}.

    Camera locations and setup settings are managed using classes such as `Location` and `CameraSettings`.

    The connections between classes show how different parts work together and rely on one another. For example, the composition connection between {SPOTAISystem} and {Camera} indicates that the system has more than one camera.

![Class Diagram](./class-diagram.png)

## Ethical and legal/privacy/terms and conditions

## Feasibility study/ Business Context

## Project cost estimation
We can provide the following estimate for the cost of the SPOT AI project based on the COCOMO (Constructive Cost methodology) methodology and an estimation of about 15,000 lines of code:

Labor Costs: Approximately 12 person-months would be needed to complete a project with 15,000 lines of code, according to COCOMO.
- The labor cost would be 12 person-months × $8,000 = $96,000 if the developers were paid an average of $8,000 per month.

Costs of Hardware and Equipment: - $30,000 for high-end workstations used for testing and development
- $80,000 for CCTV cameras and associated hardware for integration and testing

Costs of Software and Services:
- AI development frameworks and tools: $30,000.
- $100,000 for cloud computing services related to deployment and training
- APIs and services provided by third parties (such as weather, mapping, etc.): $50,000

Additional Fees:
- $80,000 for office space and utilities
- $80,000 for legal and patent filing fees
- Other costs (such as marketing, travel, etc.): $80,000

Estimated Total Cost: $626,000.

Due to the fewer lines of code, this estimate is based on a development timetable of about a year. In addition, several expenditures have been modified to reflect a more condensed project scope, including hardware and equipment, software and services, and miscellaneous fees.

## Partial Implementation/ Draft Code 

https://github.com/ChiragAgg5k/spot-ai

## Week wise Updates

### Week 1
- Our team will set up the project's development environment during the first week. As directed in the pyproject.toml file, two team members will start by installing Poetry, a dependency management tool for Python projects, and Python 3.11.
- They will install all of the dependencies—such as ultralytics, flask, torch, torchvision, and torchaudio—that are specified in the pyproject.toml file using Poetry.
- Following environment setup, each team member will become acquainted with the libraries being used and the project's structure.
- To learn more about the ultralytics library's features and how to incorporate it into our project, two additional team members will look through its examples and documentation.
- Furthermore, the initial two members of the team will investigate the possible applications and use cases of object detection and computer vision across a range of fields to aid in better defining the project's aims and objectives. In a project journal or notebook, we will record our ideas, conclusions, and any preliminary plans or thoughts.

### Week 2
- This week, we'll be concentrating on establishing the project's aims and objectives in light of the investigation and study completed last week.
- A pair of team members will ascertain the precise issue that needs to be resolved or the use case that needs to be addressed. For example, we could develop an application that can recognise and categorise objects in real-time video streams or analyse images for object recognition.
- Two additional team members will review the literature, look up current solutions or relevant fieldwork, and evaluate each one's advantages, disadvantages, and possible areas for development.
- All members of the team will work together to plan the project's architecture and high-level components, defining the key components, data flow, and interactions between various system components, based on this research.
- The team members will keep a project journal in which they will record our decisions, progress, and any issues or queries that come up during this week.

### Week 3
- This week, we'll start utilising the ultralytics library to implement the project's essential features. The first task for team members will be to configure and set up a development environment with all required dependencies.
- They will become acquainted with the various models that are available, as well as their individual advantages and disadvantages, by investigating the ultralytics library's object detection, tracking, and classification APIs and functionality.
- The core functionality will be implemented by the other two team members in accordance with the specifications of our project. This could entail importing pre-trained models, handling input data (pictures or videos), and extracting pertinent data like confidence scores, bounding boxes, and object classes.
- The  team members will also create unit tests to verify that our implementation is correct. These tests will test different scenarios, edge cases, and input data to confirm functionality and spot any potential problems or bugs.
- In our project journal, we will record our advancement, obstacles faced, and significant choices or insights gained. We may also include brief segments of code, schematics, or pseudocode to demonstrate our methodology for implementation.

### Week 4
- This week, we'll use Flask to integrate the core functionality that was developed the week before with a web interface. Our web application's user interface (UI) will be designed and developed .
- It will take user experience into account and create user-friendly interfaces for uploading photos or videos, displaying processed results, and offering any necessary controls or settings.
- The other members of the team will put the backend logic into practice to manage user input, process the data using our fundamental features, and produce the necessary outputs or visualisations. The Flask application and the ultralytics library will be integrated so that there can be smooth communication between the two parts.The web interface will be thoroughly tested by the entire team to make sure it displays the desired outcomes and handles a variety of input scenarios.
- We will fix any bugs or usability problems found during testing and record the process of developing the web application, including the backend implementation, UI design, and any difficulties or lessons learned.

### Week 5
- We are going to add some more features to the web interface this week in order to improve our application's functionality and user experience. Real-time video streaming from cameras or other sources will be implemented by two team members, giving users the ability to feed live video and receive object detection and classification results in real-time.
- To guarantee a seamless and effective video transmission, they will investigate and put into practice suitable streaming protocols and strategies. The remaining two members of the team will work on interactive result visualisation, which will entail showing confidence scores, bounding boxes, and object labels right on the input images or video frames.
- They will investigate tools or methods for overlaying this data in a way that is clear and easy to use. A  secure user authentication system will also be implemented by  members of the team utilising industry-standard techniques like hashing and salting passwords or integrating with third-party authentication providers (like OAuth).
- We will record in our project diary the specifics of the implementation, the choices we made regarding the design, and any difficulties or lessons we ran across this week.

### Week 6
- Our team's main goal for this week is to thoroughly test our web application to make sure it works as intended and meets all project specifications. A thorough testing plan that includes user acceptability, performance, and functional testing
- . The team members will oversee functional testing, which entails confirming that all of our application's features and functionalities operate as intended. To cover a range of scenarios, including various input data types, edge cases, and error conditions, they will create test cases .
- We will test our application's performance, which will help us find and fix any bottlenecks or performance problems.
- We will measure metrics like response times, resource utilisation, and scalability by simulating various load conditions using tools or techniques. Feedback from stakeholders or possible users will be gathered as part of the user acceptance testing process .
- The team members will assemble a representative sample of users and have them interact with our application in order to gather critical information about usability, user experience, and potential areas for improvement.
- We will document the entire testing process, including the test plan, test cases, and results. We will also log any issues or bugs discovered during testing, as well as any related solutions or workarounds.

### Week 7
- This week, our group will concentrate on enhancing the project's performance through the investigation of methods like GPU acceleration, parallelization, and model quantization.
- Model quantization techniques, which involve decreasing the accuracy of the weights and activations of the neural network model to produce smaller models and faster inference times, will be studied and put into practice by team members. we will look into methods such as post-training quantization or quantization-aware training.
- In order to maximise the available hardware resources and expedite processing times, members will focus on parallelization, which involves splitting up the computational workload among several processors or cores.
- We will look into frameworks or libraries for parallel processing that we can incorporate into our project. The members of the team will also look into ways to use specialised hardware libraries like CUDA to take advantage of GPU acceleration, which can result in notable performance increases for computationally demanding tasks like object detection and image processing.
- We will record the optimisation strategies we investigate, the implementation specifics, and the performance improvements attained, along with benchmarking data, code samples, and any lessons or difficulties we ran into.

### Week 8
- This week, our team will configure the required infrastructure and get our project ready for deployment.
- Two team members will investigate and assess various deployment options, taking into account aspects like cost, security, ease of management, and scalability. They will select the deployment platform that best fits the requirements of our project and is in line with the rules or preferences of our company.
- The other two team members are going to configure the deployment environment.The load balancers, databases, server instances, and other dependencies and services that are required for our application to run correctly will also be set up by them. They'll also automate deployment procedures using platforms like Docker or Kubernetes, which will make it possible to do repeatable and consistent deployments across different environments (including development, staging, and production).
- Any challenges or lessons learned during this phase will be recorded, along with the deployment process, the chosen infrastructure, and configuration standards.  An updated deployment manual will be maintained by the members.

## Week Wise Plan

### Week 9
- Our team will deploy our project to the selected infrastructure this week and conduct a comprehensive deployment process test.
- The application will be deployed to the selected infrastructure, team  will be in charge of making sure it is usable and operating as intended in the production setting. End-to-end testing will be carried out to verify the complete application flow, from user input to result generation and display.
- A variety of scenarios, such as varied input data types, load conditions, and edge cases, will be tested. We will keep an eye on how well the application performs and how its resources are used in the live environment, looking for any possible problems or bottlenecks that might need to be fixed.
- We will keep a record of the deployment procedure, including any difficulties or problems that arise and the actions taken to fix them. The first two members of the team will add any new configurations or settings needed for the production environment, as well as deployment details, to our project documentation.

### Week 10
- This week, our group will test the product with potential users and stakeholders to get their input. A representative sample of users who meet our use case or target audience will be chosen by members, and we will be asked to engage with our deployed application.
- In order to gather information about the user experience, usability, and any areas that need improvement, they will create a user testing plan that details the testing objectives, scenarios, and feedback collection methods.
- They will take into consideration methods like surveys, interviews, or user observation. The  members of the team will examine the user testing and feedback received, looking for patterns, problems, or requests for new features.
- We will rank the feedback according to its significance and congruence with the aims and purposes of the project.
- The user testing procedure will be documented, along with the testing strategy, participant demographics, and feedback obtained. The main conclusions and suggestions for further enhancements or iterations will be summed up in this documentation.

### Week 11
- Our team will add any new features or make any necessary changes to our application to meet user expectations and improve its usability based on the feedback received from users during the previous week.
- Based on their significance and the amount of work needed to implement them, The team members will rank the feedback items in order of importance, giving special attention to pressing usability problems, performance snags, or features that are still lacking but have the potential to greatly improve the user experience.
- In order to make sure that the project documentation is accurate and up to date and appropriately represents the current state of our application.
- The development guidelines, API documentation, and user guides will be refined by the team members.
- We will keep a record of the adjustments and enhancements made this week, along with the particular feedback items addressed, the specifics of the implementation, and any difficulties or lessons learned.

### Week 12
- Our team will wrap up any loose ends and tasks in this week of the project. The project documentation will be carefully examined by team members to make sure it is complete and simple to understand for Users or future developers.
- We will draft an extensive project report that includes pertinent diagrams, code snippets, and performance benchmarks to bolster our conclusions and recommendations.
- The report will cover the project's goals, implementation specifics, difficulties encountered, and prospects for future improvement.
- The members will showcase our project to peers, stakeholders, or prospective users for assessment and comments. They should be ready to go over the project's advantages and disadvantages as well as the reasoning behind our design and implementation decisions.
- We will reflect on the entire project experience, highlighting key learnings, successes, and areas for personal growth or improvement, and we will document the project's final state, including any feedback or suggestions received during the presentation or evaluation phase.

## LinkedIn Post

## Patent Research
Given that our SPOT AI research seems to incorporate unique and non-obvious technical breakthroughs, it may qualify for a patent. We might be able to patent the combination of AI-powered object detection, anomaly detection, fire detection, real-time updates, and a chatbot interface for engaging with CCTV camera data.

We should perform a comprehensive prior art search before filing for a patent to make sure that our idea is actually original and has not been anticipated by already developed technology. To help our team navigate the patent application process, which usually entails producing a comprehensive specification, claims, and supporting documentation, we need to speak with a patent attorney or agent.

But it's important to remember that because software is abstract and AI technology is always changing, patenting software and AI-related ideas might be difficult. Our claims might be examined by the patent office to make sure they are not just abstract concepts or algorithms and that they fit the requirements for patentable subject matter.

We believe that our patent application could be strengthened if our invention includes particular technical advancements such new machine learning algorithms, data processing methods, or hardware integrations.

We may still take into account alternative types of intellectual property protection, such as copyrights for the software code or trade secrets for proprietary algorithms or data, even if our innovation is not patentable.
