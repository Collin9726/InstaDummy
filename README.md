# Instadummy
#### A dummy of Instagram web app made with Django, 07/07/2020
#### By [Collin Owino](https://github.com/Collin9726)

### [Instadummy app](https://instadummyapp.herokuapp.com/)

<img src="./static/app_bg/instadummy.png"
     alt="Instadummy home image"
     style="width=100%;" />

## Description

<table>
<tr>
<td>
Instadummy is a dummy app of Instagram. It is meant to emulate Instagram web app's functionalities and UI. On this app a user can sign up for a profile, log into their account, update their profile with a bio and profile picture, post photos, search for and follow other users, view posts of people followed on the timeline, like and comment. Users can also update captions of images they posted, delete their images, unfollow users, and even delete their profiles.
</td>
</tr>
</table> 

#### Latest updated version is on 7th July 2020.

## Technologies used

1. Python v3.6
2. Django 3.0.7
3. Postgres
4. AWS S3 buckets
5. JavaScript
6. HTML & CSS

## Development

The app has been developed with Django 3.0.7. It is hosted on Heroku cloud platform. It uses PostgreSQL database for app data and AWS S3 buckets to store static and media files. The app makes use of dependencies as listed on `requirements.txt`. Testcases have been written for all model methods. It's source code is available on GitHub at https://github.com/Collin9726/InstaDummy

## Setup & Run instructions
- Clone the repo to your machine
- Create and activate a virtual environment
- Install the dependencies listed on `requirements.txt`.
- Include a `.env` file that provides `SECRET_KEY`, `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` among other environment variables as listed in `.env.sample`
- Run your app on `MODE='dev'` config for debugging purposes.

To contribute to this project on any modules, follow these easy steps:

- Fork the repo
- Create a new branch in your terminal (git checkout -b improve-feature)
- Make appropriate changes in file(s)
- Add the changes and commit them (git commit -am "Improve App")
- Push to the branch (git push origin improve-app)
- Create a Pull request

## Support and contact details
For any queries, issues, ideas or concerns contact [Collin Owino](owino.collin@gmail.com). Your feedback is highly appreciated. 
### [License](LICENSE)
MIT license
Copyright (c) 2020 **Collin Owino**