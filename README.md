<img src="https://vivifyassets.s3.ap-south-1.amazonaws.com/lifeeazy-logo1.png" align="right" width="250"/> 
<img src="https://user-images.githubusercontent.com/92524410/220310123-91c5a29e-03ad-4b13-aca7-e35f3eb5078d.png" width="100"/> 
<div align="center">
  <h1> Open-Health-Bot-API </h1>
  
</div>

  
 

Why we created Open Health Bot?

Open Health Bot has been envisioned to make healthcare information more accessable in most user friendly way.

- Accessibility: Open Health Bots provide a convenient way for people to access healthcare information and support from their homes, workplaces or on-the-go.

- Affordability: Open Health Bots has been kept open and free where people can have access to Healthcare Services and Information, making it affordable.

- Efficiency: Open Health Bots can quickly provide users with basic health information and guidance, potentially reducing the need for unnecessary and unauthenticated data on the web.

- Privacy: Open Health Bots allow users to obtain healthcare information without sharing their personal information or identity. However to keep it spam free and clean, user need to authenticate as a human. Any demographic information which has been aksed by the OHB is anonymous and required to provide relatively near to accurate information.

- Personalization: Open Health Bots can be programmed to provide personalized recommendations and support based on the user's specific health concerns and needs.

Overall, open health bots provide an innovative and effective way to deliver healthcare information and contributes to UNSDG's#3

OpenHealthBot is designed to help users with a variety of health-related questions and concerns. It can provide information on symptoms, diagnoses, treatment options, and preventive measures for a wide range of health conditions. Additionally, OpenHealthBot can provide guidance on healthy lifestyle habits, such as nutrition, exercise, and stress management.


<div align="center">
  
  <img src="https://img.shields.io/badge/Python-3.7-yellowgreen" />
    
  </div>
  
<div align="center">
 <img  src="https://user-images.githubusercontent.com/97886638/220600771-c11ddaf8-8030-4fe5-b867-6bc2647eff64.png" />
  
</div>

OpenHealthBot offers a set of APIs (Application Programming Interfaces) that enable developers to integrate OpenHealthBot's health-related features and functionalities into their own applications and services.

The OpenHealthBot APIs are designed to be easy to use, flexible, and scalable. They provide a range of capabilities, including natural language processing, intelligent recommendations, and personalized health information.

Here is an overview of the main APIs offered by OpenHealthBot:

 - LifeStyle Score Assessment API - This API enables developers to integrate OpenHealthBot's vast database of health-related information into their applications, allowing users to search for and retrieve relevant health information, including symptoms, diagnoses, treatments, and preventive measures.
 <div align="center">
 <img  src="https://user-images.githubusercontent.com/97886638/220821053-51c55048-56ee-4bd3-8cc9-ec7ad65a86a5.png" />
 </div>
 
    References: American Academy of Family Physicians
    i. https://www.aafp.org/pubs/afp/issues/2022/0900/editorial-lifestyle-medicine.html
    ii. https://www.aafp.org/dam/AAFP/documents/patient_care/lifestyle-medicine/lifestyle-medicine-guide.pdf
  

 - Diabetes Assessment API - This API enables developers to integrate OpenHealthBot's Diabetes functionality into their applications. The API can provide information on Diabetes Assessment.
 <div align="center">
 <img  src="https://user-images.githubusercontent.com/97886638/220821423-33eb0743-438e-439d-98cf-4a97f90c637b.png" />
 </div>
 
   

 - Depression Assessment API - This API enables developers to integrate OpenHealthBot's Depression functionality into their applications. The API can provide information on Depression Assessment.
 <div align="center">
 <img  src="https://user-images.githubusercontent.com/97886638/220821650-21e2e853-20b2-4079-9f63-f40a732f0388.png" />
 </div>
 

Overall, OpenHealthBot's APIs provide a powerful set of tools for developers to integrate health-related features and functionalities into their applications and services, making it easier for users to access personalized health information and recommendations.

## COWIN OPEN API's

<div align="center">
 <img  src="https://user-images.githubusercontent.com/97886638/220821957-f1027142-15e9-48e8-90c8-c828cb9f6b45.png" />
  
</div>

### Introduction:

The CoWIN (COVID Vaccine Intelligence Network) portal was created by the Government of India as a digital platform to manage the administration of COVID-19 vaccines across the country. CoWIN Open APIs (Application Programming Interfaces) allow developers to access data from the portal in real-time and build third-party applications. This documentation will provide an overview of CoWIN Open APIs, how to access them, and what data they provide.

