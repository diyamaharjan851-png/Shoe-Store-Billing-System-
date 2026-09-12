def read_file(file_path):
    try:
        product_list = []
        with open(file_path, 'r') as file:
            for line in file:
                line_split = line.replace("\n", "").split(",")
                if len(line_split) != 6:
                    continue
                product_list.append(line_split)
            return product_list
    except Exception as e:
        print("Error while reading file")
        return []