import boto3
import json

REGION = "us-east-1"


def list_ec2_instances():
    ec2 = boto3.client("ec2", region_name=REGION)
    response = ec2.describe_instances()

    instances = []

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instances.append({
                "InstanceId": instance["InstanceId"],
                "State": instance["State"]["Name"]
            })

    return instances


def list_s3_buckets():
    s3 = boto3.client("s3")
    response = s3.list_buckets()

    buckets = [bucket["Name"] for bucket in response["Buckets"]]
    return buckets


def main():
    output = {}

    ec2_instances = list_ec2_instances()
    s3_buckets = list_s3_buckets()

    output["EC2_Instances"] = ec2_instances
    output["S3_Buckets"] = s3_buckets

    print("EC2 Instances:")
    for inst in ec2_instances:
        print(f"  - {inst['InstanceId']} ({inst['State']})")

    print("\nS3 Buckets:")
    for bucket in s3_buckets:
        print(f"  - {bucket}")

    with open("aws_resources.json", "w") as f:
        json.dump(output, f, indent=4)

    print("\nOutput saved to aws_resources.json")


if __name__ == "__main__":
    main()
