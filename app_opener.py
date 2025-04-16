import app_openers as util

def main():
    try:
        csv_path = util.get_csv_path()
        print("Reading file: {}...".format(csv_path))
        with open(csv_path, mode="r") as file:
            print("Opening apps...")
            commands = util.convert_file_to_commands(file)
            util.open_all_sites(commands)
            print("Program finished")
        
    except Exception as e:
        print("Oh my god its on fire {}\n".format(e))
        
if __name__ == "__main__":
    main()