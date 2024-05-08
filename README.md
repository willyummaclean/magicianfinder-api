
<a name="readme-top"></a>



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- PROJECT LOGO -->
<br />

<h3 align="center">Magician Finder</h3>

</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project



It's a tough world out there for magician's trying to get exposure and the same goes for event-planners trying to hire magician talent. That's where Magician Finder comes in; its a prototype for a website that allows magicians to offer their services and event-planners to book appointments based on the services they need. Here a magician user can Create, Read, Update or delete their services, while a client user can Create, Read or Delete their appointments. 

Demo created with Loom:
https://www.loom.com/share/6b3c9675eb9a44c8b4c7dbf51a835ed4?sid=1b268f8a-9bd2-4213-a719-cbd3c8d2a550

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With


*  [![Python](https://www.python.org/static/community_logos/python-logo.png)](https://www.python.org/)
*  [![Django](https://www.djangoproject.com/s/img/logos/django-logo-negative.png)](https://www.djangoproject.com/)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This project utilizes a React client, https://github.com/willyummaclean/magicianfinder-client . Check that out as well!

### Installation



1. Clone the repo
   ```sh
   git clone https://github.com/willyummaclean/magicianfinder-api.git
   ```
2. Install the virtual environment
   ```sh
   pipenv install
   ```
3. Activate the virtual environment
   ```sh
   pipenv shell
   ```
4. Ensure you have the sqlite3 extentsion installed and Run the Python Debugger

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## MVP Features

1. Sign-up and sign-in using Django User Model, register your profile as a Magician or a client
2. Magicians can create the services they offer by selecting a category and providing a description as well as viewing, updating or deleting them
3. Clients can view the magician profiles and view their services
4. Clients can create appointments by selecting a magician's service and specifying a date of their event. They can also delete an exisiting appointment
5. Magicians can see a list of their appointments and delete them 


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Images 

ERD

- ![ERD](https://private-user-images.githubusercontent.com/149634021/328960597-4f69b64e-4ff3-4b70-99f5-0f9545e47a76.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTUxODQ4MzAsIm5iZiI6MTcxNTE4NDUzMCwicGF0aCI6Ii8xNDk2MzQwMjEvMzI4OTYwNTk3LTRmNjliNjRlLTRmZjMtNGI3MC05OWY1LTBmOTU0NWU0N2E3Ni5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNTA4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDUwOFQxNjA4NTBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1jMmEyOWJjNmRjM2ZhN2I5NzdjODgxZjYyZDlkZTU0MjIxOTdmYWM3MjQwYmI4YTViYTI2OTlkZTY5OTJiNjc1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.ETUqbmJ6QzsB6Jc7FJcQ2EVgMOOw4O6uS_tJtM_O3WE)

Home Page

- ![Home Page](https://private-user-images.githubusercontent.com/149634021/328963158-21ce1f3b-ec19-4cd3-9967-13481bc9495a.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTUxODUzNDEsIm5iZiI6MTcxNTE4NTA0MSwicGF0aCI6Ii8xNDk2MzQwMjEvMzI4OTYzMTU4LTIxY2UxZjNiLWVjMTktNGNkMy05OTY3LTEzNDgxYmM5NDk1YS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNTA4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDUwOFQxNjE3MjFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hYjc3NWFhMGQzZmM3MWQ1MDNkMTk5NDBmYWUxMmY1Y2FkNWFlOWEyMDI4MDMxMDYwZDg2NDYwMTYyNWI4NjQ4JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.tOIqDTDHUZzuND_3qhAYsxC4tCv1J5awLh_ZRxixki8)

Appointment List

- ![Appointments](https://private-user-images.githubusercontent.com/149634021/328965403-19904e6c-88b5-4ce3-a8ff-dd73332d4e43.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTUxODU4NzEsIm5iZiI6MTcxNTE4NTU3MSwicGF0aCI6Ii8xNDk2MzQwMjEvMzI4OTY1NDAzLTE5OTA0ZTZjLTg4YjUtNGNlMy1hOGZmLWRkNzMzMzJkNGU0My5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNTA4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDUwOFQxNjI2MTFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0zNjhjNTVhMDY5YzA4MDgwMTM1M2ZmNjIzNzMzN2E5ZWY0ODUzNjUzOWJiNzU1YTVjNzc2MWQ3NmM3ZDYyNDZhJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.iAuUgQt2H10sC2KgqFKSFqhBdkPNDfdJv4ijgzGzlfI)

Magician Services

- ![Services](https://private-user-images.githubusercontent.com/149634021/328965762-07641649-1b60-4171-b2c2-f7ed0c74bf18.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTUxODU4NzEsIm5iZiI6MTcxNTE4NTU3MSwicGF0aCI6Ii8xNDk2MzQwMjEvMzI4OTY1NzYyLTA3NjQxNjQ5LTFiNjAtNDE3MS1iMmMyLWY3ZWQwYzc0YmYxOC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNTA4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDUwOFQxNjI2MTFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT00ZGFhNGIwOGM2MTQ3OGVkMzU5MzQ4Zjg2OTU3MzA5NjEwNTEyMjk2MDA3NTM2YjZiYzQ5NmYzNTBjY2U5MzI0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.dskipOwKl91ItkVSz-uglmPj2aTEX2sOEXKQ1oewsW0)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Will MacLean - [LinkedIn-profile](https://www.linkedin.com/in/will-maclean/)

Client Repo Link: [https://github.com/willyummaclean/magicianfinder-client](https://github.com/willyummaclean/magicianfinder-client)

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
