# Flask Market
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](docs/license_apache_v2) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](docs/license_mit) ![version](https://img.shields.io/badge/version-5.0.2-orange) ![PR](https://img.shields.io/badge/PRs-Welcome-green)

This project is an implementation of an online market place for users to buy and sell stuff in Python Flask.

The whole project was implemented using the freeCodeCamp YouTube video as a reference. However, there are some deviations from that project. Some being:
- **Deployment**: The whole project was built to run on Docker containers, rather than running on local system. This lets the process to be standardized as I don't have to worry about which environment I use (such as Python versions or OS choice)
- **Database choice**: From the start I used MySQL as database (rather than SQLLite used in the lecture.) This was a personal choice as I was more familiar working with MySQL. Also, it helped me with the nitty gritty of configuration settings for a more complex database system 
- **Project Structure**: The project structure is not what default Flask applications follow. The primary reason for the deviation from standard structure is to push my understanding to the limits. When application is built using standard settings, nothing breaks as the libraries are designed to search for files in standard locations. Change something and everything starts breaking. This let me identify what configurations to use and what to change in the code

# Acknowledgements
- freeCodeCamp: This project was implemented using the lecture https://www.youtube.com/watch?v=Qr4QMBUPxWo for guidance