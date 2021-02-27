# python-codes: a python code set

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<br />
<p align="center">
  <a href="https://github.com/rodrigodalri/password-manager">
    <img src="assets/logo.png" alt="Logo" width="601" height="203">
  </a>

  <h3 align="center">password-manager</h3>

  <p align="center">
    A simple python password manager to help your life.
    <br />
    <a href="https://github.com/rodrigodalri/password-manager"><strong>Explore the docs »</strong></a>
  </p>
</p>

## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Authors](#Authors)

## About the Project
password-manager is a simple Python password manager. It allows you to securely save secrets with a simple CLI interface.

## Getting Started
To get a local copy up and running follow these simple example steps.

### Prerequisites
This is an example of how to list things you need to use the software and how to install them.
* Python 3.7 or greater
```sh
apt-get install python3
```

### Installation
1. Clone the repo
```sh
git clone https://github.com/rodrigodalri/python-codes.git
```
2. Create venv
```sh
python3 -m venv .
source bin/activate
```
3. Install pip requirements
```sh
pip3 install -r requirements.txt
```
4. Build
```sh
python3 -m build
```
## Usage
To start your password manager runs:
```sh
python3 src/manager.py
```
If it is your first access, enter your name and master password and write down your 24 mnemonical words in a safe and offline place. 
```
$ python3 src/manager.py 
Please enter your name: TestUser
Please chose your master password: senha
Save the 24 words in offline world:
pencil invest kid frost excuse glory people adult squeeze deny swallow cloud nominee wave athlete pupil legend domain wisdom jungle matrix fat soul ketchup

Your identity has been saved!
Congratulations!
Your safe has been created!
What would you like to store in it today?
```
If not, just enter your master password to access the database.
```
$ python3 src/manager.py 
Please enter the master password: senha
Welcome Back sir TestUser!
```
You now have access to the usage options. The steps are self-explanatory.
Enjoy
```
--------------------------------------------
Commands:
Press 1 : to recover your master password
Press 2 : to save a new password
Press 3 : to get a stored password
Press 4 : to list all stored services
Press 5 : to quit
--------------------------------------------
Enter: 
```

## Roadmap
See the [open issues](https://github.com/rodrigodalri/password-manager/issues) for a list of proposed features (and known issues).

## Contributing
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature/Fix Branch (`git checkout -b feature/AmazingFeature`) or (`git checkout -b fix/AmazingFix`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Authors
<table style="text-align: center;">
  <tr>
    <th>Contributors</th>
    <th>Contributions</th>
  </tr>
  <tr>
    <td>
      <img src="https://avatars.githubusercontent.com/rodrigodalri?s=75">
      <br>
      <a href="https://github.com/rodrigodalri">Rodrigo Dal Ri</a>
    </td>
    <td>
      <a href="https://github.com/rodrigodalri/password-manager/commits?author=rodrigodalri">Contributions</a> by rodrigodalri
    </td>
  </tr>
</table>

See also the full list of [contributors](https://github.com/rodrigodalri/password-manager/contributors) who participated in this project.


[contributors-shield]: https://img.shields.io/github/contributors/rodrigodalri/password-manager
[contributors-url]: https://github.com/rodrigodalri/password-manager/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/rodrigodalri/password-manager
[forks-url]: https://github.com/rodrigodalri/password-manager/network/members

[stars-shield]: https://img.shields.io/github/stars/rodrigodalri/password-manager
[stars-url]: https://github.com/rodrigodalri/password-manager/stargazers

[issues-shield]: https://img.shields.io/github/issues/rodrigodalri/password-manager
[issues-url]: https://github.com/rodrigodalri/password-manager/issues

[license-shield]: https://img.shields.io/github/license/rodrigodalri/password-manager
[license-url]: https://github.com/rodrigodalri/password-manager/blob/master/LICENSE

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/rodrigodalri
[product-screenshot]: images/screenshot.png