### Authentication:
To access CoWIN Open APIs, developers need to authenticate themselves using an API key, which can be obtained from the CoWIN portal. The API key is used to identify the developer and the application making the request.

### Endpoints:
CoWIN Open APIs provide several endpoints that can be accessed to get data related to COVID-19 vaccines. Here are some of the important endpoints:

 - Get States: This endpoint returns a list of all states and union territories in India. The response includes the state and UT IDs, along with their names.

 - Get Districts: This endpoint returns a list of all districts in a particular state. Developers need to provide the state ID to get a list of districts in that state. The response includes the district IDs and names.

 - Get Vaccine Centers by District: This endpoint returns a list of all vaccine centers in a particular district. Developers need to provide the district ID to get a list of vaccine centers in that district. The response includes the vaccine center IDs, names, addresses, and other details.

 - Get Sessions by Center: This endpoint returns a list of all vaccination sessions at a particular center. Developers need to provide the vaccine center ID to get a list of vaccination sessions at that center. The response includes the session IDs, dates, available capacity, and other details.

 - Schedule an Appointment: This endpoint allows developers to schedule a vaccination appointment for a user. Developers need to provide the user's details, including the mobile number, the vaccine center ID, the session ID, and other details.

### Data Formats:
CoWIN Open APIs provide data in JSON format. Developers need to parse the JSON response to extract the required data.

### Rate Limits:
CoWIN Open APIs have rate limits to prevent abuse and ensure the stability of the platform. Developers need to make sure they do not exceed the rate limits, which can lead to their API key being suspended.

### Conclusion:
CoWIN Open APIs provide developers with access to real-time data related to COVID-19 vaccination in India. Developers can use this data to build third-party applications and services to help users find vaccine centers, schedule appointments, and more. By following the authentication process and the rate limits, developers can create innovative applications that help fight the COVID-19 pandemic in India.

## To Intigrate COWIN API's in Real-Time and Build Third-Party Applications

To integrate CoWIN Open APIs in real-time and build third-party applications, developers need to follow these steps:

 - Register on the CoWIN portal and obtain an API key: Developers need to register on the CoWIN portal and obtain an API key by following the steps provided on the portal. The API key is required to authenticate and access the APIs.

 - Understand the endpoints: Developers need to understand the various endpoints provided by the CoWIN Open APIs and the data they provide. This will help them decide which endpoints to use and how to use them.

 - Choose a programming language: Developers need to choose a programming language to work with the CoWIN Open APIs. Most programming languages provide libraries or packages that make it easier to work with APIs.

 - Make API requests: Developers can make API requests to CoWIN Open APIs using the programming language of their choice. They need to pass the API key and required parameters in the request to get the response.

 - Parse the response: The response from the API is usually in JSON format. Developers need to parse the response to extract the required data and use it in their application.

 - Build the application: Once developers have obtained the required data, they can build their application using the programming language of their choice. They can use the data to display vaccine center information, schedule appointments, or provide other services.

 - Test and deploy the application: Developers need to test the application to ensure it works as expected. They can then deploy the application on a web server or a cloud platform to make it accessible to users.

In summary, integrating CoWIN Open APIs in real-time and building third-party applications involves obtaining an API key, understanding the endpoints, making API requests, parsing the response, building the application, testing it, and deploying it. Developers need to follow best practices and ensure they comply with the rate limits to prevent their API key from being suspended.
## Installation

- Clone the project repository
- Create an virtual environment and activate it 
  ``` python -m venv <environment name> ```
 - To activate this environment
  ``` <environment name>/Scripts/activate ```
 - After activating the environment go to the project folder where you can able to find ``` requirements.txt ``` and install the requirements.txt using
  ``` pip install -r requirements.txt ```
  so using requirements.txt you are installing packages that are required for this project
  
## Development server
Run 
``` python manage.py runserver ``` 
  for a dev server. Navigate to ``` http://localhost:8000/ ``` . The app will automatically reload if you change any of the source files.


<p align="center">
<img src="https://vivifyassets.s3.ap-south-1.amazonaws.com/cropped-vivify_login.png" margin_left="100"/>
</p>

### These API's can be used along with the [Open Health Bot](https://github.com/vivifyhealthcare/Open-Health-Bot)

