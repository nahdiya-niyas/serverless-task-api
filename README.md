# AWS Serverless Task API

A serverless REST API built using AWS Lambda and Amazon API Gateway. This project demonstrates how to build, deploy, and test HTTP endpoints using AWS serverless architecture.

## Architecture

Client → Amazon API Gateway → AWS Lambda → JSON Response

## Technologies Used

- AWS Lambda
- Amazon API Gateway (HTTP API)
- Python 3.14
- Postman
- GitHub

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Check API health |
| GET | `/tasks` | Retrieve sample tasks |
| POST | `/tasks` | Submit a task |

## Live API

Base URL:

https://6sym7eqay6.execute-api.ap-southeast-2.amazonaws.com

## Example POST Request

```json
{
  "title": "Complete AWS Serverless Project"
}
```

## Example Response

```json
{
  "message": "Task accepted successfully",
  "task": {
    "title": "Complete AWS Serverless Project",
    "status": "pending"
  }
}
```

## Features

- Serverless backend execution
- HTTP API integration
- JSON request and response handling
- Basic request validation
- Cloud-based deployment
- API testing using Postman

## Current Limitations

Tasks are not permanently stored. The GET endpoint returns predefined sample tasks, while POST validates and acknowledges submitted tasks.

## Developer

Nahdiya

Built as part of an AWS Serverless learning project.
