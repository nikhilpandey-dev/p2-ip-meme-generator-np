# Lesson 6: Python for Web

## Lesson Overview
### Outline
In this module, we will learn:
- Web fundamentals for full-stack development with Python
- How to consume web services in Python to expand capabilities using `requests`
- How to package our applications into a web application using Flask

## Web Basics

### The Internet Simpplified
Internet is basically a Client, Server model where the client (usually the frontend) sends requests to another computer to fetch some data, files or status. The result of the request is known as response and this is the backbone of the internet.

### Requests
- A network command is often referred to as a request. You can think of a request as a strutured command sent over a network between two computers.
- The ***HyperText Transfer Protocol (HTTP)*** is the protocol - or set of rules - governing how requests are sent over the internet, and it has a clear and rigid definition for how requests can be made.

#### Types of Requests
1. GET : Requesting information from  server given a *universal resource identifier (URI)*.
2. POST: Requesting that sends information as a payload of to be processed by the server and sometimes sent back again to the client via the same request route.

### Response 
After a request is processes, a server provides a response with the result. This response includes a similar structure as a request so the client can easily interpret the results. 

## Python for Web
### Using Python with the internet
Application Programming Interface (API) - a set of public commands that can be used to interact with a software system. 

## Server Basics

### What is a Server?
After developing useful software that solves a problem, we might want to make this service available to others through the web.**We can serve this (our) application through specialized software that is designed to handle networked requests and responses. We call this software a server.**
> A server is a computer that runs specialized software to accept networked requests.
- Types of Servers
    - File Servers
    - Mail Servers
    - Application Servers

#### What Does a Server Do
1. It processes incoming requests received from the client
1. Server performs action on those requests (like doing some computation, getting some data from a database, locating a static file on the network)
1. It prepares the response (which is to be sent to the client)
