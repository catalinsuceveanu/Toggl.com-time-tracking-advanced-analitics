import client


def main():
    # response = client.authentification()
    # print(response, "response")
    # print(client.get_time_entry("2378846300"))
    print(client.get_all_time_entries("8242905")[1][1])


if __name__ == "__main__":
    main()
