def write_file(file_path, product_list):
    try:
        with open(file_path, 'w') as file:
            for product in product_list:
                line = ",".join(map(str, product)) + "\n"
                file.write(line)
    except Exception as e:
        print("Error while writing file")