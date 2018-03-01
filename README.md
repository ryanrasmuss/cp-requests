# Check Point API Scripts 

by: **Ryan Rasmuss**
using: **requests by Kenneth Reitz**, **Check Point API** 

### Overview

- cpi_api.py is the main dev script
- remember that any changes need to be published to be able to see (including the api calls!)


### Current Plan

1. See if possible to run scripts on gateway side via run script api function; otherwise just run local
2. Set new gateway and establish sic with api; interactive version where you type everything, or import from a file
3. show gateway, save information, delete it, remake gateway, then preload saved information as json payload and recreate it


### ToDo

- [ ] Need to parse arguments better, need to be able to navigate commands like VBoxManage
- [x] Publish
- [x] Start adding other commands
- [ ] Show how to get information
- [ ] Dump all information
- [ ] Add new gateway
- [ ] After posts, send message to remind to publish changes!
- [ ] Create a transfer script, dumps all gateway data, spin up another, and drop same policies/settings into it
- [ ] Throw in a main()


### Introduction

- Why use the API? Easier to automate, don't waste time
- DevOps integration, every business is going devops because of the above statement, but at enterprise scale
- What languages does Check Point API integrate with? Go, Python, etc.. anything RESTful
- Ansible Integration
- General high level overview of how the api works
- limitations
- Examples

### Presentation Overview

1. Introduction, myself, and the topic
2. Agenda: Why API (why you should use it and why a customer would use it)
   High Level Overview of the API
   Example of the power of the API
3. Why API
4. High Level Overview of the API (API Architecture?)
5. Example of the power of the API, download entire policy and setting, then reload on to
   another setup
6. Conclusion
