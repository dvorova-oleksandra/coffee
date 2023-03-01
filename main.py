import data


def print_report():
    for key in data.resources:
        print(f"{key.title()} : {data.resources[key]}")


print_report()
