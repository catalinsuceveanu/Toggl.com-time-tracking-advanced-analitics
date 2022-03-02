import client
import processor


def main():
    # print("test")
    # print(client.check_authentification())
    # print("Did connect: ", response)
    # print(client.get_time_entry("2387689075"))
    # print(client.get_all_time_entries("8242905"))
    # print(client.get_time_entries_in_range("2022-02-21"))
    # print(processor.separate_requests_in_entry(7))
    print(client.get_detailed_report("2022-02-25"))


if __name__ == "__main__":
    main()
