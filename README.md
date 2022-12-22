# Voice Fingerprint System

## Table of Contents

- [Introduction](#Description)
- [Project Structure](#project-structure)
- [Quick Preview](#quick-preview)
- [How to Run The Project](#run-the-project)
- [Team](#team)


### Introduction 
A web programme called Voice Fingerprint Checker is used for voice authentication (voice biometrics voice ID or speaker
recognition). The system depends on speech, thus an authorised individual must speak the proper sentence. Team Members 
are only given the authority to "Open the door" in our application.


### Project Structure
The Web Application is built using:
- Front-end
  - ReactJS (JavaScript)
  - CSS
  - PlotlyJS
  - CanvasJS
- Backend:
  - Django (Python)
- Models:
  - GMM (Gaussian Mixture Mo dels)

This Application is built using modern JavaScript's React framework for building the frontend structure, CanvasJS was used
to plot 2D plots, while PlotlyJS were used to plot 3D Scatter plots, the backend is made using an API app on aDjango server.
both frontend and backend are linked with a route (end-point/API) which data are transferred with a POST HTTP request.


![](vrs-client/src/assets/work%20flow.gif)

````
master
├─  Model (Notebooks and Data)
├─  vrs-client (Frontend)
│  └─  src
│     └─  components
├─  vrs-server (Backend)
│  └─  server (Django Server)
│  └─  apis (Django Application)
└─  README.md
````

### Quick Preview (Demo)

> In case of team member & 'Open The Door'
 
![Demo 1](Model/ezgif.com-gif-maker%20(5).gif)

> In case of team member & any other word

![Demo 2](Model/ezgif.com-gif-maker%20(3).gif)

> In case of any other one & any word

![Demo 3](Model/ezgif.com-gif-maker%20(4).gif)


### Run The Project

1. Install Python3 on your computer
``` 
Download it from www.python.org/downloads/
```

2. Install NodeJS on your computer
```
Download it from nodejs.org/en/download/
```

3. Install the frontend dependencies
```shell
cd vrs-client
npm install

```
4. Install the backend dependencies
```shell
cd vrs-server
pip install requirements.txt
```

Open the terminal and

5. Run the Backend Server
```shell
cd vrs-server
python manage.py runserver
```

in a new terminal 

6. Run the Frontend
```shell
cd vrs-client
npm start
```

> You need to install FFMPEG to covert MP3 audios to wav in the backend using pydub, if not you will not be able to run
> the project




### Team

First Semester - Biomedical Digital Signal Processing (SBE3110) class project creat ed by:

| Team Members' Names                                    | Section | B.N. |
|--------------------------------------------------------|:-------:|:----:|
| [Ibrahim Mohamed](https://github.com/1brahimmohamed)   |    1    |  2   |
| [Amr Mohamed](https://github.com/Amrmohamed090)        |    2    |  7   |
| [Mo'men Mohamed](https://github.com/momen882001)       |    2    |  11  |
| [Mariam Wael](https://github.com/MariamWaell)          |    2    |  36  |

### Submitted to:
- Dr. Tamer Basha & Eng. Abdallah Darwish
All rights reserved © 2022 to Team 10 - Systems & Biomedical Engineering, Cairo University (Class 2024)