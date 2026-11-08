import json

TASKS = [
    {
        "id": 1,
        "title": "Learn AWS Lambda",
        "status": "completed"
    },
    {
        "id": 2,
        "title": "Connect API Gateway",
        "status": "in-progress"
    },
    {
        "id": 3,
        "title": "Build Serverless API",
        "status": "pending"
    }
]

def lambda_handler(event, context):

    method = event["requestContext"]["http"]["method"]
    path = event["rawPath"]

    if method == "GET" and path == "/health":

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "message": "Serverless API is running!",
                "status": "healthy"
            })
        }

    elif method == "GET" and path == "/tasks":

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "count": len(TASKS),
                "tasks": TASKS
            })
        }

    elif method == "POST" and path == "/tasks":

        try:
            data = json.loads(event.get("body") or "{}")
        except (TypeError, json.JSONDecodeError):
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Invalid JSON"})
            }

        title = data.get("title") if isinstance(data, dict) else None

        if not isinstance(title, str) or not title.strip():
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Task title is required"})
            }

        return {
            "statusCode": 201,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "message": "Task accepted successfully",
                "task": {
                    "title": title.strip(),
                    "status": "pending"
                }
            })
        }

    return {
        "statusCode": 404,
        "body": json.dumps({"error": "Route not found"})
    }
