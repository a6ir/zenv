def use(version: str):
    with open(".python-version", "w") as f:
        f.write(version)

    print(f"Using Python {version}")
