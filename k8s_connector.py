from kubernetes import client, config

# just my my tests

def main():
    config.load_incluster_config()
    v1 = client.CoreV1Api()
    print(v1.list_namespace())


if __name__ == "__main__":
    main()
