# 0x03. Queuing System in JS

## Project Overview

This project implements a queuing system using Redis and Node.js, covering basic operations, async operations, publishing/subscribing, and creating job queues with Kue.

## Learning Objectives

By the end of this project, you should be able to:

- Run a Redis server on your machine
- Perform simple operations with the Redis client
- Use a Redis client with Node.js for basic operations
- Store hash values in Redis
- Deal with async operations with Redis
- Use Kue as a queue system
- Build a basic Express app interacting with a Redis server
- Build a basic Express app interacting with a Redis server and queue

## Requirements

- All code will be compiled/interpreted on Ubuntu 18.04, Node 12.x, and Redis 5.0.7
- All files should end with a new line
- A `README.md` file at the root of the project folder is mandatory
- Code should use the `.js` extension

## Setup

1. Install Redis on Ubuntu 18.04
2. Install Node.js 12.x
3. Install project dependencies:
   ```bash
   npm install
   ```
## Tasks
### 0. Install a Redis instance

- Download, extract, and compile Redis 5.0.7
- Start Redis server in the background
- Verify Redis is working with ping
- Set a key-value pair using Redis CLI
- Retrieve the value for the key

### 1. Node Redis Client

- Create a Redis client
- Log connection status
- Set up error handling

### 2. Node Redis client and basic operations

- Implement functions for setting and getting school values

### 3. Node Redis client and async operations

- Modify previous functions to use ES6 async/await

### 4. Node Redis client and advanced operations

- Store hash values in Redis
- Retrieve and display stored hash

### 5. Node Redis client publisher and subscriber

- Implement a publisher and subscriber using Redis

### 6. Create the Job creator

- Create a queue with Kue
- Create a job with specific data structure

### 7. Create the Job processor

- Process jobs from the created queue
- Implement phone number blacklisting

### 8. Track progress and errors with Kue: Create the Job creator

- Create multiple jobs with an array of job data

### 9. Track progress and errors with Kue: Create the Job processor

- Process jobs with progress tracking and error handling

### 10. Writing the job creation function

- Implement a function to create push notification jobs

### 11. Writing the test for job creation

- Write tests for the job creation function

### 12. In stock?

- Create an Express server with routes for product listing and reservations
- Implement Redis for stock management

### 13. Can I have a seat? (Advanced)

- Implement a seat reservation system with Redis and Kue

## Running the Project
- To run each task:
```bash
npm run dev <filename>
```
- For tests:
```bash
npm test <filename>
```
## Author
Goodness Wema
