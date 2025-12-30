from fastapi import FastAPI
import boto3

app = FastAPI(title="DevOps Automation API")

REGION = "us-east-1"


def get_ec2_instances():
    ec2 = boto3.client("ec2", region_name=REGION)
    response = ec2.describe_instances()

    instances = []
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instances.append({
                "instance_id": instance["InstanceId"],
                "state": instance["State"]["Name"]
            })
    return instances


def get_s3_buckets():
    s3 = boto3.client("s3")
    response = s3.list_buckets()
    return [bucket["Name"] for bucket in response["Buckets"]]


def analyze_logs():
    """
    Dummy log analyzer logic.
    Replace this later with real log parsing.
    """
    logs = [
        "INFO Application started",
        "ERROR Database connection failed",
        "INFO User logged in",
        "WARNING Disk space low",
        "ERROR Timeout occurred"
    ]

    summary = {
        "total_logs": len(logs),
        "errors": sum(1 for log in logs if "ERROR" in log),
        "warnings": sum(1 for log in logs if "WARNING" in log)
    }

    return summary


# API Endpoints

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "API is healthy"
    }


@app.get("/logs")
def logs_summary():
    return analyze_logs()


@app.get("/aws")
def aws_resources():
    return {
        "ec2_instances": get_ec2_instances(),
        "s3_buckets": get_s3_buckets()
    }
